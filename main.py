import tkinter as tk
import pygame 
import os


def knealg():
    file = "asset/joyknealg.wav"
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file)
    sound.play()
def nghxng():
    file = "asset/nghxng.wav"
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file)
    sound.play()
def laugh():
    file = "asset/laugh.wav"
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file)
    sound.play()
    
root = tk.Tk()
root.geometry("720x720")
label = tk.Label(root, text="This is sound board", font=("AkiraExpanded-SuperBold", 30,))
label.pack()
button = tk.Button(root, text="knealg", command=knealg, font=("Arial", 15,))
button.place(y=100, x=360)
button = tk.Button(root, text="nghxng", command=nghxng, font=("Arial", 15,))
button.place(y=150, x=360)
button = tk.Button(root, text="laugh", command=laugh, font=("Arial", 15,))
button.place(y=200, x=360)


root.mainloop()