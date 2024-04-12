from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Ui:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.quiz.next_question()
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.score = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR,
                           font=("Arial", 12, "italic"))
        self.score.grid(row=0, column=2)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280,
                                                     text=f"Q. {self.quiz.question_number}: {self.quiz.current_question.text}",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1,column=0, columnspan=3, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_img, command=self.true_button_click)
        self.true_button.grid(row=2, column=2)

        self.false_button = Button(image=false_img, command=self.false_button_click)
        self.false_button.grid(row=2, column=0)

        self.window.mainloop()

    def update_question(self):
        self.canvas.itemconfig(self.question_text, text=f"Q. {self.quiz.question_number}: {self.quiz.current_question.text}")
        self.score.config(text=f"Score: {self.quiz.score}")
    def change_question(self):
        try:
            self.quiz.next_question()
        except IndexError:
            self.canvas.itemconfig(self.question_text, text=f"THE END! Your final score is; {self.quiz.score}")

    def true_button_click(self):
        if self.quiz.current_question.answer.lower() == "true":
            self.canvas.itemconfig(self.question_text, text="Good answer! Congratulations!")
            self.quiz.good_answer()

        else:
            self.canvas.itemconfig(self.question_text, text="Wrong answer! :(")

        self.quiz.next_question()
        self.window.after(ms=1500, func=self.update_question)

    def false_button_click(self):
        if self.quiz.current_question.answer.lower() == "false":
            self.canvas.itemconfig(self.question_text, text="Good answer! Congratulations!")
            self.quiz.good_answer()

        else:
            self.canvas.itemconfig(self.question_text, text="Wrong answer! :(")

        self.quiz.next_question()
        self.window.after(ms=1500, func=self.update_question)


