class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return(left + 1, right + 1)
            elif sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return None