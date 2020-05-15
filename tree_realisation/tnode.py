class TNode(object):
    """Represents a node for a linked tree."""

    def __init__(self, data):
        self.data = data
        self.children = []
        self.points = None
