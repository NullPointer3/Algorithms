## Sum of first n natural numbers

## Using recursion
# Time complexity O(n) 
def sum(n):
  if n == 0:
    return 0
  return sum(n-1) + n

## A better approach will be using the formula 
## Time Complexity: O(1)
def sumF(n):
  return (n*(n+1)) // 2

print(sumF(100))

## Using Loop
## T(n) = n => O(n)
def sumLoop(n):
  sum = 0
  for i in range(1, n+1):
    sum+= i
  return sum

print(sumLoop(100))