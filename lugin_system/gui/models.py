from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.sql import func
base=declarative_base()
engine = create_engine("sqlite:///data/config.db")
Session = sessionmaker(bind=engine)

class user(base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    first_name=Column(String)
    last_name=Column(String)
    email=Column(String)
    gender=Column(String)
    bio=Column(String)
    user_name=Column(String)
    password=Column(String)
    is_admin= Column(Boolean, default=False)
class Auth(base):
    id=Column(Integer,primary_key=True)
    __tablename__="auth"
    serial=Column(String)
    User=Column(String)
base.metadata.create_all(engine)
def get_session():
    return Session()
