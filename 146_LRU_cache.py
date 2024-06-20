class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove(node)
        else:
            node = Node(key, value)
            if len(self.map) == self.capacity:
                del self.map[self.tail.prev.key]
                self._remove(self.tail.prev)

        self.map[key] = node
        self._add(node)

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node):
        second_head = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = second_head
        second_head.prev = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
