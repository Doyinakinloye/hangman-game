from tkinter import *
from hangman_brain import HangBrain
from random import *
THEME_COLOR = "#375362"


class UserInterface:

    def __init__(self, brain: HangBrain):
        self.Brain = brain
        self.root = Tk()
        self.root.title("Hangman")
        self.root.config(bg=THEME_COLOR)
        self.score = Label(text=f"lives: {self.Brain.LIVES}", font=("courier", 20, "bold"), fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=2, pady=10)
        self.canvas = Canvas(width=620, height=250, highlightthickness=0, bg="white")
        self.instructions = self.canvas.create_text(310, 120,
                                                    text="welcome to Doyin's hangman game🎉\nthe rules are as follows: "
                                                         "\nyou have 6 lives at the start of the game\n"
                                                         "when you guess a wrong word, you lose a life \n"
                                                         "when you run out of live without guessing the right word, "
                                                         "you lose the game\n",
                                                    font=("courier", 10, 'bold'))

        self.canvas.grid(column=1, row=1, pady=30, padx=30, columnspan=2)
        self.entry_box = Entry(width=50)
        self.entry_box.grid(row=2, column=1, columnspan=2)
        # This makes the cursor to be in the entry box
        self.entry_box.focus()
        self.Next_Button = Button(text="Next", width=10, command=self.gameplay)
        self.Next_Button.grid(row=3, column=2, pady=10)
        # The button to collect the users input
        self.Enter_Button = Button(text="Enter", width=10, command=self.check)
        self.Enter_Button.grid(row=3, column=1, pady=10)
        self.root.mainloop()

    def check(self):
        while self.Brain.blank_lines != self.Brain.word_list:
            prompt = self.entry_box.get()
            # To delete the input in the entry box
            self.entry_box.delete(0, END)
            if prompt not in self.Brain.word_list:
                self.Brain.LIVES -= 1
                self.score.config(text=f"Lives: {self.Brain.LIVES}")
                if self.Brain.LIVES == 0:
                    self.canvas.itemconfig(self.instructions, text="You lost🤕")
            elif prompt in self.Brain.word_list:
                for position in range(self.Brain.len_of_word):
                    if prompt == self.Brain.word_list[position]:
                        self.Brain.blank_lines[position] = prompt
                self.canvas.itemconfig(self.instructions, text=f"guess the letter:\n\n\n\n{self.Brain.blank_lines}")

        self.canvas.itemconfig(self.instructions, text="You've Won🙌")


    def gameplay(self):
        word = choice(self.Brain.words_dict)
        self.Brain.len_of_word = int(len(word))
        self.Brain.word_list = [*word]
        self.Brain.blank_lines = []
        for char in range(1, self.Brain.len_of_word + 1):
            self.Brain.blank_lines.append('_')
        self.canvas.itemconfig(self.instructions, text=f"guess the letter:\n\n\n\n{self.Brain.blank_lines}")
        self.Brain.LIVES = 6
