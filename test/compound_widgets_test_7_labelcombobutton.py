import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap import Style
import compoundwidgets as cw
import random

root = tk.Tk()
root.style = Style(theme='darkly')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


def b_6_method():
    for w in label_combo_list:
        w.enable()


def b_7_method():
    for i, w in enumerate(label_combo_list):
        w.disable()
    root.update_idletasks()
    root.after(1000, label_combo_list[0].enable())


def b_8_method():
    for w in label_combo_list:
        w.readonly()
    root.update_idletasks()
    root.after(1000, label_combo_list[0].enable())


def b_9_method():
    for w in label_combo_list:
        print(w.get(), end='/')
    print()


def b_10_method():
    for i, w in enumerate(label_combo_list):
        w.set(label_text[i])


def set_style():
    label_style_list = ('danger', 'warning', 'info', 'success',
                        'secondary', 'primary', 'light', 'dark', 'no style')
    new_styles = random.sample(label_style_list, len(label_combo_list))
    for i, w in enumerate(label_combo_list):
        w.set_style(new_styles[i])


def set_button_style():
    label_style_list = ('danger', 'warning', 'info', 'success',
                        'secondary', 'primary', 'light', 'dark', 'no style')
    new_styles = random.sample(label_style_list, len(label_combo_list))
    for i, w in enumerate(label_combo_list):
        w.set_button_style(new_styles[i])


frame = ttk.LabelFrame(root, text='Label Combo Button')
frame.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)
frame.columnconfigure(0, weight=1)
b_method_list = [b_6_method, b_7_method, b_8_method, b_9_method, b_10_method]
label_text = ('Label Combo 1', 'Label Combo 2', 'Label Combo 3', 'Label Combo 4', 'Label Combo 5')
b_text = ['Enable ALL', 'Disable All', 'Readonly ALL', 'Get ALL', 'Set ALL']
label_combo_list = []
for i, item in enumerate(label_text):
    if i > 1:
        sided=True
    else:
        sided = False
    w = cw.LabelComboButton(frame, label_text=f'{item}:', label_width=12,
                            combo_method=lambda e: print('Combobox Selected'), combo_value='',
                            combo_list=label_text, combo_width=15, button_text=b_text[i],
                            button_width=15, button_method=b_method_list[i], sided=sided)
    w.grid(row=i, column=0, sticky='nsew', pady=2)
    label_combo_list.append(w)


b = ttk.Button(frame, text='STYLE', command=set_style)
b.grid(row=6, column=0, pady=2, sticky='ew', padx=2)

b2 = ttk.Button(frame, text='STYLE BUTTON STYLE', command=set_button_style)
b2.grid(row=7, column=0, pady=2, sticky='ew', padx=2)

root.mainloop()
