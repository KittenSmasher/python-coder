# Match Fruits Word

import random, time
from tkinter import Tk, Button, DISABLED, messagebox

root = Tk()
root.title('Matchmaker')
root.resizable(width=False, height=False)

buttons = {}
first = True

previousX = 0
previousY = 0
moves = 0
pairs = 0

button_symbols = {}

symbols = ['kiwi','kiwi', 'apple', 'apple', 'pear', 'pear', 'watermelon', 'watermelon', 'strawberry', 'strawberry', 'honeydew', 'honeydew', 'blueberry', 'blueberry', 'banana', 'banana', 'dragon fruit', 'dragon fruit', 'mango', 'mango', 'orange', 'orange', 'lemon', 'lemon', 'melon', 'melon', 'grape', 'grape', 'cherry', 'cherry']

def close_window():
    root.destroy()
    
def show_symbol(x, y):
    global first
    global previousX, previousY
    global moves
    global pairs
    
    buttons[x, y]['text'] = button_symbols[x, y]
    buttons[x, y].update_idletasks()
    
    if first:
        previousX = x
        previousY = y
        first = False
        moves = moves + 1
    elif previousX != x or previousY != y:
        if buttons[previousX, previousY]['text'] != buttons[x, y]['text']:
            time.sleep(0.5)
            buttons[previousX, previousY]['text'] = ''
            buttons[x, y]['text'] = ''
        else:
            buttons[previousX, previousY]['state'] = DISABLED
            buttons[x, y]['state'] = DISABLED
            pairs = pairs + 1
            
            if pairs == len(buttons)/2:
                messagebox.showinfo('Matching', 'Number of moves: ' + str(moves))
                close_window()
        
        first = True
    
random.shuffle(symbols)

for x in range(6):
    for y in range(5):
        button = Button(command=lambda x=x, y=y: show_symbol(x, y), width=12, height=3, font=('Arial', 20))
        button.grid(column=x, row=y)
        buttons[x, y] = button
        button_symbols[x, y] = symbols.pop()
   
root.mainloop()
