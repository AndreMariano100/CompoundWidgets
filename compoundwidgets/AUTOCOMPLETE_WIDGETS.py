import tkinter as tk
import tkinter.ttk as ttk
import re


def float_only(action, value, text, max_length=None):
    """ Checks that only float related characters are accepted as input """

    permitted = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '-']
    if action == '1':
        if str(max_length) != 'None':
            if len(value) > int(max_length):
                return False
        if value == '.' and text == '.':
            return False
        elif value == '-' and text == '-':
            return True
        elif text in permitted:
            try:
                float(value)
                return True
            except ValueError:
                return False
        else:
            return False
    else:
        return True


def max_chars(action, value, max_length):
    """ Checks for the maximum number of characters """
    if action == '1':
        if len(value) > int(max_length):
            return False
    return True


class AutocompleteEntryList(ttk.Frame):
    def __init__(self,
                 parent,
                 label_text='label:',
                 label_anchor='w',
                 label_width=None,
                 entry_value='',
                 entry_numeric=False,
                 entry_width=None,
                 entry_max_char=None,
                 list_method=None,
                 list_height=10,
                 full_list=('A', 'B', 'C')):

        # Parent class initialization
        super().__init__(parent, padding=2)

        # Entry validation for numbers
        validate_numbers = self.register(float_only)
        validate_chars = self.register(max_chars)

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=0)
            self.rowconfigure(1, weight=0)
            self.rowconfigure(2, weight=1)
            self.columnconfigure(0, weight=1)

        # Label
        if True:
            self.label = ttk.Label(self, text=label_text, anchor=label_anchor)
            self.label.grid(row=0, column=0, sticky='ew')

            if label_width:
                self.label['width'] = label_width

        # Entry
        if True:
            self.entry_var = tk.StringVar(value=entry_value)
            self.entry = ttk.Entry(self, textvariable=self.entry_var, justify='center')
            self.entry.grid(row=1, column=0, sticky='ew', pady=2)

            if entry_width:
                self.entry['width'] = entry_width

            # Restrict numeric values
            if entry_numeric:
                self.entry.config(validate='all', validatecommand=(validate_numbers, '%d', '%P', '%S', entry_max_char))

            # Restrict max characters
            elif entry_max_char:
                self.entry.config(validate='all', validatecommand=(validate_chars, '%d', '%P', entry_max_char))

        # List box and scroll bar
        if True:
            self.container = ttk.Frame(self)
            self.container.grid(row=2, column=0, sticky='nsew')

            self.container.rowconfigure(0, weight=1)
            self.container.columnconfigure(0, weight=1)
            self.container.columnconfigure(1, weight=0)

            # vertical scrollbar
            self.vscroll = ttk.Scrollbar(self.container, orient='vertical')
            self.vscroll.grid(row=0, column=1, sticky='ns')

            # List box
            self.full_list = full_list
            self.caps_full_list = [item.upper() for item in full_list]
            self.list_method = list_method
            self.list_var = tk.StringVar(value=self.full_list)
            self.lb = tk.Listbox(self.container, listvariable=self.list_var, height=list_height,
                                 yscrollcommand=self.vscroll.set)
            self.lb.grid(row=0, column=0, sticky='nsew')

            self.vscroll['command'] = self.lb.yview

        # Binds and initialization
        if True:
            self.entry_var.trace('w', self.changed)

            self.lb.bind("<Right>", self.selection)
            self.lb.bind('<Return>', self.selection)
            self.lb.bind("<Double-Button-1>", self.selection)
            self.lb.bind("<<ListboxSelected>>", self.selection)

    def changed(self, name, index, mode):

        if self.entry_var.get() == '':
            self.list_var.set(self.full_list)
        else:
            words = self.comparison()
            if words:
                self.lb.delete(0, tk.END)
                for w in words:
                    self.lb.insert(tk.END, w)
            else:
                self.lb.delete(0, tk.END)
                self.lb.insert(tk.END, '(no match)')

    def selection(self, event):

        if self.lb.get(tk.ACTIVE) == '(no match)':
            return

        if not self.lb.get(tk.ACTIVE):
            return

        self.entry_var.set(self.lb.get(tk.ACTIVE))
        self.list_var.set('')
        if self.list_method:
            self.list_method(event)

    def comparison(self):

        pattern = re.compile('.*' + self.entry_var.get().upper() + '.*')
        index = []
        for i, name in enumerate(self.caps_full_list):
            if re.match(pattern, name):
                index.append(i)

        result = [w for i, w in enumerate(self.full_list) if i in index]

        return result

    def set_list(self, new_list):
        self.entry_var.set('')
        self.full_list = new_list
        self.caps_full_list = [item.upper() for item in new_list]
        self.list_var.set(new_list)

    def set_entry(self, new_value):
        self.entry_var.set(new_value)

    def set(self, new_value):
        self.entry_var.set(new_value)

    def get(self):
        return self.entry_var.get()

    def disable(self):
        self.label.config(style='secondary.TLabel')
        self.entry.config(state='disabled')
        self.lb.config(state='disabled')

    def enable(self):
        self.label.config(style='TLabel')
        self.entry.config(state='normal')
        self.lb.config(state='normal')
