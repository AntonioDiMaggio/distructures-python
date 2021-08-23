class singlyLinkedNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


# Maybe remove this and stick with the binaryTreeNode.
class doublyLinkedNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class binaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
