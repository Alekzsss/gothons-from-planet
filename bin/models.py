from bin import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from bin import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):

    def __init__(self, **kwargs):
        if 'score' not in kwargs:
            kwargs['score'] = self.__table__.c.score.default.arg
        super().__init__(**kwargs)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    score = db.Column(db.Integer, default=0)


    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def normalized_score(self):
        str_score = str(self.score)
        return str_score.zfill(5)
