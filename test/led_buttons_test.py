import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap import Style
import compoundwidgets as cw

root = tk.Tk()
root.style = Style(theme='darkly')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)

# First frame, testing LedButtons
if True:
    frame = ttk.LabelFrame(root, text='Regular Led Buttons')
    frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

    frame.columnconfigure(0, weight=1)

    led_button_1 = cw.LedButton(frame, label_text='Active Primary Button',
                                label_method=lambda e: print('first led button'))
    led_button_1.grid(row=0, column=0, sticky='nsew', pady=(10, 0), padx=10)

    led_button_2 = cw.LedButton(frame, label_text='Active Secondary Button', style='secondary',
                                label_method=lambda e: print('second led button'))
    led_button_2.grid(row=1, column=0, sticky='nsew', pady=(10, 0), padx=10)

    led_button_3 = cw.LedButton(frame, label_text='Active Danger Button', style='danger',
                                label_method=lambda e: print('third led button'))
    led_button_3.grid(row=2, column=0, sticky='nsew', pady=(10, 0), padx=10)

    led_button_4 = cw.LedButton(frame, label_text='Disabled', font=('Verdada', '14', 'bold'),
                                label_method=lambda e: print('disabled led button'))
    led_button_4.grid(row=3, column=0, sticky='nsew', pady=10, padx=10)
    led_button_4.disable()
    print(led_button_1.is_disabled())
    print(led_button_4.is_disabled())

# Second frame, testing the CheckLedButton
if True:
    root.columnconfigure(1, weight=1)
    frame = ttk.LabelFrame(root, text='Check Led Buttons')
    frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

    frame.columnconfigure(0, weight=1)
    label_style_dict = (
        'danger',
        'warning',
        'info',
        'success',
        'secondary',
        'primary',
        'light',
        'dark'
    )
    for i, text in enumerate(label_style_dict):
        led_button = cw.CheckLedButton(frame, label_text=f'Button {i}', label_width=15, style=text,
                                       label_method=lambda e: print(led_button.is_selected()),
                                       bg_color='black')
        led_button.grid(row=i, column=0, sticky='nsew', pady=(10, 0), padx=10)
        if i > 5:
            led_button.disable()

# Third frame, testing the RadioLedButton
if True:
    root.columnconfigure(2, weight=1)
    frame = ttk.LabelFrame(root, text='Radio Led Buttons', padding=10)
    frame.grid(row=0, column=2, sticky='nsew', padx=10, pady=10)

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    for i, text in enumerate(label_style_dict):
        led_button = cw.RadioLedButton(frame, label_text=f'Button {i}', label_width=15, style=text,
                                       label_method=lambda e: print(led_button.is_selected()),
                                       bg_color='black', control_variable=1)
        led_button.grid(row=i, column=0, sticky='nsew', pady=(10, 0), padx=10)
        if i > 5:
            led_button.disable()

    for i, text in enumerate(label_style_dict):
        led_button = cw.RadioLedButton(frame, label_text=f'Button {i}', label_width=15, style=text,
                                       label_method=lambda e: print(led_button.is_selected()),
                                       bg_color='black', control_variable=2)
        led_button.grid(row=i, column=1, sticky='nsew', pady=(10, 0), padx=10)
        if i > 5:
            led_button.disable()

root.mainloop()
