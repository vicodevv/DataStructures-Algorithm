from pip import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda arr: arr[1], reverse=True)
        
        total_units = 0
        for num_boxes, unit in boxTypes:
            if truckSize <= num_boxes:
                total_units += truckSize * unit
                break
            total_units += num_boxes * unit
            truckSize -= num_boxes
            
        return total_units