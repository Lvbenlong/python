names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

total = 0
for x in [1,2,3,4,5]:
    total = total + x
print(total)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

n = 0
for x in [1,2,3,4,5]:
  if x == 3:
    break
  n = n + x
print(n)

w = 0
for x in [1,2,3,4,5]:
  if x == 3:
    continue
  w = w + x
print(w)
