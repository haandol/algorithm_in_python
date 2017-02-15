'''HashTable using open addressing'''


class HashTable(object):
    def __init__(self):
        self.size = 11
        self.keys = [None] * self.size
        self.data = [None] * self.size

    def hash(self, key):
        return key % self.size

    def rehash(self, key):
        return (key + 1) % self.size

    def put(self, key, data):
        slot = self.hash(key)

        if self.keys[slot] is None:
            self.keys[slot] = key
            self.data[slot] = data
        else:
            while self.keys[slot] is not None:
                slot = self.rehash(slot)
                if self.keys[slot] == key:
                    self.data[slot] = data  # replace
                    break
            else:
                self.keys[slot] = key
                self.data[slot] = data

    def get(self, key):
        slot = self.hash(key)
        if self.keys[slot] == key:
            return self.data[slot]
        else:
            start_slot = slot
            while self.keys[slot] != key:
                slot = self.rehash(slot)
                if slot == start_slot:
                    return None
            else:
                return self.data[slot]

    def __setitem__(self, key, data):
        self.put(key, data)

    def __getitem__(self, key):
        return self.get(key)

    def __str__(self):
        return ', '.join(map(str, enumerate(self.data)))


if __name__ == '__main__':
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H)

    H[9] = "duck"
    print(H[9])
    print(H)
