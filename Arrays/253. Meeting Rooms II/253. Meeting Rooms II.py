class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)
        
        s, e = 0, 0
        count, res = 0, 0
        
        while s < len(intervals):
            if end[e] > start[s]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(count, res)
        return res
        
        
        #[0, 5, 15]
        #[10, 20, 30]