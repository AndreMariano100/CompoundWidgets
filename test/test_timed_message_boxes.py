import os
import tkinter.ttk as ttk
import tkinter as tk
import compoundwidgets as cw
from ttkbootstrap import Style


# Methods for testing the message boxes
def show_danger_box():
    cw.TimedBox(root, message='This is a timed box: 3 seconds', time=3, style='danger').show()

def show_warning_box():
    cw.TimedBox(root, message='This is a timed box: 2 seconds', time=2, style='warning').show()

def show_info_box():
    cw.TimedBox(root, message='This is a timed box: 1 seconds', time=1, style='info').show()


def show_generic_box():
    cw.TimedBox(root, message='This is a generic timed box with a kind of a long text to see if it fits').show()


# Root
root = tk.Tk()
root.title('Timed Message Box Testing')
image_path = os.getcwd().replace('test', 'compoundwidgets\IMAGES')
icon_path = os.path.join(image_path, 'engineering.ico')
root.iconbitmap(icon_path)
root.style = Style(theme='flatly')
root.geometry(f'400x300+200+50')
root.columnconfigure(0, weight=1)
for i in range(4):
    root.rowconfigure(i, weight=1)

button = ttk.Button(root, text='Danger Timed Box', command=show_danger_box)
button.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

button = ttk.Button(root, text='Warning Timed Box', command=show_warning_box)
button.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

button = ttk.Button(root, text='Info Timed Box', command=show_info_box)
button.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)

button = ttk.Button(root, text='Undefined Timed Box', command=show_generic_box)
button.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)

root.mainloop()
