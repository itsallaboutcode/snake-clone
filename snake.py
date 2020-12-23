# -*- coding: utf-8 -*-

import tkinter as tk


class MainApplication(tk.Canvas):
    def __init__(self):
        super().__init__(
            width=500, height=520, background="#000", highlightthickness=0
        )

        self.score = 0

        self.game_area()

        self.pack()

    def game_area(self):
        self.create_text(
            45, 12, text=f"Score: {self.score}", tag="score", fill="#fff", font=10
        )

        self.create_rectangle(7, 27, 493, 513, outline="#fff")


def main():
    root = tk.Tk()
    root.title("snake clone")
    root.resizable(False, False)

    game = MainApplication()

    root.mainloop()


if __name__ == '__main__':
    main()
