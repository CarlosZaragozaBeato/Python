"""
    # match case -> Simplified if statement 

a = 2

if a == 1: print('1')
elif a == 2: print('2')
elif a == 3: print('3')

match a:
    case 0: print('0')
    case 1: print('1')
    case 2: print('2')
    case 3: print('3')
"""
"""
#Ternary operator / single line if statement

day_time = True

greet = 'hello' if day_time else 'goodbye'

print(f"Somenthing basic: {'hello' if day_time else 'goodbye'}")
"""
""" 
#chain comparisions
min_value = 5
max_value = 10
value = 7

if  min_value < value < max_value:
        print('Value inside boundaries')
"""
""" 
# clamp some values between a minimum and a maximum value

min_value = 0
max_value = 500
value = 50

while True:
    value += 0.05

    value = max(min_value, min(value, max_value))
    print(value)
"""

"""
eval + excec
text_string = 'hello'

# print(eval('test_string.upper()))
# print(excel('test_string.lower()))
# print(test_string)

for operation in ['upper', 'lower', 'casefold', 'title']:
    print(eval(f'text_string.{operation}()'))
    
    dict.get
test_dict = {'a':1, 'b':2, 'c':3, 'd':4}
if test_dict.get('a'):
    print(test_dict.get('a'))
"""

"""
list flattening with sum()


"""

test_list = [[1,2,3],[4,5,6,7], [8,9]]

print(sum(test_list, [1000]))