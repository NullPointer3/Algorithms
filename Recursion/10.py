## Taylor's series using recursion

def fact(n):
  if n == 0 or n == 1:
    return 1
  return fact(n-1) * n

def e(x,n):
  if n == 0:
    return 1
  return (x**n) // fact(n) + e(x, n-1)

print(e(2,10))