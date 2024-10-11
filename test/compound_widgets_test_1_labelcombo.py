import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap import Style
import compoundwidgets as cw

root = tk.Tk()
root.style = Style(theme='darkly')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

def get_all_label_combos(event=None):
    for w in label_combo_list:
        print(w.get())

def set_all_label_combos():
    for w in label_combo_list:
        w.set('none')

def set_all_label_combos_2():
    for w in label_combo_list:
        w.set('Label Combo 2')

def set_disable_combos():
    for w in label_combo_list:
        w.disable()

def set_read_only_combos():
    for w in label_combo_list:
        w.set(local_list[0])
        w.readonly()

def set_normal_combos():
    for w in label_combo_list:
        w.enable()

frame = ttk.LabelFrame(root, text='Label Combos')
frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
frame.columnconfigure(0, weight=1)
local_list = ('Label Combo 1', 'Label Combo 2', 'Label\nCombo 3', 'Label Combo 4')
label_combo_list = []
for i, item in enumerate(local_list):
    if i:
        sided=True
    else:
        sided=False
    w = cw.LabelCombo(frame, label_text=item, label_width=10, combo_list=local_list,
                      sided=sided, label_anchor='w', label_justify='left', combo_method=get_all_label_combos)
    w.grid(row=i, column=0, sticky='nsew', pady=2)
    label_combo_list.append(w)
    if i == 2:
        w.readonly()
    if i == 3:
        w.set_label_text('')
        w.disable()

b1 = ttk.Button(frame, text='GET ALL', command=get_all_label_combos)
b1.grid(row=4, column=0, pady=2, sticky='ew', padx=2)

b2 = ttk.Button(frame, text='SET ALL WRONG', command=set_all_label_combos)
b2.grid(row=5, column=0, pady=2, sticky='ew', padx=2)

b3 = ttk.Button(frame, text='SET ALL RIGHT', command=set_all_label_combos_2)
b3.grid(row=6, column=0, pady=2, sticky='ew', padx=2)

b4 = ttk.Button(frame, text='READ ONLY', command=set_read_only_combos)
b4.grid(row=7, column=0, pady=2, sticky='ew', padx=2)

b5 = ttk.Button(frame, text='DISABLE', command=set_disable_combos)
b5.grid(row=8, column=0, pady=2, sticky='ew', padx=2)

b6 = ttk.Button(frame, text='NORMAL', command=set_normal_combos)
b6.grid(row=9, column=0, pady=2, sticky='ew', padx=2)

root.mainloop()
