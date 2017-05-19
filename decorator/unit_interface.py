"""Unit Interface for Unit, Buffers and Curses"""


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
