from flask import Blueprint, render_template, request
from sqlalchemy import select
from sqlalchemy.orm import Session
from engine_init import engine
from models import Student, Teacher

bp = Blueprint('login', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/login', methods=['POST'])
def checkPassword():
    role = request.form['role']
    uid = request.form['uid']
    password = request.form['password']
    sheet = Student if role == 'student' else Teacher
    with Session(engine) as session:
        stmt = select(sheet.password).where(sheet.uid == uid)
        true_password = session.execute(stmt).scalar_one()
        print(true_password)
        if password == true_password:
            stmt = select(sheet.name).where(sheet.uid == uid)
            name = session.execute(stmt).scalar_one()
            return render_template(f'{role}.html', uid=uid, name=name)
    return render_template('index.html')
