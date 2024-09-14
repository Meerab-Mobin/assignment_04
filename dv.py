#*Create a function* that takes an array, an index, and
#  a value as parameters. Inside the function, 
# use the insert method to insert the value at the specified index in the array. Return the modified array.



# 1. Function to insert a value at a specified index in an array
def insert_value(arr, index, value):
    arr.insert(index, value)
    return arr

