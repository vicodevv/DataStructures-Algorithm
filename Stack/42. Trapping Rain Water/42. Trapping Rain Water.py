from pip import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # In order not to use extra memory, two pointers can be used where the pointer is
        #  being moved based on the minimum of the left and right pointer
        if not height:
            return 0
        l, r = 0, len(height) -1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -=1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res