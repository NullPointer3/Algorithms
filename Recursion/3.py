## Head Recursion

def head_recursive(n):
  if n > 0:
    head_recursive(n-1)
    print(n)

## Comparison with Loops
def head_loop(n):
  i = 1
  while i <= n:
    print(i)
    i+=1

