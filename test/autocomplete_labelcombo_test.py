import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
import compoundwidgets as cw


def retrieve_values(event):
    print(widget.get())
    print(widget_2.get())

    print(widget.get_combo_values())
    print(widget_2.get_combo_values())


root = tk.Tk()
root.style = Style(theme='darkly')
root.minsize(200, 100)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

full_list = ['John A', 'John B', 'John C', 'Paul A', 'Paul B', 'Paul C']

ttk.Label(root, text='Not case sensitive').grid(row=0, column=0, padx=10, pady=10)
widget = cw.AutocompleteLabelCombo(root, label_text='List of Names:',
                                   label_width=40, combo_width=20,
                                   combo_list=full_list, combo_method=retrieve_values)
widget.grid(row=1, column=0, padx=10, pady=10)

ttk.Label(root, text='Case sensitive').grid(row=2, column=0, padx=10, pady=10)
widget_2 = cw.AutocompleteLabelCombo(root, label_text='List of Names:',
                                     label_width=40, combo_width=20,
                                     combo_list=full_list, combo_method=retrieve_values,
                                     case_sensitive=True)
widget_2.grid(row=3, column=0, padx=10, pady=10)

root.mainloop()
