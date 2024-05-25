from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session, relationship


class Base(DeclarativeBase):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class Student(Base):
    __tablename__ = 'students'

    uid = Column(String, unique=True, nullable=False)
    password = Column(String, default='12345678', nullable=False)
    name = Column(String, nullable=False)
    # group_id = Column(Integer, ForeignKey('groups.id'))
    group = Column(String, nullable=False)
    total_attend = Column(Integer, default=0, nullable=False)
    late_attend = Column(Integer, default=0, nullable=False)
    failed_attend = Column(Integer, default=0, nullable=False)

    def __repr__(self):
        return f'User(id:{self.id},uid:{self.uid},password:{self.password!r},name:{self.name},group:{self.group})'


class Teacher(Base):
    __tablename__ = 'teachers'

    uid = Column(String, unique=True, nullable=False)
    password = Column(String, default='12345678', nullable=False)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f'Teacher(id:{self.id},uid:{self.uid},name:{self.name},password:{self.password!r})'


# # 班级
# class Group(Base):
#     __tablename__ = 'groups'
#     name = Column(String)
#     # 对应的多个 Student
#     members = relationship('Student', backref='group')
#
#     def __repr__(self):
#         return f'Group(id:{self.id},name:{self.name})'


# 创建sqlite连接引擎
engine = create_engine(
    'sqlite:///./sqlalchemy.db',
    echo=True,  # echo 设为 True 会打印出实际执行的 sql，调试的时候更方便
    future=True,  # 使用 SQLAlchemy 2.0 API，向后兼容
    pool_size=5,  # 连接池的大小默认为 5 个，设置为 0 时表示连接无限制
    pool_recycle=3600,  # 设置时间以限制数据库自动断开
)
# 创建表
Base.metadata.create_all(bind=engine, checkfirst=True)


if __name__ == '__main__':
    pass
    # 创建sqlite的session连接对象
    # with Session(engine) as session:
    #     datas = [
    #
    #     ]
    #     session.add_all(datas)
    #     session.commit()
