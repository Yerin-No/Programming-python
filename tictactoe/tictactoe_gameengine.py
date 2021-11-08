class TictactoeGameEngine:
    def __init__(self):
        self.board = list('.' * 9)      #['.','.','.','.','.','.','.','.']
        self.turn = 'X'
        self.SIZE = 3

    def show_board(self):
        for i, v in enumerate(self.board):
            print(v + ' ', end='')
            if i % 3 == 2:
                print()

        # for i in range(len(self.board)):
        #     print((self.board[i]+" ") if (i+1)%3!=0 else (self.board[i]+"\n"), end='')
        # print()

        # print('  '.join(self.board[0:3]))
        # print('  '.join(self.board[3:6]))
        # print('  '.join(self.board[6:9]))

    def set(self, row, col):
        #input -> 처리 -> output:row,col -> 처리 -> index
        self.board[3*(row-1)+(col-1)] = self.turn

    def position_to_index(self, row, col):
        return (row - 1) * 3 + (col - 1)

    def set_winner(self):
        # - 3줄
        for row in range(1, 3 + 1):
            if self.board[self.position_to_index(row, 1)] \
                    == self.board[self.position_to_index(row, 2)] \
                    == self.board[self.position_to_index(row, 3)] \
                    == self.turn:
                return self.turn
        # |줄
        for col in range(1, 3 + 1):
            if self.board[self.position_to_index(1, col)] \
                    == self.board[self.position_to_index(2, col)] \
                    == self.board[self.position_to_index(3, col)] \
                    == self.turn:
                return self.turn
        #/
        if self.board[self.position_to_index(1, 3)] \
            == self.board[self.position_to_index(2, 2)] \
            == self.board[self.position_to_index(3, 1)] \
            == self.turn:
            return self.turn
        #\
        if self.board[self.position_to_index(1, 1)] \
            == self.board[self.position_to_index(2, 2)] \
            == self.board[self.position_to_index(3, 3)] \
            == self.turn:
            return self.turn

        # # - 3줄 : 1,2,3 | 4,5,6 | 7,8,9 -> 0,1,2 | 3,4,5 | 6,7,8
        # for i in range(0, 7):
        #     if i == 0 or i == 3 or i == 6:
        #         if self.board[i] == self.board[i + 1] == self.board[i + 2]:
        #             print("-")
        # # | 3줄 1,4,7 | 2,5,8 | 3,6,9 -> 0,3,6 | 1,4,7 | 2,5,8
        # for i in range(0, 3):
        #     if i == 0 or i == 1 or i == 2:
        #         if self.board[i] == self.board[i + 3] == self.board[i + 6]:
        #             print("|")
        # # / 줄
        # if self.board[2] == 'X' and self.board[4] == 'X' and self.board[6] == 'X':
        #     return print('X 승리')
        # if self.board[2] == 'O' and self.board[4] == 'O' and self.board[6] == 'O':
        #     return print('O 승리')
        # # \ 줄
        # if self.board[0] == 'X' and self.board[4] == 'X' and self.board[8] == 'X':
        #     return print('X 승리')
        # if self.board[0] == 'O' and self.board[4] == 'O' and self.board[8] == 'O':
        #     return print('O 승리')

        # 끝나는 경우 : 무승부(승자가 없는 상태로 놓을 자리가 없음), 승자 결정(승자가 있음)
        # if self.board[0] != '.' and self.board[1] != '.' and self.board[2] != '.' and \
        #         self.board[3] != '.' and self.board[4] != '.' and self.board[5] != '.' and \
        #         self.board[6] != '.' and self.board[7] != '.' and self.board[8] != '.':
        if not '.' in self.board:
            return 'd'  # draw

    def change_turn(self):
        self.turn = 'O' if self.turn=='X' else 'X'

if __name__ == '__main__':
    game_engin = TictactoeGameEngine()
    game_engin.show_board()     # ...\n...\n...
    game_engin.set(2,2)
    game_engin.show_board()     #['.','.','.','.','X','.','.','.']
    game_engin.set(2,1)
    game_engin.set(2,3)
    game_engin.show_board()     #['.','.','.','.'X','X','X','.','.']
    game_engin.set_winner()     # '-' 아무것도 안뜨게
    print(game_engin.turn)  # 'O'   현재 턴
    game_engin.change_turn()
    print(game_engin.turn)      # 'O'   현재 턴
    game_engin.change_turn()
    print(game_engin.turn)  # 'O'   현재 턴