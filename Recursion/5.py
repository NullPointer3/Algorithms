## Indirect Recursion
"""Occur when two or more functions call each other in acircular manner"""

def funA(n):
  if n > 0:
    print(n)
    funB(n-1)

def funB(n):
  if n > 1:
    print(n)
    funA(n/2)

funA(20)