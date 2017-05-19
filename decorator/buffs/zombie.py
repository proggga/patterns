"""Buff that make any Unit dead and alive"""
from decorator.buff_curse_decorator import BuffCurseUnitDecorator
from decorator.exceptions import UnitIsNotDeadException


class ZombieBuff(BuffCurseUnitDecorator):
    """Make dead unit Zombie"""

    def __init__(self, unit):
        super(ZombieBuff, self).__init__(unit)
        self._unit.health = 0

    @property
    def health(self):
        self._unit.health = 0
        return self._unit.health

    @health.setter
    def health(self, value):  # pylint: disable=unused-argument
        self._unit.health = 0

    def move_forward(self):
        self._unit.health = 1
        self._unit.move_forward()
        self._unit.health = 0

    def attack(self, unit):
        self._unit.health = 1
        self._unit.attack(unit)
        self._unit.health = 0

    @staticmethod
    def __new__(cls, unit):
        if unit.health != 0:
            raise UnitIsNotDeadException()
        return super(ZombieBuff, cls).__new__(cls)
