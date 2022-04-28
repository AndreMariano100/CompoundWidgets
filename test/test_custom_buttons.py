import tkinter as tk
import compoundwidgets as cw
from ttkbootstrap import Style

root = tk.Tk()
root.columnconfigure(0, weight=1)
root.style = Style(theme='darkly')
root.minsize(250, 400)

all_buttons = (
    cw.ClearButton,
    cw.SaveButton,
    cw.CancelButton,
    cw.CalculateButton,
    cw.YesButton,
    cw.NoButton,
    cw.BackButton,
    cw.HelpButton,
    cw.AddToReport,
    cw.EditReport,
    cw.RemoveFromReport,
)
for i, widget in enumerate(all_buttons):
    widget(root).grid(row=i, column=0, padx=10, pady=10)

root.mainloop()
