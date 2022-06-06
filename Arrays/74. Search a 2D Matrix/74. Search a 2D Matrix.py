import numpy as np

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array = np.array(matrix)  
        arr = array.flatten()
        
        l, r = 0, len(arr) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target > arr[mid]:
                l = mid + 1
            elif target < arr[mid]:
                r = mid - 1
            else:
                return True
        return False
                
        