import os
from sys import prefix
from flask import Flask
from blueprints import login, student, teacher
from initialize import init_db

app = Flask(__name__)
app.register_blueprint(login.bp)
app.register_blueprint(student.bp)
app.register_blueprint(teacher.bp)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path), os.getenv('DATABASE_FILE', 'data.db'))

if not os.path.exists('sqlalchemy.db'):
    init_db()

if __name__ == '__main__':
    app.run()
