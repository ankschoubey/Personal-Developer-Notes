from dataclasses import dataclass

@dataclass
class CacheItem:
    id = 0
    compValue = 0
    def __init__(self, id, compValue) -> None:
        self.id = id
        self.compValue = compValue

class PriorityQueue:
    items = []
    def add(self, item: CacheItem):
        self.items.append(item)
        self.sort()
    def sort(self):
        self.items.sort(key = lambda x: x.compValue)
    
    def pop(self):
        return self.items.pop(0)

class SimpleCacher:
    pq = PriorityQueue()
    cache = {}
    size = 5
    def access(self, id):
        if id in self.cache.keys():
            item = self.onHit(self.cache[id])
            print("Cache Hit ", id, item.id, item.compValue)
            self.pq.sort()
            return self.cache[id]
        if len(self.cache) == self.size:
            item = self.pq.pop()
            print("cache evicted ", id, item.id, item.compValue)
        item = self.onAccess(id)
        self.pq.add(item)
        self.cache[id] = item
        print("Adding ", id, item.id, item.compValue)

from datetime import datetime

class LRU(SimpleCacher):
    def getCurrentTime(self):
        return  int(datetime.now().strftime("%Y%m%d%H%M%S"))
    def onHit(self, x: CacheItem):
        x.compValue = self.getCurrentTime()
        return x
    def onAccess(self, x):
        return CacheItem(x, self.getCurrentTime())

class LFU(SimpleCacher):
    def onHit(self, x: CacheItem):
        x.compValue = x.compValue + 1
        return x
    def onAccess(self, x):
        return CacheItem(x, 1)

ids = [1,1,1,1,1, 2,2,2,2,3,4,4,5,6,7,7,7,7,8,8,8,4,4,4,3,3,3, 9,9,9,9,11,11,11,11,0,0,1]
lru = LRU()
for i in ids:
    lru.access(i)
#del lru
#print("\n\nLFU")
# lfu = LFU()
# for i in ids:
#     lfu.access(i)