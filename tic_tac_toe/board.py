import tkinter
from tkinter import messagebox


class TicTacToe:
    """

    """
    def __init__(self, clicked=True):
        self.root = tkinter.Tk()
        self.root.title("Classic Tic-Tac-Toe")

        # Options Menu
        self.my_menu = tkinter.Menu(self.root)
        self.root.config(menu=self.my_menu)

        self.options_menu = tkinter.Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Options", menu=self.options_menu)
        self.options_menu.add_command(label="Reset Game", command= self.__reset)

        # Building the buttons for the board
        self.button_1 = tkinter.Button(self.root, text=" ",
                                       font=("Arial", 20),
                                       height=3, width=6,
                                       bg="SystemButtonFace",
                                       command= lambda: self.__click_button(self.button_1))
        self.button_2 = tkinter.Button(self.root, text=" ",
                                       font=("Arial", 20),
                                       height=3, width=6,
                                       bg="SystemButtonFace",
                                       command=lambda: self.__click_button(self.button_2))
        self.button_3 = tkinter.Button(self.root, text=" ",
                                       font=("Arial", 20),
                                       height=3, width=6,
                                       bg="SystemButtonFace",
                                       command=lambda: self.__click_button(self.button_3))
        self.button_4 = tkinter.Button(self.root, text=" ",
                                       font=("Arial", 20),
                                       height=3, width=6,
                                       bg="SystemButtonFace",
                                       command=lambda: self.__click_button(self.button_4))
        self.button_5 = tkinter.Button(self.root, text=" ",
                                       font=("Arial", 20),
                                       height=3, width=6,
                                       bg="SystemButtonFace",
                                       command=lambda: self.__click_button(self.button_5))
        self.button_6 = tkinter.Button(self.root, text=" ",
                                       font=("Arial", 20),
                                       height=3, width=6,
                                       bg="SystemButtonFace",
                                       command=lambda: self.__click_button(self.button_6))
        self.button_7 = tkinter.Button(self.root, text=" ",
                                       font=("Arial", 20),
                                       height=3, width=6,
                                       bg="SystemButtonFace",
                                       command=lambda: self.__click_button(self.button_7))
        self.button_8 = tkinter.Button(self.root, text=" ",
                                       font=("Arial", 20),
                                       height=3, width=6,
                                       bg="SystemButtonFace",
                                       command=lambda: self.__click_button(self.button_8))
        self.button_9 = tkinter.Button(self.root, text=" ",
                                       font=("Arial", 20),
                                       height=3, width=6,
                                       bg="SystemButtonFace",
                                       command=lambda: self.__click_button(self.button_9))
        # Put the buttons in a grid
        self.button_1.grid(row=0, column=0)
        self.button_2.grid(row=0, column=1)
        self.button_3.grid(row=0, column=2)
        self.button_4.grid(row=1, column=0)
        self.button_5.grid(row=1, column=1)
        self.button_6.grid(row=1, column=2)
        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)

        # Tracking the players moves
        self.clicked = clicked  # X is True and O is False
        self.count_moves = 0
        self.winner = False

    def __click_button(self, button):
        # Only allow players to select empty grids
        if button["text"] == " " and self.clicked == True:
            button["text"] = "X"
            self.clicked = False
            self.count_moves += 1
            self.__check_winner()
        elif button["text"] == " " and self.clicked == False:
            button["text"] = "O"
            self.clicked = True
            self.count_moves += 1
            self.__check_winner()
        else:
            messagebox.showerror(title="Oh No!",
                                 message="That position has been selected!\nPlease select another position...")

    def __disable_buttons(self):
        self.button_1.config(state="disabled")
        self.button_2.config(state="disabled")
        self.button_3.config(state="disabled")
        self.button_4.config(state="disabled")
        self.button_5.config(state="disabled")
        self.button_6.config(state="disabled")
        self.button_7.config(state="disabled")
        self.button_8.config(state="disabled")
        self.button_9.config(state="disabled")

    def __check_winner(self):
        # Top row solution for X
        if self.button_1["text"] == "X" and self.button_2["text"] == "X" and self.button_3["text"] == "X":
            self.button_1.config(bg="yellow")
            self.button_2.config(bg="yellow")
            self.button_3.config(bg="yellow")
            self.winner = True
            messagebox.showinfo(title="Classic Tic-Tac-Toe",
                                message="CONGRATULATIONS! X is the Winner")
            self.__disable_buttons()
        # Middle row solution for X
        elif self.button_4["text"] == "X" and self.button_5["text"] == "X" and self.button_6["text"] == "X":
             self.button_4.config(bg="yellow")
             self.button_5.config(bg="yellow")
             self.button_6.config(bg="yellow")
             self.winner = True
             messagebox.showinfo(title="Classic Tic-Tac-Toe",
                                 message="CONGRATULATIONS! X is the Winner")
             self.__disable_buttons()
        # Bottom row solution for X
        elif self.button_7["text"] == "X" and self.button_8["text"] == "X" and self.button_9["text"] == "X":
             self.button_7.config(bg="yellow")
             self.button_8.config(bg="yellow")
             self.button_9.config(bg="yellow")
             self.winner = True
             messagebox.showinfo(title="Classic Tic-Tac-Toe",
                                 message="CONGRATULATIONS! X is the Winner")
             self.__disable_buttons()
        # First column solution for X
        elif self.button_1["text"] == "X" and self.button_4["text"] == "X" and self.button_7["text"] == "X":
             self.button_1.config(bg="yellow")
             self.button_4.config(bg="yellow")
             self.button_7.config(bg="yellow")
             self.winner = True
             messagebox.showinfo(title="Classic Tic-Tac-Toe",
                                 message="CONGRATULATIONS! X is the Winner")
             self.__disable_buttons()
        # Second column solution for X
        elif self.button_2["text"] == "X" and self.button_5["text"] == "X" and self.button_8["text"] == "X":
             self.button_2.config(bg="yellow")
             self.button_5.config(bg="yellow")
             self.button_8.config(bg="yellow")
             self.winner = True
             messagebox.showinfo(title="Classic Tic-Tac-Toe",
                                 message="CONGRATULATIONS! X is the Winner")
             self.__disable_buttons()
        # Last column solution for X
        elif self.button_3["text"] == "X" and self.button_6["text"] == "X" and self.button_9["text"] == "X":
             self.button_3.config(bg="yellow")
             self.button_6.config(bg="yellow")
             self.button_9.config(bg="yellow")
             self.winner = True
             messagebox.showinfo(title="Classic Tic-Tac-Toe",
                                 message="CONGRATULATIONS! X is the Winner")
             self.__disable_buttons()
        # Left to right diagonal solution for X
        elif self.button_1["text"] == "X" and self.button_5["text"] == "X" and self.button_9["text"] == "X":
             self.button_1.config(bg="yellow")
             self.button_5.config(bg="yellow")
             self.button_9.config(bg="yellow")
             self.winner = True
             messagebox.showinfo(title="Classic Tic-Tac-Toe",
                                 message="CONGRATULATIONS! X is the Winner")
             self.__disable_buttons()
        # Right to left diagonal solution for X
        elif self.button_3["text"] == "X" and self.button_5["text"] == "X" and self.button_7["text"] == "X":
             self.button_3.config(bg="yellow")
             self.button_5.config(bg="yellow")
             self.button_7.config(bg="yellow")
             self.winner = True
             messagebox.showinfo(title="Classic Tic-Tac-Toe",
                                 message="CONGRATULATIONS! X is the Winner")
             self.__disable_buttons()
        # Top row solution for O
        elif self.button_1["text"] == "O" and self.button_2["text"] == "O" and self.button_3["text"] == "O":
             self.button_1.config(bg="yellow")
             self.button_2.config(bg="yellow")
             self.button_3.config(bg="yellow")
             self.winner = True
             messagebox.showinfo(title="Classic Tic-Tac-Toe",
                              message="CONGRATULATIONS! O is the Winner")
             self.__disable_buttons()
        # Middle row solution for O
        elif self.button_4["text"] == "O" and self.button_5["text"] == "O" and self.button_6["text"] == "O":
             self.button_4.config(bg="yellow")
             self.button_5.config(bg="yellow")
             self.button_6.config(bg="yellow")
             self.winner = True
             messagebox.showinfo(title="Classic Tic-Tac-Toe",
                                 message="CONGRATULATIONS! O is the Winner")
             self.__disable_buttons()
         # Bottom row solution for O
        elif self.button_7["text"] == "O" and self.button_8["text"] == "O" and self.button_9["text"] == "O":
             self.button_7.config(bg="yellow")
             self.button_8.config(bg="yellow")
             self.button_9.config(bg="yellow")
             self.winner = True
             messagebox.showinfo(title="Classic Tic-Tac-Toe",
                                 message="CONGRATULATIONS! O is the Winner")
             self.__disable_buttons()
        # First column solution for O
        elif self.button_1["text"] == "O" and self.button_4["text"] == "O" and self.button_7["text"] == "O":
             self.button_1.config(bg="yellow")
             self.button_4.config(bg="yellow")
             self.button_7.config(bg="yellow")
             self.winner = True
             messagebox.showinfo(title="Classic Tic-Tac-Toe",
                                 message="CONGRATULATIONS! O is the Winner")
             self.__disable_buttons()
        # Second column solution for O
        elif self.button_2["text"] == "O" and self.button_5["text"] == "O" and self.button_8["text"] == "O":
             self.button_2.config(bg="yellow")
             self.button_5.config(bg="yellow")
             self.button_8.config(bg="yellow")
             self.winner = True
             messagebox.showinfo(title="Classic Tic-Tac-Toe",
                                 message="CONGRATULATIONS! O is the Winner")
             self.__disable_buttons()
        # Last column solution for O
        elif self.button_3["text"] == "O" and self.button_6["text"] == "O" and self.button_9["text"] == "O":
             self.button_3.config(bg="yellow")
             self.button_6.config(bg="yellow")
             self.button_9.config(bg="yellow")
             self.winner = True
             messagebox.showinfo(title="Classic Tic-Tac-Toe",
                                 message="CONGRATULATIONS! O is the Winner")
             self.__disable_buttons()
        # Left to right diagonal solution for O
        elif self.button_1["text"] == "O" and self.button_5["text"] == "O" and self.button_9["text"] == "O":
             self.button_1.config(bg="yellow")
             self.button_5.config(bg="yellow")
             self.button_9.config(bg="yellow")
             self.winner = True
             messagebox.showinfo(title="Classic Tic-Tac-Toe",
                                 message="CONGRATULATIONS! O is the Winner")
             self.__disable_buttons()
        # Right to left diagonal solution for O
        elif self.button_3["text"] == "O" and self.button_5["text"] == "O" and self.button_7["text"] == "O":
             self.button_3.config(bg="yellow")
             self.button_5.config(bg="yellow")
             self.button_7.config(bg="yellow")
             self.winner = True
             messagebox.showinfo(title="Classic Tic-Tac-Toe",
                                message="CONGRATULATIONS! O is the Winner")
             self.__disable_buttons()

        # It's a tie if nobody wins and we run out of squares
        elif self.count_moves == 9 and self.winner == False:
            messagebox.showinfo(title="Classic Tic Tac Toe",
                                message="It's a TIE!")
            self.__disable_buttons()


    def __reset(self):
        self.count_moves = 0

        # Building the buttons for the board
        self.button_1 = tkinter.Button(self.root, text=" ",
                                       font=("Arial", 20),
                                       height=3, width=6,
                                       bg="SystemButtonFace",
                                       command=lambda: self.click_button(self.button_1))
        self.button_2 = tkinter.Button(self.root, text=" ",
                                       font=("Arial", 20),
                                       height=3, width=6,
                                       bg="SystemButtonFace",
                                       command=lambda: self.click_button(self.button_2))
        self.button_3 = tkinter.Button(self.root, text=" ",
                                       font=("Arial", 20),
                                       height=3, width=6,
                                       bg="SystemButtonFace",
                                       command=lambda: self.click_button(self.button_3))
        self.button_4 = tkinter.Button(self.root, text=" ",
                                       font=("Arial", 20),
                                       height=3, width=6,
                                       bg="SystemButtonFace",
                                       command=lambda: self.click_button(self.button_4))
        self.button_5 = tkinter.Button(self.root, text=" ",
                                       font=("Arial", 20),
                                       height=3, width=6,
                                       bg="SystemButtonFace",
                                       command=lambda: self.click_button(self.button_5))
        self.button_6 = tkinter.Button(self.root, text=" ",
                                       font=("Arial", 20),
                                       height=3, width=6,
                                       bg="SystemButtonFace",
                                       command=lambda: self.click_button(self.button_6))
        self.button_7 = tkinter.Button(self.root, text=" ",
                                       font=("Arial", 20),
                                       height=3, width=6,
                                       bg="SystemButtonFace",
                                       command=lambda: self.click_button(self.button_7))
        self.button_8 = tkinter.Button(self.root, text=" ",
                                       font=("Arial", 20),
                                       height=3, width=6,
                                       bg="SystemButtonFace",
                                       command=lambda: self.click_button(self.button_8))
        self.button_9 = tkinter.Button(self.root, text=" ",
                                       font=("Arial", 20),
                                       height=3, width=6,
                                       bg="SystemButtonFace",
                                       command=lambda: self.click_button(self.button_9))
        # Put the buttons in a grid
        self.button_1.grid(row=0, column=0)
        self.button_2.grid(row=0, column=1)
        self.button_3.grid(row=0, column=2)
        self.button_4.grid(row=1, column=0)
        self.button_5.grid(row=1, column=1)
        self.button_6.grid(row=1, column=2)
        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)

    def play(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
