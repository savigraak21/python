import tkinter as tk
from googletrans import Translator
import pyttsx3
import  os
import gTTS


def lang_translator(lang):
    user_input=textarea.get(0.0,tk.END)
    translator=Translator()
    output=translator.translate(user_input,dest=lang)
    result.config(text=output.text)
def speak(self):
    if self.result.dest=='en':
        pyttsx3.speak(self.result.text)
    else:
        result.config(text="can't speak")



root=tk.Tk()

root.title('Google Translator')
root.geometry('900x900')
root.resizable(0,0)
root.config(bg='white')
tk.Label(text=('Google Translator'),font=('impact',50),fg='green',bg='white').grid(row=1,column=1,columnspan=3,pady=20)
textarea=tk.Text(font=('Arial',13),relief='solid',height=10,width=95)
textarea.grid(row=2,column=1,columnspan=3,padx=20,pady=10)
translate_btn=tk.Button(text='Translate',font=('Impact',20),relief='solid',width=20,bg='red',fg='white',command=lambda:lang_translator('en'))
hindi_btn=tk.Button(text='Hindi',font=('Impact',20),relief='solid',width=20,bg='green',fg='white',command=lambda:lang_translator('hi'))
english_btn=tk.Button(text='English',font=('Impact',20),relief='solid',width=20,bg='yellow',fg='black',command=lambda:lang_translator('english'))
translate_btn.grid(row=3,column=1)
hindi_btn.grid(row=3,column=2)
english_btn.grid(row=3,column=3)

speak_btn=tk.Button(text='Speak',font=('Impact',20),relief='solid',width=65,bg='#4285F4',fg='white')
speak_btn.grid(row=4,column=1,columnspan=3,pady=10)
tk.Label(text='Translation',font=('Impact',20),bg='white',fg='#3F4E4F').grid(row=5,column=1,columnspan=3,pady=10)
result=tk.Label(text='',font=('Arial',20),bg='white',fg='#3F4E4F')
result.grid(row=6,column=1,columnspan=3,pady=10)
root.mainloop()
