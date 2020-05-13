#!/usr/bin/env python3

num = input('Enter a number:')
num = int(num)

if num < 0:
  print('负数')
elif num < 50:
  print('小于50')
else:
  print('大于50')
