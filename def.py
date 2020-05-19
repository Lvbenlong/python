# def my_abs (x):
#   if x > 0:
#     return x
#   else:
#     return -x

# def test1 (x, y):
#   return x+1, y+1

# w = my_abs(12)
# a = test1(1, 2)
# b, c = test1(1, 2)
# (d, e) = test1(1, 2)
# print(w)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# 函数参数
def my_info (name, gender, age = 18, city = 'shenzhen' ):
  print('name:', name) 
  print('gender:', gender) 
  print('age:', age) 
  print('city:', city) 

# my_info('Bob', 'Male', 20, 'Beijing')
# my_info('Alex', 'Female', 24, 'XIAN')
# my_info('Johnny', 'Male', 20)
# my_info('Amy', 'Female', city = 'Wuhan')
# my_info('Test', 'Female', city = 'Wuhan', age = 10)
# my_info('Amy', 'Female')

def my_add (L = None):
  if L is None:
    L = []
  L.append('end')
  return L

# 普通
def my_sum (numbers):
  sum = 0
  for num in numbers:
    sum = sum + num * num
  return sum

# 可变参数
def my_sum_n (*numbers):
  sum = 0
  for num in numbers:
    sum = sum + num * num
  return sum

# 关键字参数
def person (name, age, **kw):
  print('My name is %s, I\'m %d' % (name, age))
  print('Other:', kw)

# person('Johnny', 18)
# person('Johnny', 18, a = 10)
# person('Johnny', 18, a = 10, b = 'aa')

# extra = {'city': 'Beijing', 'job': 'teacher'}
# person('Johnny', 18, **extra)

# 命名关键字参数
def person (name, age, *, city, job):
   print(name, age, city, job)

# person('Johnny', 18, city='Shenzhen', job='dever')
# person('Johnny', 18, job='Teacher', city='Wuhan')


def person(name, age, *args, city, job):
  print(name, age, args, city, job)
# person('Johnny', 18, 1, 2, 3, city='Shenzhen', job='dever') # result: Johnny 18 (1, 2, 3) Shenzhen dever
# person('Johnny', 18, city='Shenzhen', job='dever') # result:Johnny 18 () Shenzhen dever


def person(name, age, *, city = 'Beijing', job):
  print(name, age, city, job)

# person('Johnny', 10, city='Shenzhen', job='dever') # result: Johnny 18 (1, 2, 3) Shenzhen dever
# person('Johnny', 20, job='dever') # result:Johnny 18 () Shenzhen dever


def fact(n):
  if n==1:
    return 1
  return n * fact(n - 1)

# print(fact(1000)) 栈溢出报错

# 优化
def fact2(n):
  return fact_iter(n, 1)

def fact_iter(num, product):
  if num == 1:
    return product
  return fact_iter(num - 1, num * product)
print(fact2(1000))
