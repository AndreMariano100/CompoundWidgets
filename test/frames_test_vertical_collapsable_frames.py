import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
import compoundwidgets as cw

root = tk.Tk()
root.geometry(f'950x600+200+50')
root.title('Horizontally Collapsable Frame Test')
root.style = Style(theme='flatly')

# In order to behave appropriately the collapsable frame shall have a '0' column weight on its parent
root.rowconfigure(0, weight=1)

frame_1 = cw.VCollapsableFrame(root, title='No style')
frame_1.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
frame_1.rowconfigure(0, weight=1)
frame_1.columnconfigure(0, weight=1)
label = ttk.Label(frame_1, text='This is the 1st collapsable frame', padding=50, anchor='center')
label.grid(row=0, column=0, sticky='nsew')

frame_2 = cw.VCollapsableFrame(root, title='Danger', style='danger')
frame_2.grid(row=0, column=2, sticky='nsew', padx=10, pady=10)
frame_2.rowconfigure(0, weight=1)
frame_2.columnconfigure(0, weight=1)
label = ttk.Label(frame_2, text='This is the 2nd collapsable frame', padding=50, anchor='center')
label.grid(row=0, column=0, sticky='nsew')

frame_3 = cw.VCollapsableFrame(root, title='Info', open_start=False, style='info')
frame_3.grid(row=0, column=4, sticky='nsew', padx=10, pady=10)
frame_3.rowconfigure(0, weight=1)
frame_3.columnconfigure(0, weight=1)
label = ttk.Label(frame_3, text='This is the 3rd collapsable frame', padding=50, anchor='center')
label.grid(row=0, column=0, sticky='nsew')

frame_4 = cw.VCollapsableFrame(root, title='Success', open_start=False, style='success')
frame_4.grid(row=0, column=6, sticky='nsew', padx=10, pady=10)
frame_4.rowconfigure(0, weight=1)
frame_4.columnconfigure(0, weight=1)
label = ttk.Label(frame_4, text='This is the 4th collapsable frame', padding=50, anchor='center')
label.grid(row=0, column=0, sticky='nsew')

frame_1 = cw.VCollapsableFrame(root, title='No style disabled', disabled=True)
frame_1.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

frame_2 = cw.VCollapsableFrame(root, title='Danger disabled', style='danger', disabled=True)
frame_2.grid(row=0, column=3, sticky='nsew', padx=10, pady=10)

frame_3 = cw.VCollapsableFrame(root, title='Info disabled', open_start=False, style='info', disabled=True)
frame_3.grid(row=0, column=5, sticky='nsew', padx=10, pady=10)

frame_4 = cw.VCollapsableFrame(root, title='Success disabled', open_start=False, style='success', disabled=True)
frame_4.grid(row=0, column=7, sticky='nsew', padx=10, pady=10)

root.mainloop()
