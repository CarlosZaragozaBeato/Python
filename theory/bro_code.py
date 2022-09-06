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
#inheritance 
"""
class Animal: 
    alive = True
    def eat(self):
        print("This animal is eating")
    
    def slumber(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This animal is running")
        
class Fish(Animal):
    def swim(self):
        print("This animal is swimming")
        
rabbit = Rabbit()
fish = Fish()
animal = Animal()

rabbit.run()
fish.swim()
animal.slumber()
animal.eat()
"""
#Multilevel inheritance
"""
class Organism:
    alive = True
    def isAlive(self):
        print("This organism is alive")
        
class Animal(Organism):
    def eat(self):
        print("This animal is eating")
    
class Dog(Animal):
    def bark(self):
        print("This dog is barking")
    
organism = Organism()
organism.isAlive()

animal = Animal()
animal.isAlive()

dog = Dog()
dog.bark()
"""
#Multiple inheritance
"""
class Prey:
    def flee(self):
        print("This animal flees")
        
class Predator:
    def hunt(self):
        print("This animal is hunting")
        
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()

rabbit.flee()
hawk.hunt()
"""
#Method overriding
"""
class Animal:
    def eat(self):
        print("This animal is eating")
        
class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating")

rabbit = Rabbit()
rabbit.eat()
"""

#Chaining methods
"""
method chaining = calling multiple methods sequentially 
        each call performs an action on the same object and returns self
"""
"""
class Car:
    
    def turn_on(self):
        print("You start the engine")
        return self
    
    def drive(self):
        print("You drive the car")
        return self
    
    def brake(self):
        print("You step on the brakes")
        return self
    
    def turn_off(self):
        print("You turn off the car")
        return self

car = Car()
car.turn_on().drive().brake().turn_off()
"""
#super function
"""
super() = Function used to give access to the methods of a parent class
Returns a temporary object of a parent class when used
"""
"""
class Rectangle:
    def __init__ (self, length, width):
        self.length = length
        self.width = width
        
class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
        
    def area(self):
            return self.length * self.width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
        
    def volumn(self):
            return self.length * self.width * self.height

square = Square(3,3)
cube = Cube(3,3,3)

print(square.area())
print(cube.volumn())
"""
"""
Prevents a user from creating an object of that class
    compels a user to override abstract methods in a child class
    
    abstract class - a class which contains one or more abstract methods
    abstract method - a method that has a declaration but does not have an implementation
    
"""#Abstract classes
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    

class Car(Vehicle):
    def go (self):
        print("You drive the car")
    
    def stop(self):
        print("This car is stopped")
        
class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
        
    def stop(self):
        print("This motorcycle is stopped")
car = Car()
motorcycle = Motorcycle()

car.go()
car.stop()
motorcycle.go()
motorcycle.stop()
"""

""" # as arguments
class Car:
    color = None
    
class Motorcycle:
    color = None
    
def change_color(vehicle, color):
        vehicle.color = color
        
car_1 = Car()
car_2 = Car() 
car_3 = Car()

change_color(car_1, "red")
change_color(car_2, "White")
change_color(car_3, "Yellow")

print(car_1.color)
print(car_2.color)
print(car_3.color)
"""

"""
Duck typing = concept where the class of an object is less importan than the methods
class type is not checked if minimum methods/attributes are present 
"If it walks like a duck, and it quacks like a duck, then it must be a duck"
class Duck:
    def walk(self):
        print("This duck is walking")
        
    def talk(self):
        print("This duck is qwuacking")
        
class Chicken:
    def walk(self):
        print("This chicken is walking")
        
    def talk(self):
        print("This chicken is clucking")
        
class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter") 
        
duck = Duck()
chicken = Chicken()
person = Person()

duck.talk()
duck.walk()
chicken.talk()
person.catch(duck)
"""

"""#Walrus operator

walrus operator :=

new to Python 3.8
assignment expression aka walrus operator
assigns values to variables a part of a large expression

foods = lists()
while True:
 food = input("What food do you like?:")
    if food == "quit":
        break
    food.append(food)
foods = list()
while food := input("What food do yoy like") != "quit":
    foods.append(food) 
print(foods)
"""
"""
# MAP () = Applies a function to each item in an iterable (list, tuple, etc.)

