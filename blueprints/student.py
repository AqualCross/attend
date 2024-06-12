from flask import Blueprint, request
from sqlalchemy import create_engine, select, update
from sqlalchemy.orm import Session
from models import Student
from time import time

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


LATE_TD = 10 * 60
MAX_TD = 45 * 60


@bp.route('/response/<uid>', methods=['POST'])
def response(uid):
    now_time = time()
    engine = create_engine('sqlite:///./sqlalchemy.db', echo=True, future=True)
    message: str
    with Session(engine) as session:
        stmt = select(Student.time_attend).where(Student.uid == uid)
        result = session.execute(stmt)
        begin_time = result.scalar_one()
        time_diff = now_time - begin_time
        if time_diff > MAX_TD:
            message = '当前没有进行中的签到'
        elif time_diff < LATE_TD:
            message = '签到成功'
            stmt = select(Student.normal_attend).where(Student.uid == uid)
            result = session.execute(stmt)
            number = result.scalar_one() + 1
            stmt = update(Student).where(Student.uid == uid).values(normal_attend=number, time_attend=0)
            session.execute(stmt)
            session.commit()
        else:
            message = '迟到了'
            stmt = select(Student.late_attend).where(Student.uid == uid)
            result = session.execute(stmt)
            number = result.scalar_one() + 1
            stmt = update(Student).where(Student.uid == uid).values(late_attend=number, time_attend=0)
            session.execute(stmt)
            session.commit()
    return message
