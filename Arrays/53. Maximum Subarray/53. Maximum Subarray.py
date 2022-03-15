from pip import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        sum = 0
        
        for num in nums:
            if sum < 0:
                sum = 0
            sum += num
            max_sub = max(sum, max_sub)
        
        return max_sub