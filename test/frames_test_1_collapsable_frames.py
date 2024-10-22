import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
import compoundwidgets as cw
import random


def test_method(event):
    print(event.widget.cget('text'))


def disable_all():
    global is_disabled

    if is_disabled:
        is_disabled = False
        for frame in frames_list:
            frame.enable()
    else:
        is_disabled = True
        for frame in frames_list:
            frame.disable()


def change_style():
    new_styles = random.sample(label_style_list, len(label_style_list))
    for i, frame in enumerate(frames_list):
        frame.set_style(new_styles[i])


global is_disabled


is_disabled = False
root = tk.Tk()
root.columnconfigure(0, weight=1)

root.geometry(f'600x650+200+50')
root.title('Vertically Collapsable Frame Test')
root.style = Style(theme='flatly')

label_style_list = ('danger', 'warning', 'info', 'success',
                    'secondary', 'primary', 'light', 'dark', 'no style')

frames_list = []
for i, style in enumerate(label_style_list):
    root.rowconfigure(i, weight=0)
    frame = cw.CollapsableFrame(root, title=style, expand_method=test_method, style=style)
    frame.grid(row=i, column=0, sticky='nsew', padx=10, pady=5)
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    label = ttk.Label(frame, text=f'This is the collapsable frame number {i+1}', padding=50, anchor='center')
    label.grid(row=0, column=0, sticky='nsew')
    frame.collapse_frame()
    frames_list.append(frame)

root.rowconfigure(19, weight=1)
b = ttk.Button(root, text='Disable/Enable ALL', command=disable_all)
b.grid(row=20, column=0, sticky='nsew')

b = ttk.Button(root, text='Change Styles', command=change_style)
b.grid(row=21, column=0, sticky='nsew', pady=5)

root.mainloop()
