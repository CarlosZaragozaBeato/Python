
def tabla_multiplicar(num:int):
    list = []
    for i in range(11):
        list.append(i*num)
    return list
    
print("La tabla de multiplicar de",5,"es:",tabla_multiplicar(5))
