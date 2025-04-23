import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap import Style
import compoundwidgets as cw
import random

root = tk.Tk()
root.style = Style(theme='darkly')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


def get_all_label_spin(event=None):
    for w in label_spin_list:
        print(w.get(), end=' / ')
    print()


def set_all_label_spin():
    for i, w in enumerate(label_spin_list):
        w.set(local_spin_list[i][1])


def set_all_label_spin_wrong():
    for w in label_spin_list:
        w.set(-100)


def set_disable_spin():
    for w in label_spin_list:
        w.disable()


def set_read_only_spin():
    for w in label_spin_list:
        w.readonly()


def set_normal_spin():
    for w in label_spin_list:
        w.enable()


def set_style():
    label_style_list = ('danger', 'warning', 'info', 'success',
                        'secondary', 'primary', 'light', 'dark', 'no style')
    new_styles = random.sample(label_style_list, len(label_spin_list))
    for i, w in enumerate(label_spin_list):
        w.set_style(new_styles[i])


frame = ttk.LabelFrame(root, text='Label Spinbox')
frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
frame.columnconfigure(0, weight=1)

local_spin_list = (
    ('Spin 1 - int 0~10', 5, 'int', 0, 10, 1, 0),
    ('Spin 2 - int -10~10', None, 'int', -10, 10, 2, 0),
    ('Spin 3 - float 0~10', 5, 'float', 0, 10, 0.02, 2),
    ('Spin 4 - float -10~10', 0, 'float', -10, 10, 0.5, 1),
    ('Spin 5 - float 0 - 2', 0, 'float', 0, 2, 0.1, 2),
)
label_spin_list = []
for i, item in enumerate(local_spin_list):
    w = cw.LabelSpinbox(frame, label_text=item[0], label_width=20,
                        entry_value=item[1], entry_width=10, entry_method=get_all_label_spin,
                        entry_type=item[2], spin_start=item[3], spin_end=item[4],
                        spin_increment=item[5], spin_precision=item[6], trace_variable=True)
    w.grid(row=i, column=0, sticky='nsew', pady=2, padx=2)
    label_spin_list.append(w)

b1 = ttk.Button(frame, text='GET ALL', command=get_all_label_spin)
b1.grid(row=5, column=0, pady=2, sticky='ew', padx=2)

b3 = ttk.Button(frame, text='SET ALL RIGHT', command=set_all_label_spin)
b3.grid(row=6, column=0, pady=2, sticky='ew', padx=2)

b3 = ttk.Button(frame, text='SET ALL WRONG', command=set_all_label_spin_wrong)
b3.grid(row=7, column=0, pady=2, sticky='ew', padx=2)

b4 = ttk.Button(frame, text='READ ONLY', command=set_read_only_spin)
b4.grid(row=8, column=0, pady=2, sticky='ew', padx=2)

b5 = ttk.Button(frame, text='DISABLE', command=set_disable_spin)
b5.grid(row=9, column=0, pady=2, sticky='ew', padx=2)

b6 = ttk.Button(frame, text='NORMAL', command=set_normal_spin)
b6.grid(row=10, column=0, pady=2, sticky='ew', padx=2)

b7 = ttk.Button(frame, text='STYLE', command=set_style)
b7.grid(row=11, column=0, pady=2, sticky='ew', padx=2)

root.mainloop()
