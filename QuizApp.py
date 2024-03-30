import tkinter as tk


Questions=[
    ('What is the capital of Hungary','Budapest'),
    ('What is the capital of Chile','Santiago'),
    ('What is the capital of Afghanistan','Kabul'),
    ('What is the capital of Taiwan','Taipei'),
    ('What is the capital of North Korea','Pyangyong'),
    ('What is the capital of Myanmar','NayPyiTaw'),
    ('What is the capital of Australia','Canberra'),
    ('What is the capital of New Zealand','Wellington'),
    ('What is the capital of Zimbabwe','Harare'),
    ('What is the capital of Libya','Tripoli')
]

score=0
current_question=0

def show_next_question():
    global current_question
    input.delete(0.0,tk.END)
    if current_question<len(Questions):
        question.config(text=Questions[current_question][0])
        current_question+=1
    else:
        next_question.pack_forget()
        question.pack_forget()
        input.pack_forget()

        show_score.config(text=f'Quiz Completed!! \n Your Total Score  is : {score}/10')
def check_answer():
    global score
    userans=input.get(0.0,tk.END)
    correct_ans=Questions[current_question-1][1]

    if userans.lower().strip() == correct_ans.lower():
        score=score+1
        show_score.config(text=f'Your current score is {score}')

    show_next_question()

root=tk.Tk()
root.config(bg='#87C4FF')
root.geometry('600x600')
root.resizable(0,0)
root.title("Let's check your Knowledge")

heading=tk.Label(text="QUIZ TIME" ,font=('Copperplate Gothic Bold',40),bg='#F4D160',fg='white',relief='raised')
heading.pack(pady=20)

question=tk.Label(text="",font=('Copperplate Gothic Bold',20), fg='white', bg='#FF4B91' ,relief='solid')
question.pack(pady=20)

input=tk.Text(height=5,width=30,font=('Arial',20),relief='solid')
input.pack(pady=20)

next_question=tk.Button(text='Next',font=('Copperplate Gothic Bold',30),bg='#FF4B91',fg='white' ,command=check_answer)
next_question.pack(pady=20)

show_score = tk.Label(text="your current score is 0",font=('Copperplate Gothic Bold',20),fg='WHITE',bg='green')
show_score.pack(pady=20)

show_next_question()

root.mainloop()