map(function, iterable)
store = [("shirt", 20.00),
        ("pants",25.00),
        ("jacket", 50.00),
        ("socks", 10.00)]

to_euros = lambda data:(data[0], data[1] * 0.82)
# to_dollars = lambda data: (data[0], data[1] / .82)

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)
"""
"""
#Filter
filter () ) creates a collection of elements from an iterable for which a function returns

filter(function, iterable)
friends = [("Rachel",29),
          ("Monica",28),
          ("Phoebe",27),
          ("Joey",26),
          ("Chandler",31),
          ("Ross",30)]

age = lambda data:data[1] >=28

old_buddies = list(filter(age, friends))

for i in old_buddies:
    print(i)
"""

"""
reduce() = apply a function to an iterable and reduce it to a single cumulative value.
    performs function on first two elements and repeats process util 1 value remains

reduce(function, iterable)

import functools

letters = ["H","E","L","L","O"]

word = functools.reduce(lambda x, y,: x + y, letters)
print(word)
"""

"""
#list comprehension = a way to create a new list with less sintax can mimic certain lambda
functions, easier to read
list = [expression for item in iterable]
list = [expression for item in iterable if condition]
list = [expression if/else for item in iterable]

students = [100,90,80,70,60,50,40,30,20,10,0]
#passed_students = listt(filter(lambda x: x >= 60, students))
#passed_students = [i for i in students if  i >= 60]

passed_students = [i if i >= 60 else "FAILED" for i in students]
print(passed_students)
"""
"""
dictionary comprehension = create dictionaries using an expression can replace for loops 
and certain lambda functions

dictionary = {key: expression for (key, value) in iterable}
dictionary = {key: expresion for (key,value) in iterable if conditional}
dictionary = {key: (if/ else) for (key, value) in iterable}
dictionary = {key: function(value) for(key, value)in iterable}

cirties_in_F = {'New York':32,
                'Boston':75,
                'Los Angeles': 100,
                'Chicago':50}
cities_in_C = {key:round((value - 32) * (5/9)) for (key, value) in cirties_in_F.items()}
print(cities_in_C)

weather = {'New York':"snowing",
            'Boston':"sunny",
            'Los Angeles': "sunny",
            'Chicago':"cloud"}

sunny_weather = {key:value for (key, value) in weather.items() if value =="sunny"}
print(sunny_weather) 
"""

"""
# zip(iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc).
    creates a zip object with paired elements stored in tuples for each element
    
usernames = ["Dude", "Bro", "Mister"]
passwords = ["passwords", "abc123", "guest"]

users = dict(zip(usernames, passwords))
print(type(users))

for key, value in users.items():
    print(key,":",value)
"""

"""
Python interpreter sets "special variables", one of which is __name__
Python will assign the __name__ variable a value of '__main__' if it's
the initial module being run

def main():
    print("heelloo")
    
if __name__ == "__main__":
    main()
"""
"""Time
import time

print(time.ctime(0))
print(time.time())
print(time.ctime(time.time()))
time_object = time.localtime()
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)
"""
"""
    cpu bound = program/task spends most of it's time waiting for internal events
    use multiprocessing

    io bound = program/task spends most of it's time waiting for external events
    use multithreading
    
    import threading
import time

def eat_breakfast():
    print("Starting to eat the breakfast")
    time.sleep(2)
    print("You eat breakfast")


def drink_coffee():
    print("Starting to drink the coffee")
    time.sleep(1)
    print("You drink coffee")

eat_breakfast()
drink_coffee()
"""
"""
daemon thread = a thread that runs in the background, not important for program the run
your program will not wait for daemon threads to complete before existing
non-daemon threads cannot normally be killed, stay alive until task is complete

ex, background tasks, garbage collection, waiting for input, long running process

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for:", count,"seconds")
        
x = threading.Thread(target = timer, daemon = True)
x.start()

x.setDaemon(True)
print(x.isDaemon())
answer = input("Do you wish to exit?")
"""
"""
Python Multiprocessing 

multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for thread
multiprocessing = better for cpu bound tasks (heavy cpu usage)
multithreading = better for io bound tasks(waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count <num:
        count +=1
        
def main():
    a = Process(target = counter, args = (10000000,))
    b = Process(target = counter, args = (100000,))
    c = Process(target = counter, args = (10000,))

    a.start()
    b.start()
    c.start()
    
    a.join()    
    b.join()
    c.join()
    print("finished in:",time.perf_counter(),"seconds")
    
if __name__ == '__main__':
    main()
"""
"""
tkinter 
from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Carlos first Gui Program")

#icon = PhotoImage(file = "logo.png")
#window.iconphoto(True, icon)
window.config(background="black")

window.mainloop()
"""
"""
Labels
label = an area widget that holds text and/or an image within a window
from tkinter import *



#photo = PhotoImage(file = 'person.png')
window = Tk()

label = Label(window,
                text = "Bro, do you even code?",
                font = ('Arial',40,'bold'),
                fg = '#00ff00',
                bg = 'black',
                relief = RAISED,
                bd = 10, 
                padx = 20,
                pady = 20,
                compound  = 'bottom')
label.pack()
window.mainloop()
"""
"""
button = you click it, the it does stuff

from tkinter import *

count = 0

def click():
    global count
    count += 1
    print(count)

window = Tk()

button = Button(window,
                text = "click me",
                command = click,
                font = ("Comic Sans",30),
                fg = "#00ff00",
                bg = "black",
                activeforeground="#00ff00",
                activebackground="black",
                state = ACTIVE,)


button.pack()

window.mainloop()
"""
"""
entry widget = textbox that accepts a single line of user input

from tkinter import *

def submit():
    username = entry.get()
    print("Hello", username)
    
def delete():
    entry.delete(0, END)
    
def backspace():
    entry.delete(len(entry.get())-1,END)

window = Tk()

entry = Entry(window,
              font = ("Arial", 50),
                fg ="#00ff00",
                bg = "black")

entry.pack(side = LEFT)
submit_button = Button(window, text = "submit",command = submit)
submit_button.pack(side = RIGHT)

window.mainloop()
"""
"""
Checkbox
from tkinter import *

def display():
    if x.get() ==1:
        print("You agree!")
    else:
        print("You don't agree:(")

window = Tk()

x = IntVar()

check_button = Checkbutton(window,
                           text = "I agree to somenthing",
                           variable = x,
                           onvalue = 1,
                           offvalue = 0,
                           command = display,
                           font= ("Arial",20),
                           fg = "#00ff00",
                           bg="black",
                           activeforeground="#00ff00",
                           activebackground= "black")
check_button.pack()
window.mainloop()
"""

"""
radio button = similar to checkbox, but yoy can only select one from a group

from tkinter import *

food = ["pizza","hamburger","hotdog"]


def order():
    if(x.get() == 0): 
        print("You ordered pizza!")
    elif(x.get()==1):
        print("You ordered hamburger!")
    elif(x.get()==2):
        print("You ordered hotdog!")


window = Tk()

x = IntVar()
for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text = food[index], variable =x,
                              value = index,
                              command = order)
    radiobutton.pack(anchor = W)
    
window.mainloop()
"""

"""
 GUI scale
 from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+ " degrees C")

window = Tk()


scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL, #orientation of scale
              font = ('Consolas',20),
              tickinterval = 10, #adds numeric indicators for value
              #showvalue = 0, #hide current value
              resolution = 5, #increment of slider
              troughcolor = '#69EAFF',
              fg = '#FF1C00',
              bg = '#111111'

              )
scale.set(((scale['from']-scale['to'])/2)+scale['to']) #set current value of slider

scale.pack()


button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()
"""
"""
Gui ListBox
listbox = A listing of selectable text items within it's own container

def submit():

    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("You have ordered: ")
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())

from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia",35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

frame = Frame(window)
frame.pack()

submitButton = Button(frame,text="submit",command=submit)
submitButton.pack(side=LEFT)

addButton = Button(frame,text="add",command=add)
addButton.pack(side=LEFT)

deleteButton = Button(frame,text="delete",command=delete)
deleteButton.pack(side=LEFT)

window.mainloop()
"""
"""
color chooser

from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    colorHex = color[1]
    window.config(bg=colorHex)
    
window = Tk()
window.geometry("420x420")
button = Button(text='click me',command=click)
button.pack()
window.mainloop()
"""
"""
Message box
from tkinter import *
from tkinter import messagebox #import messagebox library

