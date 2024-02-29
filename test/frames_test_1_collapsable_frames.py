import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
import compoundwidgets as cw

root = tk.Tk()
root.columnconfigure(0, weight=1)
# In order to behave appropriately the collapsable frame shall have a '0' row weight on its parent
for i in range(10):
    root.rowconfigure(i, weight=0)

root.geometry(f'600x650+200+50')
root.title('Vertically Collapsable Frame Test')
root.style = Style(theme='flatly')

frame_1 = cw.CollapsableFrame(root, title='No style')
frame_1.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
frame_1.rowconfigure(0, weight=1)
frame_1.columnconfigure(0, weight=1)
label_1 = ttk.Label(frame_1, text='This is the 1st collapsable frame', padding=50, anchor='center')
label_1.grid(row=0, column=0, sticky='nsew')

frame_2 = cw.CollapsableFrame(root, title='Danger', style='danger')
frame_2.grid(row=2, column=0, sticky='nsew', padx=10, pady=(0, 10))
frame_2.rowconfigure(0, weight=1)
frame_2.columnconfigure(0, weight=1)
label2 = ttk.Label(frame_2, text='This is the 2nd collapsable frame', padding=50, anchor='center')
label2.grid(row=0, column=0, sticky='nsew')

frame_3 = cw.CollapsableFrame(root, title='Info', open_start=False, style='info')
frame_3.grid(row=4, column=0, sticky='nsew', padx=10, pady=(0, 10))
frame_3.rowconfigure(0, weight=1)
frame_3.columnconfigure(0, weight=1)
label3 = ttk.Label(frame_3, text='This is the 3rd collapsable frame', padding=50, anchor='center')
label3.grid(row=0, column=0, sticky='nsew')

frame_4 = cw.CollapsableFrame(root, title='Success', open_start=False, style='success')
frame_4.grid(row=6, column=0, sticky='nsew', padx=10, pady=(0, 10))
frame_4.rowconfigure(0, weight=1)
frame_4.columnconfigure(0, weight=1)
label4 = ttk.Label(frame_4, text='This is the 4th collapsable frame', padding=50, anchor='center')
label4.grid(row=0, column=0, sticky='nsew')

frame_11 = cw.CollapsableFrame(root, title='No style disabled', disabled=True)
frame_11.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

frame_22 = cw.CollapsableFrame(root, title='Danger disabled', style='danger', disabled=True)
frame_22.grid(row=3, column=0, sticky='nsew', padx=10, pady=(0, 10))

frame_33 = cw.CollapsableFrame(root, title='Info disabled', open_start=False, style='info', disabled=True)
frame_33.grid(row=5, column=0, sticky='nsew', padx=10, pady=(0, 10))

frame_44 = cw.CollapsableFrame(root, title='Success disabled', open_start=False, style='success', disabled=True)
frame_44.grid(row=7, column=0, sticky='nsew', padx=10, pady=(0, 10))

root.mainloop()
