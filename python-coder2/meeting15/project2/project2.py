# Simple Translator

from tkinter import Tk, messagebox, font, Label, Entry, Button

print('Simple English Translator')

root = Tk()
root.withdraw()

lang = {}

def read_from_file():
    with open('python-coder2\meeting15\project2\language.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            ind, eng = line.split('/')
            lang[ind] = eng
            
def write_to_file(ind, eng):
    with open('python-coder2\meeting14\project2\language.txt', 'a') as file:
        file.write('\n' + ind + '/' + eng)

read_from_file()

def custom_askstring(title, prompt, dialog_size="450x150", bg_color="lightblue", font_size=12, font_weight="bold"):
    dialog = Tk()
    dialog.title(title)
    dialog.configure(bg=bg_color)
    
    custom_font = font.Font(size=font_size, weight=font_weight)
    
    label = Label(dialog, text=prompt, bg=bg_color)
    label.configure(font=custom_font)
    label.pack()
    
    entry = Entry(dialog, font=custom_font)
    entry.pack()
    
    def ok():
        dialog.result = entry.get()
        dialog.destroy()

    button = Button(dialog, text="OK", command=ok, bg=bg_color, font=custom_font)
    button.pack()
    dialog.geometry(dialog_size) 
    dialog.eval('tk::PlaceWindow . center') 
    
    entry.focus_set()
    dialog.wait_window()
    
    try:
        return dialog.result
    except AttributeError:
        return ""

while True:
    query_input = custom_askstring('Indonesia', 'Type a word in Bahasa', dialog_size="450x150", bg_color="lightgreen", font_size=14, font_weight="bold")
    
    if query_input:
        query = query_input.capitalize()
        
        if query in lang:
            result = lang[query]
            messagebox.showinfo('Answer', 'In English, ' + query + ' is ' + result + '!')
    
        else:
            new_ind = custom_askstring('Teach me', 'I don\'t know! What is ' + query + ' in english ?', dialog_size="450x150", bg_color="lightblue", font_size=12, font_weight="bold")
            lang[query] = new_ind
            write_to_file(query, new_ind)
            
    else  :
        break