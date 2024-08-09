# Calling and returning phase
# Instructions before the calling phase will be executed during the calling phase
# Instructions after the calling phase will be executed during the returning phase

def fun1(n):
  if n > 0:
    print(n)
    fun1(n - 1)

def fun2(n):
  if n > 0:
    fun2(n-1)
    print(n)

fun1(5) # prints 5,4,3,2,1
fun2(5) # prints 1,2,3,4,5