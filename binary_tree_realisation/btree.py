from btnode import BTNode
import copy
import random


class BinaryTree:
    """
    Tree for representing two of the possible game moves.
    """
    def __init__(self, board, is_first):
        self._root = BTNode(board)
        self.is_first = is_first
        self.build_btree()

    def build_btree(self):
        """
        Builds tree with two possible moves.
        :return:
        """
        def recursive(node, val):
            board = node.data
            valid_moves = board.get_free_cells()
            if len(valid_moves) == 0:
                return None
            if len(valid_moves) == 1:
                new_board = copy.deepcopy(board)
                if val:
                    new_board[valid_moves[0]] = "X"
                else:
                    new_board[valid_moves[0]] = "O"
                self.add_left(node, new_board)
                recursive(node.left, not val)
            else:
                random.shuffle(valid_moves)
                new_board1 = copy.deepcopy(board)
                new_board2 = copy.deepcopy(board)
                if val:
                    new_board1[valid_moves[0]] = "X"
                    new_board2[valid_moves[1]] = "X"
                else:
                    new_board1[valid_moves[0]] = "O"
                    new_board2[valid_moves[1]] = "O"
                self.add_left(node, new_board1)
                self.add_right(node, new_board2)
                recursive(node.left, not val)
                recursive(node.right, not val)
        recursive(self._root, self.is_first)

    def add_left(self, cur_node, value):
        """
        Adds left child to given node.
        :param cur_node: BTNode
        :param value: Board
        :return: None
        """
        cur_node.left = BTNode(value)

    def add_right(self, cur_node, value):
        """
        Adds right child to given node.
        :param cur_node: BTNode
        :param value: Board
        :return: None
        """
        cur_node.right = BTNode(value)

    def count_points(self):
        """
        Counts point for each node.
        :return: int
        """
        def recursive(cur_node):
            if not cur_node.left and not cur_node.right:
                result = cur_node.data.finished()
                if result == 0:
                    cur_node.points = 0
                elif result == 1:
                    cur_node.points = 1 if self.is_first else -1
                else:
                    cur_node.points = -1 if self.is_first else 1
                return cur_node.points
            cur_node.points = 0
            if cur_node.left:
                cur_node.points += recursive(cur_node.left)
            if cur_node.right:
                cur_node.points += recursive(cur_node.right)
            return cur_node.points
        recursive(self._root)

    def best_choice(self):
        """
        Returns best possible move.
        :return: tuple
        """
        if not self._root.right:
            return self._root.left.data.get_last_turn()
        if self._root.left.points > self._root.right.points:
            return self._root.left.data.get_last_turn()
        return self._root.right.data.get_last_turn()
