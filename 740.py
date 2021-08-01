class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_nums = max(nums)
        n = [0] * max_nums
        for i in range(len(nums)):
            n[nums[i] - 1] += 1
        for i in range(len(n)):
            n[i] *= (i + 1)
        print(n)
        if len(n) <= 2:
            return max(n)
        else:
            x, y, z = 0, n[0], max(n[0], n[1])
            for i in range(len(n) - 2):
                r = max(x + n[i + 1], y + n[i + 2])
                print(r)
                x, y, z = y, z, r
            return r