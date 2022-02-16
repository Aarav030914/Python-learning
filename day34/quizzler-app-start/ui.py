from tkinter import Button, Label, PhotoImage, Tk, Canvas
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain


class QuizInterface:
    
    def __init__(self, quiz: QuizBrain):
        self.score = 0
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Fun Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        
        self.canvas = Canvas(height=250, width=300)
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.canv_text = self.canvas.create_text(
            150, 
            125,
            width=280, 
            text=f"Some sort of text", 
            font=("Arial", 20, "bold"),
            )
        self.score_lable = Label(text=f"SCORE: {self.score}", bg=THEME_COLOR, fg= "#ffffff", padx=20, pady=20)
        self.score_lable.grid(column=1, row=0)
        def user_ans_right(): 
               
            if self.quiz.check_answer("True"):
                self.score += 1
                self.score_lable.config(text=f"SCORE: {self.score}")
            self.get_next_question()
        
        def user_ans_wrong():
                     
            if self.quiz.check_answer("False"):
                
                self.score += 1
                
                self.score_lable.config(text=f"SCORE: {self.score}")
            self.get_next_question()
        
        

        right_img = PhotoImage(file="./day34/quizzler-app-start/images/true.png")
        wrong_img = PhotoImage(file="./day34/quizzler-app-start/images/false.png")
        
        self.right_button = Button(image=right_img, highlightthickness=0, bg=THEME_COLOR, command=user_ans_right)
        self.right_button.grid(column=0, row=2, padx=20, pady=20)
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, bg=THEME_COLOR, command=user_ans_wrong)
        self.wrong_button.grid(column=1, row=2, padx=20, pady=20)
        
        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        self.quiz.next_question()
        q_text = self.quiz.current_question.text
        q_number = self.quiz.question_number
        self.canvas.itemconfig(self.canv_text, text=f"Q.{q_number}: {q_text}")
    
    
       

