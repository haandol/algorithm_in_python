class LRUCache(object):
    def __init__(self, size):
        self.size = size
        self.lru = {}
        self.cache = {}
        self.counter = 0

    def put(self, key, value):
        if key not in self.cache:
            if len(self.lru) >= self.size:
                k, _ = min(self.lru.iteritems(), key=lambda x: x[1])
                self.lru.pop(k)
                self.cache.pop(k)

        self.counter += 1
        self.lru[key] = self.counter
        self.cache[key] = value

    def get(self, key):
        if key in self.cache:
            self.counter += 1
            self.lru[key] = self.counter
            return self.cache[key]
        return None


if "__main__" == __name__:
    cache = LRUCache(3)
    cache.put('a', 1)
    cache.put('b', 2)
    cache.put('c', 3)
    assert 3 == len(cache.cache)
    print cache.cache

    cache.put('d', 4)
    cache.put('a', 5)
    assert 3 == len(cache.cache)
    assert None is cache.get('b')
    assert 4 == cache.get('d')
    assert 5 == cache.get('a')
