from pip import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1,1
        
        for n in nums:
            tmp = curMax * n
            curMax = max(n, n * curMax, n * curMin)
            curMin = min(n, tmp, n * curMin)
            res = max(res, curMax)
        return res