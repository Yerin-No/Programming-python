import tkinter
from tkinter import messagebox

from tictactoe_gameengine import TictactoeGameEngine

class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()
        self.init_GUI()
    def init_GUI(self):
        self.CANVAS_SIZE = 300
        self.root = tkinter.Tk()
        self.root.title('틱택토')
        self.root.geometry(f'{self.CANVAS_SIZE}x{self.CANVAS_SIZE}')
        self.root.resizable(width=False, height=False)

        self.canvas = tkinter.Canvas(self.root, bg='white', width=self.CANVAS_SIZE, height=self.CANVAS_SIZE)

        self.canvas.pack()

        self.images = {}        #{'X' : PhotoImage객체, 'O' : PhotoImage객체}
        self.images['X'] = tkinter.PhotoImage(file='X.gif')
        self.images['O'] = tkinter.PhotoImage(file='O.gif')

        self.canvas.bind('<Button-1>', self.click_handler)      #***매우중요***

        self.root.mainloop()

    def click_handler(self, event):
        # print(f'{event.x}, {event.y}')
        row, col = self.coordinate_to_position(event.x,event.y)
        #set row, col
        self.game_engine.set(row, col)
        #show board
        self.game_engine.show_board()
        self.draw_board()
        #set winner
        winner = self.game_engine.set_winner()
        #승자가 있거나 무승부이면, 게임오벼, 결과 표시
        if winner == 'O' or winner == 'X':
            messagebox.showinfo('Game Over', f'{winner}이김!')
        elif winner =='d':
            messagebox.showinfo('Game Over', '무승부!')
            self.root.quit()
        #change_turn
        self.game_engine.change_turn()

    def draw_board(self):
        TILE_SIZE = self.CANVAS_SIZE // self.game_engine.SIZE       #300 // 3 = 100
        x = 0
        y = 0

        for i, v in enumerate(self.game_engine.board):
            if v == '.':
                pass
            else:       #elif v == 'X' or v == 'O':
                self.canvas.create_image(x, y, anchor='nw', image=self.images[v])
            x += TILE_SIZE

            if i % self.game_engine.SIZE == self.game_engine.SIZE -1:
                x = 0
                y += TILE_SIZE

    def coordinate_to_position(self, x, y):
        # if 0<=x<100:
        #     col = 1
        # elif 100<=x<200:
        #     col = 2
        # elif 200<=x<300:
        #     col = 3
        # elif 0<=y<100:
        #     row = 1
        # elif 100<=y<100:
        #     row = 2
        # elif 200<=y<300:
        #     row = 3

        row = y//(self.CANVAS_SIZE // self.game_engine.SIZE)+1
        cal = x//(self.CANVAS_SIZE // self.game_engine.SIZE)+1
        # cal = x//100+1

        return row, cal


if __name__ == '__main__':
    ttt_GUI = TictactoeGUI()