"""
1. Write a Python program to print the following string in a 
specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, 
How I wonder what you are! Up above the world so high, Like a diamond 
in the sky. Twinkle, twinkle, little star, How I wonder what you are" 
Output :
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
"""
def Exercise1():
    print("Twinkle, twinkle, little star,"       
		  "\n\tHow I wonder what you are! "		
		  "\n\t\tUp above the world so high,"	
		  "\n\t\tLike a diamond in the sky."
	      "\nTwinkle, twinkle, little star, "	
		  "\n\tHow I wonder what you are")
#Exercise1()

"""
2. Write a Python program to get the Python version you are using.
"""
import sys
def Exercise2():
       
    print("Python Version:")	
    print(sys.version)
    print("")
    print("Version Info:")
    print(sys.version_info)

#Exercise2()

"""
3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""

import datetime
def Exercise3():
    now = datetime.datetime.now()
    print("Current date and time:")
    print(now.strftime("%Y-%m-%d"))

#Exercise3()


"""
4. Write a Python program which accepts 
the radius of a circle from the user and 
compute the area. 
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""

import math
def Exercise4():
    radius = input("introduce the value of the radius: ")
    area = math.floor((math.pow(float(radius),2))*math.pi)
    print(area)
#Exercise4()

"""
5. Write a Python 
program which accepts the
 user's first and last name and print 
 them in reverse order with a space between them
"""
def Exercise5():
    firstName = input("introduce your first Name: ") 
    lastName = input("Introduce your last Name: ") 
    print(f"Last Name: {lastName} , First Name {firstName}")

Exercise5()
"""
6. Write a Python program which accepts 
a sequence of comma-separated numbers from 
user and generate a list and a tuple with 
those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

def Exercise6():
    lista = ['3','5','7','23']
    tupple=('3','5','7','23')
    for lst in lista: 
        print(lst)
    print("/************/")
    for tpl in tupple: 
        print(tpl)

Exercise6()

"""
7. Write a Python program to accept a 
filename from the user and print the extension 
of that. Go to the editor
Sample filename : abc.java
Output : java
"""
def Exercise7():
    fileName="abc.java"
    if(fileName.find('.')):
        extension = fileName.index('.')
        print(fileName[extension+1:len(fileName)])
    else:
        print("Please, introduce a valid file.")
Exercise7()

"""
8. Write a Python program to display 
the first and last colors from the following 
list. Go to the editor
color_list = ["Red","Green","White" ,"Black"]
"""

def Exercise8():
    color_list = ['Red','Green','White','Black']
    selectColor = int(input('Introduce the number that you want to pick: '))
    if(selectColor>=len(color_list)):
        print(f"enter a value less than: {len(color_list)}")
    else:
        print(color_list[selectColor])
    
Exercise8()


"""
9. Write a Python program to display 
the examination schedule. (extract the 
date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : 
The examination will start from : 11 / 12 / 2014
"""

def Exercise9():
    exam_st_date = (11,12,2014)
    print("The examination will start from: %i %i %i"%exam_st_date)    	

Exercise9()


"""
10. Write a Python program that 
accepts an integer (n) and computes 
the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615
"""

def Exercise10 ():
    value = int(input("Introduce a sample value"))
    value1 = int("%s" % value)
    value2 = int("%s%s" % (value,value))
    value3 = int("%s%s%s" % (value,value,value))

    print(value1+value2+value3)

Exercise10()