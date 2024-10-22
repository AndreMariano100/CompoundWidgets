import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
import compoundwidgets as cw
import random


def change_style():
    label_style_list = ('danger', 'warning', 'info', 'success',
                        'secondary', 'primary', 'light', 'dark', 'no style')
    new_style = random.choice(label_style_list)
    frame.set_style(new_style)


root = tk.Tk()
root.columnconfigure(0, weight=1)

root.geometry(f'600x300+200+50')
root.title('Scrollable frame test')
root.style = Style(theme='flatly')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create frame instance
frame = cw.ScrollableFrame(root)
frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

# To add widgets to the frame, they shall be children of its 'widgets_frame' as follows
frame.columnconfigure(0, weight=0)
for i in range(10):
    label = ttk.Label(frame, text=f'This is label {i+1}', style='secondary.Inverse.TLabel',
                      width=120)
    label.grid(row=i, column=0, sticky='nsew', pady=5, padx=20)

# the scrollable frame does not behave appropriately if you use two of them on the same container

b = ttk.Button(root, text='Change Styles', command=change_style)
b.grid(row=15, column=0, sticky='nsew', pady=5)
root.mainloop()
