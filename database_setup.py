import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
        return {
            'User Name': self.name,
            'User Id': self.id,
            'User Email' : self.email,
            'User Picture' : self.picture,
        }

class MedCategory(Base):
    __tablename__ = 'medcategory'

    id = Column(Integer, primary_key=True)
    category = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    @property
    def serialize(self):
        return {
            'Medication Category': self.category,
            'Medication Category Id': self.id,
            'User Id' : self.user_id,
        }


class MedList(Base):
    __tablename__ = 'medlist'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(650))
    adverseEffect = Column(String(250))
    pregnancyCategory = Column(String(80))
    medcategory_id = Column(Integer, ForeignKey('medcategory.id'))
    medcategory = relationship(MedCategory)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    @property
    def serialize(self):
        return {
            'Medication Id': self.id,
            'Medication Name': self.name,
            'Description': self.description,
            'Pregnancy Category': self.pregnancyCategory,
            'Adverse Effect': self.adverseEffect,
            'Category Id' : self.medcategory_id,
            'User Id' : self.user_id,
        }

engine = create_engine('sqlite:///medication.db')
Base.metadata.create_all(engine)
