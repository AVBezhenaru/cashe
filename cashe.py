from random import randint

class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        index = 0
        for c in key:
            code = ord(c)
            index = (index * 17) + code

        index = index % self.size
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

    def get(self, key):
        for i in range(self.size):
            if self.values[i] == key:
                self.hits[i] += 1
                return self.slots[i]

        return None

    def put(self, key, value):
        index = self.seek_slot(key)

        if index == None:
            index = self.hits.index(min(self.hits))

        self.slots[index] = value
        self.values[index] = key


nc = NativeCache(5)

nc.put("1", 1)
nc.put("2", 2)
nc.put("3", 3)
nc.put("4", 4)
nc.put("5", 5)

print("slots before", nc.slots)

nc.get("1")
nc.get("1")
nc.get("2")
nc.get("2")
nc.get("3")
nc.get("3")
nc.get("4")
nc.get("4")
nc.get("5")


nc.put("5", 6)

print(nc.hits)
print("slots after", nc.slots)

