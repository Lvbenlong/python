def my_abs (x):
  if x > 0:
    return x
  else:
    return -x

def test1 (x, y):
  return x+1, y+1

w = my_abs(12)
a = test1(1, 2)
b, c = test1(1, 2)
(d, e) = test1(1, 2)
print(w)
print(a)
print(b)
print(c)
print(d)
print(e)