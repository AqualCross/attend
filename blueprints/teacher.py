from time import time

from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import create_engine, select, update
from sqlalchemy.orm import Session

from models import Teacher, Student

bp = Blueprint('teacher', __name__, url_prefix='/teacher')


# @bp.route('/')
# def teacher(uid, password):
#     uid = request.args.get('uid')
#     password = request.args.get('password')
#     engine = create_engine('sqlite:///./sqlalchemy.db', echo=True, future=True)
#     with Session(engine) as session:
#         stmt = select(Teacher.password).where(Teacher.uid == uid)
#         true_password = session.execute(stmt)
#
#         if password == true_password:
#             stmt = select(Teacher.name).where(Teacher.uid == uid)
#             name = session.execute(stmt)
#             return render_template('teacher.html', uid=uid, name=name)

@bp.route('/updatePassword/<uid>', methods=['POST'])
def updatePassword(uid):
    new_password = request.form['new_password']
    engine = create_engine('sqlite:///./sqlalchemy.db', echo=True, future=True)
    with Session(engine) as session:
        stmt = select(Teacher.password).where(Teacher.uid == uid)
        _password = session.execute(stmt)
        stmt = update(Teacher).where(Teacher.uid == uid).values(password=new_password)
        session.execute(stmt)
    return jsonify({"message": "成功修改密码"})


attendance_request = {}


@bp.route('/start/<group>')
def startAttendance(group):
    global attendance_request
    now_time = time()
    engine = create_engine('sqlite:///./sqlalchemy.db', echo=True, future=True)
    with Session(engine) as session:
        stmt = select(Student.uid).where(Student.group == group)
        result = session.execute(stmt)
        for row in result:
            uid = row[0]
            attendance_request[uid] = now_time
