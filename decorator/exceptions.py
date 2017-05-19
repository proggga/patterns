"""Decorator exceptions"""


class UnitDeadException(Exception):
    """Exception when try to do something when unit is dead"""
    pass


class UnitIsNotDeadException(Exception):
    """Raises when someone reccurect not dead unit and make Zombie"""
    pass
