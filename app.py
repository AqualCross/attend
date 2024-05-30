from flask import Flask
from blueprints import login, student, teacher

app = Flask(__name__)
app.register_blueprint(login.bp)
app.register_blueprint(student.bp)
app.register_blueprint(teacher.bp)


if __name__ == '__main__':
    app.run()
