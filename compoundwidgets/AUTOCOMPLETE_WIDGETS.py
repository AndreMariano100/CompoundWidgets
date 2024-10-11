import tkinter as tk
import ttkbootstrap as ttk
import re
from .SCRIPTS import *
from .COMPOUND_WIDGETS import LabelCompoundWidget


class AutocompleteEntryList(ttk.Frame):
    """
    Autocomplete compound widget which combines an Entry Widget and a Listbox Widget
    Filling the entry widget filters the content from the listbox widget.
    Parameters:
        parent: parent widget
        label_text: label text value
        label_anchor: anchor position for the text within the label
        label_width: minimum width of the label
        entry_value: value to be shown on the entry widget
        entry_numeric: limits the entry value to numbers only
        entry_width: minimum width of the entry
        entry_max_char: maximum number of characters for the entry
        list_method: method to be called when an item is selected
        list_height: number of lines on the listbox
        list_values: values to be shown on the listbox
        case_sensitive: whether char case shall be respected
    Methods for the user:
        set_list(new_list): sets a new list of values to the listbox widget
        set_entry(value): sets a value to the entry widget
        set(value): sets a value to the entry widget
        get(): gets the current value from the entry widget
        disable(): turns the whole widget 'off'
        enable(): turns the whole widget 'on'
    
    """

    def __init__(self, parent, label_text='label:', label_anchor='w', label_width=None,
                 entry_value='', entry_numeric=False, entry_width=None, entry_max_char=None,
                 entry_change_method=None, list_method=None, list_height=5, case_sensitive=False,
                 list_values=('Value 1', 'Value 2', 'Value 3', 'Value 4')):

        # Parent class initialization
        super().__init__(parent, padding=5)

        # Entry validation for numbers
        validate_numbers = self.register(float_only)
        validate_chars = self.register(max_chars)

        self.case_sensitive = case_sensitive

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=0)  # label
            self.rowconfigure(1, weight=0)  # entry
            self.rowconfigure(2, weight=1)  # listbox
            self.columnconfigure(0, weight=1)

        # Label
        if True:
            self.label = ttk.Label(self, text=label_text, anchor=label_anchor)
            self.label.grid(row=0, column=0, sticky='ew')

            if label_width:
                self.label['width'] = label_width

        # Entry
        if True:
            self.entry_change_method = entry_change_method
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
            self.full_list = list_values
            self.caps_full_list = [item.upper() for item in list_values]
            self.list_method = list_method
            self.list_var = tk.StringVar(value=self.full_list)
            self.lb = tk.Listbox(self.container, listvariable=self.list_var, height=list_height,
                                 yscrollcommand=self.vscroll.set)
            self.lb.grid(row=0, column=0, sticky='nsew')

            self.vscroll['command'] = self.lb.yview

        # Binds and initialization
        if True:
            self.entry_var.trace('w', self._entry_changed)
            self.entry_var.trace('u', self._entry_changed)
            self.lb.bind("<Right>", self._listbox_selection)
            self.lb.bind('<Return>', self._listbox_selection)
            self.lb.bind("<Double-Button-1>", self._listbox_selection)
            self.lb.bind("<<ListboxSelected>>", self._listbox_selection)

    def _entry_changed(self, name, index, mode):
        """ Keeps track of any change in the entry widget and updates the listbox values """

        if str(mode) == 'w':
            if self.entry_change_method:
                self.entry_change_method()

        if self.entry_var.get() == '':
            self.list_var.set(self.full_list)

        else:
            words = self._comparison()
            if words:
                self.lb.delete(0, tk.END)
                for w in words:
                    self.lb.insert(tk.END, w)
            else:
                self.lb.delete(0, tk.END)
                self.lb.insert(tk.END, '(no match)')

    def _listbox_selection(self, event):
        """ Responds to a selection event on the listbox """

        if self.lb.get(tk.ACTIVE) == '(no match)':
            return

        if not self.lb.get(tk.ACTIVE):
            return

        if str(self.lb.cget('state')) == 'disabled':
            return

        self.entry_var.set(self.lb.get(tk.ACTIVE))
        self.list_var.set('')
        if self.list_method:
            self.list_method(event)

    def _comparison(self):
        """ Responsible for the pattern match from the entry value """

        if not self.case_sensitive:
            pattern_1 = re.compile('.*' + self.entry_var.get().upper() + '.*')
            pattern_2 = re.compile('.*' + self.entry_var.get().upper().replace(' ', '\u00a0') + '.*')
            index = []
            for i, name in enumerate(self.caps_full_list):
                if re.match(pattern_1, name) or re.match(pattern_2, name):
                    index.append(i)
        else:
            pattern_1 = re.compile('.*' + self.entry_var.get() + '.*')
            pattern_2 = re.compile('.*' + self.entry_var.get().replace(' ', '\u00a0') + '.*')
            index = []
            for i, name in enumerate(self.full_list):
                if re.match(pattern_1, name) or re.match(pattern_2, name):
                    index.append(i)

        result = [w for i, w in enumerate(self.full_list) if i in index]

        return result

    def set_list(self, new_list):
        """ Sets a new list for the listbox """
        self.entry_var.set('')
        self.full_list = new_list
        self.caps_full_list = [item.upper() for item in new_list]
        self.list_var.set(new_list)

    def get_list(self):
        return self.full_list

    def set_entry(self, new_value):
        """ Sets a value to the entry widget """
        if str(self.entry.cget('state')) == 'disabled':
            return
        self.entry_var.set(new_value)

    def set(self, new_value):
        """ Sets a value to the entry widget """
        self.set_entry(new_value)

    def get(self):
        """ Gets the current value from the entry widget """
        return self.entry_var.get()

    def disable(self):
        """ Style adjust for 'disabled' widgets """
        self.label.config(style='secondary.TLabel')
        self.set_entry('')
        self.entry.config(state='disabled', takefocus=0)
        self.lb.config(state='disabled', takefocus=0)

    def enable(self):
        """ Style adjust for 'normal' widgets """
        self.label.config(style='TLabel')
        self.entry.config(state='normal', takefocus=1)
        self.lb.config(state='normal', takefocus=1)


