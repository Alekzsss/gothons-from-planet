from bin import app, db
from bin.models import User

@app.shell_context_processor
def make_shell_context():
    return {"db": db,"User": User}


if __name__ == '__main__':
    app.run(debug=True)
