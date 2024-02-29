import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap import Style
import compoundwidgets as cw

root = tk.Tk()
root.style = Style(theme='darkly')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


def get_all_label_entries(event=None):
    print('/'.join([w.get() for w in label_entry_list]))

def set_all_label_entries():
    for w in label_entry_list:
        w.set('none')

def set_disable_entries():
    for w in label_entry_list:
        w.disable()

def set_read_only_entries():
    for w in label_entry_list:
        w.readonly()

def set_normal_entries():
    for w in label_entry_list:
        w.enable()

def set_empty_entries():
    for w in label_entry_list:
        w.set('')

frame = ttk.LabelFrame(root, text='Label Entries')
frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)
frame.columnconfigure(0, weight=1)

local_list = ('1000', '2000.00', 'Label Entry', 'Label Entry', 'Very Long Label Entry')
label_entry_list = []
for i, item in enumerate(local_list):
    if i in range(3):
        w = cw.LabelEntry(frame, label_text=f'Label Entry {i+1}', label_width=10,
                          entry_method=get_all_label_entries,
                          entry_numeric=True, entry_value=item, entry_max_char=10, trace_variable=True,
                          precision=0)
    else:
        w = cw.LabelEntry(frame, label_text=f'Label Entry {i+1}', label_width=10,
                          entry_method=get_all_label_entries,
                          entry_numeric=False, entry_value=item, entry_max_char=10, trace_variable=True,
                          precision=3)
    w.grid(row=i, column=0, sticky='nsew', pady=2)
    label_entry_list.append(w)
    if i == 2:
        w.readonly()
    if i == 3:
        w.disable()

b1 = ttk.Button(frame, text='GET ALL', command=get_all_label_entries)
b1.grid(row=5, column=0, pady=2, sticky='ew', padx=2)

b3 = ttk.Button(frame, text='SET ALL', command=set_all_label_entries)
b3.grid(row=6, column=0, pady=2, sticky='ew', padx=2)

b4 = ttk.Button(frame, text='READ ONLY', command=set_read_only_entries)
b4.grid(row=7, column=0, pady=2, sticky='ew', padx=2)

b5 = ttk.Button(frame, text='DISABLE', command=set_disable_entries)
b5.grid(row=8, column=0, pady=2, sticky='ew', padx=2)

b6 = ttk.Button(frame, text='NORMAL', command=set_normal_entries)
b6.grid(row=9, column=0, pady=2, sticky='ew', padx=2)

b7 = ttk.Button(frame, text='SET EMPTY', command=set_empty_entries)
b7.grid(row=10, column=0, pady=2, sticky='ew', padx=2)

root.mainloop()
