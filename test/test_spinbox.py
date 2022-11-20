import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap import Style
import compoundwidgets as cw


def show_values(event):
    print(event)


root = tk.Tk()
root.style = Style(theme='darkly')
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)

frame = ttk.LabelFrame(root, text='Spinbox')
frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

frame.columnconfigure(0, weight=1)

spin_1 = cw.LabelSpinbox(frame, label_text='First Spin Integer', label_width=20, entry_width=10,
                         entry_method=show_values, spin_start=0, spin_end=10, spin_increment=1)
spin_1.grid(row=0, column=0, sticky='nsew', pady=(10, 0), padx=10)

spin_2 = cw.LabelSpinbox(frame, label_text='Second Spin Float', label_width=20, entry_width=10,
                         entry_method=show_values, spin_start=0, spin_end=1, spin_increment=0.1, spin_precision=3)
spin_2.grid(row=1, column=0, sticky='nsew', pady=(10, 0), padx=10)

spin_3 = cw.LabelSpinbox(frame, label_text='Third Spin Integer', label_width=20, entry_width=10,
                         entry_method=show_values, spin_start=0, spin_end=10, spin_increment=1, entry_type='int')
spin_3.grid(row=2, column=0, sticky='nsew', pady=(10, 0), padx=10)

root.mainloop()
