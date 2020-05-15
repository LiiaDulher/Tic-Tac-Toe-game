from tnode import TNode
import copy


class Tree:
    """
    Tree for representing the possible game moves.
    """
    def __init__(self, board, is_first):
        self._root = TNode(board)
        self.is_first = is_first
        self.build_tree()

    def build_tree(self):
        """
        Builds tree with two possible moves.
        :return:
        """
        def recursive(node, val):
            board = node.data
            valid_moves = board.get_free_cells()
            if len(valid_moves) == 0:
                return None
            else:
                for move in valid_moves:
                    new_board = copy.deepcopy(board)
                    if val:
                        new_board[move] = "X"
                    else:
                        new_board[move] = "O"
                    self.add_child(node, new_board)
                for child in node.children:
                    recursive(child, not val)
        recursive(self._root, self.is_first)

    def add_child(self, cur_node, value):
        """
        Adds child to given node.
        :param cur_node: BTNode
        :param value: Board
        :return: None
        """
        new_node = TNode(value)
        cur_node.children.append(new_node)

    def count_points(self):
        """
        Counts point for each node.
        :return: int
        """
        def recursive(cur_node):
            if not cur_node.children:
                result = cur_node.data.finished()
                if result == 0:
                    cur_node.points = 0
                elif result == 1:
                    cur_node.points = 1 if self.is_first else -1
                else:
                    cur_node.points = -1 if self.is_first else 1
                return cur_node.points
            cur_node.points = 0
            for child in cur_node.children:
                cur_node.points += recursive(child)
            return cur_node.points
        recursive(self._root)

    def best_choice(self):
        """
        Returns best possible move.
        :return: tuple
        """
        maximum = self._root.children[0].points
        max_node = self._root.children[0]
        for child in self._root.children:
            if child.points > maximum:
                max_node = child
                maximum = child.points
        return max_node.data.get_last_turn()
