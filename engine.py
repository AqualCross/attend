from sqlalchemy import create_engine

engine = create_engine(
        'sqlite:///./sqlalchemy.db',
        echo=True,  # log出SQL语句
        future=True,  # 使用 SQLAlchemy 2.0
)