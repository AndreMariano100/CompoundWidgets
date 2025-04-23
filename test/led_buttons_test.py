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
    def led_button_status():
        for i, b in enumerate(all_led_buttons):
            print(f'{i} is disabled: {b.is_disabled()}. {i} is selected: {b.is_selected()}')

    def disable_led_buttons():
        for b in all_led_buttons:
            if b.is_disabled():
                b.enable()
            else:
                b.disable()

    frame = ttk.LabelFrame(root, text='Check Led Buttons')
    frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
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
    all_led_buttons = []
    for i, text in enumerate(label_style_dict):
        led_button = cw.CheckLedButton(frame, label_text=f'Button {i}', label_width=15, style=text)
        led_button.grid(row=i, column=0, sticky='nsew', pady=(10, 0), padx=10)
        all_led_buttons.append(led_button)

    label_style_dict = (
        'inverse-danger',
        'inverse-warning',
        'inverse-info',
        'inverse-success',
        'inverse-secondary',
        'inverse-primary',
        'inverse-light',
        'inverse-dark'
    )

    for i, text in enumerate(label_style_dict):
        led_button = cw.CheckLedButton(frame, label_text=f'Button {i}', label_width=15, style=text)
        led_button.grid(row=i, column=1, sticky='nsew', pady=(10, 0), padx=10)
        all_led_buttons.append(led_button)


    for i, text in enumerate(label_style_dict):
        led_button = cw.CheckLedButton(frame, label_text=f'Button {i}', label_width=15, style=text,
                                       active_led_color='snow', inactive_led_color='gray40',
                                       relief=False)
        led_button.grid(row=i, column=2, sticky='nsew', pady=(10, 0), padx=10)
        all_led_buttons.append(led_button)

    status_button = ttk.Button(frame, text='Check Status', command=led_button_status)
    status_button.grid(row=20, column=0, sticky='nsew', pady=10, padx=10)
    disable_button = ttk.Button(frame, text='Enable/Disable', command=disable_led_buttons)
    disable_button.grid(row=21, column=0, sticky='nsew', pady=(0, 10), padx=10)

# Second frame, testing the CheckLedButton
if True:
    def check_button_status(event=None):
        for i, b in enumerate(all_check_buttons):
            print(f'{i} is disabled: {b.is_disabled()}. {i} is selected: {b.is_selected()}')

    def disable_all(event=None):
        for b in all_check_buttons:
            if b.is_disabled():
                b.enable()
            else:
                b.disable()


    frame = ttk.LabelFrame(root, text='Check Switch Led Buttons')
    frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)

    label_style_dict = (
        'danger',
        'warning',
        'info',
        'success',
        'secondary',
        'primary',
        'light',
        'dark',
    )
    all_check_buttons = []
    for i, text in enumerate(label_style_dict):
        led_button = cw.CheckSwitchLedButton(frame, label_text=f'Button {i}', label_width=15, style=text)
        led_button.grid(row=i, column=0, sticky='nsew', pady=(10, 0), padx=10)
        all_check_buttons.append(led_button)

    label_style_dict = (
        'inverse-danger',
        'inverse-warning',
        'inverse-info',
        'inverse-success',
        'inverse-secondary',
        'inverse-primary',
        'inverse-light',
        'inverse-dark'
    )
    for i, text in enumerate(label_style_dict):
        led_button = cw.CheckSwitchLedButton(frame, label_text=f'Button {i}', label_width=15, style=text,
                                             relief=False)
        led_button.grid(row=i, column=1, sticky='nsew', pady=(10, 0), padx=10)
        all_check_buttons.append(led_button)

    label_style_dict = (
        'danger',
        'warning',
        'info',
        'success',
        'secondary',
        'primary',
        'light',
        'dark',
    )
    for i, text in enumerate(label_style_dict):
        led_button = cw.CheckSwitchLedButton(frame, label_text=f'Button {i}', label_width=15, style=text,
                                             active_led_color='snow', inactive_led_color='gray40',
                                             relief=False
                                             )
        led_button.grid(row=i, column=2, sticky='nsew', pady=(10, 0), padx=10)
        all_check_buttons.append(led_button)

    status_button = ttk.Button(frame, text='Check Status', command=check_button_status)
    status_button.grid(row=20, column=0, sticky='nsew', pady=10, padx=10)

    disable_button = ttk.Button(frame, text='Disable/Enable', command=disable_all)
    disable_button.grid(row=21, column=0, sticky='nsew', pady=(0, 10), padx=10)

# Third frame, testing the RadioLedButton
if True:
    def radio_button_status(event=None):
        for i, b in enumerate(all_radio_buttons):
            if b.is_selected():
                print(f'{i} is selected: {b.is_selected()}')

    def radio_button_status_2(event=None):
        for i, b in enumerate(all_radio_buttons_2):
            if b.is_selected():
                print(f'{i} is selected: {b.is_selected()}')

    def radio_button_disable(event=None):
        for b in all_radio_buttons:
            if b.is_disabled():
                b.enable()
            else:
                b.disable()
        for b in all_radio_buttons_2:
            if b.is_disabled():
                b.enable()
            else:
                b.disable()

    frame = ttk.LabelFrame(root, text='Radio Led Buttons', padding=10)
    frame.grid(row=0, column=2, sticky='nsew', padx=10, pady=10)

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    all_radio_buttons = []
    all_radio_buttons_2 = []

    for i, text in enumerate(label_style_dict):
        led_button = cw.RadioLedButton(frame, label_text=f'Button {i}', label_width=15, style=text,
                                       control_variable=1, label_method=radio_button_status,
                                       switch_type=True, relief=False, active_led_color='snow',
                                       inactive_led_color='gray40')
        led_button.grid(row=i, column=0, sticky='nsew', pady=(10, 0), padx=10)
        all_radio_buttons.append(led_button)

    for i, text in enumerate(label_style_dict):
        led_button = cw.RadioLedButton(frame, label_text=f'Button {i}', label_width=15, style='secondary',
                                       control_variable=2, label_method=radio_button_status_2,
                                       relief=False, active_led_color='snow', inactive_led_color='gray40')
        led_button.grid(row=i, column=1, sticky='nsew', pady=(10, 0), padx=10)
        all_radio_buttons_2.append(led_button)

    status_button = ttk.Button(frame, text='Check Status', command=radio_button_status)
    status_button.grid(row=20, column=0, columnspan=2, sticky='nsew', pady=10, padx=10)

    disable_button = ttk.Button(frame, text='Enable/Disable', command=radio_button_disable)
    disable_button.grid(row=21, column=0, columnspan=2, sticky='nsew', pady=10, padx=10)


root.mainloop()
