from bin import app, db
from bin.forms import LoginForm, RegistrationForm
from bin.models import User
import planisphere, planisphere_ru
from flask import session, redirect, url_for, request, render_template, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


@app.route("/browser/")
def checkout():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/map")
@login_required
def map1():
    session['room_name'] = planisphere.START
    return redirect(url_for("game"))

@app.route("/map2")
@login_required
def map2():
    session['room_name'] = planisphere_ru.START
    return redirect(url_for("game"))

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/play_again/")
def delete_state():
    session.pop('room_name', None)  # удаление данных о посещениях
    return redirect(url_for("index"))


@app.route("/game", methods=['GET', 'POST'])
@login_required
def game():
    room_name = session.get('room_name')
    print(room_name)
    if "ru" in room_name:
        map = planisphere_ru.rooms
    else:
        map = planisphere.rooms


    if request.method == 'GET':
        if room_name:
            room = planisphere.load_room(map, room_name)
            return render_template("show_room.html", room=room)
        else:
            return redirect(url_for('index'))
    else:
        action = request.form.get('action')

        if room_name and action:
            room = planisphere.load_room(map, room_name)
            next_room = room.go(action)

            if not next_room:
                session['room_name'] = planisphere.name_room(map, room)
            else:
                session['room_name'] = planisphere.name_room(map, next_room)
                if 'generic_death' not in planisphere.name_room(map, next_room):
                    user = User.query.filter_by(username=current_user.username).first()
                    if 'the_end_winner' not in planisphere.name_room(map, next_room):
                        user.score += 10
                    else:
                        user.score += 100
                    db.session.commit()
        return redirect(url_for("game"))
