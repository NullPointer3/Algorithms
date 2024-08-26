## Appending into an array
def appendd(array, element: any):
    """A function that adds an element to an array without using append()"""
    # Create a new array with one more slot than the original
    new_array = [None] * (len(array) + 1)
    
    # Copy elements from the original array to the new array
    for i in range(len(array)):
        new_array[i] = array[i]
    
    # Add the new element at the end
    new_array[len(array)] = element
    
    # Return the new array
    return new_array

# Example usage:
my_list = [1, 2, 3]
my_list = appendd(my_list, 4)
print(my_list)
