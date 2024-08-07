def sum_array(arr):
  """A function that returns the sum of an array"""
  sum = 0
  for i in range(len(arr)):
    sum += arr[i]
  return sum

## Rewrite Insertion Sort so that it is monotonically decreasing
def insertion_sort(arr):
  """Sorting an array in descending order of magnitude"""
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key > arr[j]:
      arr[j + 1] = arr[j]
      j = j - 1
    arr[j + 1] = key
  return arr

## Serching Problem
def search(arr, val):
  """A function that searchs through an array for a value
    and return the index of the value or null"""
  index = None
  for i in range(len(arr)):
    if arr[i] == val:
      index = i
  return index

def selection_sort(arr):
  """Selection sort algorithm"""
  for i in range(len(arr)):
    min = i
    for j in range(i+1,len(arr)):
      if arr[j] < arr[min]:
        min = j
    arr[i], arr[min] = arr[min], arr[i]
  return arr
