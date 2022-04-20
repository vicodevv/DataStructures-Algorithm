class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #map key to node
        
        #left = LRU, right = MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

        
    #remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    #insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
            
        if len(self.cache) > self.cap:
            #remove from the list and delete the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


#Another Solution
# Define a node class for a doubly-linked list (DLL)
class _Node:
    __slots__ = '_prev', '_val', '_key', '_next'
    
    def __init__(self, val, key, prev, nxt):
        self._val = val
        self._key = key
        self._prev = prev
        self._next = nxt

class LRUCache:
    # LRU Cache is implemented as a doubly linked list (DLL)
    # Addition of nodes takes place only at the end  of the DLL
    # Deletion of nodes takes place only at the head of the DLL     (least frequently used)
    # Once any element is accessed, move it to end of DLL           (most recently used)

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._head = None
        self._tail = None
        self._size = 0
        self._hashmap = {}
    
    def add_node(self, node):
        if self._size == 0:
            self._head = node
            self._tail = node
        else:
            node._prev = self._tail
            self._tail._next = node
            self._tail = self._tail._next
    
    def remove_node(self):
        del self._hashmap[self._head._key]
        self._head = self._head._next
        if self._head: self._head._prev = None
        self._size -= 1
    
    def update_cache(self, node):
        # if there is a single node, return
        if self._size == 1: return
        # if node is already most recently accessed node
        elif node == self._tail: return 
        # if node is least recently used node
        elif node == self._head:
            self._head = self._head._next
            self._head._prev = None
        else:
            if node._next: node._next._prev = node._prev
            if node._prev: node._prev._next = node._next
        node._next = None
        node._prev = None
        self.add_node(node)
    
    # Not needed, but EXTREMELY helpful while debugging / designing. 
    def display(self):
        p = self._head
        while p:
            if p._next:
                print(str(p._key) + ":" + str(p._val), end=' <--> ')
            else:
                print(str(p._key) + ":" + str(p._val), end=' \n')
            p = p._next
    
    def get(self, key: int) -> int:
        if key in self._hashmap: 
            node = self._hashmap[key]
            self.update_cache(node)
            return node._val
        else: return -1

        
    def put(self, key: int, value: int) -> None:
        if key in self._hashmap: 
            self._hashmap[key]._val = value
            self.update_cache(self._hashmap[key])
        else:
            newest = _Node(value, key, None, None)
            if self._size < self._capacity: 
                self.add_node(newest)
            else:
                self.remove_node()
                self.add_node(newest)
            self._hashmap[key] = newest
            self._size += 1 

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#Input :::
#["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
#[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

#Step by step progress of cache :::
#Put operation, key and val ::: 1 1
#1:1
#Put operation, key and val ::: 2 2
#1:1 <--> 2:2
#Get operation, key::: 1 found
#1:1 <--> 2:2
#Put operation, key and val ::: 3 3
#1:1 <--> 3:3
#Get operation, key::: 2 not found
#1:1 <--> 3:3
#Put operation, key and val ::: 4 4
#3:3 <--> 4:4
#Get operation, key::: 1 not found
#3:3 <--> 4:4
#Get operation, key::: 3 found
#3:3 <--> 4:4
#Get operation, key::: 4 found
#4:4 <--> 3:3

#Output :::
#[null,null,null,1,null,-1,null,-1,3,4]