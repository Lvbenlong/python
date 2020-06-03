from types import MethodType

# class Student(object):
#     __slots__ = ('name', 'age')


# class Student(object):
#     def __init__(self):
#         self.test = 11

# def set_age (self, age):
#     self.age = age

# s1 = Student()
# s2 = Student()

# s1.set_age = MethodType(set_age, s1)
# s1.set_age(80)

# s1.name = 's1name'
# s2.name = 's2name'

# print('s1', s1.name)
# print('s2', s2.name)
# print('s1', s1.age)

# =========================================================Start
# class Student(object):
#     def set_score (self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be int')

#         if value < 0 or value > 100:
#             raise ValueError('score must be 1 ~ 100')

#         self._score = value
    
#     def get_score (self):
#         return self._score

# s1 = Student()
# s1.set_score(90)
# print(s1.get_score())


# class Student(object):
#     @property
#     def score (self):
#         return self._score
    
#     @score.setter
#     def score (self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be int')

#         if value < 0 or value > 100:
#             raise ValueError('score must be 1 ~ 100')

#         self._score = value


# s1 = Student()
# s1.score = 60
# print(s1.score)

# class Screen(object):
#     @property
#     def width(self):
#         return self._width
    
#     @width.setter
#     def width(self, value):
#         self._width = value

#     @property
#     def height(self):
#         return self._height
    
#     @height.setter
#     def height(self, value):
#         self._height = value
    
#     @property
#     def resolution(self):
#         return self._height * self._width

# s2 = Screen()
# s2.width = 100
# s2.height = 100
# print('width', s2.width)
# print('height', s2.height)
# print('resolution', s2.resolution)

# =========================================================END


# =========================================================Start
from enum import Enum
class Week (Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Week.Mon
print(day1)
print(day1.value)
# =========================================================END
