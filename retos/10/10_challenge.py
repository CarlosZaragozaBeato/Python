""" 
  Reto #10
  EXPRESIONES EQUILIBRADAS
  Dificultad: MEDIA
 
  Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
  - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
  - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
  - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
  - Expresión no balanceada: { a * ( c + d ) ] - 5 }
"""


open_list = ["[","{","("] 
close_list = ["]","}",")"] 
  
def check(myStr): 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "Unbalanced"
    if len(stack) == 0: 
        return "Balanced"
    else: 
        return "Unbalanced"
  
  
string = "{[]{()}}"
print(string,"-", check(string)) 
  
string = "[{}{})(]"
print(string,"-", check(string)) 
  
string = "((()"
print(string,"-",check(string)) 
  

            


