"""UnitInterface, Unit class, BuffCurseUnitDecorator and Buffs"""
from decorator.helpers import raise_if_dead
from decorator.unit_interface import UnitInterface


class Unit(UnitInterface):
    """Common Unit Class"""

    def __init__(self):
        self._x = 0
        self._speed = 5
        self._health = 100
        self._max_health = 100
        self._damage = 10

    def debuff(self):
        return self

    @property
    def coordinate(self):
        return self._x

    @coordinate.setter
    def coordinate(self, value):
        self._x = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value > self._max_health:
            value = self._max_health
        if value < 0:
            value = 0
        self._health = value

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        self._damage = value

    @raise_if_dead
    def move_forward(self):
        self.coordinate += self.speed

    @raise_if_dead
    def attack(self, unit):
        unit.health -= self.damage
