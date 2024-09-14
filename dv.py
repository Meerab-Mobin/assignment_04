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


# 5. Function to calculate factorial of a number using while loop
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# 6. Program to remove negative numbers from an array
def remove_negative_numbers(arr):
    return [num for num in arr if num >= 0]

# 7. Function to calculate the sum of numbers in an array using while loop
def sum_of_array(arr):
    i, total = 0, 0
    while i < len(arr):
        total += arr[i]
        i += 1
    return total

# 8. Program to convert Celsius to Fahrenheit using while loop
def convert_celsius_to_fahrenheit(celsius_list):
    fahrenheit_list = []
    i = 0
    while i < len(celsius_list):
        fahrenheit = (celsius_list[i] * 9/5) + 32
        fahrenheit_list.append(fahrenheit)
        i += 1
    return fahrenheit_list

# 9. Program to remove odd numbers from an array
def remove_odd_numbers(arr):
    return [num for num in arr if num % 2 == 0]


# Example Usage:

# Task 1: Insert value
arr = [10, 20, 30]
arr_with_insert = insert_value(arr, 1, 25)
print(arr_with_insert)

# Task 2: Shopping Cart
add_item(("Apple", 2))
add_item(("Banana", 5))
update_item_quantity("Apple", 3)
remove_item(("Banana", 5))
print("Shopping Cart:", shopping_cart)

# Task 3: Print first 25 integers
print_first_25_integers()

# Task 4: Print first 10 even numbers
print_first_10_even_numbers()

# Task 5: Factorial of 5
print("Factorial of 5:", factorial(5))

# Task 6: Remove negative numbers
print("Without Negatives:", remove_negative_numbers([-1, 2, -3, 4, -5]))

# Task 7: Sum of array
print("Sum of array:", sum_of_array([1, 2, 3, 4, 5]))

# Task 8: Convert Celsius to Fahrenheit
print("Fahrenheit:", convert_celsius_to_fahrenheit([0, 20, 37]))

