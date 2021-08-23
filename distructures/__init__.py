class cyclicQueue(object):
    def __init__(self, size):
        self._size = size
        self._elements = [None for i in range(size)]
        self._count = 0
        self._front = 0
        self._rear = 0

    def __str__(self):
        s = "["
        for i in range(self._count - 1):
            s += str(self._elements[(i + self._front) % self._size]) + ", "
        if 0 < self._count:
            s += str(self._elements[(self._count - 1 + self._front) % self._size])
        s += "]"
        return s

    def __len__(self):
        return self._count

    def front(self):
        return self._elements[self._front]

    def rear(self):
        return self._elements[self._rear]

    # Add value to rear of queue.
    def push(self, value):
        if 0 == self._count:
            self._elements[self._rear] = value
            self._count += 1
        else:
            self._rear = (self._rear + 1) % self._size
            self._elements[self._rear] = value
            self._count += 1

            if self._rear == self._front:
                self._front = (self._front + 1) % self._size
                self._count -= 1

    def pop(self):
        if 0 == self._count:
            return None
        if 1 == self._count:
            front = self._elements[self._front]
            self._elements[self._front] = None
            self._count -= 1
            return front

        front = self._elements[self._front]
        self._elements[self._front] = None
        self._front = (self._front + 1) % self._size
        self._count -= 1

        return front

    def trimToSize(self, newSize):
        pass
