import math

primeNumbers = []

def primeCheck(n):
  flag = 0
  if (n <= 1):
    flag = 1
  else:
    flag = 0
    for i in range(2,int(math.sqrt(n))+1):
      if (n%i == 0):
        flag = 1
        break
  return flag


for i in range(0,15):
  if (primeCheck(i) == 0):
    primeNumbers.append(i)
  else:
    continue

print(primeNumbers)
