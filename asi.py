# cheking conditional statements no is odd ,even

num:int = int(input("enter the number: "))

if num % 2 == 0 : 
    print("the number is even")
else: 
    print("the number is odd")


# to check the no. is posiive,negative or zero  
num2:int = int(input("the no : "))
if num2 > 0  :
  print("no is positive ")
elif num2 == 0 :
    print("the num is zero ")
else :
    print("no is negative ")
      
#no enter no is / by 2 or 3 or not / by both 
num3:int = int (input("enter no 3 "))
if num3 % 2 == 0 :
    print ("the num is / of 2 ")
elif num3 == 0 :
    print("no is itself divisible ")
else : 
    print("no is / by 3 ")
 

# user age if pakistani or 18 > can vote 
age:int = int(input("enter the age: "))
if age > 18 : 
    print("the user can vote ")
elif  age  != "pakistani "  :
    print(" user is not  pakistani ")
else : 
    print("the user can't vote ")


# Write a program that takes the age of a person as input and determines
#  whether they are a child (0-12 years), teenager (13-19 years), adult (20-59 years),
#  or senior citizen (60 years and above)

age2 :int = int (input("the age 2 is :"))
if age2 == 12 :
    print("the user is child  ")
elif age2 == 12_20 : 
    print("the user is teenager ")
elif age2 ==20_59 :
    print("the user is senior ")
else  :
    print("the user is senior citizen ")

 # Enter a month (as a number between 1 and 12).
 #   Print the number of days in that month. Assume a non-leap year.


