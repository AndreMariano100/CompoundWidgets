import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
import compoundwidgets as cw


def method_1(event=None):
    print(widget_1.get())


def method_2(event=None):
    print(widget_2.get())


def set_new_list():
    new_list = ('Value 1', 'Value 2', 'Value 3', 'Value 4', 'Value 5', 'Value 6',)
    widget_1.set_list(new_list)
    widget_2.set_list(new_list)


def set_entry_value():
    widget_1.set_entry('Value 1')
    widget_2.set_entry('Value Z')


def get_entry_value():
    print(f'Widget 1: {widget_1.get()}')
    print(f'Widget 2: {widget_2.get()}')


def alternate_style():
    if str(widget_1.lb.cget('state')) == 'disabled':
        widget_1.enable()
    else:
        widget_1.disable()

    if str(widget_2.lb.cget('state')) == 'disabled':
        widget_2.enable()
    else:
        widget_2.disable()

def edit_message():
    print('entry i has been edited')

root = tk.Tk()
root.style = Style(theme='darkly')
root.minsize(300, 200)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

full_list = ['John', 'Paul', 'Ringo', 'Jonathan', 'Neo', 'Robert']

# First frame, enabled
frame = ttk.LabelFrame(root, text='Autocomplete Entry and List 1')
frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
frame.columnconfigure(0, weight=1)

widget_1 = cw.AutocompleteEntryList(frame, label_text='Auto Complete Test',
                                    label_anchor='w', list_method=method_1,
                                    list_height=10, list_values=full_list,
                                    entry_change_method=edit_message)
widget_1.grid(row=0, column=0, sticky='nsew', pady=(10, 0), padx=10)

# Second frame, disabled
frame = ttk.LabelFrame(root, text='Autocomplete Entry and List 2')
frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)
frame.columnconfigure(0, weight=1)

widget_2 = cw.AutocompleteEntryList(frame, label_text='Auto Complete Test',
                                    label_anchor='w', list_method=method_2,
                                    list_height=10, list_values=full_list)
widget_2.grid(row=0, column=0, sticky='nsew', pady=(10, 0), padx=10)
widget_2.disable()

# third frame, action buttons
frame = ttk.Frame(root)
frame.rowconfigure(0, weight=1)
frame.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)

button_1 = ttk.Button(frame, text='Set New List', command=set_new_list)
button_1.grid(row=0, column=0)

button_2 = ttk.Button(frame, text='Set Entry', command=set_entry_value)
button_2.grid(row=0, column=1, padx=(5, 0))

button_3 = ttk.Button(frame, text='Get Entry', command=get_entry_value)
button_3.grid(row=0, column=2, padx=(5, 0))

button_4 = ttk.Button(frame, text='Alternate Enable/Disable', command=alternate_style)
button_4.grid(row=0, column=3, padx=(5, 0))


root.mainloop()
