class HashTable:
    def __init__(self):
        self.size = 10
        self.slots = [[None]] * self.size
        self.data = [[None]] * self.size


    def put(self, key,data):
        hashvalue = self.hashfunction(key,len(self.slots))
        if self.slots[hashvalue] == [None]:
            self.slots[hashvalue] = [key]
            self.data[hashvalue] = [data]
        else:
            if self.slots[hashvalue] == [key]:
                self.data[hashvalue] = [data]
            else:
                self.slots[hashvalue].append(key)
                self.data[hashvalue].append(data)
    def hashfunction(self, key, size):
        return key%size
    def rehash(self, oldhash, size):
        return (oldhash + 1)%size

    def Search(self, key,):
        hashvalue = self.hashfunction(key, len(self.slots))
        x = self.slots[hashvalue]
        y = self.data[hashvalue]
        for i in range(0,len(x)):
           if x[i] == key:
               return [y[i]]

H = HashTable()
H.put(54,'cat')
H.put(26,'dog')
H.put(90, 'lion')
H.put(10, 'tiger')
H.put(78,'man')
print H.Search(54)
print H.Search(10)
print H.data
print H.slots