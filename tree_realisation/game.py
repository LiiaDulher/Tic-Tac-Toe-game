from board import Board
from tree import Tree


def print_rules():
    """
    Prints rules of the game.
    :return: None
    """
    print("Welcome to Tic-Tac-Toe game!")
    print("You will play with computer.")
    print("You and computer will make a move one by one.")
    print("To make a move choose a sell on the board.")
    print("First player to have three equal symbols horizontally, vertically or diagonally wins")
    print("First player has symbol 'X', and second - 'O'")
    print("Have a nice game!")


def computer(board, is_first):
    board_tree = Tree(board, is_first)
    board_tree.count_points()
    return board_tree.best_choice()


def first_player(board):
    while board.finished() == -1:
        while True:
            print("Please enter cell coordinates:")
            coordinates = input().split(' ')
            row = int(coordinates[0])
            col = int(coordinates[1])
            if (row, col) in board.get_free_cells():
                try:
                    board[row, col] = "X"
                    break
                except AssertionError:
                    print("Wrong coordinates!")
            else:
                print("Wrong coordinates!")
        board.draw()
        if board.finished() != -1:
            return board.finished()
        print("Computer makes its move.")
        row, col = computer(board, False)
        board[row, col] = "O"
        board.draw()
    return board.finished()


def second_player(board):
    while board.finished() == -1:
        print("Computer makes its move.")
        row, col = computer(board, True)
        board[row, col] = "X"
        board.draw()
        if board.finished() != -1:
            return board.finished()
        while True:
            print("Please enter cell coordinates:")
            coordinates = input().split(' ')
            row = int(coordinates[0])
            col = int(coordinates[1])
            if (row, col) in board.get_free_cells():
                try:
                    board[row, col] = "O"
                    break
                except AssertionError:
                    print("Wrong coordinates!")
            else:
                print("Wrong coordinates!")
        board.draw()
    return board.finished()


def main():
    print_rules()
    board = Board()
    while True:
        print("Game starts!")
        print("Which player would you like to be 1 or 2:")
        number = input()
        while number != "1" and number != "2":
            number = input("Player's number is 1 or 2:")
        number = int(number)
        board.draw()
        if number == 1:
            result = first_player(board)
            if result:
                if result == 1:
                    print("You won!")
                else:
                    print("Computer won!")
            else:
                print("You have a tie!")
        else:
            result = second_player(board)
            if result:
                if result == 2:
                    print("You won!")
                else:
                    print("Computer won!")
            else:
                print("You have a tie!")
        print("Do you wont to restart the game(yes/no)?")
        wish = input()
        while wish != "yes" and wish != "no":
            wish = input("yes or no")
        if wish == "no":
            print("Thank you for playing the game!")
            break
        else:
            board.clear()


if __name__ == "__main__":
    main()
