import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
import compoundwidgets as cw


root = tk.Tk()
root.style = Style(theme='darkly')
root.minsize(200, 100)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

full_list = ['John A', 'John B', 'John C', 'Paul A', 'Paul B', 'Paul C']

widget = cw.AutocompleteCombobox(root, values=full_list, width=30)
widget.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()
