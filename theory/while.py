#Example1
"""
x = 1
while x<3:
    print(x)
    x+=1

y = 100
while y>=0:
    print(y)
    y -=2
"""
#Fibonacci
num_one, num_two = 0,1
while num_two <= 1000:
    print(num_one, num_two, end = " ")
    num_one = num_one + num_two
    num_two = num_one + num_two
