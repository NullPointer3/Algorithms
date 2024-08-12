## Power m^n

## Using recursion
def pow(m: int, n: int) -> int:
  if n == 0:
    return 1
  return pow(m, n-1) * m


def power(m: int, n: int) -> int:
  if n == 0:
    return 1
  elif n % 2 == 0:
    return power(m*m, n // 2)
  else:
    return power(m*m, (n-1) // 2) * m

## Using iteration
def pow_loop(m : int, n: int):
  result = 1
  for _ in range(n):
    result *= m
  return result
