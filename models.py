from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Student(Base):
    """
    ``uid`` 学号
    ``name`` 姓名
    ``group`` 班级
    ``password`` 密码
    ``normal_attend`` 完美签到成功次数
    ``late_attend`` 迟到次数
    ``total_attend`` 总需签到次数
    ``time_attend`` 签到起始时间
    """
    __tablename__ = 'students'

    uid = Column(String, primary_key=True, unique=True)
    name = Column(String)
    group = Column(String)
    password = Column(String, default='12345678')
    normal_attend = Column(Integer, default=0)
    late_attend = Column(Integer, default=0)
    total_attend = Column(Integer, default=0)
    time_attend = Column(Float, default=0)
    last_time_attend = Column(Float, default=0)
    latitude = Column(Float, default=0)
    longitude = Column(Float, default=0)


class Teacher(Base):
    __tablename__ = 'teachers'

    uid = Column(String, primary_key=True, unique=True)
    password = Column(String, default='12345678')
    name = Column(String)


if __name__ == '__main__':
    engine = create_engine('sqlite:///./sqlalchemy.db', echo=True, future=True)

    # 创建所有Base类的表
    Base.metadata.create_all(bind=engine, checkfirst=True)
