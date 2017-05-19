"""Main Buff and Curse decorator for Unit"""
from decorator.helpers import raise_if_dead
from decorator.unit_interface import UnitInterface


class BuffCurseUnitDecorator(UnitInterface):
    """Common Decorator for Buffs"""

    def __init__(self, unit):
        self._unit = unit

    def debuff(self):
        return self._unit

    @property
    def coordinate(self):
        return self._unit.coordinate

    @coordinate.setter
    def coordinate(self, value):
        self._unit.coordinate = value

    @property
    def speed(self):
        return self._unit.speed

    @speed.setter
    def speed(self, value):
        self._unit.speed = value

    @property
    def health(self):
        return self._unit.health

    @health.setter
    def health(self, value):
        self._unit.health = value

    @property
    def damage(self):
        return self._unit.damage

    @damage.setter
    def damage(self, value):
        self._unit.damage = value

    @raise_if_dead
    def attack(self, unit):
        self._unit.attack(unit)

    @raise_if_dead
    def move_forward(self):
        self._unit.move_forward()
