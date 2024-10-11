import tkinter as tk
import compoundwidgets as cw
from ttkbootstrap import Style

root = tk.Tk()
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.style = Style(theme='darkly')
root.minsize(250, 400)

all_buttons = (
    cw.YesButton,
    cw.NoButton,
    cw.OKButton,
    cw.CancelButton,

    cw.ClearButton,
    cw.SaveButton,
    cw.CalculateButton,

    cw.HelpButton,
    cw.BackButton,
    cw.AddToReport,
    cw.EditReport,
    cw.RemoveFromReport,
    cw.AddNewButton,
    cw.EraseButton,
    cw.QuitButton,
    cw.ClipBoardButton,

    cw.NextButton,
    cw.PreviousButton,
    cw.UpButton,
    cw.DownButton,

    cw.SearchButton,
    cw.HomeButton,
    cw.MainMenuButton,
    cw.AppsMenuButton,
    cw.ConfigurationButton,

)
for i, widget in enumerate(all_buttons):
    widget(root, width=12).grid(row=i, column=0, padx=10, pady=1)

for i, widget in enumerate(all_buttons):
    widget(root, language='br').grid(row=i, column=1, padx=10, pady=1)

for i, widget in enumerate(all_buttons):
    widget(root, language='en', style='primary', padding=1).grid(row=i, column=2, padx=10, pady=1)

root.mainloop()
