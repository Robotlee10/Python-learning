class HashTable:
    def __init__(self):
        # 2. collection attribute initialized to an empty dictionary
        self.collection = {}

    def hash(self, string):
        # 4, 5. Take string and return sum of Unicode values
        return sum(ord(char) for char in string)

    def add(self, key, value):
        # 7, 15, 16. Add key-value pair to nested dictionary at the hashed index
        index = self.hash(key)
        if index not in self.collection:
            self.collection[index] = {}
        self.collection[index][key] = value

    def remove(self, key):
        # 9, 10, 11, 17. Remove specific key-value pair without raising error
        index = self.hash(key)
        if index in self.collection and key in self.collection[index]:
            del self.collection[index][key]

    def lookup(self, key):
        # 13, 18, 19, 20. Return value if key exists, else None
        index = self.hash(key)
        if index in self.collection and key in self.collection[index]:
            return self.collection[index][key]
        return None
