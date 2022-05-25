import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap import Style
import compoundwidgets as cw

root = tk.Tk()
root.columnconfigure(0, weight=1)

root.geometry(f'600x600+200+50')
root.title('Collapsable frame test')

# All compound widgets use ttkboostrap Style
root.style = Style(theme='darkly')

# In order to behave appropriately the collapsable frame shall have a '0' row weight on its parent
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=0)
root.rowconfigure(2, weight=0)

# Minimum information: parent for the frame
frame_1 = cw.CollapsableFrame(root)
frame_1.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
frame_1.rowconfigure(0, weight=1)
frame_1.columnconfigure(0, weight=1)

# To add widgets to the frame, they shall be children of its 'widgets_frame' as follows
label = ttk.Label(frame_1, text='This is the 1st collapsable frame', padding=50, anchor='center')
label.grid(row=0, column=0, sticky='nsew')

# Adding title information on initialization
frame_2 = cw.CollapsableFrame(root, title='Second Frame')
frame_2.grid(row=1, column=0, sticky='nsew', padx=10, pady=(0, 10))
frame_2.rowconfigure(0, weight=1)
frame_2.columnconfigure(0, weight=1)
label = ttk.Label(frame_2, text='This is the 2nd collapsable frame', padding=50, anchor='center')
label.grid(row=0, column=0, sticky='nsew')

# The frame may start opened (standard) or collapsed
frame_3 = cw.CollapsableFrame(root, title='Third Frame', open_start=False)
frame_3.grid(row=2, column=0, sticky='nsew', padx=10, pady=(0, 10))
frame_3.rowconfigure(0, weight=1)
frame_3.columnconfigure(0, weight=1)
label = ttk.Label(frame_3, text='This is the 3rd collapsable frame', padding=50, anchor='center')
label.grid(row=0, column=0, sticky='nsew')

root.mainloop()
