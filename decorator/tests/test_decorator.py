"""Test Unit class, and then decorator"""
import unittest

import mock

from decorator.buff_curse_decorator import BuffCurseUnitDecorator
from decorator.unit import Unit

from decorator.buffs.heal_on_move import HealOnMoveBuff
from decorator.buffs.zombie import ZombieBuff
from decorator.curses.damage_before_attack import DamageWhenAttackCurse

from decorator.exceptions import UnitDeadException
from decorator.exceptions import UnitIsNotDeadException


class TestUnitClass(unittest.TestCase):
    """test unit class"""

    def test_unit_constructor(self):
        """test class pls"""
        unit1 = Unit()
        self.assertTrue(hasattr(unit1, 'coordinate'))
        self.assertEqual(unit1.coordinate, 0)
        self.assertTrue(hasattr(unit1, 'speed'))
        self.assertEqual(unit1.speed, 5)
        self.assertTrue(hasattr(unit1, 'damage'))
        self.assertEqual(unit1.damage, 10)
        self.assertTrue(hasattr(unit1, 'health'))
        self.assertEqual(unit1.health, 100)
        self.assertTrue(hasattr(unit1, 'attack'))
        self.assertTrue(hasattr(unit1, 'speed'))
        self.assertTrue(hasattr(unit1, 'move_forward'))

    def test_speed_and_move(self):
        """test class pls"""
        unit1 = Unit()
        self.assertEqual(unit1.speed, 5)
        self.assertEqual(unit1.coordinate, 0)

        unit1.move_forward()
        self.assertEqual(unit1.coordinate, 5)

        unit1.speed = 2
        unit1.move_forward()
        self.assertEqual(unit1.coordinate, 7)

    def test_unit_dead(self):
        """test unit is dead"""
        unit1 = Unit()
        unit2 = Unit()
        unit1.health -= 100
        with self.assertRaises(UnitDeadException):
            unit1.move_forward()
        with self.assertRaises(UnitDeadException):
            unit1.attack(unit2)

    def test_unit_zombie(self):
        """test unit is zombie, but dead too"""
        unit1 = Unit()
        unit1.health -= 100
        with self.assertRaises(UnitDeadException):
            unit1.move_forward()
        unit1 = ZombieBuff(unit1)
        try:
            unit1.move_forward()
        except UnitDeadException:
            self.fail("Should not raise UnitDeadException,"
                      " because he is Zombie")

    def test_zombie_fails(self):
        """ZombieBuff should fail if unit is not dead"""
        with self.assertRaises(UnitIsNotDeadException):
            ZombieBuff(Unit())

    def test_attack(self):
        """Test unit can attack another unit"""
        unit1 = Unit()
        unit2 = Unit()
        self.assertEqual(unit1.damage, 10)
        self.assertEqual(unit2.health, 100)
        unit1.attack(unit2)
        self.assertEqual(unit2.health, 90)

    def test_decorator(self):
        """Test decorator work same as unit"""
        unit1 = Unit()
        unit2 = Unit()
        unit1 = BuffCurseUnitDecorator(unit1)
        self.assertEqual(unit1.coordinate, 0)
        self.assertEqual(unit1.health, 100)
        self.assertEqual(unit1.speed, 5)

        unit1.move_forward()
        self.assertEqual(unit1.coordinate, 5)

        self.assertEqual(unit2.health, 100)
        unit1.attack(unit2)
        self.assertEqual(unit2.health, 90)

    def test_heal_decorator(self):
        """Test HealBuff decorator"""
        unit1 = Unit()
        unit2 = Unit()
        unit1.attack(unit2)
        unit1.attack(unit2)
        unit1.attack(unit2)
        unit2 = HealOnMoveBuff(unit2)
        self.assertEqual(unit2.health, 70)
        unit2.move_forward()
        self.assertEqual(unit2.health, 80)
        unit2.move_forward()
        self.assertEqual(unit2.health, 90)
        unit2.move_forward()
        self.assertEqual(unit2.health, 100)
        unit2.move_forward()
        self.assertEqual(unit2.health, 100)

    def test_debuff_healbuff(self):
        """test debuff works"""
        unit1 = Unit()
        unit1.health = 50
        unit1 = HealOnMoveBuff(unit1)
        unit1.move_forward()
        self.assertEqual(unit1.health, 60)
        unit1 = unit1.debuff()
        unit1.move_forward()
        self.assertEqual(unit1.health, 60)

    def test_attack_curse(self):
        """test debuff works"""
        unit1 = Unit()
        unit2 = Unit()
        unit1.attack(unit2)
        self.assertEqual(unit1.health, 100)
        self.assertEqual(unit2.health, 90)
        unit1 = DamageWhenAttackCurse(unit1)
        random_path = 'decorator.curses.damage_before_attack.random.randint'
        with mock.patch(random_path) as mock_method:
            mock_method.return_value = 7
            unit1.attack(unit2)
        self.assertEqual(unit1.health, 93)
        self.assertEqual(unit2.health, 80)
        unit1 = unit1.debuff()
        unit1.attack(unit2)
        self.assertEqual(unit1.health, 93)
        self.assertEqual(unit2.health, 70)

    def test_two_decorators(self):
        """Test two decorators interactions"""
        unit1 = Unit()
        unit2 = Unit()
        unit1 = HealOnMoveBuff(unit1)
        unit1 = DamageWhenAttackCurse(unit1)

        random_path = 'decorator.curses.damage_before_attack.random.randint'
        with mock.patch(random_path) as mock_method:
            mock_method.return_value = 6
            unit1.attack(unit2)
        self.assertEqual(unit1.health, 94)
        self.assertEqual(unit2.health, 90)

        unit1.move_forward()
        self.assertEqual(unit1.health, 100)

        with mock.patch(random_path) as mock_method:
            mock_method.return_value = 4
            unit1.attack(unit2)
        self.assertEqual(unit1.health, 96)
        self.assertEqual(unit2.health, 80)

        unit1 = unit1.debuff()
        with mock.patch(random_path) as mock_method:
            mock_method.return_value = 9
            unit1.attack(unit2)
        self.assertEqual(unit1.health, 96)
        self.assertEqual(unit2.health, 70)

        unit1 = unit1.debuff()
        unit1.move_forward()
        self.assertEqual(unit1.health, 96)
