from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config()
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        # Canvas
        self.canvas = Canvas(highlightthickness=0, height=250, width=300)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(150, 125, text="Test", font=('arial', 20, 'italic'),
                                                     fill=THEME_COLOR, width=280)
        # Buttons
        false_image = PhotoImage(file='images/false.png')
        true_image = PhotoImage(file='images/true.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)
        # Score Label
        self.score = Label(text=f'Score: {self.quiz.score}', fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1, pady=20, padx=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score.config(text=f'Score: {self.quiz.score}')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have finished the quiz.')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
    def true_pressed(self):
        is_right = self.quiz.check_answer('true')
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('false')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        elif not is_right:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
