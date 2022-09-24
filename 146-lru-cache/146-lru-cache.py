class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self,node):  #remove the lru
        prev,nxt = node.prev,node.next
        prev.next,nxt.prev = nxt,prev
        
        
    def insert(self,node):  #insert to rightnmost
        prev, nxt = self.right.prev,self.right
        prev.next= nxt.prev = node
        node.prev,node.next = prev,nxt
        

    def get(self, key: int) -> int:
        if key in self.cache:
            #should be removed and set the node to mru in list
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]  = Node(key,value)
        self.insert(self.cache[key])
            
            
        if len(self.cache) > self.cap:
            lru = self.left.next
            
            self.remove(lru)   #remove from list
            del self.cache[lru.key]  # del from hashmap
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)