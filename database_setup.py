import os
import sys
from sqlalchemy import Column,ForeignKey,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base= declarative_base()

class College(Base):
      __tablename__ = 'college'
      id = Column(Integer, primary_key=True)
      name = Column(String(250), nullable=False)

class CollegePlacements(Base):
      __tablename__='College_Pl'
      name=Column(String(80),nullable=False)
      id=Column(Integer,primary_key=True)
      year=Column(Integer)
      company=Column(String(50))
      salary=Column(Integer)
      dept=Column(String(20))
      college_id = Column(Integer, ForeignKey('college.id'))
      college = relationship(College)

      

engine=create_engine('sqlite:///placementsData.db')
Base.metadata.create_all(engine)

