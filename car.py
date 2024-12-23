

from validatitor import *


class Car:
    def __init__(self, name, model, man_year, pelak):
        self.name = name
        self.model = model
        self.man_year = man_year
        self.pelak = pelak

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name=name_validator(value)

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model=model_validator(value)

    @property
    def man_year(self):
        return self._man_year

    @man_year.setter
    def man_year(self, value):
        self._man_year=man_year_validator(value)

    @property
    def pelak(self):
        return self._pelak

    @pelak.setter
    def pelak(self, value):
        self._pelak=pelak_validator(value)

    def to_tuple(self):
        return self.name, self.model, self.man_year, self.pelak
