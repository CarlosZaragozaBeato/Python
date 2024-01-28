try: 
    k = 5 // 0 
except ZeroDivisionErrror as e:
    print(f"Can't divide by zero: {str(e)}")
finally: 
    print("This is always executed")

try:
    raise NameError("Hi There")
except NameError as e:
    print(f"An Exception: {str(e)}")
    raise

