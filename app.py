import os
from flask import Flask
from blueprints import login, student, teacher
from initialize import init_db

app = Flask(__name__)
app.register_blueprint(login.bp)
app.register_blueprint(student.bp)
app.register_blueprint(teacher.bp)
SECRET_KEY = os.getenv('SECRET_KEY', 'localhost+3-key.pem')


if not os.path.exists('data.db'):
    init_db()

if __name__ == '__main__':
    app.run(key=SECRET_KEY)
