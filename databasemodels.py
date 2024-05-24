from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()


class Student(Base):
    """
    id 数据库索引
    uid 学号
    name 姓名
    password 密码
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(String, unique=True, nullable=False)
    password = Column(String, default='12345678', nullable=False)
    name = Column(String, unique=True, nullable=False)
    group = Column(String, nullable=False)

    def __repr__(self):
        return f'User(id:{self.id},uid:{self.uid},password:{self.password!r},name:{self.name},group:{self.group})'


class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(String, unique=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f'Teacher(id:{self.id},uid:{self.uid},name:{self.name},password:{self.password!r})'


# sqlite连接初始化
def sqliteSession():
    # 创建sqlite连接引擎
    engine = create_engine('sqlite:///./sqlalchemy.db', echo=True)
    # 创建表
    Base.metadata.create_all(bind=engine, checkfirst=True)
    # 创建sqlite的session连接对象
    return sessionmaker(bind=engine)()


if __name__ == '__main__':
    with sqliteSession() as session:
        datas = [

        ]
        session.add_all(datas)
        session.commit()
