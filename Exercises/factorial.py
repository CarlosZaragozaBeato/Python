"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""
"""_summ
def two_sum(inputs, target):
    i = 0
    j = 1
    while i < len(inputs):
        var1 = inputs[i]
        while j <len(inputs):
            var2 = inputs[j]
            result = var1 +var2
            if result == target:
                return result
            j = j + 1
        i = i + 1


print(two_sum([2,11,7,15], 9))
ary_
"""


"""
def twoSum(nums, target) -> List[int]:
        i = 0
        j = 1
        while i < len(nums):
            var1 = nums[i]
            j =1
            while j < len(nums):
                var2 = nums[j]
                result = var1 +var2
                if result == target:
                    if i>0:
                        return [i, j+1]
                    else:
                        return [i,j]
                j = j + 1
            i = i + 1
            
print(" ",twoSum([2,5,5,11],10))
""" 

def factorial(num):
    result = 0
    i = num
    for i in 0:
        return i

print(factorial(8))
