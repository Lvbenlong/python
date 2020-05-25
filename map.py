from functools import reduce

def x (x):
  return x * x

def d (x):
  return {'key': x}

res = map(x, [1,2,3,4])
print(list(res))

res1 = map(d, [1,2,3,4])
print(list(res1))

def add (x, y):
  return x + y

res2 = reduce(add, [1,2,3,4,5,6])
print(res2)