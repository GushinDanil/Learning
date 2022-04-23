"""This module contains class for parsing string field to type integer"""
class NumberFormatter:
  """This class have method(parseInt) for parsing string to integer"""
  @staticmethod
  def isdigit(data: str) -> bool:
    """method for getting confident about digit values in string field """
    digits = '+-0123456789'
    if '__getitem__' in dir(data) \
            or '__iter__' in dir(data):
      for i in data:
        if i not in digits:
          raise ValueError('string field data should contain only digit values')
      return True
    else:
      raise TypeError('data is not iterable object, string field should be')

  @staticmethod
  def length(data: str) -> int:
    """method counts length of string field"""
    if '__getitem__' in dir(data) \
            or '__iter__' in dir(data):
      result = 0
      for _ in data:
        result += 1
      return result
    else:
      raise TypeError('data is not iterable object, string field should be')

  @staticmethod
  def is_not_decimal(data: str) -> bool:
    """method checks string field for decimal values"""
    if '__getitem__' in dir(data) \
            or '__iter__' in dir(data):
      if '.' not in data:
        return True
      else:
        raise ValueError('decimal values are not applicable, integer should be')

    raise TypeError('data is not iterable object, string field should be')

  @staticmethod
  def my_reduce(func, seq : list) ->int:
    """method unites all digits of list in number
    sample: [1,2,3] -> 123"""
    result = seq[0]
    for i in seq[1:]:
      result = func(result, i)
    return result

  @staticmethod
  def parseInt(data: str) -> int:
    """method for parsing string field to integer"""
    if 2 <= NumberFormatter.length(data) <= 2 ** 32 - 1:
      if NumberFormatter.is_not_decimal(data) \
                and NumberFormatter.isdigit(data):
        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        digits_str = '0123456789'
        result_list = []
        for i in data:
          index = 0
          for j in digits_str:
            if i == j:
              result_list += [digits[index]]  # подумать
            index += 1
        result = NumberFormatter.my_reduce(lambda x, y: x * 10 + y, result_list)
        if data[0] == '-': result *= -1
      return result

    raise ValueError('length should be in range 2 ≤ |s| ≤ 2^32-1')

