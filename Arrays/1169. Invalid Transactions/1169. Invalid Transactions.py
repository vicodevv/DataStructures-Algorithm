from pip import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        import collections
        from collections import defaultdict
        store = defaultdict(list)
        transactions = [t.split(',') for t in transactions]
        transactions.sort(key=lambda x : int(x[1]))
        invalid = set()
 
        
        for i,transaction in enumerate(transactions):
            name,time,amount,city = transaction
            time,amount = int(time),int(amount)
            if amount>1000:
                invalid.add(i)
            if name in store:
                idx = len(store[name])-1
                while idx>=0 and time-int(transactions[store[name][idx]][1])<=60:
                    if city != transactions[store[name][idx]][3]:
                        invalid.add(i)
                        invalid.add(store[name][idx])
                    idx-=1
            store[name].append(i)
        return [','.join(transactions[i]) for i in invalid]
                    