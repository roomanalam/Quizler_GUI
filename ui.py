from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class Quizinterface():
    def __init__(self,quiz:QuizBrain):
        self.quiz = quiz
        self.timer=""
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_label =Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.Canvas = Canvas(width=300, height=250,bg="white")

        #self.Canvas.create_rectangle((300,250),fg="white")
        self.question_text =self.Canvas.create_text(150,120,width=280,text="hello there",font=("Arial",20,"italic"))
        self.Canvas.grid(column=0,row=1,columnspan=2,pady=50)

        image_true = PhotoImage(file="Day-34/quizler app/images/true.png")
        self.button_for_true = Button(image= image_true ,command=self.for_true)
        self.button_for_true.grid(column=0,row=2)

        image_false = PhotoImage(file="Day-34/quizler app/images/false.png")
        self.button_for_false =Button(image= image_false,command=self.for_false )
        self.button_for_false.grid(column=1,row=2)

        self.question_no_label =Label(text=f"Question No: {self.quiz.question_number+1}/{len(self.quiz.question_list)}",bg=THEME_COLOR,fg="white")
        self.question_no_label.grid(column=0,row=0)

        self.next_question()
        self.window.mainloop()  

    



    def for_true(self):
       
        is_right =self.quiz.check_answer("True")
        self.give_feedback(is_right)
       
        
    
    def for_false(self): 
        self.give_feedback(self.quiz.check_answer("False") )
      

    def give_feedback(self,is_right):
        self.button_for_true.config(state="disable")
        self.button_for_false.config(state="disable")
        if is_right:
            self.Canvas.config(bg="green")  
        else:
            self.Canvas.config(bg="red")
            #self.window.after_cancel(self.timer)
        self.timer= self.window.after(1000,self.next_question)    
    
    
    def next_question(self):
        self.button_for_true.config(state="active")
        self.button_for_false.config(state="active")   
        self.Canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.question_no_label.config(text=f"Question No: {self.quiz.question_number}/{len(self.quiz.question_list)}")
        if self.quiz.still_has_questions():
            
            q_text =self.quiz.next_question()
            self.Canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.Canvas.itemconfig(self.question_text,text="You've reached end of quiz") 
            self.button_for_true.config(state="disable")
            self.button_for_false.config(state="disable")   