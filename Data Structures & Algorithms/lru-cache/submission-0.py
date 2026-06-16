class ListNode():
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:


    '''

    doubly linked list -> removing and adding nodes according to lru and recently inserted
    cahce to store key : ListNode() object  pair

    since this is a cache with an LRU policy, every time we visit (get) a key, we move it to the right
        Need helper functions that can remove and insert nodes in O(1) time

    '''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key : ListNode() object  pair
                            # remember, a node is a ListNode(key, value) object where key and value are integers

        #initialize doubly linked list
            # create left and right dummy nodes with ListNode(0,0) default values
        
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    

    '''

        removes the node from linkedlist in O (1) time

        if node.prev exists # it will exist because we have dummy left and right pointers


        node.prev.next = node.next.next

    '''
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev



    




    '''
        insert the node to the linkedlist in O(1) time
        prev_temp = right.prev
        right.prev = node
        node.prev = prev_temp
        right.next = right

        unlink prev from right
        link prev.next to node
        node.prev = prev
        node.next = right

    '''
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    '''
    if key exists in cache hashmap:
        return val from cache hashamp
        remove key from lru linkedlist, insert it to the end of lru linkedlist
    else:
        return -1

    '''



    def get(self, key: int) -> int:

        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        
    


    '''

    if key exists:
        update value of key 
    else:
        if capacity is not full
            add key-value pair to cache in the end
        else: #if capacity is full
            remove LRU and then add cache
        


    '''

    def put(self, key: int, value: int) -> None:

        if key in self.cache: # if key exists
            self.remove(self.cache[key])
            self.cache[key] = ListNode(key, value)
            
            self.insert(self.cache[key])
        else:
            if len(self.cache) >= self.capacity: #if over capacity, we need to remove the lru
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]
                
            self.cache[key] = ListNode(key, value)
            self.insert(self.cache[key])















        
