class LinkedList:
    def __init__(self):
        self._begin = None

    def insert(self, x):
        self._begin = [x, self._begin]
        print("{} appended to list".format(x))

    def pop(self):
        # assert self._begin is not None, "List empty"
        if self._begin is None:
            print("List empty")
            return
        x = self._begin[0]
        self._begin = self._begin[1]
        return x


a = LinkedList()
a.insert(5)
a.insert(10)
print(a.pop())
print(a.pop())
print(a.pop())
