import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap import Style
import compoundwidgets as cw

root = tk.Tk()
root.style = Style(theme='darkly')
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

# First frame, testing LabelCombo
if True:
    def get_all_label_combos():
        for w in label_combo_list:
            print(w.get())

    def set_all_label_combos():
        for w in label_combo_list:
            w.set('none')

    def set_all_label_combos_2():
        for w in label_combo_list:
            w.set('Label Combo 2')

    def set_disable_combos():
        for w in label_combo_list:
            w.disable()

    def set_read_only_combos():
        for w in label_combo_list:
            w.readonly()

    def set_normal_combos():
        for w in label_combo_list:
            w.enable()

    frame = ttk.LabelFrame(root, text='Label Combos')
    frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
    frame.columnconfigure(0, weight=1)
    local_list = ('Label Combo 1', 'Label Combo 2', 'Label Combo 3', 'Label Combo 4')
    label_combo_list = []
    for i, item in enumerate(local_list):
        w = cw.LabelCombo(frame, label_text=item, label_width=10, combo_list=local_list)
        w.grid(row=i, column=0, sticky='nsew', pady=2)
        label_combo_list.append(w)
        if i == 2:
            w.readonly()
        if i == 3:
            w.disable()

    b1 = ttk.Button(frame, text='GET ALL', command=get_all_label_combos)
    b1.grid(row=4, column=0, pady=2, sticky='ew', padx=2)

    b2 = ttk.Button(frame, text='SET ALL WRONG', command=set_all_label_combos)
    b2.grid(row=5, column=0, pady=2, sticky='ew', padx=2)

    b3 = ttk.Button(frame, text='SET ALL RIGHT', command=set_all_label_combos_2)
    b3.grid(row=6, column=0, pady=2, sticky='ew', padx=2)

    b4 = ttk.Button(frame, text='READ ONLY', command=set_read_only_combos)
    b4.grid(row=7, column=0, pady=2, sticky='ew', padx=2)

    b5 = ttk.Button(frame, text='DISABLE', command=set_disable_combos)
    b5.grid(row=8, column=0, pady=2, sticky='ew', padx=2)

    b6 = ttk.Button(frame, text='NORMAL', command=set_normal_combos)
    b6.grid(row=9, column=0, pady=2, sticky='ew', padx=2)

# Second frame, testing LabelEntry
if True:
    def get_all_label_entries(event=None):
        for w in label_entry_list:
            print(w.get())

    def set_all_label_entries():
        for w in label_entry_list:
            w.set('none')

    def set_disable_entries():
        for w in label_entry_list:
            w.disable()

    def set_read_only_entries():
        for w in label_entry_list:
            w.readonly()

    def set_normal_entries():
        for w in label_entry_list:
            w.enable()

    def set_empty_entries():
        for w in label_entry_list:
            w.set('')

    frame = ttk.LabelFrame(root, text='Label Entries')
    frame.grid(row=0, column=1, sticky='nsew', padx=(0, 10), pady=10)
    frame.columnconfigure(0, weight=1)

    local_list = ('1000', '2000.00', 'Label Entry', 'Label Entry', 'Very Long Label Entry')
    label_entry_list = []
    for i, item in enumerate(local_list):
        if i in range(3):
            w = cw.LabelEntry(frame, label_text=f'Label Entry {i+1}', label_width=10, entry_method=get_all_label_entries,
                              entry_numeric=True, entry_value=item, entry_max_char=10, trace_variable=True)
        else:
            w = cw.LabelEntry(frame, label_text=f'Label Entry {i+1}', label_width=10, entry_method=get_all_label_entries,
                              entry_numeric=False, entry_value=item, entry_max_char=10, trace_variable=True)
        w.grid(row=i, column=0, sticky='nsew', pady=2)
        label_entry_list.append(w)
        if i == 2:
            w.readonly()
        if i == 3:
            w.disable()

    b1 = ttk.Button(frame, text='GET ALL', command=get_all_label_entries)
    b1.grid(row=5, column=0, pady=2, sticky='ew', padx=2)

    b3 = ttk.Button(frame, text='SET ALL', command=set_all_label_entries)
    b3.grid(row=6, column=0, pady=2, sticky='ew', padx=2)

    b4 = ttk.Button(frame, text='READ ONLY', command=set_read_only_entries)
    b4.grid(row=7, column=0, pady=2, sticky='ew', padx=2)

    b5 = ttk.Button(frame, text='DISABLE', command=set_disable_entries)
    b5.grid(row=8, column=0, pady=2, sticky='ew', padx=2)

    b6 = ttk.Button(frame, text='NORMAL', command=set_normal_entries)
    b6.grid(row=9, column=0, pady=2, sticky='ew', padx=2)

    b7 = ttk.Button(frame, text='SET EMPTY', command=set_empty_entries)
    b7.grid(row=10, column=0, pady=2, sticky='ew', padx=2)

