def calc_hash(data):
    k = 3571
    s = 0
    i = 1
    data += 84832941
    while data > 0:
        s += data % 2 * k ** i
        i += 1
        data //= 2
    return s % 2 ** 8
    # return s % 2 ** 32  # 32 bit hash
    # return s % 2 ** 64  # 64 bit hash
    # return s % 2 ** 128  # 32 bit hash


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, element):
        if not self.search(element):
            node = [element, None]
            if self.head is None:
                self.head = node
            else:
                self.tail[1] = node
            self.tail = node

    def search(self, element):
        curr = self.head
        while curr is not None:
            if curr[0] == element:
                return True
            else:
                curr[0] = curr[1]
        return False


class Hashable:
    def __init__(self):
        self.table = [LinkedList() for _ in range(256)]

    def add(self, element):
        hsh = calc_hash(element)
        self.table[hsh].add(element)

    def search(self, element):
        hsh = calc_hash(element)
        return self.table[hsh].search(element)

    def print_table(self):
        for node in self.table:
            print(str(node.head) + ", " + str(node.tail))


a = Hashable()
for x in range(60):
    a.add(x)
a.print_table()
