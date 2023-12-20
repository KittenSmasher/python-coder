# My Family Birthday Countdown

from tkinter import Tk, Canvas
from datetime import datetime

def get_events():
    list_member = []
    
    with open('python-coder2\meeting15\project1\listbday.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            fam_member = line.split(',')
            
            try:
                event_date = datetime.strptime(fam_member[1], '%d/%m/%Y').date()
                fam_member[1] = event_date
                list_member.append(fam_member)
            except ValueError as e:
                print(f"Error processing line: {line}. Error: {e}")
        return list_member

def days_between_dates(date1, date2):
    time_between = str(date1 - date2)
    number_of_days = time_between.split(' ')
    return number_of_days[0]

def update_clock():
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    current_date = now.strftime('%d/%m/%Y')
    c.itemconfig(clock_text, text=f"Date: {current_date}\nTime: {current_time}")
    root.after(1000, update_clock)
    
root = Tk()
c = Canvas(root, width=1000, height=500, bg='green')
c.pack()

c.create_text(100, 50, anchor='w', fill='orange', font='Arial 28 bold underline', text='My Countdown Calendar')

clock_text = c.create_text(750, 400, anchor='e', fill='white', font='Arial 18 bold')

events = get_events()
today = datetime.now().date()
vertical_space = 100

events.sort(key=lambda x: x[1])

for event in events:
    event_name = event[0]
    days_until = days_between_dates(event[1], today)
    display = f"It is {days_until} days until My {event_name}'s Birthday"
    
    if int(days_until) <= 7:
        text_col = 'red'
    else:
        text_col = 'lightblue'
  
    c.create_text(100, vertical_space, anchor='w', fill=text_col, font='Arial 28 bold', text=display)
    vertical_space += 30
    
update_clock() 
root.mainloop()