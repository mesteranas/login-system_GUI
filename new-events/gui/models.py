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
    posts_count = Column(Integer, default=0)
    is_admin= Column(Boolean, default=False)
class Post(base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(500))
    body = Column(Text)
    resources = Column(Text)
    date = Column(DateTime(timezone=True), server_default=func.now())
    User = Column(String)
    is_view = Column(Boolean, default=False)
    like = Column(Integer, default=0)
    dislike = Column(Integer, default=0)
    category = Column(String(100))
class Auth(base):
    id=Column(Integer,primary_key=True)
    __tablename__="auth"
    serial=Column(String)
    User=Column(String)
base.metadata.create_all(engine)
def get_session():
    return Session()
