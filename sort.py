a = [1,-2,5,3,2,4,-5,61]
# print(sorted(a))
# print(sorted(a, key=abs))
# print(sorted(a, key=abs, reverse=True))

t = (
  {'name': 'AA', 'score': 80},
  {'name': 'BB', 'score': 70},
  {'name': 'CC', 'score': 88},
  {'name': 'DD', 'score': 25},
  {'name': 'EE', 'score': 60},
)

t2 = (
  ('AA', 80),
  ('BB', 70),
  ('CC', 90),
  ('DD', 50),
  ('EE', 60),
)

def fs (val) :
  return val['score']

def fn (val) :
  return val['name']

def f3 (val) :
  return val[0]

def f4 (val) :
  return val[1]

print(sorted(t, key=fs))
print(sorted(t, key=fn))
print(sorted(t, key=fn, reverse=True))

print(sorted(t2, key=f3))
print(sorted(t2, key=f4))
print(sorted(t2, key=f4, reverse=True))

