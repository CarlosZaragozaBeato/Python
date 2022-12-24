data = [2,1,4,7,8,5,6,9,25,4,1,5,3,25]
target = 2
#linear search 
def linear_search(data, targe):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

#print(linear_search(data, target))
#iterative Binary search
def binary_search(data, target):
    low = 0
    high = len(data) -1
    
    while low <= high:
        mid = (low + high) // 2 
        if (target == data[mid]):
            return True
        elif target < data[mid]:
            high = mid -1
        else:
            low = mid + 1
    return False
             

#Recursive Binary search
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else: 
        mid = (low+high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid -1)
        else: 
            return binary_search_recursive(data, target, mid+1, high)
        
#print(binary_search(data,target))
#print(binary_search_recursive(data, target,0, len(data)-1))
############################################################
#Find Closest Number
""" 
Given an array of sorted itegers, We need to find the closest value tothe given 
number,
Array may contain duplicate values and negative numbers.
Example:
    Input: arr[] = [1,2,3,4,5,6,7,8,9]
    Targe number = 11
    OutPut 9
    9 is close in 11 in given array
    
    Input :arr[]= [1,5,6,7,8,8,9]
    Target number = 4
    Output:5
    
    midpoint: 7
    right of midpoint:8 - 4 = 4 
    left of midpoin: 6 - 4 = 2
"""
A = [1,2,4,5,6,6,8,9]
B = [2,5,6,7,8,8,9]

def find_closest_num(arr, target):
    min_diff = float("inf")
    low = 0
    high = len(arr)-1
    closest_num = None
    
    #Edge cases for empy list or 
    #when the list i only one element
    if len(arr) == 0:
        return None
    if len(arr) ==1:
        return arr[0]
    
    while low <= high:
        mid = (low+high)//2
        if mid +1 < len(arr):
            min_diff_right = abs(arr[mid+1]-target)
        if mid>0:
            min_diff_left = abs(arr[mid-1]-target)
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = arr[mid-1]
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = arr[mid+1] 
        
        if arr[mid] < target:
            low = mid+1
        elif arr[mid]>target:
            high = mid-1
        else: 
            return A[mid]
    return closest_num

#print(find_closest_num(A,10))
############################################################
#Find Fixed Point
""" 
A fixed point in an array "A" is an index "i" such that A[i] is equal to "i"

Given a array of "n" distinct integers sorted in ascending order, write a function
that returns a "fixed point" in the array. If there is not a fixed point returm "None"
"""
#Fixed point is 3
A = [-10,-5,0,3,7]

#Fixed point is 0
B = [0,2,5,8,17]

#No foxed point, Return NONE:
C = [-10,-5,3,4,7,9] 

#Time Complexity: 0(n)
def find_fixed_point_linear(a):
    for i in range(len(a)):
        if a[i] == i:
            return a[i]
    return None

def find_fixed_point(a):
    low = 0
    high = len(a) -1
    while low <= high:
        mid = (low+high)//2
        
        if a[mid]<mid:
            low = mid+1
        elif a[mid]>mid:
            high = mid-1
        else:
            return a[mid]
    return None
#print(find_fixed_point(C))
############################################################
#Find Bitonic Peak
""" 
Defina a bitonic sequence as a sequence of integers such that:
x_1 <=... <= x_k>=...>=x_n-1 for som k, 0<=k<n
For example 1,2,3,4,5,4,3,2,1

is a bitonic sequence. Write a program to find the largest element in such
a sequence. In the example above, the program should returm '5'
We assume that such a "peak" element exists
"""
#Peak element is "5"
A = [1,2,3,4,5,4,3,2,1]

#Peak element is "4"
B = [1,2,3,4,1]

#Peak element is "6"
C = [1,6,5,4,3,2,1]

def find_highest_number(A): 
    low = 0
    high = len(A) -1
    
    #Require a leat 3 element for a valid bitonic sequence
    if len(A) <3:
        return None
    
    while low <= high:
        mid = (low+high)//2
        
        mid_left = A[mid-1] if mid - 1>0 else float("-inf")
        mid_right = A[mid+1] if mid + 1 < len(A) else float("inf")
        
        if mid_left < A[mid] and mid_right > A[mid]:
            low = mid +1
        elif mid_left > A[mid] and mid_right < A[mid]:
            high = mid -1
        elif mid_left < A[mid] and mid_right < A[mid]:
            return A[mid]
        
#print(find_highest_number(A))
#print(find_highest_number(B))            
#print(find_highest_number(C))
############################################################
#Find First Entry in List with Duplicates
"""
Write a function that takes an array sorted of integers and a key
and returns the index of the first ocurrence of that key from the array

Example:
idx 0   1   2   3   4   5   6   7   8   9
A=[-14, 10  2   108     108     243     285     285     401]
Returns index 3 since 108 appears for the first time at index 3 
"""

A = [-14, 10, 2, 108, 108, 234, 285, 285,401]
target = 108

def find (A, target):
    low = 0
    high = len(A) -1
    while low <= high:
        mid = (low+high)//2
        if A[mid] < target:
            low = mid +1
        elif A[mid] > target:
            high = mid - 1
        else:
            if mid -1 < 0:
                return mid
            if A[mid -1] != target:
                return mid
            high = mid -1
    return None
            
#print(find(A, target))
############################################################
#Python's Bisect Method
"""
Bisect: 
    -"Built-in" binary search method in Python 
    -Can be used to search for an element in a sorted list 
"""

import bisect

A = [-14,-10,2,108,108,243,285,285,285,401]

#print(bisect.bisect_left(A,285))
#print(bisect.bisect_right(A, 285))
#print(bisect.bisect_right(A, -10))
############################################################
#Integer Square Root

""" 
Write a function that takes a non-negative integer and returns
the largest integer whose square is less than or equal to the
integer given

Example:
    Assume input is integer 300.
    Then the expected output of the function should be 17,
    since 17^2 = 289 < 300. Notte tthat 18^2 = 324 > 300
    so the number 17 is the correct response
"""
k = 300
def integer_square_root(k):
    low = 0
    high = k
    
    while low <= high:
        mid = (low+high)//2
        mid_square = mid*mid
        
        if mid_square <=k:
            low = mid+1
        else:
            high = mid-1
            
    return low -1       
#print(integer_square_root(k))
############################################################
#Cyclically Shifted Array
"""
An array is 'cyclically sorted' if it is possible the ciclycally
shift its entries so that it becomes sorted.

The following list is in an exmples sorted array:
A = [4,5,6,7,1,2,3]
Write a function that determines the index of the smallest element
of the cyclically sorted array
"""

A = [4,5,6,7,1,2,3]

def find(A):
    low = 0
    high = len(A)-1
    while low < high:
        mid = (low+high) //2
        
        if A[mid]>high:
            low = mid +1
        elif A[mid]<=high:
            high = mid
    return low
#print(find(A))
############################################################