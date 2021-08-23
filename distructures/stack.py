from .nodes import singlyLinkedNode


class stack(object):
    def __init__(self):
        self._top = None
        self._bottom = None
        self._length = 0

    def __str__(self):
        if self._top is None:
            return "[]"
        current = self._top
        s = "["
        while current.next:
            s += str(current.value) + " <- "
            current = current.next
        if current:
            s += str(current.value)
        s += "]"
        return s

    def __len__(self):
        return self._length

    def empty(self):
        return 0 == self._length

    def top(self):
        return self._top.value

    def bottom(self):
        return self._bottom

    def push(self, value):
        if self._top is None or self._bottom is None:
            self._top = self._bottom = singlyLinkedNode(value)
            self._length += 1
        else:
            temp = self._top
            self._top = singlyLinkedNode(value)
            self._top.next = temp
            self._length += 1

    def pop(self):
        if self._top is None:
            return None
        temp = self._top.next
        value = self._top.value
        del self._top
        self._top = temp
        self._length -= 1
        return value
