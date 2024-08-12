## Nested Recursion
"""occurs when a function's argument itself involves a recursive call"""

def fun(n): 
  if n > 100:
    return n - 10
  else:
    return fun(fun(n+10))
  
print(fun(101))