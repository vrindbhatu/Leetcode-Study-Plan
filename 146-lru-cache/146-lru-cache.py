class Node:
    def __init__(self, key,val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # need a hashmap which maps the key to nodes
        
        
        self.left,self.right = Node(0,0), Node(0,0)    
        self.left.next, self.right.prev = self.right, self.left  #want these node to be connected because if we are addin gany node we want it to be added in the middle
    
    def remove(self,node):  #remove from list
        prev,nxt = node.prev,node.next
        prev.next,nxt.prev = nxt,prev
    
    def insert(self,node):  #insert at right
        prev,nxt = self.right.prev,self.right
        prev.next, nxt.prev = node,node
        node.next,node.prev = nxt,prev
    
    def get(self, key: int) -> int:
        if key in self.cache:
            #whenever we get a node we need to update it to most recent
            self.remove(self.cache[key])  
            self.insert(self.cache[key])  #for reordering and inserting at rightmost position
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            
        self.cache[key] = Node(key,value) #now we have this value in our hashmap
        self.insert(self.cache[key]) #insert to our linked list
        
        if len(self.cache) > self.cap:
            #remove from the list and delete the lru from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)