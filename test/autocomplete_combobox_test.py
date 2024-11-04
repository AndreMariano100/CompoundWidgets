import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
import compoundwidgets as cw


def change_style(event):
    style = style_combobox.get()
    widget_1.set_style(style)
    widget_2.set_style(style)


def disable_widgets():
    if widget_1.is_disabled:
        widget_1.enable()
        widget_2.enable()
    else:
        widget_1.disable()
        widget_2.disable()


def show_combobox_values(event):
    print(event.widget)
    print(widget_1.get())
    print(widget_2.get())


root = tk.Tk()
root.style = Style(theme='darkly')
root.minsize(200, 100)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

full_list = ['John A', 'John B', 'John C', 'Paul A', 'Paul B', 'Paul C']

ttk.Label(root, text='Not case sensitive').grid(row=0, column=0, padx=10, pady=10)
widget_1 = cw.AutocompleteCombobox(root, values=full_list, width=30, combobox_method=show_combobox_values)
widget_1.grid(row=1, column=0, padx=10, pady=10)

ttk.Label(root, text='Case sensitive').grid(row=2, column=0, padx=10, pady=10)
widget_2 = cw.AutocompleteCombobox(root, values=full_list, width=30, case_sensitive=True,
                                   combobox_method=show_combobox_values)
widget_2.grid(row=3, column=0, padx=10, pady=10)

disable_button = ttk.Button(root, text='Disable/Enable', command=disable_widgets)
disable_button.grid(row=4, column=0, padx=10, pady=10)

style_combobox = ttk.Combobox(root, values=['danger', 'warning', 'info', 'success', 'secondary',
                                            'primary', 'light', 'dark'])
style_combobox.grid(row=5, column=0, padx=10, pady=10)
style_combobox.bind('<<ComboboxSelected>>', change_style)

root.mainloop()
