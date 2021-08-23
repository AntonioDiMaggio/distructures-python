from .nodes import singlyLinkedNode


class linkedList(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def __str__(self):
        if self._head is None:
            return "[]"
        current = self._head
        s = "["
        while current.next:
            s += str(current.value) + " -> "
            current = current.next
        if current:
            s += str(current.value)
        s += "]"
        return s

    def __len__(self):
        return self._length

    def empty(self):
        return 0 == self._length

    def head(self):
        return self._head

    def tail(self):
        return self._tail

    def append(self, value):
        if self._head is None or self._tail is None:
            self._head = self._tail = singlyLinkedNode(value)
            self._length += 1
        else:
            self._tail.next = singlyLinkedNode(value)
            self._tail = self._tail.next
            self._length += 1

    def remove(self, value):
        if self._head is None or 0 == self._length:
            raise ValueError("Value not in linked list.")
            return

        # We have 4 cases.
        # 1.) There is one item in the list.
        # 2.) We are removing head.
        # 3.) We are removing something from the middle of the list.
        # 4.) We are removing the tail.

        # 1.)
        if self._head == self._tail or 1 == self._length:
            if self._head.value == value:
                del self._head
                self._head = self._tail = None
                self._length -= 1
                return
            else:
                raise ValueError("Value not in linked list.")
                return

        # 2.)
        if self._head.value == value:
            temp = self._head.next
            del self._head
            self._head = temp
            self._length -= 1
            return

        current = self._head
        while current.next:
            if current.next.value == value:
                # 3.)
                if current.next.next:
                    temp = current.next
                    current.next = current.next.next
                    del temp
                    self._length -= 1
                    return
                # 4.)
                else:
                    self._tail = current
                    del current.next
                    self._tail.next = None
                    self._length -= 1
                    return
            current = current.next

        raise ValueError("Value not in linked list.")
        return

    def pop(self):
        value = self._tail.value
        del self._tail
        return value
