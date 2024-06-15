import os
from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_FILE', 'sqlite:///./data.db')

engine = create_engine(
        SQLALCHEMY_DATABASE_URI,
        echo=True,  # log出SQL语句
        future=True,  # 使用 SQLAlchemy 2.0
)
