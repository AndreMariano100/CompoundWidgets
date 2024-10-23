import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap import Style
import compoundwidgets as cw
import random

root = tk.Tk()
root.style = Style(theme='darkly')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


def b_1_method():
    for w in all_label_entry_button:
        w.enable()


def b_2_method():
    for w in all_label_entry_button:
        w.disable()
    root.update_idletasks()
    root.after(1000, all_label_entry_button[0].enable())


def b_3_method():
    for w in all_label_entry_button:
        w.readonly()
    root.update_idletasks()
    root.after(1000, all_label_entry_button[0].enable())

def b_4_method():
    for w in all_label_entry_button:
        print(w.get(), end='/')
    print()


def b_5_method():
    for w in all_label_entry_button:
        w.set(100)


def set_style():
    label_style_list = ('danger', 'warning', 'info', 'success',
                        'secondary', 'primary', 'light', 'dark', 'no style')
    new_styles = random.sample(label_style_list, len(all_label_entry_button))
    for i, w in enumerate(all_label_entry_button):
        w.set_style(new_styles[i])

def set_button_style():
    label_style_list = ('danger', 'warning', 'info', 'success',
                        'secondary', 'primary', 'light', 'dark', 'no style')
    new_styles = random.sample(label_style_list, len(all_label_entry_button))
    for i, w in enumerate(all_label_entry_button):
        w.set_button_style(new_styles[i])


frame = ttk.LabelFrame(root, text='Label Entry Button')
frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)
frame.columnconfigure(0, weight=1)

b_method_list = [b_1_method, b_2_method, b_3_method, b_4_method, b_5_method]
b_text = ['Enable ALL', 'Disable All', 'Readonly ALL', 'Get ALL', 'Set ALL']
all_label_entry_button = []
for i in range(5):
    if i > 1:
        sided=True
    else:
        sided = False
    w = cw.LabelEntryButton(frame, label_text=f'Label Entry Button {i+1}:', label_width=30, entry_value='0',
                            entry_width=12, entry_numeric=True, entry_max_char=10, button_text=b_text[i],
                            button_method=b_method_list[i], button_width=15, precision=0, sided=sided,
                            entry_method=b_4_method)
    w.grid(row=i, column=0, sticky='nsew', pady=5, padx=10)
    all_label_entry_button.append(w)

b = ttk.Button(frame, text='STYLE', command=set_style)
b.grid(row=6, column=0, pady=2, sticky='ew', padx=2)

b2 = ttk.Button(frame, text='STYLE BUTTON STYLE', command=set_button_style)
b2.grid(row=7, column=0, pady=2, sticky='ew', padx=2)

root.mainloop()
