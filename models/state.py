#!/usr/bin/python3
'''
    Implementation of the State class
'''
import models
from models.base_model import BaseModel
from sqlalchemy import Column, String
from models.base_model import Base
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = 'states'
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City',
            cascade="all,delete-orphan",
            backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """"""
            list_cities = []
            for item in models.storage.all(City).values():
                if item.state_id == self.id:
                    list_cities.append(item)
            return list_cities
