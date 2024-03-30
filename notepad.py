import tkinter as tk
from tkinter import filedialog

class note():
    def __init__(self,root):
        self.root=root
        self.file_path=None
        root.title('Notepad')
        root.geometry('1150x1150')
        root.resizable(0,0)
        root.config(bg='#EEC759')

        tk.Label(text='NOTEPAD',font=('Segoe UI Black',25)).grid(row=1,column=1,columnspan=5,pady=20)

        open_btn=tk.Button(text='Open',font=('forte',25),relief='solid',width=8,bg='#D9EDBF',fg='black',command=self.open_file)
        save_btn=tk.Button(text='Save',font=('forte',25),relief='solid',width=8,bg='#FFB996',fg='black')
        saveas_btn=tk.Button(text='Save As',font=('forte',25),relief='solid',width=8,bg='#FFCF81',fg='black',command=self.save_as)
        clear_btn=tk.Button(text='Clear',font=('forte',25),relief='solid',width=8,bg='#FDFFAB',fg='black',command=self.clear)
        help_btn=tk.Button(text='Help',font=('forte',25),relief='solid',width=8,bg='#7BD3EA',fg='black',command=self.help)
        open_btn.grid(row=2,column=1,pady=3,padx=8)
        save_btn.grid(row=2,column=2,pady=3,padx=8)
        saveas_btn.grid(row=2,column=3,pady=3,padx=8)
        clear_btn.grid(row=2,column=4,pady=3,padx=8)
        help_btn.grid(row=2,column=5,pady=3,padx=8)

        self.textarea=tk.Text(font=('Berlin Sans FB',20), relief='solid', width=70,height=19)
        self.textarea.grid(row=3,column=1,columnspan=5,padx=10,pady=10)

    def open_file(self):
        self.file_path=filedialog.askopenfilename()
        with open(self.file_path,'r') as text_files:
            text=text_files.read()
        self.clear()
        self.textarea.insert(0.0,text)
        self.root.title(f'Notepad : {self.file_path}')

    def save(self):
        if self.file_path:
            text=self.textarea.get(0.0,tk.END)
            with open (self.file_path,'w') as text_file:
                text_file.write(text)
            pass
        else:
            self.save_as()
    def save_as(self):
        text=self.textarea.get(0.0,tk.END)
        extenstions=[('Text File','*.txt'),('python file','*.py'),('csv','*.csv'),('All types','*.*')]
        save_file=filedialog.asksaveasfile(defaultextension=".txt",filetypes=extenstions)
        with open(save_file,'w') as text_file:
            text_file.write(text)
    def clear(self):
        self.textarea.delete(0.0,tk.END)
    def help(self):
        self.clear()
        help_text='''Notepad is a basic text editor that is included with Windows. It is a simple program that can be used to create and 
        edit text files. Notepad is not a word processor, so it does not have many of the features that are found in word 
        processors, such as the ability to create and edit tables, images, or charts. However, Notepad is a great tool for 
        creating simple text files, such as program code, scripts, or notes.
        Open-- use to open file 
        Save- saves a file
        Save as- save file with the name you like
        Clear -- clears the text / content'''
        self.textarea.insert(0.0,help_text)

root=tk.Tk()
notepad=note(root)
root.mainloop()