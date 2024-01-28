import functools 

lst [1,3,5,4,6,7]

print("The maximum element of the list is: ", end="")

print(functools.reduce(lambda a, b: a if a > b else b, lst))
