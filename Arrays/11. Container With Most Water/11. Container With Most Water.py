from pip import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            if height[l] < height[r]:
                area = (r - l) * min(height[l], height[r])
                res = max(res,area)
                l += 1
            else:
                area = (r - l) * min(height[l], height[r])
                res = max(res,area)
                r -= 1
                
        return res