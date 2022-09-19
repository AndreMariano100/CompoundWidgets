import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap import Style
import compoundwidgets as cw

root = tk.Tk()
root.columnconfigure(0, weight=1)

root.geometry(f'600x300+200+50')
root.title('Scrollable frame test')

# All compound widgets use ttkboostrap Style
root.style = Style(theme='darkly')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create frame instance
frame = cw.ScrollableFrame(root, style='warning.TFrame')
frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
# The scroll is not active while all widgets fit in the frame

# To add widgets to the frame, they shall be children of its 'widgets_frame' as follows
frame.columnconfigure(0, weight=1)
for i in range(10):
    label = ttk.Label(frame, text=f'This is label {i}', style='secondary.Inverse.TLabel')
    label.grid(row=i, column=0, sticky='nsew', pady=5, padx=20)

# the scrollable frame does not behave apropriately if you use two of the on the same container

root.mainloop()
