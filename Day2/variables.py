#1.Write a python comment saying 'Day 2: 30 Days of python programming'
#Day 2: 30 Days of python programming

#2. Declare a first name variable and assign a value to it
first_name = 'srijana'

#3.Declare a last name variable and assign a value to it
last_name = 'kamat'

#4.Declare a full name variable and assign a value to it
full_name = first_name + ' ' + last_name

#5.Declare a country variable and assign a value to it
country = 'Nepal'

#6.Declare a city variable and assign a value to it
city = 'Biratnagar'

#7.Declare an age variable and assign a value to it
age = 20

#8.Declare a year variable and assign a value to it
year = 2082

#9.Declare a variable is_married and assign a value to it
is_married = False

#10.Declare a variable is_true and assign a value to it
is_true = True

#11.Declare a variable is_light_on and assign a value to it
is_light_on = False

#12.Declare multiple variable on one line
first_name , last_name , country = 'Rajesh' , 'kamat' , 'Nepal'

#13.Printing the output
print(first_name)
print(last_name)
print(full_name)
print(country)
print(city)
print(age)
print(year)
print(is_married)
print(is_true)
print(is_light_on)

#14.Check the data type of all your variables using type() built-in function
print('\n')
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#15.Using the len() built-in function, find the length of your first name
print(len(first_name))
print(len(last_name))

#16.Compare the length of your first name and your last name
if(len(first_name) == len(last_name)):
    print('Both are of same length')

elif(len(first_name) >= len(last_name)):
    print("length of first name is longer than last name")

else:
    print("length of second is longer than first name ")

#17.Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#18.Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

#19.Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

#20.Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one

#21.Divide num_one by num_two and assign the value to a variable division
division = num_two / num_one

#22.Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one

#23. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

#24. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

#25.The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.

r = 30
area_of_circle = 3.14 * r ** 2
print(f'Area of circle: {area_of_circle:.4f}')

circum_of_circle = 2 * 3.14 * r
print(f'Circumference of Circle: {circum_of_circle}')

radius = int(input('Enter the radius: '))
area_of_circle = 3.14 * radius ** 2
print(f'Area: {area_of_circle}')

#26. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

first_name = input('Enter the first name: ')
last_name = input('Enter the Last name: ')
country = input('Enter the Country: ')
age = int(input('Enter the age: '))


print(f'Name: {first_name} {last_name}, country: {country}, age: {age}')





