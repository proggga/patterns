"""Buff that heal after every move"""
from decorator.buff_curse_decorator import BuffCurseUnitDecorator
from decorator.helpers import raise_if_dead


class HealOnMoveBuff(BuffCurseUnitDecorator):
    """Heal unit after move"""

    @raise_if_dead
    def move_forward(self):
        super(HealOnMoveBuff, self).move_forward()
        self.health += 10
