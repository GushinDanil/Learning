"""Module for testing class NumberFormatter from module tasks.parse"""
from tasks.parse import NumberFormatter
import unittest


class TestNumberFormatter(unittest.TestCase):
  """This class tests func parseInt from task.parce.NumberFormatted"""
  def testParseInt(self):
    self.assertEqual(NumberFormatter().parseInt('12345'), 12345)
    self.assertEqual(NumberFormatter().parseInt('+12345'), 12345)
    self.assertEqual(NumberFormatter().parseInt('-123+45'), -12345)
    self.assertEqual(NumberFormatter().parseInt('-123--'), -123)
    self.assertRaises(ValueError, NumberFormatter().parseInt, '')
    self.assertRaises(ValueError, NumberFormatter().parseInt, '123a')
    self.assertRaises(TypeError, NumberFormatter().parseInt, 1)
    self.assertRaises(ValueError, NumberFormatter().parseInt, '1.2')
