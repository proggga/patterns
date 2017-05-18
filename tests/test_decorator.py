"""Test Unit class, and then decorator"""
import unittest
from decorator.unit import Unit
from decorator.unit import HealBuff


class TestUnitClass(unittest.TestCase):
    """test unit class"""

    def test_UnitClass(self):
        """test class pls"""
        unit1 = Unit()
        self.assertTrue(hasattr(unit1, 'x'))
        self.assertEqual(unit1.x, 0)
        self.assertTrue(hasattr(unit1, 'speed'))
        self.assertEqual(unit1.x, 5)
        self.assertTrue(hasattr(unit1, 'damage'))
        self.assertEqual(unit1.x, 10)
        self.assertTrue(hasattr(unit1, 'health'))
        self.assertEqual(unit1.x, 100)
        self.assertTrue(hasattr(unit1, 'attack'))
        self.assertTrue(hasattr(unit1, 'speed'))
        self.assertTrue(hasattr(unit1, 'move_forward'))

    def test_speed_and_move(self):
        """test class pls"""
        unit1 = Unit()
        self.assertEqual(unit1.speed, 5)
        self.assertEqual(unit1.x, 0)

        unit1.move_forward()
        self.assertEqual(unit1.x, 5)

        unit1.speed = 2
        unit1.move_forward()
        self.assertEqual(unit1.x, 7)

    def test_attack(self):
        unit1 = Unit()
        unit2 = Unit()
        self.assertEqual(unit1.damage, 10)
        self.assertEqual(unit2.health, 100)
        unit1.attack(unit2)
        self.assertEqual(unit2.health, 90)

    def test_heal_decorator(self):
        unit1 = Unit()
        unit1 = HealBuff(unit1)
        self.assertEqual(unit1.x, 0)
        self.assertEqual(unit1.health, 100)
        self.assertEqual(unit1.speed, 5)
        unit1.move_forward()
        self.assertEqual(unit1.x, 5)
        self.assertEqual(unit1.health, 100)
