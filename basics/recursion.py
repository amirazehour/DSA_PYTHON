def countdown(n):
    if n<=0:
        print("done")
    else :
        print(n)
        countdown(n-1)


countdown(4)

"""
every recursive function must have  
    BASE CASE (STOP CONDITION)
    RECURSIVE CASE (WITH MODIFIED ARGUMENT)
"""

def febonacci(n):
    if n<=1:
        return n
    else :
        return febonacci(n-2)+febonacci(n-1)
    
print(febonacci(6))


def sumlist(nums):
    if len(nums)==0:
        return 0
    else:
        return nums[0]+sumlist(nums[1:])
    
def maxinlist(nums):
    if len(nums)==0:
        return 0
    elif len(nums)==1:
        return nums[0]
    else :
        max_nums=maxinlist(nums[1:])
        return max_nums if max_nums>nums[0] else nums[0]

nums = [1,3,5]

print(sumlist(nums))
print(maxinlist(nums))


#depth limit
import sys
print(sys.getrecursionlimit())
#can increase limit but this can cause crashes
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
#done with caution for deep recursion use iterations