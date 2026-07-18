class LongTermMemory:

    def __init__(self):

        self.storage = {}


    def save(self, key, value):

        self.storage[key] = value


    def retrieve(self, key):

        return self.storage.get(key)