import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap import Style
import compoundwidgets as cw
import random

root = tk.Tk()
root.style = Style(theme='darkly')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


def get_all_label_text(event=None):
    for w in label_text_list:
        print(w.get())


def set_all_label_text():
    for i, w in enumerate(label_text_list):
        w.set(local_text_list[i])


def set_disable_text():
    for w in label_text_list:
        w.disable()


def set_read_only_text():
    for w in label_text_list:
        w.readonly()


def set_normal_text():
    for w in label_text_list:
        w.enable()


def set_style():
    label_style_list = ('danger', 'warning', 'info', 'success',
                        'secondary', 'primary', 'light', 'dark', 'no style')
    new_styles = random.sample(label_style_list, len(label_text_list))
    for i, w in enumerate(label_text_list):
        w.set_style(new_styles[i])


frame = ttk.LabelFrame(root, text='Label Text')
frame.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=10, pady=10)
frame.columnconfigure(0, weight=1)

local_text_list = (
    """Now is the winter of our discontent Made glorious summer by this sun of York; And all the clouds that lour'd upon our house In the deep bosom of the ocean buried. Now are our brows bound with victorious wreaths; Our bruised arms hung up for monuments; Our stern alarums changed to merry meetings, Our dreadful marches to delightful measures.""",
    """Grim-visaged war hath smooth'd his wrinkled front; And now, instead of mounting barded steeds To fright the souls of fearful adversaries, He capers nimbly in a lady's chamber To the lascivious pleasing of a lute. But I, that am not shaped for sportive tricks, Nor made to court an amorous looking-glass; I, that am rudely stamp'd, and want love's majesty To strut before a wanton ambling nymph; I, that am curtail'd of this fair proportion."""
)
label_text_list = []
for i, item in enumerate(local_text_list):
    if i:
        w = cw.LabelText(frame, label_text=f'Label Text {i+1}', label_width=10,
                         text_height=7, text_width=40, text_method=get_all_label_text, text_value=item,
                         sided=True)
    else:
        w = cw.LabelText(frame, label_text=f'Label Text {i + 1}', label_width=10, label_anchor='w',
                         text_height=5, text_width=60, text_method=get_all_label_text, text_value=item,
                         sided=False, label_font=('Verdana', '12'))
    w.grid(row=i, column=0, sticky='nsew', pady=2, padx=2)
    label_text_list.append(w)

local_frame = ttk.Frame(frame)
local_frame.grid(row=0, column=1, rowspan=2, sticky='nsew')

b1 = ttk.Button(local_frame, text='GET ALL', command=get_all_label_text)
b1.grid(row=0, column=1, pady=(30, 2), sticky='ew', padx=2)

b3 = ttk.Button(local_frame, text='SET ALL', command=set_all_label_text)
b3.grid(row=1, column=1, pady=2, sticky='ew', padx=2)

b4 = ttk.Button(local_frame, text='READ ONLY', command=set_read_only_text)
b4.grid(row=2, column=1, pady=2, sticky='ew', padx=2)

b5 = ttk.Button(local_frame, text='DISABLE', command=set_disable_text)
b5.grid(row=3, column=1, pady=2, sticky='ew', padx=2)

b6 = ttk.Button(local_frame, text='NORMAL', command=set_normal_text)
b6.grid(row=4, column=1, pady=2, sticky='ew', padx=2)

b7 = ttk.Button(frame, text='STYLE', command=set_style)
b7.grid(row=5, column=1, pady=2, sticky='ew', padx=2)

root.mainloop()
