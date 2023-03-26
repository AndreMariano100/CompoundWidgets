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
        print('Converted:', w.get_metric_value())


def reset_all_values():
    all_label_entry_units[0].set(0, '°C')
    all_label_entry_units[1].set(0, 'mm')
    all_label_entry_units[2].set(0, 'MPa')
    all_label_entry_units[3].set(0, 'MPa')
    all_label_entry_units[4].set(0, 'N')
    all_label_entry_units[5].set(0, 'N.m')
    all_label_entry_units[6].set(0, '-')

def convert_to_metric():
    global all_label_entry_units

    for widget in all_label_entry_units:
        widget.convert_to_metric()

def convert_to_imperial():
    global all_label_entry_units
    for widget in all_label_entry_units:
        widget.convert_to_imperial()


unit_options = ('temperature',
                'length',
                'pressure',
                'stress',
                'force',
                'moment',
                'none',
                'pressure')

unit_values = (25, 100, 10, 200, 50, 40, 200, 1)

all_label_entry_units = []
for i, item in enumerate(unit_options):
    if i == 7:
        w = cw.LabelEntryUnit(root, label_text=str(item).capitalize(), label_width=20, entry_value=unit_values[i],
                              entry_numeric=True, entry_width=10, entry_max_char=6,
                              combobox_unit=item, combobox_unit_width=6, combobox_unit_conversion=True)
        w.readonly()
    else:
        w = cw.LabelEntryUnit(root, label_text=str(item).capitalize(), label_width=20, entry_value=unit_values[i],
                              entry_numeric=True, entry_width=10, entry_max_char=6,
                              combobox_unit=item, combobox_unit_width=6)
    w.grid(row=i, column=0, sticky='nsew', pady=5, padx=10)
    all_label_entry_units.append(w)

    if i == 5:
        w.lock_unit()


print(all_label_entry_units)

button = ttk.Button(root, text='Read All Values', command=get_all_values)
button.grid(row=8, column=0, padx=10, pady=10, sticky='nsew')

button = ttk.Button(root, text='Reset All Values', command=reset_all_values)
button.grid(row=9, column=0, padx=10, pady=10, sticky='nsew')

button = ttk.Button(root, text='Convert to Metric', command=convert_to_metric)
button.grid(row=10, column=0, padx=10, pady=10, sticky='nsew')

button = ttk.Button(root, text='Convert to Imperial', command=convert_to_imperial)
button.grid(row=11, column=0, padx=10, pady=10, sticky='nsew')

root.mainloop()
