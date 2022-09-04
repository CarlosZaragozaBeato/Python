

def calculator(operation, val1, val2):
    if operation == "1":
        return suma(val1, val2)
    elif operation == "2":
        return subs(val1, val2)
    elif operation == "3":
        return division(val1, val2)
    elif operation == "4":
        return multiply(val1, val2)
    elif operation == "5":
        return module(val1, val2)
    elif operation == "6":
        return exponent(val1, val2)
    else:
        return False

    

def suma(val1, val2):
    return val1 + val2

def subs(val1, val2):
    return val1 - val2

def multiply(val1, val2):
    return val1 * val2

def division(val1, val2):
    return val1/val2

def module(val1, val2):
    return val % val2

def exponent(val1,val2):
    return val1 ** val2


print("1.Sum\n"+
      "2.Substract\n"+
      "3.Division\n"+
      "4.Multiplication\n"+
      "5.Module\n"+
      "6.Exponent")

option =  input("Please introduce a operation: ")
result = False
if(option == "1"
   or option== "2"
   or option == "3"
   or option == "4"
   or option == "5"):
    val1 = float(input("Introduce the first value: "))
    val2 = float(input("Introduce the second value: "))           
    result = calculator(option, val1, val2)

while(result!= False):
    option =  input("Please introduce a operation: ")
    val1= float(input("Introduce the first value: "))
    val2 = float(input("Introduce the second value: "))
    result = calculator(option, val1, val2)
    print("The value of the operation is", result)
    

