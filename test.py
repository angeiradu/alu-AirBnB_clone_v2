from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///data.sql', echo=False)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False)

    def __init__(self, *args, **kwargs):

        for k, v in kwargs.items():
            setattr(self, k, v)


Session = sessionmaker(engine)
session = Session()

users = session.query(User).all()

for user in users:
    print(user.__class__.__name__)
