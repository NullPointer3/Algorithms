def insertion_sort(arr):
  """An efficient algorithms for sorting a small number of elements"""
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key

my_arr = [23,3,4,6,7,5,33,121,34,5,77,8]
insertion_sort(my_arr)
print(f"Sorted Array: {my_arr}")