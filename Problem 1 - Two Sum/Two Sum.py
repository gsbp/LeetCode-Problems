import math
# Leetcode Promeb


def runSolution ():
    import random
    listSize = 1 + random.randint(3,10)
    nums = []

    for i in range(listSize):
        nums.append(random.randint(-100,100))
    
    a = b = 0 

    while a==b:
        a = nums[random.randint(0, len(nums)-1)]
        b = nums[random.randint(0, len(nums)-1)]

    target = a + b
    
    print(nums)
    print(target)

    
    sol = solution2(nums, target)
    
    return sol

#Git Hub Copliot
def solution(nums, target):
    #Two sum soloution
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]


 #n^2 solution 
def solution(nums, target):
    solutionIndex = []
 
    for i in range(len(nums)):
        firstVal = nums[i]
        j = i + 1
        while j < len(nums):
            if firstVal + nums[j] == target:
                solutionIndex.append(i)
                solutionIndex.append(j)
                break
            else:
                j += 1

    if solutionIndex:
        print(solutionIndex)
    else:
        print("None")

    return solutionIndex

#n soloution
def solution2(nums, target):
    hashmap = {}
        
    for i in range(len(nums)):
        c = target - nums[i]
        if c in hashmap:
            return [i, hashmap[c]]
        else:
            hashmap[nums[i]] = i
        
        
    
        



runSolution()
