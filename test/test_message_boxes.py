import tkinter.ttk as ttk
import tkinter as tk
import compoundwidgets as cw
from ttkbootstrap import Style
import time


# Methods for testing the message boxes
def show_ok_cancel_box():
    answer = cw.OkCancelBox(root, message='This is a OK / Cancel message box.\nTest the answers!').show()
    if answer:
        print(f'Selected OK ({answer})')
    else:
        print(f'Selected Cancel ({answer})')


def show_yes_no_box():
    answer = cw.YesNoBox(root, message='This is a Yes / No message box.\nTest the answers!').show()
    if answer:
        print(f'Selected Yes ({answer})')
    else:
        print(f'Selected No ({answer})')


def show_progress_bar():
    p_bar = cw.ProgressBar(root, message='Showing progress bar...', final_value=50)
    for i in range(51):
        time.sleep(0.02)
        p_bar.update_bar(i)
    p_bar.destroy()


def show_warning_box():
    cw.WarningBox(root, message='This is a Warning box!').show()


def show_success_box():
    cw.SuccessBox(root, message='This is a Success box!').show()


# Root
root = tk.Tk()
root.title('Message Box Testing')
root.style = Style(theme='darkly')
root.geometry(f'400x300+200+50')
root.columnconfigure(0, weight=1)
for i in range(5):
    root.rowconfigure(i, weight=1)

button = ttk.Button(root, text='OK / CANCEL Message Box', command=show_ok_cancel_box)
button.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

button = ttk.Button(root, text='Yes / No Message Box', command=show_yes_no_box)
button.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

button = ttk.Button(root, text='Progress Bar', command=show_progress_bar)
button.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)

button = ttk.Button(root, text='Warning Box', command=show_warning_box)
button.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)

button = ttk.Button(root, text='Success Box', command=show_success_box)
button.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)

button = ttk.Button(root, text='Tool Tip')
button.grid(row=5, column=0, sticky='nsew', padx=10, pady=10)
tool_tip_text = "This is a sample help text, that will be shown on a pop up window in the form of a tool tip"
cw.Tooltip(button, text=tool_tip_text, wrap_length=200)

root.mainloop()
