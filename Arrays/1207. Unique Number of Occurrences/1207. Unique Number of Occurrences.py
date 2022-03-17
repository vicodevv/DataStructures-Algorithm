from tabnanny import check
from pip import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        store_frequency = {}
        for i in arr:
            if i in store_frequency:
                store_frequency[i] += 1
            else:
                store_frequency[i] = 1
        list_frequency = list(store_frequency.values())
        check_frequency = {}
        for i in list_frequency:
            if i in check_frequency:
                return False
            check_frequency[i] = 1
        return True

            



