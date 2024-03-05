from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

engine = create_engine("mariadb+pymysql://root:aa04190825!!@localhost:3307/")

sessionmaker(bind=engine)
