from courtfinderapi.app import session, engine, Base

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    height = Column(Integer)
    weight = Column(Integer)
    court_visits = Column(Integer)
    skill_level = Column(Integer)
    admin = Column(Boolean)
    friend_count = Column(Integer)
    join_date = Column(DateTime)

    favorite_court = Column(Integer, ForeignKey('court.id'))

    def __repr__(self):
        return "<User(username='%s')>" % (self.username)

Base.metadata.create_all(engine)
