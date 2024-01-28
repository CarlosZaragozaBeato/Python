# MAP FUNCTION
def addition(n):
    return n + n 



numbers = (1,2,3,4,5)
result = map(addition, numbers)
print(list(result))



numbers = (1,2,3,4,5)
result = map(lambda x:x+x, numbers)
print(list(result))



numbers1 = [1,2,3]
numbers2 = [4,5,6]
result = map(lambda x, y: x+y, numbers1, numbers2)
print(list(result))



l = ['sat', 'bat', 'cat', 'mat']
test = list(map(list, l))
print(test)




def double_even(num):
    if num % 2 == 0:
        return num * 2 
    else:
        return num 


numbers = [1,2,3,4,5]

result = list(map(double_even, numbers))
print(result)















