# A Python program to show different 
# ways to create Counter 
from collections import Counter 
	
# With sequence of items 
print(Counter(['B','B','A','B','C','A','B', 
			'B','A','C'])) 
	
# with dictionary 
print(Counter({'A':3, 'B':5, 'C':2})) 
	
# with keyword arguments 
print(Counter(A=3, B=5, C=2))




# A Python program to demonstrate working 
# of OrderedDict 

from collections import OrderedDict 
	
print("This is a Dict:\n") 
d = {} 
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
	
for key, value in d.items(): 
	print(key, value) 
	
print("\nThis is an Ordered Dict:\n") 
od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
	
for key, value in od.items(): 
	print(key, value)








# A Python program to demonstrate working 
# of OrderedDict 

from collections import OrderedDict 
	
print("This is a Dict:\n") 
d = {} 
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
	
for key, value in d.items(): 
	print(key, value) 
	
print("\nThis is an Ordered Dict:\n") 
od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
	
for key, value in od.items(): 
	print(key, value)







# A Python program to demonstrate working 
# of OrderedDict 

from collections import OrderedDict 


od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
	
print('Before Deleting') 
for key, value in od.items(): 
	print(key, value) 
	
# deleting element 
od.pop('a') 

# Re-inserting the same 
od['a'] = 1

print('\nAfter re-inserting') 
for key, value in od.items(): 
	print(key, value)




# Python program to demonstrate 
# defaultdict 
	
	
from collections import defaultdict 
	
	
# Defining the dict 
d = defaultdict(int) 
	
L = [1, 2, 3, 4, 2, 4, 1, 2] 
	
# Iterate through the list 
# for keeping the count 
for i in L: 
		
	# The default value is 0 
	# so there is no need to 
	# enter the key first 
	d[i] += 1
		
print(d)















# Python code to demonstrate ChainMap and 
# new_child() 
	
import collections 
	
# initializing dictionaries 
dic1 = { 'a' : 1, 'b' : 2 } 
dic2 = { 'b' : 3, 'c' : 4 } 
dic3 = { 'f' : 5 } 
	
# initializing ChainMap 
chain = collections.ChainMap(dic1, dic2) 
	
# printing chainMap 
print ("All the ChainMap contents are : ") 
print (chain) 
	
# using new_child() to add new dictionary 
chain1 = chain.new_child(dic3) 
	
# printing chainMap 
print ("Displaying new ChainMap : ") 
print (chain1)
