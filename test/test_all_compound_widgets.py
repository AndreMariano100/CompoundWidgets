import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap import Style
import compoundwidgets as cw

root = tk.Tk()
root.style = Style(theme='darkly')
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# First frame, testing LedButtons
if True:
    root.columnconfigure(0, weight=1)
    frame = ttk.LabelFrame(root, text='Regular Buttons')
    frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

    frame.columnconfigure(0, weight=1)

    led_button_1 = cw.LedButton(frame, label_text='First Button', label_width=20,
                                label_method=lambda e: print('first led button'))
    led_button_1.grid(row=0, column=0, sticky='nsew', pady=(10, 0), padx=10)

    led_button_2 = cw.LedButton(frame, label_text='Second Button', label_width=10,
                                label_method=lambda e: print('second led button'))
    led_button_2.grid(row=1, column=0, sticky='nsew', pady=(10, 0), padx=10)

    led_button_3 = cw.LedButton(frame, label_text='Third Button', label_width=15,
                                label_method=lambda e: print('third led button'))
    led_button_3.grid(row=2, column=0, sticky='nsew', pady=10, padx=10)
    led_button_3.disable()

# Second frame, testing the CheckLedButton
if True:
    root.columnconfigure(1, weight=1)
    frame = ttk.LabelFrame(root, text='Check Buttons')
    frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

    frame.columnconfigure(0, weight=1)

    led_button_1 = cw.CheckLedButton(frame, label_text='First Button', label_width=20,
                                     label_method=lambda e: print('first led button'))
    led_button_1.grid(row=0, column=0, sticky='nsew', pady=(10, 0), padx=10)

    led_button_2 = cw.CheckLedButton(frame, label_text='Second Button', label_width=10,
                                     label_method=lambda e: print('second led button'))
    led_button_2.grid(row=1, column=0, sticky='nsew', pady=(10, 0), padx=10)

    led_button_3 = cw.CheckLedButton(frame, label_text='Third Button', label_width=15,
                                     label_method=lambda e: print('third led button'))
    led_button_3.grid(row=2, column=0, sticky='nsew', pady=10, padx=10)
    led_button_3.disable()

# Third frame, testing the RadioLedButton
if True:
    root.columnconfigure(2, weight=1)
    frame = ttk.LabelFrame(root, text='Radio Buttons', padding=10)
    frame.grid(row=0, column=2, sticky='nsew', padx=10, pady=10)

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    all_buttons = []
    for i in range(3):
        led_button = cw.RadioLedButton(frame, label_text=f'Button {i}', control_variable='first group',
                                       label_method=lambda e: print('first group'))
        led_button.grid(row=i, column=0, sticky='nsew', pady=(0, 10), padx=10)
        all_buttons.append(led_button)

    for i in range(3, 6):
        led_button = cw.RadioLedButton(frame, label_text=f'Button {i}', control_variable='second group',
                                       label_method=lambda e: print('second group'))
        led_button.grid(row=i-3, column=1, sticky='nsew', pady=(0, 10), padx=10)
        all_buttons.append(led_button)

    all_buttons[0].select()
    all_buttons[3].select()

# Fourth frame, testing LabelEntryUnits
if True:
    def get_all_values(event):
        for w in all_label_entry_units:
            print('Separate data:', w.get_entry(), w.get_unit(), end=' / ')
            print('Altogether:', w.get(), end=' / ')
            print('Converted:', w.get_metric_value())

    root.columnconfigure(3, weight=1)
    frame = ttk.LabelFrame(root, text='Label-Entry-Units')
    frame.grid(row=0, column=3, sticky='nsew', padx=10, pady=10)

    frame.columnconfigure(0, weight=1)
    unit_options = ('temperature', 'length', 'pressure', 'stress', 'force', 'moment', 'none')

    all_label_entry_units = []
    for i, item in enumerate(unit_options):
        w = cw.LabelEntryUnit(frame, label_text=str(item).capitalize(), label_width=20, entry_value='0',
                              entry_numeric=True, entry_width=10, entry_max_char=6, entry_method=get_all_values,
                              combobox_unit=item, combobox_unit_width=6)
        w.grid(row=i, column=0, sticky='nsew', pady=5, padx=10)
        all_label_entry_units.append(w)

    all_label_entry_units[-1].disable()
    all_label_entry_units[-2].readonly()

# Fifth frame, testing LabelCombo
if True:
    frame = ttk.LabelFrame(root, text='Label Combos')
    frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
    frame.columnconfigure(0, weight=1)
    local_list = ('Label Combo 1', 'Label Combo 2', 'Label Combo 3', 'Label Combo 4')
    for i, item in enumerate(local_list):
        w = cw.LabelCombo(frame, label_text=item, label_width=20, combo_list=local_list)
        w.grid(row=i, column=0, sticky='nsew', pady=2)

        if i == 2:
            w.set(w.combobox['values'][0])
            w.readonly()
        if i == 3:
            w.disable()

# Sixth frame, testing LabelEntry
if True:
    frame = ttk.LabelFrame(root, text='Label Entries')
    frame.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)
    frame.columnconfigure(0, weight=1)
    local_list = ('Label Entry 1', 'Label Entry 2', 'Label Entry 3', 'Label Entry 4')
    for i, item in enumerate(local_list):
        w = cw.LabelEntry(frame, label_text=item, label_width=20, entry_max_char=5)
        w.grid(row=i, column=0, sticky='nsew', pady=2)
        w.set(i * 100)

        if i == 3:
            w.disable()

# Seventh frame, testing LabelText
if True:
    frame = ttk.LabelFrame(root, text='Label Text')
    frame.grid(row=1, column=2, columnspan=2, sticky='nsew', padx=10, pady=10)
    frame.rowconfigure(0, weight=1)
    local_list = ('Label Text 1', 'Label Text 2')
    for i, item in enumerate(local_list):
        w = cw.LabelText(frame, label_text=item)
        w.grid(row=0, column=i, sticky='nsew')

root.mainloop()
