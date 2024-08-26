## Inserting an element at a given index in an array
def insert(arr, idx, element):
  for i in range(len(arr) - 1, -1):
    arr[i] = arr[i-1]
  arr[idx] = element

my_list = [2,3,4,2,5,9,0,1]
insert(my_list, 7, 12)
print(my_list)