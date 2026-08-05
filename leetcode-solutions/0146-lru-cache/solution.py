class Node:
    def __init__(self,key:int,val:int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    def _remove(self,node:Node):
        person_behind = node.prev
        person_ahead = node.next
        person_behind.next = person_ahead
        person_ahead.prev = person_behind
    def _add(self,node:Node):
        old_first_person = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = old_first_person
        old_first_person.prev = node
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add(node)
        else:
            if len(self.cache)>= self.capacity:
                oldest_person = self.tail.prev
                self._remove(oldest_person)
                del self.cache[oldest_person.key]
            new_node = Node(key,value)
            self.cache[key] = new_node
            self._add(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
