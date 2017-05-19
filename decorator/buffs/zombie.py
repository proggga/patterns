"""Buff that make any Unit dead and alive"""
from decorator.buff_curse_decorator import BuffCurseUnitDecorator


class ZombieBuff(BuffCurseUnitDecorator):
    """Heal unit after move"""

    def __init__(self, unit):
        super(ZombieBuff, self).__init__(unit)
        self._unit.health = 0

    def move_forward(self):
        self._unit.health = 1
        self._unit.move_forward()
        self._unit.health = 0

    def attack(self, unit):
        self._unit.health = 1
        self._unit.attack(unit)
        self._unit.health = 0
