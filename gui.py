import tkinter as tk
# tkinter makes gui 
root=tk.Tk()

root.title('My Title')
root.geometry('400x400')
# to set size of the screen
heading=tk.Label(text='Heading',font=('Arial',35),bg='red',fg='white')
heading.pack(pady=20)

heading1=tk.Label(text="Heading 1",font=('Arial',28),bg='#5A4FCF',fg='white',pady=10)
heading1.pack()
# pack--- row wise entry  grid--rows and columns acc  to excel and place-- x-y coordinates

# code betwwen these statements
root.mainloop()