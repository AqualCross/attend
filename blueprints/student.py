from flask import Blueprint, request
from sqlalchemy import select, update
from sqlalchemy.orm import Session
from models import Student
from engine_init import engine
from time import time

bp = Blueprint('student', __name__, url_prefix='/student')


@bp.route('/updatePassword/<uid>', methods=['POST'])
def updatePassword(uid):
    new_password = request.form['new_password']
    with Session(engine) as session:
        stmt = update(Student).where(Student.uid == uid).values(password=new_password)
        session.execute(stmt)
        session.commit()
    return '成功修改密码'


LATE_TD = 10 * 60
MAX_TD = 45 * 60


@bp.route('/response/<uid>', methods=['POST'])
def response(uid):
    data = request.get_json()
    latitude = float(data['latitude'])
    longitude = float(data['longitude'])
    now_time = time()
    message: str
    with Session(engine) as session:
        stmt = select(Student).where(Student.uid == uid)
        student = session.execute(stmt).scalars().one()
        begin_time = student.time_attend
        time_diff = now_time - begin_time
        if time_diff > MAX_TD:
            message = '当前没有进行中的签到'
        elif latitude - student.latitude > 0.000045 or longitude - student.longitude > 0.0067:
            message = '不在签到范围内'
        elif time_diff < LATE_TD:
            message = '签到成功'
            number = student.normal_attend + 1
            stmt = update(Student).where(Student.uid == uid).values(
                normal_attend=number, time_attend=0, last_time_attend=now_time, latitude=latitude, longitude=longitude)
            session.execute(stmt)
        else:
            message = '迟到了'
            number = student.late_attend + 1
            stmt = update(Student).where(Student.uid == uid).values(
                late_attend=number, time_attend=0, last_time_attend=now_time, latitude=latitude, longitude=longitude)
            session.execute(stmt)
        session.commit()
    return message
