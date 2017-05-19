"""UnitInterface, Unit class, BufferedUnitDecorator and Buffs"""
import random


class UnitDeadException(Exception):
    """Exception when try to do something when unit is dead"""
    pass


def raise_if_dead(decorate_method):
    """decorator method"""
    def check_function(*args, **kwargs):
        """decorated method body"""
        unit = args[0]
        if unit.health == 0:
            raise UnitDeadException("Unit is dead")
        return decorate_method(*args, **kwargs)
    return check_function


class UnitInterface(object):
    """UnitInterface which allow user"""

    def debuff(self):
        """Should return unit without last buff"""
        raise NotImplementedError()

    @property
    def coordinate(self):
        """x coordinate getter"""
        raise NotImplementedError()

    @coordinate.setter
    def coordinate(self, value):
        """coordinate setter"""
        raise NotImplementedError()

    @property
    def speed(self):
        """move speed getter"""
        raise NotImplementedError()

    @speed.setter
    def speed(self, value):
        """move speed setter"""
        raise NotImplementedError()

    @property
    def health(self):
        """health getter"""
        raise NotImplementedError()

    @health.setter
    def health(self, value):
        """health setter"""
        raise NotImplementedError()

    @property
    def damage(self):
        """damage getter"""
        raise NotImplementedError()

    @damage.setter
    def damage(self, value):
        """damage setter"""
        raise NotImplementedError()

    def move_forward(self):
        """move forward"""
        raise NotImplementedError()

    def attack(self, unit):
        """attack unit"""
        raise NotImplementedError()


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


class BufferedUnitDecorator(UnitInterface):
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


class HealWhenMoveBuff(BufferedUnitDecorator):
    """Heal unit after move"""

    @raise_if_dead
    def move_forward(self):
        super(HealWhenMoveBuff, self).move_forward()
        self.health += 10


class DamageWhenAttackCurse(BufferedUnitDecorator):
    """Damage to unit before attack"""

    @raise_if_dead
    def attack(self, unit):
        self.health -= random.randint(3, 10)
        super(DamageWhenAttackCurse, self).attack(unit)


class ZombieBuff(BufferedUnitDecorator):
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
