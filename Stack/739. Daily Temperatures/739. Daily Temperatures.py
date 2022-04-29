from pip import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #[index, temp]
        
        for i, t in enumerate(temperatures):
#is stack empty and is temperature greater than temperature on top of stack
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = (i - stackI)
            stack.append([t, i])
        return res