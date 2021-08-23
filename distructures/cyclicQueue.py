

class cyclicQueue(object):
    def __init__(self, size):
        self._size = size
        self._elements = [None for i in range(size)]
        self._front = 0
        self._rear = 0
        self._length = 0

    # O(n)
    def __str__(self):
        s = "["
        for i in range(self._length - 1):
            s += str(self._elements[(i + self._front) % self._size]) + ", "
        if 0 < self._length:
            s += str(self._elements[(self._length - 1 + self._front) % self._size])
        s += "]"
        return s

    # O(1)
    def __len__(self):
        return self._length

    def empty(self):
        return 0 == self._length

    # O(1)
    def front(self):
        return self._elements[self._front]

    # O(1)
    def rear(self):
        return self._elements[self._rear]

    # O(1)
    def push(self, value):
        if 0 == self._length:
            self._elements[self._rear] = value
            self._length += 1
        else:
            self._rear = (self._rear + 1) % self._size
            self._elements[self._rear] = value
            self._length += 1

            if self._rear == self._front:
                self._front = (self._front + 1) % self._size
                self._length -= 1

    # O(1)
    def pop(self):
        if 0 == self._length:
            return None
        if 1 == self._length:
            front = self._elements[self._front]
            self._elements[self._front] = None
            self._length -= 1
            return front

        front = self._elements[self._front]
        self._elements[self._front] = None
        self._front = (self._front + 1) % self._size
        self._length -= 1

        return front

    def trimToSize(self, newSize):
        pass
