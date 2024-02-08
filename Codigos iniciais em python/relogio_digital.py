import tkinter as tk
import time

# cores

co0 = "#000000"  # preto
co1 = "#FFFFFF"  # branco
co2 = "#FF0000"  # vermelho
co3 = "#228B22"  # verde

# janela
janela = tk.Tk()
janela.title("Relógio Digital")
janela.geometry("200x50")
janela.resizable(False, False)
janela.configure(bg=co0)

# função do relógio
def relogio():
    tempo = time.strftime("%H:%M:%S")
    label.config(text=tempo, fg=co3, bg=co0)
    label.after(200, relogio)


# label

label = tk.Label(janela, font=("Arial", 30), bg=co0)
label.pack()
relogio()

janela.mainloop()
