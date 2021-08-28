class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        l = len(nums)
        if l % 2 == 0:
            return float(nums[l / 2] + nums[l / 2 - 1]) / 2
        else:
            return float(nums[l // 2])