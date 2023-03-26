import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap import Style
import compoundwidgets as cw

root = tk.Tk()
root.style = Style(theme='darkly')
root.minsize(300, 200)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

full_list = ['John', 'Paul', 'Ringo', 'Jonathan', 'Neo', 'Robert']

# First frame, testing LedButtons
frame = ttk.LabelFrame(root, text='Autocomplete Entry and List')
frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
frame.columnconfigure(0, weight=1)

widget = cw.AutocompleteEntryList(frame, label_text='Auto Complete Test',
                                  label_anchor='w', list_method=None,
                                  list_height=10, full_list=full_list)
widget.grid(row=0, column=0, sticky='nsew', pady=(10, 0), padx=10)


root.mainloop()
