import tkinter as tk

root=tk.Tk()
root.title('BLOG')
root.geometry('500x500')
heading=tk.Label(text='MY BLOG',font=('Arial',40),fg='white' ,bg='purple')
heading.pack(pady=20)

paragraph=tk.Label(text='Paragraph',font=('Comic Sans MS',20),bg='skyblue')
paragraph.pack(pady=10)
paragraph_content=tk.Label(text=" Lorem Ipsum is simply dummy text of the printing and typesetting industry", font=('Aptos',10))
paragraph_content.pack(pady=10)

paragraph_content1=tk.Label(text=" Lorem Ipsum is simply dummy text of the printing and typesetting industry", font=('Aptos',10))
paragraph_content1.pack(pady=10)

paragraph1=tk.Label(text='Paragraph',font=('Comic Sans MS',20),bg='skyblue')
paragraph1.pack(pady=10)
paragraph1_content=tk.Label(text=" Lorem Ipsum is simply dummy text of the printing and typesetting industry", font=('Aptos',10))
paragraph1_content.pack(pady=10)

paragraph1_content1=tk.Label(text=" Lorem Ipsum is simply dummy text of the printing and typesetting industry", font=('Aptos',10))
paragraph1_content1.pack(pady=10)

Thank_you=tk.Label(text='Thanks for reading',font=('Freestyle Script',20),fg='white',bg='red')
Thank_you.pack()

root.mainloop()