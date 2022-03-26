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



"""
11. Write a Python program to print the documents
(syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
"""


def Exercise11():
    number= float(input("Introduce a number: "))
    try:
        print(abs(number))
    except:
        print("Please introduce a number.")

Exercise11()

"""
12. Write a Python program to print 
the calendar of a given month and year.
Note : Use 'calendar' module.
"""






"""
13. Write a Python program to print the following 'here document'. Go to the editor
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
"""






"""
14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""





"""
15. Write a Python program to get the volume of a sphere with radius 6.
"""





"""
16. Write a Python program to 
get the difference between a given
number and 17, if the number is greater
than 17 return double the absolute difference
""" 





"""
17. Write a Python program to test whether
a number is within 100 of 1000 or 2000.
"""





"""
18. Write a
Python program to calculate 
the sum of three given numbers, 
if the values are equal then return three 
times of their sum.
"""




"""
19. Write a Python program to get 
a new string from a given string where 
"Is" has been added to the front.
If the given string already begins 
with "Is" then return the string unchanged.
"""





"""
20. Write a Python program to get a string which 
is n (non-negative integer) copies of a given string.
"""





"""
21. Write a Python program to find whether 
a given number (accept from the user) 
is even or odd, print out an appropriate message to the user.
"""




"""
22. Write a Python program to count the number 4 in a given list.
"""



"""
23. Write a Python program to get the n (non-negative integer) copies
of the first 2 characters of a given string. 
Return the n copies of the whole string if the 
length is less than 2
"""


"""
24. Write a Python 
program to test whether a passed 
letter is a vowel or not.
"""




"""
25. Write a Python program to check whether a specified
 value is contained in a group of values.
"""


"""
26. Write a Python program to create a
histogram from a given list of integers.
"""



"""
27. Write a Python program to concatenate
all elements in a list into a string and return it.
"""


"""
28. Write a Python program to print all even numbers
from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence. Go to the editor
Sample numbers list :

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 
	597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 
	248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 
	81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
"""





"""
29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Go to the editor
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
"""


"""
30. Write a Python program that will accept the base and
height of a triangle and compute the area.
"""
