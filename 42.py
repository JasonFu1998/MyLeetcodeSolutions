class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        a = 0
        for i in range(len(height)):
            l = max(height[i], l)
            r = max(height[- 1 - i], r)
            a += l + r
        return a - sum(height) - l * len(height)