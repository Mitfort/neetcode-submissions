class Node:
    def __init__(self, key:int, val:int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.currSize = 0
        self.memory = {}
        
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:        
        if key not in self.memory:
            return -1

        node = self.memory[key]
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.memory:
            node = self.memory[key]
            node.val = value
            self._remove(node)
            self._add_to_front(node)
            return

        if self.currSize >= self.capacity:
            last_used = self.tail.prev
            self._remove(last_used)
            self.memory.pop(last_used.key,None)
        
        new_node = Node(key,value)
        self.memory[key] = new_node
        self._add_to_front(new_node)
        self.currSize += 1

    def _remove(self, node:Node) -> None:
        prev_node = node.prev
        next_node = node.next 
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_front(self,node:Node) -> None:
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node




        
