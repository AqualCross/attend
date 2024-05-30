import uuid

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session


class Base(DeclarativeBase):
    pass


class Student(Base):
    """
    uid name group password normal_attend late_attend failed_attend
    """
    __tablename__ = 'students'

    uid = Column(String, primary_key=True, unique=True)
    name = Column(String)
    group = Column(String)
    password = Column(String, default='12345678')
    normal_attend = Column(Integer, default=0)
    late_attend = Column(Integer, default=0)
    failed_attend = Column(Integer, default=0)


class Teacher(Base):
    __tablename__ = 'teachers'

    uid = Column(String, primary_key=True, unique=True)
    password = Column(String, default='12345678')
    name = Column(String)


if __name__ == '__main__':
    # 创建sqlite连接引擎
    engine = create_engine('sqlite:///./sqlalchemy.db', echo=True, future=True)

    # 创建所有Base类的表
    Base.metadata.create_all(bind=engine, checkfirst=True)
