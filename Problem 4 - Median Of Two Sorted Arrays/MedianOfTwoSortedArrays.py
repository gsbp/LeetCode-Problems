class Solution:
    def Median_of_Two_Sorted_Arrays():
        nums1 = [1,2]

        nums2 = [3,4]

        totalLength = len(nums1) + len(nums2)
        
        isEven = False
        if totalLength % 2 == 0:
            isEven = True

        middleIndex = (totalLength-1) // 2  
        i = 0
        j = 0
        index = 0
        while index <= middleIndex:

            if i >= len(nums1):
                number = nums2[j]
                j += 1  
            elif j >= len(nums2):
                number = nums1[i]
                i += 1
            elif nums1[i] < nums2[j]:
                number = nums1[i]
                i += 1
            else:
                number = nums2[j]
                j += 1    
            index +=1
            
        median = number
        if isEven:
            if i >= len(nums1):
                number2 = nums2[j] 
            elif j >= len(nums2):
                number2 = nums1[i]
            elif nums1[i] < nums2[j]:
                number2 = nums1[i]
            else:
                number2 = nums2[j]

            median = (number + number2) / 2

        return median





# For Testing

s = Solution()

nums1 = [1, 3]
nums2 = [2]
median = s.findMedianSortedArrays(nums1, nums2)
print(median)

nums1 = [1, 3]
nums2 = []
median = s.findMedianSortedArrays(nums1, nums2)
print(median)

nums1 = [1, 3]
nums2 = [2, 4]
median = s.findMedianSortedArrays(nums1, nums2)
print(median)






def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
    totalLength = len(nums1) + len(nums2)

    isEven = False
    if totalLength % 2 == 0:
        isEven = True
    
    if isEven:
        middleIndex = (totalLength) // 2
    else:
        middleIndex = (totalLength - 1) // 2
    
    i = 0
    j = 0
    index = 0
    halfSort = []

    while index <= middleIndex:

        # If the list is empty this might break?
        if i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                halfSort.append(nums1[i])
                i += 1
            else:
                halfSort.append(nums2[j])
                j += 1

        elif i < len(nums1):
            halfSort.append(nums1[i])
            i += 1

        else:
            halfSort.append(nums2[j])
            j += 1

        index += 1

    if isEven:
        median = (halfSort[-1] + halfSort[-2]) / 2.0
    else:
        median = float(halfSort[-1])

    return median