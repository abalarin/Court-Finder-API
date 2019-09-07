from courtfinderapi.app import session, engine, Base

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

class Court(Base):
    __tablename__ = 'court'
    id = Column(Integer, primary_key=True)
    uid = Column(String)
    address = Column(String)
    name = Column(String)

    total_courts = Column(Integer)
    total_visits = Column(Integer)
    total_ratings = Column(Integer)
    average_rating = Column(Integer)

    lights = Column(Integer)
    membership_required = Column(Integer)
    description = Column(String)
    latitude = Column(Integer)
    longitude = Column(Integer)

    def __repr__(self):
        return  "<Court(name='%s', id='%s')>" % (self.name, self.id)

Base.metadata.create_all(engine)
