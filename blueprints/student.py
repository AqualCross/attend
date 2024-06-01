from flask import Blueprint, request
from sqlalchemy import create_engine, select, update
from sqlalchemy.orm import Session
from models import Student
from time import time
from blueprints.teacher import attendance_request

bp = Blueprint('student', __name__, url_prefix='/student')


@bp.route('/updatePassword/<uid>', methods=['POST'])
def updatePassword(uid):
    new_password = request.form['new_password']
    engine = create_engine('sqlite:///./sqlalchemy.db', echo=True, future=True)
    with Session(engine) as session:
        stmt = update(Student).where(Student.uid == uid).values(password=new_password)
        session.execute(stmt)
        session.commit()
    return '成功修改密码'


@bp.route('/response/<uid>', methods=['POST'])
def response(uid):
    late_time_diff = 10 * 60
    failed_time_diff = 45 * 60
    now_time = time()
    begin_time = attendance_request.get(uid, None)
    if begin_time is None:
        return '当前没有进行中的签到'
    time_diff = now_time - begin_time
    engine = create_engine('sqlite:///./sqlalchemy.db', echo=True, future=True)
    with Session(engine) as session:
        if time_diff < late_time_diff:
            stmt = select(Student.normal_attend).where(Student.uid == uid)
            result = session.execute(stmt)
            normal_attend = result.scalar_one()
            normal_attend += 1
            stmt = update(Student).where(Student.uid == uid).values(normal_attend=normal_attend)
            session.execute(stmt)
            session.commit()
            return '签到成功'
        elif time_diff < failed_time_diff:
            stmt = select(Student.late_attend).where(Student.uid == uid)
            result = session.execute(stmt)
            late_attend = result.scalar_one()
            late_attend += 1
            stmt = update(Student).where(Student.uid == uid).values(late_attend=late_attend)
            session.execute(stmt)
            session.commit()
            return '迟到了'
        else:
            stmt = select(Student.failed_attend).where(Student.uid == uid)
            result = session.execute(stmt)
            failed_attend = result.scalar_one()
            failed_attend += 1
            stmt = update(Student).where(Student.uid == uid).values(failed_attend=failed_attend)
            session.execute(stmt)
            session.commit()
            return '旷课'
