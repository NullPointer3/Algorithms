## Power m^n

## Using recursion
def pow(m: int, n: int) -> int:
  if n == 0:
    return 1
  return pow(m, n-1) * m

print(pow(2,5))

## Using iteration
def pow_loop(m : int, n: int):
  result = 1
  for i in range(n):
    result *= m
  return result
