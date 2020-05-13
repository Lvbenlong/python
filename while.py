sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

w = 5
wsum = 0
while w > 0:
  w = w - 1
  if w == 3:
    break
  wsum = wsum + w
print(wsum)

m = 5
msum = 0
while m > 0:
  m = m - 1
  if m == 3:
    continue
  msum = msum + m
print(msum)