class AutocompleteCombobox(ttk.Frame):
    """
    Autocomplete Combobox Widget
    Filling the entry field filters the content from the combobox.
    Parameters:
        case_sensitive: whether the search shall be case sensitive
        all other parameters are the same as for a regular Combobox
    Methods for the user:
        set_list(new_list): sets a new list of values to the listbox widget
        set_entry(value): sets a value to the entry widget
        set(value): sets a value to the entry widget
        get(): gets the current value from the entry widget
        disable(): turns the whole widget 'off'
        enable(): turns the whole widget 'on'

    """

    def __init__(self, parent, case_sensitive=False, **kwargs):

        # Frame configuration
        super().__init__(parent)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Does not accept other variable to control the widget
        try:
            kwargs.pop('textvariable')
        except KeyError:
            pass

        # Values
        self.combo_list = kwargs.get('values', [])
        kwargs.pop('values')

        # Variable
        self.variable = tk.StringVar(value='')

        # Combobox
        self.combobox = ttk.Combobox(self, values=self.combo_list, state='normal', textvariable=self.variable, **kwargs)
        self.combobox.grid(row=0, column=0, sticky='nsew')

        # Bind method
        self.variable.trace('w', self._entry_changed)

        self.case_sensitive = case_sensitive

    def _entry_changed(self, name, index, mode):
        """ Keeps track of any change in the entry widget and updates the dropdown values """

        if self.variable.get() == '':
            self._set_filtered_values(values=self.combo_list)

        else:
            words = self._comparison()
            if words:
                self._set_filtered_values(values=words)
            else:
                self._set_filtered_values(values=['(no match)'])

    def _comparison(self):
        """ Responsible for the pattern match from the entry value """

        if not self.case_sensitive:
            pattern = re.compile('.*' + self.variable.get().upper() + '.*')
            index = []
            caps_values = [item.upper() for item in self.combo_list]
            for i, name in enumerate(caps_values):
                if re.match(pattern, name):
                    index.append(i)
        else:
            pattern = re.compile('.*' + self.variable.get() + '.*')
            index = []
            for i, name in enumerate(self.combo_list):
                if re.match(pattern, name):
                    index.append(i)

        result = [w for i, w in enumerate(self.combo_list) if i in index]

        return result

    def _set_filtered_values(self, values):
        self.combobox.config(values=values)

    def set_combo_values(self, values):
        self.combo_list = values
        self.combobox.config(values=values)

    def get_combo_values(self):
        return self.combo_list

    def set(self, new_value):
        """ Sets a value to the entry widget """
        if str(self.cget('state')) == 'disabled':
            return
        if new_value in self.combo_list:
            self.variable.set(new_value)
        else:
            self.variable.set('')

    def get(self):
        """ Gets the current value from the entry widget """
        return self.variable.get()

    def enable(self):
        self.combobox.config(state='normal', values=self.combo_list, takefocus=1)

    def disable(self):
        self.variable.set('')
        self.combobox.config(state='disabled', takefocus=0)


