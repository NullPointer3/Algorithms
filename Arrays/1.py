## 2D arrays

# a 2D array with 3 rows and 4 columns
arr = [
  [1,2,3,4],
  [5,6,7,8],
  [9,1,6,0]
]

# Accessing elements of an array
value = arr[1][2]
print(value)

# Iterating through a 2D array
for row in arr:
  for element in row:
    print(element, end=" ")
  print()
