from pip import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in range(1, len(nums)):
            if nums[left - 1] != nums[right]:
                nums[left] = nums[right]
                left += 1
        return left
        