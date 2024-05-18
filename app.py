from flask import Flask
from flask_migrate import Migrate
from blueprints.login import bp as login_bp
from blueprints.user import bp as user_bp
from models import *
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
app.register_blueprint(user_bp)
app.register_blueprint(login_bp)
migrate = Migrate(app, db)

#
# class User:
#     def __init__(self, uid, name, password):
#         self.id = uid
#         self.name = name
#         self.password = password
#
#
# class Student(User):
#     def __init__(self, uid, name, password, major, classname):
#         super().__init__(uid, name, password)
#         self.major = major
#         self.classname = classname
#
#
# class Teacher(User):
#     def __init__(self, uid, name, password):
#         super().__init__(uid, name, password)
#
#
# class attend:
#     """
#     latel   迟到时间线
#     final   旷课时间线
#     time    实际签到时间
#     location签到地点
#     """
#     def __init__(self):
#         self.name = None
#         self.lateline = None
#         self.finalline = None
#         self.time = None
#         self.location = None


if __name__ == '__main__':
    app.run()
