"""
If else 
age = int(input("How old are you?: "))

if age >= 100:
    print("You are a century old:")
elif age>= 18:
    print("You are an adult!")
elif age==0:
    print("You haven't been born yet!")
else:
    print("You are a child")
"""
"""
Logical Operators
choice = input("Enter your metric temp C/F: ")
temp = int(input("Enter the temperature: "))

if(choice.upper() == "C"):
    if(temp >= 0 and temp<=30):
        print("The temperature is good today!!!!")
    else:
        print("The temperature is bad today!!!!!")
elif (choice.upper() =="F"):
    if(temp >=32  and temp<=90):
        print("The temperature is good today!!!!")
    else:
        print("The temperature is bad today!!!!!")
else:
    print("Enter a valid choice C/F")
"""
"""
while loops
i=0
while i<=50:
    print(i)
    i+=1
"""
"""
1) Write a program to keep asking for a
number until you enter a negative number.
At the end, print the sum of all entered numbers.
number = 0

while number >=0:
    number = int(input("Please enter a number: "))
    print("the entered number was: ", number)

print("The last number entered was: ", number)
"""
"""
2) Write a program to ask for a name until the
user enters END. Print the name each time.
When you are done, print "I am done."

name = input("Enter a name please. \"To end the program insert END\"")

while name.upper() != "END":
    print("The name that you insert is ", name)
    name = input("Enter a name please. \"To end the program insert END\"")

print("I am done")
"""
"""
3) Test Average problem: (on powerpoint for while loops)

As long as there are more grades, add them to the total
Divide the total by the number of courses (each grade is a course)
Print the corresponding letter grade
Stop when the user enters a negative grade
grade = int(input("Enter a grade pls"))
course = 0
letter = ""
total = 0
while(grade>=0):
    if(grade <59):
        letter ="F"
    elif(grade <67 and grade >= 60):
        letter = "D"
    elif(grade< 69 and grade >= 68):
        letter = "D+"
    elif(grade< 73 and grade >= 70):
        letter = "C-"
    elif(grade< 77 and grade>= 74):
        letter = "C"
    elif(grade<80 and grade>=78):
        letter = "C+"
    elif(grade<83 and grade>=80):
        letter= "B-"
    elif(grade<87 and grade >= 84):
        letter = "B"
    elif(grade<90 and grade>= 87):
        letter ="B+"
    elif(grade < 97 and grade>=90):
        letter = "A-"
    elif(grade==100 and grade>=97):
        letter = "A"

    print("Your grade is: ", letter)
    print("*****************")
    total += grade
    course +=1
    grade = int(input("Enter your grade, please"))
print("The total is: ", total/course)
"""
#For Loop
"""
name = "Gaucho el fresco"
for i in name:
    print(i)
    
for i in range (100):
    if(i%3 == 0 and i%5 == 0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)
"""
#Nested Loops
"""
rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use?: ")
for i in range(rows):
    for j in range(columns):
        print(symbol, end = "")
    print()
"""
#break work
"""
while True:
    name = input("Enter your name: ")
    if name!= "":
        break
"""
#lists in python
"""
food = ["pizza", "hamburger", "hotdog","spaghetti", "pudding"]

food.append("ice cream")
food.remove("hotdog")
food.pop()
food.insert(0, "cake")
food.sort()
food.clear()
for i in food:
    print(i)
"""
#2D Lists
"""
drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]
print(food[0])
print(food[1])
print(food[2])
"""
#Tuples
"""
student = ("Bro", 23, "male")
print(student.count("Bro"))
print(student.index("male"))

for x in student :
    print(x)

if("Bro" in student):
    print("Bro is here")
"""
#Sets
"""
utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate","cup", "knife"}
utensils.add("napkin")
utensils.remove("fork")
dishes.remove("knife")
utensils.clear()
dishes.update(utensils)
print(utensils)
print(dishes)
dinner_table = utensils.union(dishes)
for x in dinner_table:
    print(x)
"""
#dictionaries
"""
capitals  = {
   'USA':'Washington DC',
   'India': 'New Dehli',
   'China': 'Beijing',
   'Russia': 'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA': 'Las Vegas'})
capitals.pop('China')
print(capitals['USA'])
print(capitals.get("Russia"))
capitals.clear()
print(capitals)
"""
#Indexing
"""
name = "bro Code"
if(name[0].islower()):
        name = name.capitalize()
first_name = name[:3].upper()
last_name = name[4:].lower()
last_character = name[-1]
print(first_name)
print(last_name)
print(last_character)
"""
#Functions
"""
def hello(first_name, last_name, age):
    print("Hello",first_name, last_name)
    print("You are ",age," years old")
    print("Have a nice day!!")

hello("Carrlaaaao", "Gaucho", 23)
"""
#return statement
"""
def multiply(number1, number2):
    return number1 * number2

y = multiply(10,5)
print(y)
print("The result is",multiply(50,10))
"""

#nested functions calls
"""
num = input("Enter a whale positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)
print(round(abs(float(input("Enter a wale positive number: ")))))
"""

#variable scope

