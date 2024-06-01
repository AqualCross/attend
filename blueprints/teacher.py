from time import time
from flask import Blueprint, request
from sqlalchemy import create_engine, select, update
from sqlalchemy.orm import Session
from models import Teacher, Student

bp = Blueprint('teacher', __name__, url_prefix='/teacher')


@bp.route('/updatePassword/<uid>', methods=['POST'])
def updatePassword(uid):
    new_password = request.form['new_password']
    engine = create_engine('sqlite:///./sqlalchemy.db', echo=True, future=True)
    with Session(engine) as session:
        stmt = update(Teacher).where(Teacher.uid == uid).values(password=new_password)
        session.execute(stmt)
    return '成功修改密码'


attendance_request = {}


@bp.route('/start', methods=['POST'])
def startAttendance():
    global attendance_request
    group = request.form['group']
    now_time = time()
    engine = create_engine('sqlite:///./sqlalchemy.db', echo=True, future=True)
    with Session(engine) as session:
        stmt = select(Student.uid).where(Student.group == group)
        result = session.execute(stmt)
        for row in result:
            uid = row[0]
            attendance_request[uid] = now_time
    return '成功发起签到'
