import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
import compoundwidgets as cw
import random


def change_style():
    new_styles = random.sample(label_style_list, len(label_style_list))
    for i, frame in enumerate(frames_list):
        frame.set_border_style(new_styles[i])

    new_styles = random.sample(label_style_list, len(label_style_list))
    for i, frame in enumerate(frames_list):
        frame.set_frame_style(new_styles[i])



root = tk.Tk()
root.columnconfigure(0, weight=1)

root.geometry(f'600x650+200+50')
root.title('Border Frame Test')
root.style = Style(theme='flatly')

frame_1 = cw.BorderFrame(root, border_width=1, border_style='secondary')
frame_1.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
label = ttk.Label(frame_1, text='Border 1')
label.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

frame_2 = cw.BorderFrame(root, border_width=(1, 10, 1, 1), border_style='secondary')
frame_2.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
label = ttk.Label(frame_2, text='Border 2')
label.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

frame_3 = cw.BorderFrame(root, border_width=(2, 6, 2, 2), border_style='danger', frame_style='warning')
frame_3.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
label = ttk.Label(frame_3, text='Border 3')
label.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

frame_4 = cw.BorderFrame(root, border_width=(1, 5, 1, 5), border_style='primary')
frame_4.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)
label = ttk.Label(frame_4, text='Border 4')
label.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

frames_list = [frame_1, frame_2, frame_3, frame_4]
label_style_list = ('danger', 'warning', 'info', 'success',
                    'secondary', 'primary', 'light', 'dark', 'no style')

b = ttk.Button(root, text='Change Styles', command=change_style)
b.grid(row=4, column=0, sticky='nsew', pady=5, columnspan=len(frames_list))

root.mainloop()
