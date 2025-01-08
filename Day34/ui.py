from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 16, "italic")


class Interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="White")
        self.text = self.canvas.create_text(
            150,
            125,
            text="Question",
            width=280,
            font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # Button
        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")
        self.wrong_button = Button(image=false_img, highlightthickness=0, command=self.wrong_button_press)
        self.wrong_button.grid(column=0, row=2)
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_button_press)
        self.true_button.grid(column=1, row=2)
        # Text-Score
        self.score_label = Label(
            text="Score: 0",
            fg="White",
            bg=THEME_COLOR,
            font=("Arial", 10, "bold")
        )
        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        self.true_button.config(state="normal")
        self.wrong_button.config(state="normal")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.score_label.config(text="")
            self.canvas.itemconfig(self.text, text=f"You have reached the end of the quiz.\nYour final score: "
                                                   f"{self.quiz.score}")
            self.disable_buttons()

    def true_button_press(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)
        self.disable_buttons()

    def wrong_button_press(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)
        self.disable_buttons()

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(500, self.get_next_question)

    def disable_buttons(self):
        self.true_button.config(state="disabled")
        self.wrong_button.config(state="disabled")
