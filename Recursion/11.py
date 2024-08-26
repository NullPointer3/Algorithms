## Fibonacci Series

## using recursion
## Time Complexity O(2^n)
def fibo_recursive(n: int) -> int:
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibo_recursive(n-2) + fibo_recursive(n-1)


## Using Iteration
## Time complexity O(n)
## Space complexity O(1)
def fibo_iterative(n: int):
  if n <= 1:
    return n
  
  prev, curr = 0,1
  for _ in range(2,n+1):
    prev, curr = curr, prev+curr

  return curr

## Recursive with memoization
## Time Complexity O(n)
## Space Complexity O(n)

def fibo_memo(n: int) -> int:
  memo = None

  if memo is None:
    memo = [-1] * (n+1)

  if n <= 1:
    memo[n] = n
    return n
  
  else:
    if memo[n-2] == -1:
      memo[n-2] = fibo_memo(n-2)
    if memo[n-1] == -1:
      memo[n-1] = fibo_memo(n-1)
    return memo[n-2] + memo[n-1]
  
print(fibo_iterative(60))