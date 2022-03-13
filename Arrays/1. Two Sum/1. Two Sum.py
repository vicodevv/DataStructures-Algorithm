from pip import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} 
        for i, n in enumerate(nums):
            difference = target - n
            if difference in prevMap:
                return [prevMap [difference], i]
            prevMap[n] = i
        return
