class ListNode:

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.dummy = ListNode(None, None)
        self.capacity = capacity
        self.curr_length = 0
        self.last_node = self.dummy

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        if node != self.last_node:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.last_node
            node.next = None
            self.last_node.next = node
            self.last_node = node

        return node.val[key]

    def evict(self):

        node = self.dummy.next
        key = next(iter(node.val))

        self.cache.pop(key)
        self.dummy.next = node.next

        if node.next:
            node.next.prev = self.dummy

        else:
            self.last_node = self.dummy
        self.curr_length -= 1

    def put(self, key: int, value: int) -> None:
        
        # existing key
        if key in self.cache:
            node = self.cache[key]
            node.val[key] = value

            # make it most recently used
            if node != self.last_node:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.prev = self.last_node
                node.next = None
                self.last_node.next = node
                self.last_node = node

            return

        if self.curr_length >= self.capacity:
            self.evict()

        node = ListNode({key: value}, None)

        node.prev = self.last_node
        self.last_node.next = node
        self.last_node = node
        self.cache[key] = node
        self.curr_length += 1

lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
print(lRUCache.get(1))
lRUCache.put(3, 3)
print(lRUCache.get(2))
lRUCache.put(4, 4)
print(lRUCache.get(1))
print(lRUCache.get(3))
print(lRUCache.get(4))
