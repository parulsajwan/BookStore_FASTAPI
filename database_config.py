from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# for sqlite
# SQLALCHEMY_DATABASE_URL = "sqlite:///bookstore.db"

# for postgresql
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost/bookstore"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
