import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap import Style
import compoundwidgets as cw

root = tk.Tk()
root.style = Style(theme='darkly')
root.columnconfigure(0, weight=1)
root.title('Label-Entry-Units')


def get_all_values():
    for w in all_label_entry_units:
        print('Separate data:', w.get_entry(), w.get_unit(), end=' / ')
        print('Altogether:', w.get(), end=' / ')
        print('Converted to metric:', w.get_metric_value())


def reset_all_values():
    for widget in all_label_entry_units:
        widget.convert_to_metric()
        widget.set_entry(1)

def convert_to_metric():
    global all_label_entry_units

    for widget in all_label_entry_units:
        widget.convert_to_metric()

def convert_to_imperial():
    global all_label_entry_units
    for widget in all_label_entry_units:
        widget.convert_to_imperial()


unit_options = ('temperature',
                'area',
                'length',
                'pressure',
                'stress',
                'force',
                'moment',
                'none',
                'toughness',
                'energy',
                'j-integral')


all_label_entry_units = []
count = 0
for i, item in enumerate(unit_options):
    w = cw.LabelEntryUnit(root, label_text=str(item).capitalize(), label_width=20,
                          entry_value=1, entry_numeric=True, entry_width=10, entry_max_char=6,
                          combobox_unit=item, combobox_unit_width=8, combobox_unit_conversion=True)
    w.grid(row=count, column=0, sticky='nsew', padx=10, pady=5)
    w.readonly()
    all_label_entry_units.append(w)
    count += 1

button = ttk.Button(root, text='Read All Values', command=get_all_values)
button.grid(row=count, column=0, padx=10, pady=10, sticky='nsew')

button = ttk.Button(root, text='Reset All Values', command=reset_all_values)
button.grid(row=count+1, column=0, padx=10, pady=10, sticky='nsew')

button = ttk.Button(root, text='Convert to Metric', command=convert_to_metric)
button.grid(row=count+2, column=0, padx=10, pady=10, sticky='nsew')

button = ttk.Button(root, text='Convert to Imperial', command=convert_to_imperial)
button.grid(row=count+3, column=0, padx=10, pady=10, sticky='nsew')

root.mainloop()
