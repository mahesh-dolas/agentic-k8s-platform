class ShortTermMemory:

    def __init__(self):

        self.context = []


    def add(self, message):

        self.context.append(message)


    def get_all(self):

        return self.context


    def clear(self):

        self.context = []