"""
scope = The region that a variable is recognized.
            A variable is only available from inside the region it is created.
            A global variable and locally scoped versions of a variable can be created.
name = "Bro" #global scope(available inside & outside functions)
def display_name():
    name = "Code" #local scope (available only inside this function)
    print(name)
print(name)
display_name()
"""
#String format
"""
number = 1000
print("The number pi is {:.3f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:X}".format(number))
print("The number is {:E}".format(number))
animal = "cow"
item = "moon"
print("The "+animal+" jumped over the "+item)
print("The {} jumped over the {}".format(animal, item))
print("The {0} jumped over the {1}".format(animal,item))
print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))
text = "The {} jumped over the {}"
print(text.format(animal, item))
"""
#sort
"""
sort() method = used with lists
sort() funtion = used with iterables

students = (("Squidward","F",60),
            ("Sandy", "A",33),
            ("Patrick","D",36),
            ("Spongebob","B",20),
            ("Mr.Krab","C",78))

grade = lambda grades:grades[1]
#studenst.sort(key = age)
sorted_students = sorted(students, key=grade)
for i in sorted_students:
    print(i)
"""
#lambda
"""
lambda function = function written in 1 line using lambda keyword
                    accepts any number of arguments, but only has one expression
                    (think of it as a shortcut)
                    (useful if needed for a short period of time, throw-away)           

double = lambda x: x*2
multiply = lambda x, y: x*y
add = lambda x,y,z: x+y+z
full_name = lambda first_name, last_name: first_name +" "+ last_name
age_check = lambda age: True if age>= 18 else False
print(age_check(18))
print(double(5))
print(multiply(10,5))
print(add(1,2,85))
print(full_name("Carlos","Orgaz"))
"""
#Args
"""
def add(*stuff):
        sum = 0
        stuff = list(stuff)
        for i in stuff:
            sum += i
        return sum
print(add(1,2,3,4,5,6,7,8,9,0))
"""
#**kwargs
"""
def hello(**kwargs):
    #print("Hello "+kwargs['first']+" "+kwargs['last'])
    print("Heello",end = " ")
    for key, value in kwargs.items():
        print(value, end =" ")
hello(first_name = "CARLAO", last_name= "Orgaz", third_name="Gaucho")
"""
#Random Number
"""
import random
x = random.randint(1,6)
y = random.random()
myList= ['rock', 'paper', 'scissors']
z = random.choice(myList)
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)
print(x)
print(y)
print(z)
"""
#Exceptio Handling
"""
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero.")
except ValueError as e:
    print(e)
    print("Enter only number please!")
except Exception as e:
    print(e)
    print("Somenthing went wrong")
finally:
    print("The result is",result)
"""                    
#File Detection
"""
import os
path = "C:\\Users\\carlo\\Desktop\\test.txt"
if os.path.exists(path):
    print("That location exists: ")
    if os.path.isfile(path):
        print("That is a file: ")
    elif os.path.isdir(path):
        print("That direction is a directory: ")
else:
    print("That location doesn't exitss")
"""
#Read file
"""
try:
    with open("C:\\Users\\carlo\\Desktop\\test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
"""
#Write a file
"""
text = "CARLAO\nEl gaucho\nDe Anonimos"
with open("C:\\Users\\carlo\\Desktop\\test.txt","w") as file:
    file.write(
"""
#copy a file
"""
import shutil
shutil.copyfile("C:\\Users\\carlo\\Desktop\\test.txt","C:\\Users\\carlo\\Desktop\\test2.txt")
"""
#Move a file
"""
import os
source = "C:\\Users\\carlo\\Desktop\\test.txt"
destination = "C:\\Users\\carlo\\test.txt"

try:
    if os.path.exists(destination):
        print("The is already a file there")
    else:
        os.replace(source, destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source,"was not found")
"""
#DELETE a file
"""
import os
path = "C:\\Users\\carlo\\Desktop\\test.txt"

try:
    os.remove(path)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("That folder contains files")
"""
#Rock, paper and scissors
"""
import random
while True:

    print("1.Rock")
    print("2.Paper")
    print("3.Scissors")
    player = int(input("Enter an opcion: "))
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    state = "error"
    
    if player == 1 and computer == "paper":
        state = "computer wins"
    elif player ==1 and computer =="rock":
        state = "draw"
    elif player == 1 and computer =="scissors":
        state = "Player wins"
    elif player == 2 and computer == "paper":
        state = "draw"
    elif player ==2 and computer =="rock":
        state = "Player wins"
    elif player == 2 and computer =="scissors":
        state = "computer wins"
    elif player == 3 and computer == "paper":
        state = "Player Wins"
    elif player ==3 and computer =="rock":
        state = "computer wins"
    elif player == 3 and computer =="scissors":
        state = "draw"
        
    print(state)
    print("")
    continues = (input("Enter 1 if you want to continue\n introduce somenthing else to exit"))

    if(continues == "1"):
        continue
    else: break
"""
#Object Oriented Program
"""
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This car is driving")

    def stop(self):
        print("This car is stopped")

car_1 = Car("Chevy","Corvette", 2021, "blue")
car_2 = Car("Nissan","Gt-R", 2008, "gray")
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
car_1.drive()
car_1.stop()

print("")

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
car_2.drive()
car_2.stop()

Car.wheels = 2
print(car_1.wheels)
print(car_2.wheels)
"""
