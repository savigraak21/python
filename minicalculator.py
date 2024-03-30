import tkinter as tk

root=tk.Tk()

def cal_sum():
    num1=eval(Number1_input.get())
    num2=eval(Number2_input.get())
    output=num1+num2
    result.config(text=f'The Sum is :{output}')
def cal_diff():
    num1=eval(Number1_input.get())
    num2=eval(Number2_input.get())
    output1=num1-num2
    result.config(text=f'The Difference is :{output1}')
def cal_mul():
    num1=eval(Number1_input.get())
    num2=eval(Number2_input.get())
    output2=num1*num2
    result.config(text=f'The Product is :{output2}')
def cal_div():
    num1=eval(Number1_input.get())
    num2=eval(Number2_input.get())
    output3=num1/num2
    result.config(text=f'The Remainder is :{output3}')

def cal_powerof():
    num1=eval(Number1_input.get())
    num2=eval(Number2_input.get())
    output4=num1**num2
    result.config(text=f'The Remainder is :{output4}')
root.title('Calculator')
root.geometry('800x800')
root.resizable(0,0)

root.config(bg="#FF915A")
heading=tk.Label(text='CALCULATOR',font=('Broadway',35),bg='white',fg='Black')
heading.pack(pady=20)

image=tk.PhotoImage(file="")

Number_1=tk.Label(text="Enter Number 1:",font=('Copperplate Gothic Bold',20))
Number_1.pack(pady=10)

Number1_input=tk.Entry(font=('Arial',20),relief='solid')
Number1_input.pack(pady=20)

Number_2=tk.Label(text="Enter Number 2:",font=('Copperplate Gothic Bold',20))
Number_2.pack(pady=10)

Number2_input=tk.Entry(font=('Arial',20),relief='solid')
Number2_input.pack(pady=20)

btn=tk.Button(text="Sum",font=('Arial',20,'bold'),bg='#F5DD61', fg='black',width=10,relief='solid',command=cal_sum)
btn.pack(pady=5)

btn=tk.Button(text="Subtract",font=('Arial',20,'bold'),bg='#F5DD61', fg='black',width=10,relief='solid',command=cal_diff)
btn.pack(pady=5)

btn=tk.Button(text="Multiply",font=('Arial',20,'bold'),bg='#F5DD61', fg='black',width=10,relief='solid',command=cal_mul)
btn.pack(pady=5)

btn=tk.Button(text="Divide",font=('Arial',20,'bold'),bg='#F5DD61', fg='black',width=10,relief='solid',command=cal_div)
btn.pack(pady=5)

btn=tk.Button(text="Power Of",font=('Arial',20,'bold'),bg='#F5DD61', fg='black',width=10,relief='solid',command=cal_powerof)
btn.pack(pady=5)

result=tk.Label(text='',font=('Comic Sans MS',30))
result.pack(pady=20)
# command  =hello calls the function in the button
root.mainloop()