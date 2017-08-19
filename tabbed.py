from tkinter import *
from tkinter import ttk

root = Tk()
notebook = ttk.Notebook(root)
notebook.pack()

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text='One')
notebook.add(frame2, text='Two')

ttk.Button(frame2, text='Click me').pack()
frame3 = ttk.Frame(notebook)

notebook.add(frame3, text='Three')


# disables the tab
# notebook.tab(0, state = 'disabled')


# entering and displaying multiple lines with the text widget

text = Text(frame1, width=40, height=10)
text.pack()


if __name__ == '__main__':
    mainloop()