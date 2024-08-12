## Factorial of a number

## Using recursion
def fact(n):
  if n == 0 or n == 1:
    return 1
  return fact(n-1)*n

## Using iteration
def fact_loop(n):
  result=1
  for i in range(1,n+1):
    result*=i
  return result