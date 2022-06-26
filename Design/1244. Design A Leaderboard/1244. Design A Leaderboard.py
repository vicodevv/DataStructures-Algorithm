from collections import Counter
class Leaderboard:

    def __init__(self):
        self.counter = Counter()

    def addScore(self, playerId: int, score: int) -> None:
        self.counter[playerId] += score

    def top(self, K: int) -> int:
        return sum(map(lambda x:x[1], self.counter.most_common(K)))

    def reset(self, playerId: int) -> None:
        self.counter[playerId] = 0 


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)