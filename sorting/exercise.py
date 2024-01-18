def sum_array(arr):
  """calculate the total sum of values in an array"""
  sum = 0
  for i in range(0, len(arr)):
    sum += arr[i]
  return sum

# Insertion Sort (monotonically decreasing)
def insertion_sort(arr): 
  """sort an array in descending order"""
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] < key:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key

# Linear search 
def linear_search(arr, value):
  """An algorithm which scans through an array and returns 
    the index of the value we searching for or returns none"""
  j = None
  for i in range(0, len(arr)):
    if arr[i] == value:
      j = i
  return j

my_arr = [2,33,4,55,4,3,22,0]
print(linear_search(my_arr, 22))