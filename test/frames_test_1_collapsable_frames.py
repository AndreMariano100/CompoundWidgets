import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
import compoundwidgets as cw


def test_method(event):
    print(event.widget.cget('text'))


root = tk.Tk()
root.columnconfigure(0, weight=1)

root.geometry(f'600x650+200+50')
root.title('Vertically Collapsable Frame Test')
root.style = Style(theme='flatly')

label_style_list = ('danger', 'warning', 'info', 'success',
                    'secondary', 'primary', 'light', 'dark', 'no style')

for i, style in enumerate(label_style_list):
    root.rowconfigure(i, weight=0)
    frame = cw.CollapsableFrame(root, title=style, expand_method=test_method, style=style)
    frame.grid(row=i, column=0, sticky='nsew', padx=10, pady=5)
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    label = ttk.Label(frame, text=f'This is the collapsable frame number {i+1}', padding=50, anchor='center')
    label.grid(row=0, column=0, sticky='nsew')
    frame.collapse_frame()

root.mainloop()
