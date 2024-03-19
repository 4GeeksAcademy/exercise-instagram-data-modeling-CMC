import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base, backref
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

followers = Table('followers',
            Base.metadata,
    Column('user_from_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('user_to_id', Integer, ForeignKey('user.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    followers = relationship('follower', secondary=followers, lazy='subquery',
            backref=backref('user', lazy=True))

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    post = relationship(Post)



class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id') , nullable=False)
    author = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    post = relationship(Post)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
