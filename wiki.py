import tkinter as tk
import wikipedia

def result():
    user_search=user_input.get()
    try:
        result=wikipedia.summary(user_search,sentences=3)
        result_label.config(text=result)
    except:
            result_label.config(text='No Data Found',font=('Harlow Solid Italic',25),pady=20)
root=tk.Tk()
root.title("WIKIPEDIA")
root.geometry("650x650")
root.resizable(0,0)
root.config(bg="#0174BE")
wikipedia.set_lang('hi')

tk.Label(text='WIKIPEDIA',font=('Broadway',30)).pack(pady=20)

tk.Label(text="Search Here...", font=('Berlin Sans FB',30),bg="#FFC436",fg="white").pack(pady=20)

user_input=tk.Entry(font=('Arial',20),width=25)
user_input.pack(pady=20)
btn=tk.Button(text="Search",font=('Forte',20),width=23,bg="#000000",fg="white",command=result)
btn.pack(pady=10)

result_label = tk.Label(text='',font=('Bahnschrift Light Condensed',15),bg='#0174BE',wraplength=700)
result_label.pack()

root.mainloop()