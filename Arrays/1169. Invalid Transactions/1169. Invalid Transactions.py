from collections import defaultdict
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

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        transactions = [t.split(",") for t in transactions]
        transactions = sorted(transactions, key = lambda x: int(x[1]))
        invalid = set()
        store = defaultdict(list)
        
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction
            time = int(time)
            amount = int(amount)
            
            if amount > 1000:
                invalid.add(i)
                
            if name in store:
                j = len(store[name]) - 1
                while j >= 0 and time - int(transactions[store[name][j]][1]) <= 60:
                    if city != transactions[store[name][j]][3]:
                        invalid.add(i)
                        invalid.add(store[name][j])
                        
                    j -= 1
                    
            store[name].append(i)
            
        return [",".join(transactions[i]) for i in invalid]
            
        

#["alice,20,800,mtv","alice,50,100,beijing"]


#   0     1  2   3        0    1   2   3
#["alice,20,800,mtv"], ["alice,50,100,beijing"] ["alice,80,100,china"] 
#        0                       1
        
#procedure
#1. split by comma
#2. sort by time
#3. store invalid transaction in a data structure
#4. Have a data structure that stores the name and index of each transaction so we can confirm with the previous if it is invalid or not

#store = {alice: [0, 1]}        