def click():
    messagebox.showinfo(title='This is an info message box',message='You are a person')
    messagebox.showwarning(title='WARNING!',message='You have A VIRUS!!!!')
    messagebox.showerror(title='ERROR!',message='something went wrong :(')
    
    if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do the thing?'):
        print('You did a thing!')
    else:
        print('You canceled a thing! :(')

    if messagebox.askretrycancel(title='ask ok cancel',message='Do you want retry the thing?'):
        print('You retried a thing!')
    else:
        print('You canceled a thing! :(')

    if messagebox.askyesno(title='ask yes or no',message='Do you like cake?'):
        print('I like cake too :)')
    else:
        print('Why do you not like cake? :(')

    answer = messagebox.askquestion(title='ask question',message='Do you like pie?')
    if(answer == 'yes'):
        print('I like pie too :)')
    else:
        print('Why do you not like pie? :(')

    answer = messagebox.askyesnocancel(title=' Yes no cancel',message='Do you like to code?',icon='question')
    if(answer==True):
        print("You like to code :)")
    elif(answer==False):
        print("Then why are you watching a video on coding?")
    else:
        print("You have dodged the question ")

window = Tk()

button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()
"""

"""
# text widget = functions like a text area, you can enter multiple lines of text
from tkinter import *

def submit():
    input = text.get("1.0",END)
    print(input)
    
window = Tk()
text = Text(window,
            bg="light yellow",
            font=("Ink Free",25),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="purple")
text.pack()
button = Button(window,text="submit",command=submit)
button.pack()
window.mainloop()
"""

"""
Python GUI open a file (filedialog)
from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Carlo\\Desktop\\Python",
                                          title="Open file okay?",
                                          filetypes= (("text files","*.txt"),
                                          ("all files","*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()
"""

"""
Python GUI save a file (filedialog) 

from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Carlo\\Desktop\\",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    
    if file is None:
        return

    filetext = str(text.get(1.0,END))
    #filetext = input("Enter some text I guess: ") //use this if you want to use console window
    file.write(filetext)
    file.close()
    
window = Tk()
button = Button(text='save',command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()
"""

"""
Python GUI menubar 

from tkinter import *

def openFile():
    print("File has been opened!")
def saveFile():
    print("File has been saved!")
def cut():
    print("You cut some text!")
def copy():
    print("You copied some text!")
def paste():
    print("You pasted some text!")
    
window = Tk()



menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile,compound='left')
fileMenu.add_command(label="Save",command=saveFile,compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,compound='left')

editMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)


window.mainloop()
"""


"""
Python GUI frames 
# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
frame.pack()

Button(frame,text="W",font=("Consolas",25),width=3).pack(side=TOP)
Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)

window.mainloop()
"""

"""
Python how to: open new window
from tkinter import *

def create_window():
    new_window = Tk()       #Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
                            #Tk() = new independent window
    #old_window.destroy()   #close out of old window

old_window = Tk()

Button(old_window,text="create new window",command=create_window).pack()

old_window.mainloop()
"""
"""
Python how to: add window tabs
from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) #widget that manages a collection of windows/displays

tab1 = Frame(notebook) #new frame for tab 1
tab2 = Frame(notebook) #new frame for tab 2

notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")
notebook.pack(expand=True,fill="both")  #expand = expand to fill any space not otherwise used
                                       #fill = fill space on x and y axis
Label(tab1,text="Hello, this is tab#1",width=50,height=25).pack()
Label(tab2,text="Goodbye, this is tab#2",width=50,height=25).pack()

window.mainloop()
"""

"""
Python GUI grid 
from tkinter import *

#grid() = geometry manager that organizes widgets in a table-like structure in a parent widget

window = Tk()

titleLabel = Label(window,text="Enter your info",font=("Arial",25)).grid(row=0,column=0,columnspan=2)

firstNameLabel = Label(window,text="First name: ",width=20,bg="red").grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=1,column=1)

lastNameLabel = Label(window,text="Last name: ",bg="green").grid(row=2,column=0)
lastNameEntry = Entry(window).grid(row=2,column=1)

