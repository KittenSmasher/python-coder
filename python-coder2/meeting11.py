# TKinter project (Canvas)

from tkinter import Tk, Canvas

root = Tk()
root.title("Empty Canvas")

# canvas = Canvas(root, width=400, height=300, bg="white")
canvas = Canvas(root, width=600, height=1200, bg="white")
canvas.pack()

root.mainloop()