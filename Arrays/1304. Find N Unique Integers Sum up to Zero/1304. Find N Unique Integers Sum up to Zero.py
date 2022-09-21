class Solution:
    def sumZero(self, n: int) -> List[int]:
        sum = []
        if n % 2 != 0:
            sum.append(0)
        for i in range(1, n // 2 + 1):
            sum.extend([i, -i])
        return sum
        