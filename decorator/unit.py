
class UnitInterface(object):

    def __init__(self):
        self.x = None
        self.health = None
        self.damage = None
        self.speed = None

    def move_forward(self):
        raise NotImplementedException()

    def attack(self):
        raise NotImplementedException()

class Unit(UnitInterface):

    def __init__(self):
        super(Unit, self).__init__()
        self.x = 0
        self.health = 100
        self.damage = 10
        self.speed = 5

    def move_forward(self):
        self.x += self.speed

    def attack(self, unit):
        unit.health -= self.damage

def HealBuff(UnitInterface):

    def __init__(self, unit):
        print('construc')
        self._unit = unit

    @property
    def x(self):
        return self._unit.x

    @x.setter
    def x_setter(self, value):
        self._unit.x = value

    def attack(self, unit):
        self._unit.attack(unit)

    def move_forward(self):
        self._unit.move_forward()
        self._unit.health += 10
