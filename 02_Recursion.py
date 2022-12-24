########333Find Uppercase Letter in String#################
input_string_1 = "carlosZaragozaBeato"
input_string_2 = "CarlosZaragozabEato"
input_string_3 = "carloszaragozabeato"
#Iterative solution
def find_uppercase_iterative(input_str):
    for i in input_str:
        if i.isupper():
            return i
    return "No uppercase letter found"
#print(find_uppercase_iterative(input_string_1))
#print(find_uppercase_iterative(input_string_2))
#print(find_uppercase_iterative(input_string_3))
#Recursive solution
def find_uppercase_recursive(input_str, index = 0):
    if input_str[index].isupper():
        return input_str[index]
    if index == len(input_str) - 1:
        return "No uppercase letter found"
    if index < len(input_str) - 1:
        return find_uppercase_recursive(input_str, index + 1)
#print(find_uppercase_recursive(input_string_2))
##########################################################################
#####################Calculate String length #############################
input_str = "CarlosZaragozaBeato"
def iterative_string_length(input_str):
    value = 0
    for i in range(len(input_str)):
        value += 1
    return value

#print(iterative_string_length(input_str))
def recursive_string_length(input_str, index = 0):
    if index == len(input_str)-1:
        return index+1
    if index < len(input_str) - 1:
        return recursive_string_length(input_str, index+1)
    
def recursive_str_len(input_str): 
    if input_str == "":
        return 0
    return 1 + recursive_str_len(input_str[1:])   
#print(recursive_str_len(input_str))
#print(recursive_string_length(input_str))
###########################################################################
###############Count Consonants in String #################################
input_string_1 = "abc_de"
input_string_2 = "CarlosZaragozaBeato"

vowel = "aeiou"
def consonants_iterative(input_str):
    count = 0
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowel and input_str[i].isalpha():
            count+=1
    return count
#print(consonants_iterative(input_string_1))

def consonants_recursive(input_str):
    if input_str == "":
        return 0
    if input_str[0].lower() not in vowel and input_str[0].isalpha():
        return 1 +  consonants_recursive(input_str[1:])
    else:
        return consonants_recursive(input_str[1:])
#print(consonants_recursive(input_string_1))
############################################################################
#####################Product of Two Numbers#################################
x = 5
y = 3

def recursive_product_of_two_numbers(x, y):
    
    if x < y:
        return recursive_product_of_two_numbers(y, x)
    if y == 0:
        return 0 
    return x + recursive_product_of_two_numbers(x, y-1)

#print(recursive_product_of_two_numbers(x, y))
############################################################################