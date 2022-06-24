class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass




# For Testing

s = Solution()

nums1 = [1, 3]
nums2 = [2]
median = findMedianSortedArrays(nums1, nums2)
print(median)

nums1 = [1, 3]
nums2 = []
median = findMedianSortedArrays(nums1, nums2)
print(median)

nums1 = [1, 3]
nums2 = [2, 4]
median = findMedianSortedArrays(nums1, nums2)
print(median)