# Third Frame, testing LabelSpinbox
if True:
    def get_all_label_spin(event=None):
        for w in label_spin_list:
            print(w.get())

    def set_all_label_spin():
        for i, w in enumerate(label_spin_list):
            w.set(local_spin_list[i][1])

    def set_all_label_spin_wrong():
        for w in label_spin_list:
            w.set(-100)

    def set_disable_spin():
        for w in label_spin_list:
            w.disable()

    def set_read_only_spin():
        for w in label_spin_list:
            w.readonly()

    def set_normal_spin():
        for w in label_spin_list:
            w.enable()

    frame = ttk.LabelFrame(root, text='Label Spinbox')
    frame.grid(row=0, column=2, sticky='nsew', padx=(0, 10), pady=10)
    frame.columnconfigure(0, weight=1)

    local_spin_list = (
        ('Spin 1 - int 0~10', 5, 'int', 0, 10, 1, 0),
        ('Spin 2 - int -10~10', None, 'int', -10, 10, 2, 0),
        ('Spin 3 - float 0~10', 5, 'float', 0, 10, 0.02, 2),
        ('Spin 4 - float -10~10', 0, 'float', -10, 10, 0.5, 1),
    )
    label_spin_list = []
    for i, item in enumerate(local_spin_list):
        w = cw.LabelSpinbox(frame, label_text=item[0], label_width=15,
                            entry_value=item[1], entry_width=10, entry_method=get_all_label_spin,
                            entry_type=item[2], spin_start=item[3], spin_end=item[4],
                            spin_increment=item[5], spin_precision=item[6])
        w.grid(row=i, column=0, sticky='nsew', pady=2, padx=2)
        label_spin_list.append(w)

    b1 = ttk.Button(frame, text='GET ALL', command=get_all_label_spin)
    b1.grid(row=5, column=0, pady=2, sticky='ew', padx=2)

    b3 = ttk.Button(frame, text='SET ALL RIGHT', command=set_all_label_spin)
    b3.grid(row=6, column=0, pady=2, sticky='ew', padx=2)

    b3 = ttk.Button(frame, text='SET ALL WRONG', command=set_all_label_spin_wrong)
    b3.grid(row=7, column=0, pady=2, sticky='ew', padx=2)

    b4 = ttk.Button(frame, text='READ ONLY', command=set_read_only_spin)
    b4.grid(row=8, column=0, pady=2, sticky='ew', padx=2)

    b5 = ttk.Button(frame, text='DISABLE', command=set_disable_spin)
    b5.grid(row=9, column=0, pady=2, sticky='ew', padx=2)

    b6 = ttk.Button(frame, text='NORMAL', command=set_normal_spin)
    b6.grid(row=10, column=0, pady=2, sticky='ew', padx=2)

# Fourth frame, testing LabelText
if True:
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
                             sided=False, font=('Verdana', '12'))
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

root.mainloop()
