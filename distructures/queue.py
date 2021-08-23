from .nodes import singlyLinkedNode


class queue(object):
    def __init__(self):
        self._front = None
        self._rear = None
        self._length = 0

    # O(n)
    def __str__(self):
        if self._front is None:
            return "[]"
        current = self._front
        s = "["
        while current.next:
            s += str(current.value) + " -> "
            current = current.next
        if current:
            s += str(current.value)
        s += "]"
        return s

    # O(1)
    def __len__(self):
        return self._length

    def empty(self):
        return 0 == self._length

    # O(1)
    def front(self):
        return self._front.value

    # O(1)
    def rear(self):
        return self._rear.value

    # O(1)
    def push(self, value):
        if self._front is None or self._rear is None:
            self._front = self._rear = singlyLinkedNode(value)
            self._length += 1
        else:
            self._rear.next = singlyLinkedNode(value)
            self._rear = self._rear.next
            self._length += 1

    # O(1)
    def pop(self):
        if self._front is None:
            return None
        temp = self._front.next
        value = self._front.value
        del self._front
        self._front = temp
        self._length -= 1
        return value
