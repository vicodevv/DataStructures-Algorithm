class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        currentSum = 0
        prefixSum = {0 : 1}
        
        for n in nums:
            currentSum += n
            diff = currentSum - k
            
            res += prefixSum.get(diff, 0)
            prefixSum[currentSum] = 1 + prefixSum.get(currentSum, 0)
            
        return res