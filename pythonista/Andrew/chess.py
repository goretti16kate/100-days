import tkinter as tk

class BoardGuiTk(tk.Frame):
    color = "gray"
    rows = 7
    column = 7 
    square_size ="20x20"

    def canvas_size(self):
        return (self.column*self.square_size, self.rows*self.square_size)

    def __init__(self, chessboard