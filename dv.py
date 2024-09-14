#*Create a function* that takes an array, an index, and
#  a value as parameters. Inside the function, 
# use the insert method to insert the value at the specified index in the array. Return the modified array.



# 1. Function to insert a value at a specified index in an array
def insert_value(arr, index, value):
    arr.insert(index, value)
    return arr


# 2. Shopping cart program using array
shopping_cart = []

def add_item(item):
    shopping_cart.append(item)
    return shopping_cart

def remove_item(item):
    if item in shopping_cart:
        shopping_cart.remove(item)
    return shopping_cart

def update_item_quantity(item, quantity):
    # This assumes items are stored as tuples (item, quantity) in the cart
    for i in range(len(shopping_cart)):
        if shopping_cart[i][0] == item:
            shopping_cart[i] = (item, quantity)
            break
    return shopping_cart


# 3. Program to print the first 25 integers using while loop
def print_first_25_integers():
    i = 1
    while i <= 25:
        print(i)
        i += 1


# 4. Program to print the first 10 even numbers
def print_first_10_even_numbers():
    i, count = 1, 0
    while count < 10:
        if i % 2 == 0:
            print(i)
            count += 1
        i += 1
