import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap import Style
import compoundwidgets as cw

root = tk.Tk()

def entry_method():
    print(f'entry method')
    all_values = []
    for w in label_entry_list:
        all_values.append(w.get())
    print(all_values)

def set_values():
    count = 0
    for w in label_entry_list:
        w.set(f'value {count}')
        count += 1

label_entry_list = []
for i in range(10):
    w = cw.LabelEntry(root, label_text=f'Label Entry {i+1}', label_width=15, entry_method=entry_method,
                      entry_numeric=False, entry_value='', entry_max_char=10, trace_variable=True)
    w.grid(row=i, column=0, sticky='nsew', pady=2)
    label_entry_list.append(w)

button = ttk.Button(root, text='Set Values', command=set_values)
button.grid(row=10, column=0, sticky='nsew', pady=2)

root.mainloop()
