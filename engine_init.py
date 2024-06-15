from sqlalchemy import create_engine

engine = create_engine(
        'sqlite:///./sqlalchemy.db',
        echo=True,  # log出SQL语句
        future=True,  # 使用 SQLAlchemy 2.0
        pool_size=5,  # 连接池中初始连接的数量
        max_overflow=10,  # 超过pool_size后允许创建的额外连接数
        pool_pre_ping=True,  # 在每次连接checkout时测试连接是否可用
)
