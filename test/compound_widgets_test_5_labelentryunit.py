import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap import Style
import compoundwidgets as cw
import random

root = tk.Tk()
root.style = Style(theme='darkly')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


def get_all_label_entry_values(event=None):
    print('/'.join([str(w.get()) for w in all_label_entry_units]))


def get_all_label_entry_metric():
    print('/'.join([str(w.get_metric_value()) for w in all_label_entry_units]))


def get_all_label_entry_imperial():
    print('/'.join([str(w.get_imperial_value()) for w in all_label_entry_units]))


def disable_all_label_entry():
    for w in all_label_entry_units:
        w.disable()


def enable_all_label_entry():
    for w in all_label_entry_units:
        w.enable()


def readonly_all_label_entry():
    for w in all_label_entry_units:
        w.readonly()


def fill_entry_values():
    for w in all_label_entry_units:
        w.set_entry(random.randint(-100, 400))
        range_2 = len(w.unit_combo.values) - 1
        w.set_unit(w.unit_combo.values[random.randint(0, range_2)])


def lock_entry_units():
    for w in all_label_entry_units:
        if w.is_locked:
            w.unlock_unit()
        else:
            w.lock_unit()


def convert_entry_to_metric():
    for w in all_label_entry_units:
        w.convert_to_metric()


def convert_entry_to_imperial():
    for w in all_label_entry_units:
        w.convert_to_imperial()


def enable_self_conversion():
    for w in all_label_entry_units:
        if not w.combobox_unit_conversion:
            w.activate_self_conversion()
        else:
            w.deactivate_self_conversion()


def set_style():
    label_style_list = ('danger', 'warning', 'info', 'success',
                        'secondary', 'primary', 'light', 'dark', 'no style',
                        'danger', 'warning', 'info', 'success',
                        'secondary', 'primary', 'light', 'dark', 'no style')
    new_styles = random.sample(label_style_list, len(all_label_entry_units))
    for i, w in enumerate(all_label_entry_units):
        w.set_style(new_styles[i])


frame = ttk.LabelFrame(root, text='Label Entry Units')
frame.grid(row=0, column=0, rowspan=2, sticky='nsew', padx=10, pady=10)
frame.columnconfigure(0, weight=1)

unit_options = ('none', 'temperature', 'temperature rate', 'length', 'area', 'pressure', 'stress',
                'force', 'moment', 'energy', 'toughness', 'j-integral', 'thermal expansion', 'time')

all_label_entry_units = []
for i, item in enumerate(unit_options):
    if i > 5:
        sided = True
    else:
        sided = False
    w = cw.LabelEntryUnit(frame, label_text=f'{str(item).capitalize()}:', label_width=10, entry_value='0',
                          entry_width=8, combobox_unit=item, combobox_unit_width=10, precision=i % 5,
                          entry_method=get_all_label_entry_values, sided=sided, trace_variable=True)
    w.grid(row=i, column=0, sticky='nsew', pady=5, padx=10)
    all_label_entry_units.append(w)

b1 = ttk.Button(frame, text='GET ALL', command=get_all_label_entry_values)
b1.grid(row=0, column=1, pady=2, sticky='ew', padx=2)

b2 = ttk.Button(frame, text='GET ALL METRIC', command=get_all_label_entry_metric)
b2.grid(row=1, column=1, pady=2, sticky='ew', padx=2)

b3 = ttk.Button(frame, text='GET ALL IMPERIAL', command=get_all_label_entry_imperial)
b3.grid(row=2, column=1, pady=2, sticky='ew', padx=2)

b4 = ttk.Button(frame, text='DISABLE ALL', command=disable_all_label_entry)
b4.grid(row=3, column=1, pady=2, sticky='ew', padx=2)

b5 = ttk.Button(frame, text='ENABLE ALL', command=enable_all_label_entry)
b5.grid(row=4, column=1, pady=2, sticky='ew', padx=2)

b6 = ttk.Button(frame, text='READONLY ALL', command=readonly_all_label_entry)
b6.grid(row=5, column=1, pady=2, sticky='ew', padx=2)

b7 = ttk.Button(frame, text='FILL RANDOM VALUES', command=fill_entry_values)
b7.grid(row=6, column=1, pady=2, sticky='ew', padx=2)

b8 = ttk.Button(frame, text='LOCK/UNLOCK UNITS', command=lock_entry_units)
b8.grid(row=7, column=1, pady=2, sticky='ew', padx=2)

b9 = ttk.Button(frame, text='CONVERT TO METRIC', command=convert_entry_to_metric)
b9.grid(row=8, column=1, pady=2, sticky='ew', padx=2)

b10 = ttk.Button(frame, text='CONVERT TO IMPERIAL', command=convert_entry_to_imperial)
b10.grid(row=9, column=1, pady=2, sticky='ew', padx=2)

b11 = ttk.Button(frame, text='ENABLE/DISABLE CONVERSION', command=enable_self_conversion)
b11.grid(row=10, column=1, pady=2, sticky='ew', padx=2)

b12 = ttk.Button(frame, text='SET STYLES', command=set_style)
b12.grid(row=11, column=1, pady=2, sticky='ew', padx=2)

root.mainloop()
