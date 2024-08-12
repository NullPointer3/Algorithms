## Tree Recursion
## This is when a function makes more than one recursive calls

def fun(n):
  if n > 0:
    print(n)
    fun(n-1)
    fun(n-1)

## Fibonacci Sequence
def fibo(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  return fibo(n-1) + fibo(n-2)

print(fibo(7))
