""" Tail Recursion: Type of recursion fuction where the recursive 
call is the last operation in the function"""
## Comparison with looping

def tailrecursive(n):
  if n > 0:
    print(n)
    tailrecursive(n - 1)

## tailrecursive(5) ## 5,4,3,2,1

## Using while loop
def whileLoop(n):
  while n > 0:
    print(n)
    n-=1

## whileLoop(5) ## 5,4,3,2,1

## Using for loop
def forLoop(n):
  for i in range(n, 0, -1):
    print(i)

forLoop(5)
