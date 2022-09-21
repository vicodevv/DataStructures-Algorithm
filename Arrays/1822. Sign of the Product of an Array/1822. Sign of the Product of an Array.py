class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        product = 1
        for num in nums:
            product = product * num
        if product >= 0:
            return 1
        elif product < 0:
            return -1
        