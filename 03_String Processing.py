##################################Look-and-Say Sequence############################
def next_number(string):
    result = []
    i = 0
    while i< len(string):
        count = 1
        while i+1 < len(string) and string[i] == string[i+1]:
            i+=1
            count+=1
        result.append(str(count) + string[i])
        i += 1
    return ''.join(result)
#s = "1211"
#print(next_number(s))        
##################################################################################
#################################Spreadsheet Encoding#############################
def spreadsheet_encode_column(col_str):
    num = 0
    count = len(col_str) - 1
    for s in col_str:
        num += 26**count * (ord(s) - ord('A') +1)
        count -=1
    return num   
#print(spreadsheet_encode_column("A"))
#print(spreadsheet_encode_column("AA"))
#print(spreadsheet_encode_column("ZZ"))
##################################################################################
#################################Is Palindrome####################################
s = "Was it a cat i saw?"
def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        while not s[i].isalnum() and i<j:
            i+=1
        while not s[j].isalnum() and i<j:
            j-=1
        if s[i].lower() != s[j].lower():
            return False
        i+=1
        j-=1
    return True
#print(is_palindrome(s))
##################################################################################
#################################Is Anagram#######################################
s1 = "fairy tales"
s2 = "rail safety"

s1 = s1.replace(" ","").lower()
s2 = s2.replace(" ","").lower()

def is_anagram(s1, s2):
    ht = dict()
    if len(s1) != len(s2): return False
    
    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1
    for i in ht:
        if ht[i] != 0: return False
    return True
#print(is_anagram(s1,s2))
##################################################################################
#Is Palindrome Permutation
palin_perm = "Tact Coa"
not_paln_perm = "This is not a palidrome permutation"

def is_palidrome(input_str):
    input_str = input_str.replace(" ", "").lower()
    d = dict()
    for i in input_str:
        if i in d:
            d[i] +=1
        else:
            d[i] = 1
    odd_count = 0
    for K,v in d.items():
        if v % 2!= 0 and odd_count == 0:    
            odd_count += 1
        elif v%2 !=0 or odd_count != 0:
            return False
    return True    
#print(is_palidrome(not_paln_perm))
##################################################################################
#Check Permutation
is_permutation_1 = "god"
is_permutation_2 = "dog"
not_permutation_1 = "not"
not_permutation_2 = "top"

def is_perm_1 (str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()
    if len(str_1) != len(str_2):
        return False
    
    str_1 = ''.join(sorted(str_1))
    str_2 = ''.join(sorted(str_2))
    
    n = len(str_1)
    for i in range(n):
        if str_1[i] != str_2[i]:
            return False  
    return True

def is_perm_2(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()
    
    if len(str_1) != len(str_2):
        return False

    d = dict()
    
    for i in str_1:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1
    for i in str_2:
        if i in d:
            d[i] -= 1
        else: 
            d[i] = 1
    return all(value == 0 for value in d.values())
#print(is_perm_2(is_permutation_1, is_permutation_2))    
#print(is_perm_2(not_permutation_1, not_permutation_2))    
#print(is_perm_1(is_permutation_1, is_permutation_2))    
#print(is_perm_1(not_permutation_1, not_permutation_2))    
##################################################################################
#is Unique
import string as s
def normalize(str):
    str = str.replace(" ","")
    return str.lower()

unique_str = normalize("ABCDEF")
non_unique_str = normalize("non unique STR")


def is_unique_1 (input):
    d = dict()
    for i in input:
        if i in d:
            return False
        else:
            d[i] = 1
    return True
#print(is_unique_1(unique_str))
#print(is_unique_1(non_unique_str))
def is_unique_2(str):
    return len(set(str)) == len(str)
#print(is_unique_2(unique_str))
#print(is_unique_2(non_unique_str))   
def is_unique_3(str):
    alpha = s.ascii_lowercase
    for i in str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False
    return True
#print(is_unique_3(unique_str))
#print(is_unique_3(non_unique_str))
##################################################################################
#Integer to String
"""
You are givve some integer as input 

Convert the integer you are given to a sttring, Do not make 
use of the built-in "str" functions 
"""
def int_to_str(input_int):
    if input_int < 0:
        is_negative = True
        input_int *= -1
    else:
        is_negative = False

    output_str = []
    while input_int > 0:
        output_str.append(chr(ord('0')+ input_int % 10))
        input_int //= 10
    output_str = output_str[::-1]
    output_str = ''.join(output_str)
        
    if is_negative:
        return '-' + output_str
    else:
        return output_str
        
input_int = 123
#print(type(int_to_str(input_int=input_int)))
##################################################################################
#String to Integer
""" 
You are given some numeric string as input. Convert the string you are
given to an integer. Do not make use of built-in 'int' funcio.
"""

def str_to_int(input_str):
    output_int = 0
    if input_str[0] == '-':
        start_idx = 1
        is_negative = True
    else: 
        start_idx = 0
        is_negative = False
    for i in range(start_idx, len(input_str)):
        place = 10**(len(input_str)-(i+1))
        digit = ord(input_str[i]) - ord('0')
        output_int += place*digit
    if is_negative:
        return -1*output_int
    else:
        return output_int
s = '-123'
print(str_to_int(s))        

##################################################################################