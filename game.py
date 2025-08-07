import chess
from ai import get_best_move
from utils import print_board

class ChessGame:
    def __init__(self):
        self.board = chess.Board()

    def play(self):
        print("Welcome to Chess vs AI!")
        print_board(self.board)

        while not self.board.is_game_over():
            if self.board.turn == chess.WHITE:
                move = input("Your move (in UCI format, e.g., e2e4): ")
                try:
                    self.board.push_uci(move)
                except:
                    print("Invalid move. Try again.")
                    continue
            else:
                print("AI is thinking...")
                ai_move = get_best_move(self.board, depth=2)
                print(f"AI plays: {ai_move}")
                self.board.push(ai_move)

            print_board(self.board)

        print("Game over!")
        print(self.board.result())
