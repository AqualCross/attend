import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Student, Teacher

engine = create_engine(
    'sqlite:///./sqlalchemy.db',
    echo=True,  # log出SQL语句
    future=True,  # 使用 SQLAlchemy 2.0
)

with Session(engine) as session:
    students = pd.read_excel('初始化.xlsx', '学生')
    teacher = pd.read_excel('初始化.xlsx', '教师')

    # 清除所有表的内容
    session.query(Student).delete()
    session.query(Teacher).delete()

    for _, row in students.iterrows():
        session.add(Student(
            uid=row['学号'],
            name=row['姓名'],
            group=row['班级'],
            password=row.get('密码', 12345678),
            normal_attend=row.get('签到次数', 0),
            late_attend=row.get('迟到次数', 0),
            failed_attend=row.get('旷课次数', 0),
        ))
    for _, row in teacher.iterrows():
        session.add(Teacher(
            uid=row['工号'],
            name=row['姓名'],
            password=row.get('密码', 12345678),
        ))

    session.commit()
