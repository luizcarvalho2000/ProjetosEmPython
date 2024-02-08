import tkinter as tk
from tkinter import Label, Button, messagebox
import random


def não():
    messagebox.showinfo('Eu ja sabia, obrigado!')
    quit()


def motionMouse(event):
    btnSim.place(x=random.randint(0, 500), y=random.randint(0, 500))


def toggle():
    global counter
    counter += 1
    messagebox.showinfo('Obrigado', 'Eu ja sabia')


# cria a janela principal do programa

root = tk.Tk()
root.geometry('600x600')
root.title('survey')
root.resizable(width=False, height=False)
root['bg'] = 'white'

# cria os widgets

label = Label(root, text='Me faz um Pix?', font='Arial 20 bold', bg='white')
label.pack()
btnSim = Button(root, text='Não', font='Arial 16', bg='red', fg='white')
btnSim.pack()
btnSim.bind('Enter', motionMouse)

btnNao = Button(root, text='Sim', font='Arial 16', bg='green', command=toggle)
btnNao.place(x=350, y=100)
root.bind('<Motion>', motionMouse)

counter = 0
root.mainloop()