emailLabel = Label(window,text="email: ",bg="blue").grid(row=3,column=0)
emailEntry = Entry(window).grid(row=3,column=1)

submitButton = Button(window,text="Submit").grid(row=4,column=0,columnspan=2)

window.mainloop()
"""

"""
Python GUI progress bar 

from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 100
    download = 0
    speed = 1
    while(download<GB):
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" GB completed")
        window.update_idletasks()
    
window = Tk()

percent = StringVar()
text = StringVar()
bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

percentLabel = Label(window,textvariable=percent).pack()
taskLabel = Label(window,textvariable=text).pack()

button = Button(window,text="download",command=start).pack()

window.mainloop()
"""

"""
Python GUI canvas
# canvas =  widget that is used to draw graphs, plots, images in a window
from tkinter import *
window = Tk()
canvas = Canvas(window,height=500,width=500)

#canvas.create_line(0,0,500,500,fill="blue",width=5)
#canvas.create_line(0,500,500,0,fill="red",width=5)
#canvas.create_rectangle(50,50,250,250,fill="purple")
#points = [250,0,500,500,0,500]
#canvas.create_polygon(points,fill="yellow",outline="black",width=5)
#canvas.create_arc(0,0,500,500,style=PIESLICE,start=270,width=5)

canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
canvas.create_oval(190,190,310,310,fill="white",width=10)
canvas.pack()

window.mainloop()
"""

"""
Python GUI keyboard events
from tkinter import *

def doSomething(event):
    #print("You pressed: " + event.keysym)
    label.config(text=event.keysym)

window = Tk()

window.bind("<Key>",doSomething)

label = Label(window,font=("Helvetica",100))
label.pack()

window.mainloop()
"""

"""
Python GUI mouse events
from tkinter import *

def doSomething(event):
    print("Mouse coordinates: " + str(event.x)+","+str(event.y))

window = Tk()

window.bind("<Button-1>",doSomething) #left mouse click
#window.bind("<Button-2>",doSomething) #scroll wheel
#window.bind("<Button-3>",doSomething) #right mouse click
#window.bind("<ButtonRelease>",doSomething)#mousebutton release
#window.bind("<Enter>",doSomething) #enter the window
#window.bind("<Leave>",doSomething) #leave the window
#window.bind("<Motion>",doSomething) #Where the mouse moved
window.mainloop()
"""

"""
Python drag & drop GUI
from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)
    
window = Tk()

label = Label(window,bg="red",width=10,height=5)
label.place(x=0,y=0)

label2 = Label(window,bg="blue",width=10,height=5)
label2.place(x=100,y=100)

label.bind("<Button-1>",drag_start)
label.bind("<B1-Motion>",drag_motion)

label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)

window.mainloop()
"""

"""
Python move images w/ keys


#------------move widgets on window-------------

from tkinter import *

def move_up(event):
   label.place(x=label.winfo_x(), y=label.winfo_y()-10)
def move_down(event):
   label.place(x=label.winfo_x(), y=label.winfo_y()+10)
def move_left(event):
   label.place(x=label.winfo_x()-10, y=label.winfo_y())
def move_right(event):
   label.place(x=label.winfo_x()+10, y=label.winfo_y())
   
   
window = Tk()
window.geometry("500x500")

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

label = Label(window, text="CAR")
label.place(x=0,y=0)


window.mainloop()

#-------------move images on canvas-------------
from tkinter import *

def move_up(event):
   canvas.move(myimage,0,-10)
def move_down(event):
   canvas.move(myimage,0,10)
def move_left(event):
   canvas.move(myimage,-10,0)
def move_right(event):
   canvas.move(myimage,10,0)

window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

canvas = Canvas(window,width=500,height=500)
canvas.pack()

photoimage = PhotoImage(file='racecar.png')
myimage = canvas.create_image(0,0,image = photoimage,anchor=NW)
"""
"""
Python animations
from tkinter import *
import time


WIDTH = 500
HEIGHT = 500
xVelocity = 1
yVelocity = 1
window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()


background_photo = PhotoImage(file='space.png')
background = canvas.create_image(0,0,image=background_photo,anchor=NW)

photo_image = PhotoImage(file='ufo.png')
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        xVelocity = -xVelocity
    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
        yVelocity = -yVelocity
    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)
    
