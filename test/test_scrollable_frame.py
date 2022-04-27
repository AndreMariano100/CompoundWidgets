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
frame = cw.ScrollableFrame(root)
frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
# The scroll is not active while all widgets fit in the frame

# To add widgets to the frame, they shall be children of its 'widgets_frame' as follows
frame.widgets_frame.columnconfigure(0, weight=1)
for i in range(20):
    label = ttk.Label(frame.widgets_frame, text=f'This is label {i}')
    label.grid(row=i, column=0, sticky='nsew', pady=5)

# the srollable frame does not behave apropriatelly if you use two of the on the same container

root.mainloop()
