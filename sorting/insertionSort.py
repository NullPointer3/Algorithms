def insertion_sort(arr):
  """An efficient algorithms for sorting a small number of elements"""
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key

sorted = insertion_sort([1,22,11,3,44,2,11,6,0,8,99,6])
print(sorted)