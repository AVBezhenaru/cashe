from random import randint

class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
         index = len(key) % self.size
         return index

    def seek_slot(self, key):
        index = self.hash_fun(key)
        len = self.size

        while len > 0:
            if self.slots[index] == None:
                return index

            index += 1

            if index > self.size - 1:
                index -= self.size
            len -= 1

        return None

    def hit(self):
        for i in range(self.size):
            self.hits[i] = randint(0, self.size)

        return min(self.hits)

    def put(self, key, value):
        index = self.seek_slot(key)

        if index == None:
            index = self.hit()

        self.slots[index] = value
        self.values[index] = key



nc = NativeCache(5)

nc.put("1", 1)
nc.put("1", 2)
nc.put("1", 3)
nc.put("1", 4)
nc.put("1", 5)
nc.put("1", 6)

print(nc.slots)
