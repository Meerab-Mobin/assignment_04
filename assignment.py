#asignment_04
# problem no 1:your age 
def your_age  (current_year:int, birth_year:int):
    
    result_age  = current_year - birth_year
    return  result_age




print("Age calculator!")
birth_year=int(input("Enter your birth_year:"))
current_year = 2024
print("Your age is:",your_age(current_year,birth_year))



#area of rectangle
def area (lenght:int , width:int):
   
    area= (lenght )* (width)
    print(area)

print(area)
lenght=int(input("enter the lenght of rectangle"))
width=int(input("enter width of ractangle "))

print("area is :",area (lenght , width) )


#area of circle 
def area2 (r:int, pie_of_circle:int):
    
    area2 = (r**2)*(pie_of_circle)
    print(area2)
 

print(area2)
r = float(input(" enter the radius of the circle: "))
pie_of_circle = float(input("enter the pie:   "))

print("area2 is :" , area2 (r , pie_of_circle ))

#area of cube
#area=6a**2
def cube (a:int ,v:int ):
   
    cube =(a**2)*v
    print(cube)

print(cube)
a =float(input("a is equal to: "))
v=int(6)
print("cube is : ", cube (a , v) )


#temp from F to C
def celsius1 (FRY:int ):
    celsius1 =(5) /(9)*(FRY)-(32)
    print(celsius1)

print(celsius1)
FRY=float(input("temp in F:  "))
print("celsius is : ", celsius1 ( FRY) )



#calculate a percentage
def percentage(obtain_number:int , total_number: int ):
    percentage = (obtain_number)/(total_number)*(100)
    print(percentage)

print(percentage)
obtain_number =float(input("obtain number:  "))
total_number = float(input("total number:  "))

print("percentage is " , (obtain_number ,total_number ))


#seconds into minutes
def second (variable:int ):
    seconds=(variable)/(60)
    print(seconds)
 
print(second)
variable=int(input("variables:  "))
print("second is ", second (vaiables ))




#minutes into seconds
def minutes(variable2:int):
    minutes= (variable2)*(60)
    print(minutes)

print(minutes)
variable2=int(input("variable:  "))
print("minutes are ", minutes(variable2))

#volume of a cylinder
#formula :pie r saqure h
def volume (height:int ,r:float ,pie:float ):
   
    volume =(pie)*(r)**2 *(height)
    print (volume)

print(volume)
height = float(input("heightof a cylinder: "))
r = float(input("r :  "))
pie =float(input("pie:  ")) 
print("volume is ", volume)



#calculate the BMI
def BMI ():
    height =float(input("height: "))
    weight =float(input("weight: "))
    BMI =(weight)/(height)**2
    print(BMI)       
 
 
 


