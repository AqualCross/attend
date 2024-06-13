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


@bp.route('/start', methods=['POST'])
def startAttendance():
    group = request.form['group']
    latitude = float(request.form['latitude'])
    longitude = float(request.form['longitude'])
    now_time = time()
    engine = create_engine('sqlite:///./sqlalchemy.db', echo=True, future=True)
    with Session(engine) as session:
        stmt = update(Student).where(Student.group == group).values(
            time_attend=now_time, latitude=latitude, longitude=longitude)
        session.execute(stmt)
        stmt = select(Student).where(Student.group == group)
        result = session.execute(stmt)
        students = result.scalars().all()
        for student in students:
            uid, total_attend = student.uid, student.total_attend
            stmt = update(Student).where(Student.uid == uid).values(total_attend=total_attend+1)
            session.execute(stmt)
        session.commit()
    return '成功发起签到'
