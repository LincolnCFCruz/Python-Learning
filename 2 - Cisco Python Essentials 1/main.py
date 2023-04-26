import random

class JogoDaVelha():
    def __init__(self):
        print('Welcome to Tic Tac Toe!')
        pass

    # Imprime o tabuleiro do jogo.
    def display_board(self, board):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   {}   |   {}   |   {}   |".format(board[0], board[1], board[2]))
        print("|       |       |       |")
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   {}   |   {}   |   {}   |".format(board[3], board[4], board[5]))
        print("|       |       |       |")
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   {}   |   {}   |   {}   |".format(board[6], board[7], board[8]))
        print("|       |       |       |")
        print("+-------+-------+-------+")

    # Pede ao jogador que escolha entre X ou O e retorna uma tupla com as escolhas do jogador e do computador.
    def player_input(self):
        marker = ''
        while not (marker == 'O' or marker == 'X'):
            marker = input("Do you want to be X or O? ").upper()
        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')

    # Recebe uma posição e uma marcação, depois coloca a marcação na posição correspondente no tabuleiro.
    def place_marker(self, board, marker, position):
        board[position-1] = marker

    # Verifica se alguma linha, coluna ou diagonal do tabuleiro contém três marcas iguais.
    def win_check(self, board, mark):
        return ((board[0] == mark and board[1] == mark and board[2] == mark) or
        (board[3] == mark and board[4] == mark and board[5] == mark) or
        (board[6] == mark and board[7] == mark and board[8] == mark) or
        (board[0] == mark and board[3] == mark and board[6] == mark) or
        (board[1] == mark and board[4] == mark and board[7] == mark) or
        (board[2] == mark and board[5] == mark and board[8] == mark) or
        (board[0] == mark and board[4] == mark and board[8] == mark) or
        (board[2] == mark and board[4] == mark and board[6] == mark))

    # Escolhe aleatoriamente qual jogador começa.
    def choose_first(self):
        if random.randint(0, 1) == 0:
            return 'computer'
        else:
            return 'player'

    # Verifica se uma posição no tabuleiro está vazia.
    def space_check(self, board, position):
        return board[position-1] == ' '

    # Verifica se o tabuleiro está completamente preenchido.
    def full_board_check(self, board):
        return not ' ' in board

    # Pede ao jogador que escolha uma posição no tabuleiro.
    def player_choice(self,board):
        position = 0
        while position not in range(1, 10) or not self.space_check(board, position):
            position = int(input("Choose your next position (1-9): "))
        return position

    # Escolhe uma posição aleatória no tabuleiro.
    def computer_choice(self, board):
        position = random.randint(1, 9)
        while not self.space_check(board, position):
            position = random.randint(1, 9)
        return position

    # Define a lógica principal do jogo, em que os jogadores alternam jogadas até que alguém ganhe ou o tabuleiro fique cheio.
    def game(self):
        board = [' '] * 9
        player_marker, computer_marker = self.player_input()
        turn = self.choose_first()
        print(turn + ' will go first.')
        while True:
            # Turno do jogador
            if turn == 'player':
                self.display_board(board)
                position = self.player_choice(board)
                self.place_marker(board, player_marker, position)
                if self.win_check(board, player_marker):
                    self.display_board(board)
                    print("Congratulations! You have won the game!")
                    break
                elif self.full_board_check(board):
                    self.display_board(board)
                    print("The game is a tie!")
                    break
                turn = 'computer'

            # Turno do computador
            else:
                self.display_board(board)
                print("Computer's turn...")
                position = self.computer_choice(board)
                self.place_marker(board, computer_marker, position)
                if self.win_check(board, computer_marker):
                    self.display_board(board)
                    print("Sorry, the computer has won the game!")
                    break
                elif self.full_board_check(board):
                    self.display_board(board)
                    print("The game is a tie!")
                    break
                turn = 'player'


if __name__ == "__main__":
    exec_jogo = JogoDaVelha()
    exec_jogo.game()

    while True:
        play_again = input("Do you want to play again? (Y/N)").upper()
        if play_again == 'Y':
            exec_jogo.game()
        else:
            print("Thanks for playing Tic Tac Toe!")
            break