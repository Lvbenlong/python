class Student(object):
  def __init__ (self, name, score):
    self.name = name
    self.score = score

  def print_score (self):
    print('%s : %s' % (self.name, self.score))
  
  def get_grade (self):
    if self.score > 90:
      print('A')
    elif self.score >800:
      print('B')
    elif self.score >60:
      print('C')
    else:
      print('D')


# a = Student('A', 100)
# b = Student('B', 90)
# c = Student('C', 20)
# a.print_score()
# c.get_grade()
# print(a.name)
# a.name = 'ccc'
# print(a.name)

class Student1(object):
  def __init__ (self, name, score):
    self.__name = name
    self.__score = score

  def print_score (self):
    print('%s : %s' % (self.__name, self.__score))
  
  def get_grade (self):
    if self.__score > 90:
      print('A')
    elif self.__score >800:
      print('B')
    elif self.__score >60:
      print('C')
    else:
      print('D')

class Animal(object):
  def run(self):
    print('Animal is running...')

  def eat(self):
    print('Animal is eating...')

class Dog(Animal):
  def run(self):
    print('Dog is running...')

class Cat(Animal):
  def run(self):
    print('Cat is running...')

# D = Dog()
# C = Cat()

# D.eat()
# C.run()


class Student2(object):
  a = 'test'
  def __init__ (self, name, score):
    self.name = name
    self.score = score

  def print_score (self):
    print('%s : %s' % (self.__name, self.__score))

a = Student2('A', 10)
b = Student2('B', 100)

