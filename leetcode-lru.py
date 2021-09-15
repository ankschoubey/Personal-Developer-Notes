class CacheItem:
    def __init__(self, id, value, compValue=1, order = 1) -> None:
        self.id = id
        self.compValue = compValue
        self.value = value
        self.order = order

class PriorityQueue:
    items = []
    def add(self, item: CacheItem):
        self.items.append(item)
        self.sort()
    def sort(self):
        self.items.sort(key = lambda x: (x.compValue, x.order))
    def pop(self):
        return self.items.pop(0)
class LFUCache:
    pq = PriorityQueue()
    cache = {}
    def __init__(self, capacity: int):
        self.size = capacity

    def get(self, key: int) -> int:
        value = self.cache.get(key, -1)
        if value == -1:
            return value
        value.compValue += 1
        self.pq.sort()
        return value.value

    order = 1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            item = self.cache[key]
            item.value = value
            self.pq.sort()
            return
        item = CacheItem(key, value, 1, self.order)
        self.order +=1
        if len(self.cache) == self.size:
            popped = self.pq.pop()
            del self.cache[popped.id]
        self.pq.add(item)
        self.cache[key] = item
    

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)