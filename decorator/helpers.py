"""Helpers"""
from decorator.exceptions import UnitDeadException


def raise_if_dead(decorate_method):
    """decorator method"""
    def check_function(*args, **kwargs):
        """decorated method body"""
        unit = args[0]
        if unit.health == 0:
            raise UnitDeadException("Unit is dead")
        return decorate_method(*args, **kwargs)
    return check_function
