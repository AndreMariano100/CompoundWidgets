import os
import tkinter.ttk as ttk
import tkinter as tk
import compoundwidgets as cw
from ttkbootstrap import Style
import time


# Methods for testing the message boxes
def show_ok_cancel_box():
    answer = cw.OkCancelBox(root, icon_path=icon_path, title='OK Cancel Box',
                            message='This is a OK / Cancel message box.\nTest the answers!').show()
    if answer:
        print(f'Selected OK ({answer})')
    else:
        print(f'Selected Cancel ({answer})')


def show_yes_no_box():
    answer = cw.YesNoBox(root, icon_path=icon_path, title='Yes No Box',
                         message='This is a Yes / No message box. This one has a very long text message. Test the answers!',
                         language='en').show()
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
    cw.WarningBox(root, icon_path=icon_path, title='Warning Box',
                  message='This is a Warning box!').show()


def show_success_box():
    cw.SuccessBox(root, icon_path=icon_path, title='Success Box',
                  message='This is a Success box!').show()

# Methods for testing the message boxes
def show_timed_danger_box():
    cw.TimedBox(root, message='This is a timed box: 1 seconds', time=1, style='danger').show()

def show_timed_warning_box():
    cw.TimedBox(root, message='This is a timed box: 0.5 seconds', time=0.5, style='warning').show()

def show_timed_info_box():
    cw.TimedBox(root, message='This is a timed box: 0.2 seconds', time=0.2, style='info').show()

def show_timed_generic_box():
    cw.TimedBox(root, message='This is a generic timed box with a kind of a long text to see if it fits').show()

# Root
root = tk.Tk()
root.title('Message Box Testing')
image_path = os.getcwd().replace('test', 'compoundwidgets\IMAGES')
icon_path = os.path.join(image_path, 'engineering.ico')
root.iconbitmap(icon_path)
root.style = Style(theme='darkly')
root.geometry(f'400x600+200+50')
root.columnconfigure(0, weight=1)
for i in range(10):
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

button = ttk.Button(root, text='Danger Timed Box', command=show_timed_danger_box)
button.grid(row=6, column=0, sticky='nsew', padx=10, pady=10)

button = ttk.Button(root, text='Warning Timed Box', command=show_timed_warning_box)
button.grid(row=7, column=0, sticky='nsew', padx=10, pady=10)

button = ttk.Button(root, text='Info Timed Box', command=show_timed_info_box)
button.grid(row=8, column=0, sticky='nsew', padx=10, pady=10)

button = ttk.Button(root, text='Undefined Timed Box', command=show_timed_generic_box)
button.grid(row=9, column=0, sticky='nsew', padx=10, pady=10)

root.mainloop()
