"""Curse that deal random damage before every move"""
import random

from decorator.buff_curse_decorator import BuffCurseUnitDecorator
from decorator.helpers import raise_if_dead


class DamageWhenAttackCurse(BuffCurseUnitDecorator):
    """Damage to unit before attack"""

    @raise_if_dead
    def attack(self, unit):
        self.health -= random.randint(3, 10)
        super(DamageWhenAttackCurse, self).attack(unit)
