import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()



class MedCategory(Base):
    __tablename__ = 'medcategory'

    id = Column(Integer, primary_key=True)
    category = Column(String(250), nullable=False)


    @property
    def serialize(self):
        return {
            'Medication Category': self.category,
            'Medication Category Id': self.id,
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


    @property
    def serialize(self):
        return {
            'Medcation Id': self.id,
            'Medication Name': self.name,
            'Description': self.description,
            'Pregnancy Category': self.pregnancyCategory,
            'Adverse Effect': self.adverseEffect,
            'Category Id' : self.medcategory_id,
        }

engine = create_engine('sqlite:///medication.db')
Base.metadata.create_all(engine)