class AutocompleteLabelCombo(LabelCompoundWidget):
    """
    Autocomplete compound widget which combines an Label Widget and a Autocomplete Combobox
    Filling the entry field filters the content from the combobox.
    Parameters:
        case_sensitive: whether the search shall be case sensitive
        all other parameters are the same as for a regular Combobox
    Methods for the user:
        set_list(new_list): sets a new list of values to the listbox widget
        set_entry(value): sets a value to the entry widget
        set(value): sets a value to the entry widget
        get(): gets the current value from the entry widget
        disable(): turns the whole widget 'off'
        enable(): turns the whole widget 'on'

    """

    def __init__(self, parent, label_text='Label:', label_anchor='e', label_width=None,
                 label_justify=None, label_font=None, sided=True, combo_value='',
                 combo_list=('No values informed',), combo_width=None, combo_method=None,
                 case_sensitive=False, **kwargs):

        # Parent class initialization
        super().__init__(parent, label_text, label_anchor, label_width, label_justify, label_font, sided, **kwargs)

        # Combobox configuration
        if True:
            self.combo_list = combo_list
            self.case_sensitive = case_sensitive
            self.variable = tk.StringVar(value=combo_value)
            self.combobox = ttk.Combobox(self, textvariable=self.variable, justify='center',
                                         values=combo_list, state='normal')
            if sided:
                self.combobox.grid(row=0, column=1, sticky='nsew', padx=2)
            else:
                self.combobox.grid(row=1, column=0, sticky='nsew', padx=2, pady=(2, 0))

            if combo_width:
                self.combobox['width'] = combo_width

        # Bind method to the combobox
        if combo_method:
            self.combobox.bind('<<ComboboxSelected>>', combo_method, add='+')

        # Bind method
        self.variable.trace('w', self._entry_changed)

    def _entry_changed(self, name, index, mode):
        """ Keeps track of any change in the entry widget and updates the dropdown values """

        if self.variable.get() == '':
            self._set_filtered_values(values=self.combo_list)

        else:
            words = self._comparison()
            if words:
                self._set_filtered_values(values=words)
            else:
                self._set_filtered_values(values=['(no match)'])

    def _comparison(self):
        """ Responsible for the pattern match from the entry value """
        if not self.case_sensitive:
            pattern = re.compile('.*' + self.variable.get().upper() + '.*')
            index = []
            caps_values = [item.upper() for item in self.combo_list]
            for i, name in enumerate(caps_values):
                if re.match(pattern, name):
                    index.append(i)
        else:
            pattern = re.compile('.*' + self.variable.get() + '.*')
            index = []
            for i, name in enumerate(self.combo_list):
                if re.match(pattern, name):
                    index.append(i)

        result = [w for i, w in enumerate(self.combo_list) if i in index]

        return result

    def _set_filtered_values(self, values):
        self.combobox.config(values=values)

    def set_combo_values(self, values):
        self.combo_list = values
        self.combobox.config(values=values)

    def get_combo_values(self):
        return self.combo_list

    def get(self):
        current_value = self.variable.get()
        if current_value in self.combo_list:
            return current_value
        else:
            return ''

    def set(self, value):
        if str(self.combobox.cget('state')) == 'disabled':
            return
        if value in self.combo_list:
            self.variable.set(value)
        else:
            self.variable.set('')

    def enable(self):
        self.label.config(style='TLabel')
        self.combobox.config(state='normal', values=self.combo_list, takefocus=1)

    def disable(self):
        self.variable.set('')
        self.label.config(style='secondary.TLabel')
        self.combobox.config(state='disabled', takefocus=0)
