from pandas import read_excel
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Student, Teacher

if __name__ == '__main__':
    engine = create_engine(
        'sqlite:///./sqlalchemy.db',
        echo=True,  # log出SQL语句
        future=True,  # 使用 SQLAlchemy 2.0
    )

    with Session(engine) as session:
        students = read_excel('初始化.xlsx', '学生')
        teacher = read_excel('初始化.xlsx', '教师')

        # 清除所有表的内容
        session.query(Student).delete()
        session.query(Teacher).delete()

        for _, row in students.iterrows():
            session.add(Student(
                uid=row['学号'],
                name=row['姓名'],
                group=row['班级'],
                password=row.get('密码', 0),
                normal_attend=row.get('签到次数', 0),
                late_attend=row.get('迟到次数', 0),
                total_attend=row.get('需签到总次数', 0),
                time_attend=row.get('签到起始时间', 0),
                last_time_attend=row.get('最新一次签到时间', 0),
                latitude=row.get('纬度', 0),
                longitude=row.get('经度', 0)
            ))
        for _, row in teacher.iterrows():
            session.add(Teacher(
                uid=row['工号'],
                name=row['姓名'],
                password=row.get('密码', 0),
            ))

        session.commit()
