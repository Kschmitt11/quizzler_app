from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.canvas = Canvas(self.window, width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)


        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=self.true_img, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=self.false_img, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white", font=("Arial", 12, "bold"))
        self.score_label.grid(column=1, row=0, pady=20)


        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)