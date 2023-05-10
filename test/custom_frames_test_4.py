import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
import compoundwidgets as cw

root = tk.Tk()
root.geometry(f'600x600+200+50')
root.title('Vertically Collapsable Frame Test with Scrolled Frame')
root.style = Style(theme='flatly')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

base_frame = cw.ScrollableFrame(root, style='light')
base_frame.grid(row=0, column=0, sticky='nsew')
base_frame.columnconfigure(0, weight=1)
base_frame.rowconfigure(0, weight=0)

frame_1 = cw.CollapsableFrame(base_frame, title='No style')
frame_1.grid(row=0, column=0, sticky='nsew', padx=(10, 20), pady=10)
frame_1.rowconfigure(0, weight=1)
frame_1.columnconfigure(0, weight=1)
label = ttk.Label(frame_1, text='This is the 1st collapsable frame', padding=50, anchor='center')
label.grid(row=0, column=0, sticky='nsew')

frame_2 = cw.CollapsableFrame(base_frame, title='Danger', style='danger')
frame_2.grid(row=2, column=0, sticky='nsew', padx=(10, 20), pady=(0, 10))
frame_2.rowconfigure(0, weight=1)
frame_2.columnconfigure(0, weight=1)
label = ttk.Label(frame_2, text='This is the 2nd collapsable frame', padding=50, anchor='center')
label.grid(row=0, column=0, sticky='nsew')

frame_3 = cw.CollapsableFrame(base_frame, title='Info', open_start=False, style='info')
frame_3.grid(row=4, column=0, sticky='nsew', padx=(10, 20), pady=(0, 10))
frame_3.rowconfigure(0, weight=1)
frame_3.columnconfigure(0, weight=1)
label = ttk.Label(frame_3, text='This is the 3rd collapsable frame', padding=50, anchor='center')
label.grid(row=0, column=0, sticky='nsew')

frame_4 = cw.CollapsableFrame(base_frame, title='Success', open_start=False, style='success')
frame_4.grid(row=6, column=0, sticky='nsew', padx=(10, 20), pady=(0, 10))
frame_4.rowconfigure(0, weight=1)
frame_4.columnconfigure(0, weight=1)
label = ttk.Label(frame_4, text='This is the 4th collapsable frame', padding=50, anchor='center')
label.grid(row=0, column=0, sticky='nsew')

frame_1 = cw.CollapsableFrame(base_frame, title='No style disabled', disabled=True)
frame_1.grid(row=1, column=0, sticky='nsew', padx=(10, 20), pady=10)

frame_2 = cw.CollapsableFrame(base_frame, title='Danger disabled', style='danger', disabled=True)
frame_2.grid(row=3, column=0, sticky='nsew', padx=(10, 20), pady=(0, 10))

frame_3 = cw.CollapsableFrame(base_frame, title='Info disabled', open_start=False, style='info', disabled=True)
frame_3.grid(row=5, column=0, sticky='nsew', padx=(10, 20), pady=(0, 10))

frame_4 = cw.CollapsableFrame(base_frame, title='Success disabled', open_start=False, style='success', disabled=True)
frame_4.grid(row=7, column=0, sticky='nsew', padx=(10, 20), pady=(0, 10))

root.mainloop()