window.mainloop()
"""

"""
Python multiple animations 
from tkinter import *

import time


class Ball:
    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coordinates = self.canvas.coords(self.image)

        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.xVelocity = -self.xVelocity
        if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.yVelocity = -self.yVelocity

        self.canvas.move(self.image,self.xVelocity,self.yVelocity)


window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,"white")
tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
basket_ball = Ball(canvas,0,0,125,3,5,"orange")
bowling_ball = Ball(canvas,0,0,75,2,1,"black")


while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    bowling_ball.move()
    window.update()
    time.sleep(0.01)
    
window.mainloop()
"""

"""
Python clock program
from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)


window = Tk()

time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
time_label.pack()

day_label = Label(window,font=("Ink Free",25,"bold"))
day_label.pack()

date_label = Label(window,font=("Ink Free",30))
date_label.pack()

update()

window.mainloop()
"""

"""
Python send an email
import smtplib

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "password123"
subject = "Python email test"
body = "I wrote an email! :D"

# header
message = f""From: Snoop Dogg{sender}
To: Nicholas Cage{receiver}
Subject: {subject}
{body}

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")
"""

"""
Python run with command prompt


print("Hello World!")

name = input("What's your name?: ")

print("Hello "+name)
"""
"""
Python pip 
# 
# Python pip
# 
#       pip = package manager for packages and modules from Python Package Index
#
#       included for Python versions 3.4+
#       open command prompt
#
#       help:                                          pip
#       check:                                       pip --version
#       update:                                     pip install --upgrade pip
#       installed packages:                pip list
#       check outdated packages:    pip list --outdated
#       update a package:                  pip install "package name" --upgrade
#       install a package:                    pip install "package name"
#
# 
"""

"""
Python calculator app
from tkinter import *

def button_press(num):
    
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""

def clear():
    
    global equation_text
    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Calculator program")
window.geometry("500x500")

equation_text = ""
equation_label = StringVar()


label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35,
                 command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35,
                 command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35,
                 command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35,
                 command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35,
                 command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35,
                 command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35,
                 command=lambda: button_press(7))
button7.grid(row=2, column=0)


button8 = Button(frame, text=8, height=4, width=9, font=35,
                 command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35,
                 command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35,
                 command=lambda: button_press(0))
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=4, width=9, font=35,
                 command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35,
                 command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35,
                 command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35,
                 command=lambda: button_press('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=4, width=9, font=35,
                 command=equals)
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=4, width=9, font=35,
                 command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

clear = Button(window, text='clear', height=4, width=12, font=35,
                 command=clear)
clear.pack()

window.mainloop()
"""
"""
Python text editor program

import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    color = colorchooser.askcolor(title="pick a color...or else")
    text_area.config(fg=color[1])
    
def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))
    
def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)
    
def open_file():
    file = askopenfilename(defaultextension=".txt",
                           file=[("All Files", "*.*"),
                                 ("Text Documents", "*.txt")])
    
    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            text_area.delete(1.0, END)

            file = open(file, "r")

            text_area.insert(1.0, file.read())

        except Exception:
            print("couldn't read file")

        finally:
            file.close()
            
def save_file():
    file = filedialog.asksaveasfilename(initialfile='unititled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])
    

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")

            file.write(text_area.get(1.0, END))

        except Exception:
            print("couldn't save file")

        finally:
            file.close()
            
def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")
    
def about():
    showinfo("About this program", "This is a program written by YOUUUUU!!!")

def quit():
    window.destroy()
    
    
window = Tk()
window.title("Text editor program")
file = None

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()

color_button = Button(frame, text="color", command=change_color)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()
"""
"""
Python Tic Tac Toe game
from tkinter import *
import random

def next_turn(row, column):
    
    global player
    
    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))
            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))
            elif check_winner() == "Tie":
                label.config(text="Tie!")
                
            else:
                
                buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
        
        

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    
    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False
    
def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1


    if spaces == 0:
        return False
    else:
        return True

def new_game():

    global player

    player = random.choice(players)

    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")



window = Tk()
window.title("Tic-Tac-Toe")
players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=player + " turn", font=('consolas',40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()
"""

"""
Python snake game
from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:

    def __init__(self):

        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")



def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")


window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
"""


