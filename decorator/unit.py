
class UnitInterface(object):

    @property
    def x(self):
        raise NotImplementedException()

    @x.setter
    def x_setter(self, value):
        raise NotImplementedException()

    @property
    def speed(self):
        raise NotImplementedException()

    @x.setter
    def speed_setter(self, value):
        raise NotImplementedException()

    @property
    def health(self):
        raise NotImplementedException()

    @x.setter
    def health_setter(self, value):
        raise NotImplementedException()

    @property
    def damage(self):
        raise NotImplementedException()

    @x.setter
    def damage_setter(self, value):
        raise NotImplementedException()

    def move_forward(self):
        raise NotImplementedException()

    def attack(self):
        raise NotImplementedException()

class Unit(UnitInterface):

    def __init__(self):
        self._x = 0
        self._speed = 5
        self._health = 100
        self._damage = 10

    @property
    def x(self):
        return self._x

    @x.setter
    def x_setter(self, value):
        self._x = value

    @property
    def speed(self):
        return self._speed

    @x.setter
    def speed_setter(self, value):
        self._speed = value

    @property
    def health(self):
        return self._speed

    @x.setter
    def health_setter(self, value):
        self._health = value

    @property
    def damage(self):
        return self._damage

    @x.setter
    def damage_setter(self, value):
        self._damage = value

    def move_forward(self):
        self.x += self.speed

    def attack(self, unit):
        unit.health -= self.damage

class HealBuff(UnitInterface):

    def __init__(self, unit):
        self._unit = unit

    @property
    def x(self):
        return self._unit.x

    @x.setter
    def x_setter(self, value):
        self._unit.x = value

    @property
    def speed(self):
        return self._unit.speed

    @x.setter
    def speed_setter(self, value):
        self._unit.speed = value

    @property
    def health(self):
        return self._unit.health

    @x.setter
    def health_setter(self, value):
        self._unit.health = value

    @property
    def damage(self):
        return self._unit.damage

    @x.setter
    def damage_setter(self, value):
        self._unit.damage = value

    def attack(self, unit):
        self._unit.attack(unit)

    def move_forward(self):
        self._unit.move_forward()
        self._unit.health += 10
