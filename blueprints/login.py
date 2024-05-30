from flask import Blueprint, render_template, request
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Student, Teacher

bp = Blueprint('login', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/login', methods=['POST'])
def checkPassword():
    role = request.form.get('role')
    uid = request.form.get('uid')
    password = request.form.get('password')
    if role == 'student':
        sheet = Student
    else:
        sheet = Teacher
    engine = create_engine('sqlite:///./sqlalchemy.db', echo=True, future=True)
    with Session(engine) as session:
        stmt = select(sheet.password).where(sheet.uid == uid)
        true_password = session.execute(stmt).one()[0]
        print(true_password)
        if password == true_password:
            stmt = select(sheet.name).where(sheet.uid == uid)
            name = session.execute(stmt).one()[0]
            return render_template(f'{role}.html', uid=uid, name=name)
    return render_template('index.html')