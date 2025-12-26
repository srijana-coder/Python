#1.Declare your age as integer variable
age = 60

#2.Declare your height as a float variable
height = 12.4

#3.Declare a variable that store a complex number
com = 1 + 2j

#4.Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = 0.5 * base * height
print(f"The area of the triangle is {int(area)}")

#5.Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
print(f"The perimeter of the triangle is {int(a+b+c)}")

#6.Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("Enter the Length: "))
width = int(input("Enter the width: "))
print(f"The area of a rectangle is {length * width}")
print(f"The perimeter of a rectangle is {2* (length + width)}")

#7.Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
import math
radius = int(input("Enter the radius of a circle: "))
print(f"The area of the circle is {(math.pi * radius * radius):.2f}")
print(f"The circumference of the circle is {(2 * math.pi * radius):.2f}")

# #8.Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope1 = 2
y_intercept = -2
x_intercept = 2 / 2
print(f"Slope : {slope1}, x-intercept : {x_intercept} and y-intercept :{y_intercept}")

#9.Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math
(x1, y1) = (2, 2)
(x2, y2) = (6, 10)
slope2 = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
print(f"The slope between the points is {slope2:.2f}")
print(f"The Euclidean distance is {distance:.2f}")

#10.Compare the slopes in tasks 8 and 9.
if(slope1 > slope2):
    print(f"slope1: {slope1:.2f} is greater then slope2: {slope2:.2f}")
elif(slope2 > slope1):
    print(f"slope2: {slope2:.2f} is greater then slope1: {slope1:.2f}")
else:
    print(f"slope2: {slope2:.2f} is equal then slope1: {slope1:.2f}")

#11.Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
for x in range(-10, 11):
    y = x**2 +6*x + 9
    print(f"x = {x}, y = {y}")
    if y == 0:
        print(f"Found! y = 0 when x = {x}")
        break

#12.Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') > len('dragon'))

#13.Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

#14.Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('jargon' in 'I hope this course is not full of jargon')

#15.There is no 'on' in both dragon and python
print('on' not in 'python' and 'on' not in 'dragon')

#16.Find the length of the text python and convert the value to float and convert it to string
x = len('python')
print(f"The x: {x}")
y = float(x)
print(f"The float value of x: {y}")
z = str(y)
print(f"The float value into str: {z}")

#17.Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = 5
if(num%2 == 0):
    print(f"Hence, the given number: ({num}) is even ")

#18.Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
if(7 // 3 == int(2.7)):
    print("yes")

#19.Check if type of '10' is equal to type of 10
if(type('10') == type(10)):
    print("yes")
else:
    print("no")

#20. Check if int('9.8') is equal to 10
if(int(float('9.8')) == 10):
    print('yes')

#21.Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hour = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
print(f"Your weekly earning is {hour * rate}")

#22.Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
year = int(input("Enter number of years you have lived: "))
print(f"You have lived for {year * 365 * 24 * 60 * 60}")

#23.Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

print("\nTable:")
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 19 64")
print("5 1 5 25 125")


