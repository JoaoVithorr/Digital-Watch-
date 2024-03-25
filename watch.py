from tkinter import *
import tkinter
import pyglet
pyglet.font.add_file("fonts/digital-7.ttf")

# Cores
color1 = "#3d3d3d"  # black
color2 = "#fafcff"  # white
color3 = "#21c25c"  # green 
color4 = "#eb463b"  # red
color5 = "#dedcdc"  # gray
color6 = "#3080f0"  # blue

# Definindo cor de fundo e da fonte 
background_color = color1
font_color = color3

# Criando a janela
window = Tk()
window.title("")
window.geometry("440x100") # Definindo tamanho da janela 
window.resizable(width = FALSE, height = FALSE)
window.configure(background= background_color)

from datetime import datetime
# Obtendo a hora do dia e a data 
def watch():
    time = datetime.now()
    hour = time.strftime("%H:%M:%S")
    day_week = time.strftime("%A")
    day = time.day
    month = time.strftime("%b")
    year = time.strftime("%Y")

    l1.configure(text= hour) # Alterando o texto do label, fazendo-o mostrar a hora atual
    l1.after(200, watch) # Mantendo o tempo dinâmico

    l2.config(text=day_week + "   " + str(day) + "/" + str(month) + "/" + (year))

# Criando um label que mostra a hora
l1 = Label(window, text="10:05:05", font=('Arial  80'), bg=background_color, fg=font_color)
l1.grid(row=0, column=0, sticky=NW, padx=5)

# Criando outro label para a data
l2 = Label(window,  font=('Arial  20'), bg=background_color, fg=font_color)
l2.grid(row=1, column=0, sticky=NW, padx=5)

# Executando o relógio
watch() 
window.mainloop()