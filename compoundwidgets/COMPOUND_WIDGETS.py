import tkinter as tk
import ttkbootstrap as ttk
from .SCRIPTS import *


class LabelCombo(ttk.Frame):
    """
    Compound widget, with a label and a combobox within a frame.
    Parameters:
        parent: parent widget
        label_text: label text value
        label_anchor: anchor position for the text within the label
        label_width: minimum width of the label
        combo_value: initial value to show at the combobox (if any)
        combo_list: list of values to be shown at the combobox
        combo_width: combo box minimum width
        combo_method: method to associate when combobox is selected
        font: font to be used for the label
    Methods for the user:
        set(value): sets a value to the combobox widget
        get(): gets the current value from the combobox widget
        disable(): turns the whole widget 'off'
        enable(): turns the whole widget 'on'
        readonly(): turn the whole widget 'readonly' (non-editable)
        set_combo_values(values): sets the combobox values after it has been created
    """

    def __init__(self, parent,
                 label_text='Label:', label_anchor='e', label_width=None,
                 combo_value='', combo_list=('No values informed',), combo_width=None,
                 combo_method=None, font=None):

        # Parent class initialization
        super().__init__(parent)

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=0)

        # Label configuration
        if True:
            self.label = ttk.Label(self, text=label_text, anchor=label_anchor)
            self.label.grid(row=0, column=0, sticky='ew', padx=2)

            if label_width:
                self.label['width'] = label_width
            if font:
                self.label.config(font=font)

        # Combobox configuration
        if True:
            self.combo_list = combo_list
            self.variable = tk.StringVar(value=combo_value)
            self.combobox = ttk.Combobox(self, textvariable=self.variable, justify='center',
                                         values=combo_list, state='readonly')
            self.combobox.grid(row=0, column=1, sticky='ew', padx=2)

            if combo_width:
                self.combobox['width'] = combo_width

        # Bind method
        if combo_method:
            self.combobox.bind('<<ComboboxSelected>>', combo_method, add='+')

    def enable(self):
        self.label.config(style='TLabel')
        self.combobox.config(state='readonly', values=self.combo_list)

    def disable(self):
        self.variable.set('')
        self.label.config(style='secondary.TLabel')
        self.combobox.config(state='disabled')

    def readonly(self):
        self.label.config(style='TLabel')
        self.combobox.config(state='readonly', values=[])

    def get(self):
        return self.variable.get()

    def set(self, value):
        if str(self.combobox.cget('state')) == 'disabled':
            return
        if value in self.combo_list:
            self.variable.set(value)
        else:
            self.variable.set('')

    def set_combo_values(self, values):
        self.combo_list = values
        self.combobox.config(values=values)


class LabelEntry(ttk.Frame):
    """
    Create a compound widget, with a label and an entry field within a frame.
    Parameters:
        parent: parent widget
        label_text: label text value
        label_anchor: anchor position for the text within the label
        label_width: minimum width of the label
        entry_value: initial value to show at the entry (if any)
        entry_numeric: whether the entry accepts only numbers
        entry_width: entry width in number of characters
        entry_method: method to associate with the entry events
        entry_max_char: maximum number of characters in the entry field
        font: font to be used for the label and for the entry
    Methods for the user:
        set(value): sets a value to the entry widget
        get(): gets the current value from the entry widget
        disable(): turns the whole widget 'off'
        enable(): turns the whole widget 'on'
        readonly(): turn the whole widget 'readonly' (non-editable)
    """

    def __init__(self, parent,
                 label_text='label:', label_anchor='e', label_width=None,
                 entry_value='', entry_numeric=False, entry_width=None,
                 entry_max_char=None, entry_method=None, font=None, precision=2,
                 trace_variable=False):

        # Parent class initialization
        super().__init__(parent)

        # Entry validation for numbers
        validate_numbers = self.register(float_only)
        validate_chars = self.register(max_chars)
        self.entry_numeric = entry_numeric
        self.entry_max_chars = entry_max_char
        self.precision=precision
        self.trace_variable = trace_variable

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=0)

        # Label configuration
        if True:
            self.label = ttk.Label(self, text=label_text, anchor=label_anchor)
            self.label.grid(row=0, column=0, sticky='ew', padx=2)

            if label_width:
                self.label['width'] = label_width
            if font:
                self.label.config(font=font)

        # Entry configuration
        if True:
            self.variable = tk.StringVar(value=entry_value)
            self.entry = ttk.Entry(self, textvariable=self.variable, justify='center')
            self.entry.grid(row=0, column=1, sticky='ew', padx=2)

            if entry_width:
                self.entry['width'] = entry_width

            if font:
                self.entry.config(font=font)

            # Restrict numeric values
            if entry_numeric:
                if not isfloat(entry_value):
                    self.variable.set('')
                self.entry.config(validate='all', validatecommand=(validate_numbers, '%d', '%P', '%S', entry_max_char))

            # Restrict max characters
            if entry_max_char:
                entry_value = str(entry_value[:entry_max_char])
                self.variable.set(entry_value)
                self.entry.config(validate='all', validatecommand=(validate_chars, '%d', '%P', entry_max_char))

        # Bind method
        if True:
            if self.trace_variable:
                self.cb_name = self.variable.trace_add("write", self._update_value)
            self.entry_method = entry_method
            self.entry.bind("<FocusOut>", self._adjust_value, add='+')
            if self.entry_method:
                self.entry.bind("<Return>", self.entry_method, add='+')

    def _update_value(self, name, index, mode):
        if self.entry_method:
            self.entry.event_generate("<Return>")

    def _adjust_value(self, event):
        value = self.get()
        if isfloat(value):
            if self.trace_variable:
                self.variable.trace_remove('write', self.cb_name)
                self.variable.set("%0.*f" % (self.precision, float(value)))
                self.cb_name = self.variable.trace_add("write", self._update_value)
            else:
                self.variable.set("%0.*f" % (self.precision, float(value)))
        if self.entry_method:
            self.entry.event_generate("<Return>")

    def enable(self):
        self.label.config(style='TLabel')
        self.entry.config(state='normal')

    def disable(self):
        self.set('')
        self.label.config(style='secondary.TLabel')
        self.entry.config(state='disabled')

    def readonly(self):
        self.label.config(style='TLabel')
        self.entry.config(state='readonly')

    def get(self):
        return self.variable.get()

    def set(self, value):
        if str(self.entry.cget('state')) == 'disabled':
            return

        if self.entry_numeric:
            if value == '':
                if self.trace_variable:
                    self.variable.trace_remove('write', self.cb_name)
                    self.variable.set(value)
                    self.cb_name = self.variable.trace_add("write", self._update_value)
                else:
                    self.variable.set(value)
            elif isfloat(value):
                if self.trace_variable:
                    self.variable.trace_remove('write', self.cb_name)
                    self.variable.set("%0.*f" % (self.precision, float(value)))
                    self.cb_name = self.variable.trace_add("write", self._update_value)
                else:
                    self.variable.set("%0.*f" % (self.precision, float(value)))
            else:
                return

        else:
            if self.entry_max_chars:
                value = str(value)[:self.entry_max_chars]
            if self.trace_variable:
                self.variable.trace_remove('write', self.cb_name)
                self.variable.set(value)
                self.cb_name = self.variable.trace_add("write", self._update_value)
            else:
                self.variable.set(value)


class LabelText(ttk.Frame):
    """
    Compound widget, with a label and a text field within a frame.
    Parameters:
        parent: parent widget
        label_text: label text value
        label_anchor: anchor position for the text within the label
        label_width: minimum width of the label
        text_width: text width in number of characters
        text_height: text width in number of lines
        text_method: method to associate when the text widget loosed focus
        text_value: initial value to show at the text (if any)
        sided: True for label and text side by side, False for text below label
        font: font to be used for the label and for the text
    Methods for the user:
        set(text): sets a text to the text widget
        get(): gets the current text from the text widget
        disable(): turns the whole widget 'off'
        enable(): turns the whole widget 'on'
        readonly(): turn the whole widget 'readonly' (non-editable)
    """

    def __init__(self, parent,
                 label_text='label:', label_anchor='e', label_width=None,
                 text_value='', text_width=None, text_height=None, text_method=None,
                 sided=True, font=None):

        # Parent class initialization
        super().__init__(parent)

        # Frame configuration
        if True:
            if sided:
                self.rowconfigure(0, weight=1)
                self.columnconfigure(0, weight=0)
                self.columnconfigure(1, weight=1)
                self.columnconfigure(2, weight=0)
            else:
                self.rowconfigure(0, weight=0)
                self.rowconfigure(0, weight=1)
                self.columnconfigure(0, weight=1)
                self.columnconfigure(1, weight=0)

        # Label configuration
        if True:
            self.label = ttk.Label(self, text=label_text, anchor=label_anchor)

            if sided:
                self.label.grid(row=0, column=0, sticky='ne', padx=2, pady=2)
            else:
                self.label.grid(row=0, column=0, columnspan=2,
                                sticky='nsew', padx=2, pady=2)
            if label_width:
                self.label['width'] = label_width
            if font:
                self.label.config(font=font)

        # Text configuration
        if True:
            self.text = tk.Text(self, wrap=tk.WORD, spacing1=2, padx=2, pady=2)
            self.enabled_color = self.text.cget('fg')
            self.disabled_color = parent.winfo_toplevel().style.colors.secondary
            if sided:
                self.text.grid(row=0, column=1, sticky='nsew', padx=2, pady=2)
            else:
                self.text.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)

            if text_width:
                self.text['width'] = text_width
            if text_height:
                self.text['height'] = text_height
            if font:
                self.text.config(font=font)
            self.set(text_value)

        # Scroll bar for the text widget
        if True:
            y_scroll = ttk.Scrollbar(self, orient='vertical', command=self.text.yview)
            if sided:
                y_scroll.grid(row=0, column=2, sticky='ns')
            else:
                y_scroll.grid(row=1, column=1, sticky='ns')
            self.text.configure(yscrollcommand=y_scroll.set)
            self.text.bind('<MouseWheel>', self._on_mouse_wheel)
            y_scroll.bind('<MouseWheel>', self._on_mouse_wheel)

        # Bind method
        if text_method:
            self.text.bind("<FocusOut>", text_method, add='+')

    def _on_mouse_wheel(self, event):
        self.text.yview_scroll(int(-1 * event.delta / 120), 'units')

    def enable(self):
        self.label.config(style='TLabel')
        self.text.config(state='normal')
        self.text.config(fg=self.enabled_color)

    def disable(self):
        self.label.config(style='secondary.TLabel')
        self.set('')
        self.text.config(state='disabled')
        self.text.config(fg=self.disabled_color)

    def readonly(self):
        self.label.config(style='TLabel')
        self.text.config(state='disabled')
        self.text.config(fg=self.enabled_color)

    def get(self):
        return str(self.text.get('1.0', tk.END)).rstrip('\n')

    def set(self, value):
        if self.text.cget('fg') == self.disabled_color:
            return
        original_state = self.text.cget('state')
        self.text.config(state='normal')
        self.text.delete('1.0', tk.END)
        self.text.insert('1.0', value)
        self.text.config(state=original_state)


class LabelSpinbox(ttk.Frame):
    """
    Create a compound widget, with a label and a spinbox within a frame.
    Parameters:
        parent: parent widget
        label_text: label text value
        label_anchor: anchor position for the text within the label
        label_width: minimum width of the label
        entry_value: initial value to show at the entry (if any)
        entry_width: entry width in number of characters
        entry_method: method to associate with the entry events
        entry_type: whether the value will be a float or an integer
        spin_start: initial spinbox value
        spin_end: spinbox end_value
        spin_increment: spinbox increment
        spin_precision: number of decimal places to show for float type spinbox
    Methods for the user:
        set(value): sets a value to the spinbox widget
        get(): gets the current value from the spinbox widget
        disable(): turns the whole widget 'off'
        enable(): turns the whole widget 'on'
        readonly(): turn the whole widget 'readonly' (non-editable)
        """

    def __init__(self, parent,
                 label_text='label:', label_anchor='e', label_width=None,
                 entry_value=None, entry_width=None, entry_method=None, entry_type='float',
                 spin_start=0, spin_end=10, spin_increment=1, spin_precision=2,
                 font=None, trace_variable=False):

        # Parent class initialization
        super().__init__(parent)

        # Spinbox atributes initialization
        self.start = spin_start
        self.end = spin_end
        self.increment = spin_increment
        self.precision = spin_precision
        self.type = entry_type
        self.initial_value = entry_value
        self.trace_variable = trace_variable

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=0)

        # Label configuration
        if True:
            self.label = ttk.Label(self, text=label_text, anchor=label_anchor)
            self.label.grid(row=0, column=0, sticky='ew', padx=2)

            if label_width:
                self.label['width'] = label_width
            if font:
                self.label.config(font=font)

        # Spinbox configuration
        if True:
            if entry_value and str(entry_value):
                if isfloat(entry_value):
                    if self.start <= float(entry_value) <= self.end:
                        value = entry_value
                    else:
                        value = spin_start
                else:
                    value = spin_start
            else:
                if self.type == 'float':
                    value = spin_start
                else:
                    value = int(spin_start)
                    self.start = int(self.start)
                    self.end = int(self.end)
                    self.increment = int(self.increment)

            self.variable = tk.StringVar(value=str(value))

            self.spin = ttk.Spinbox(self, textvariable=self.variable, justify='center', command=self._spin_selected,
                                    from_=self.start, to=self.end, increment=self.increment)
            self.spin.grid(row=0, column=1, sticky='ew', padx=2)

            if entry_width:
                self.spin['width'] = entry_width
            if font:
                self.spin.config(font=font)

        # Bind method
        if True:
            if trace_variable:
                self.cb_name = self.variable.trace_add("write", self._update_value)
            self.entry_method = entry_method
            if self.entry_method:
                self.spin.bind("<Return>", entry_method, add='+')
                self.spin.bind("<FocusOut>", entry_method, add='+')

            self.spin.bind("<Return>", self._check_user_value, add='+')
            self.spin.bind("<FocusOut>", self._check_user_value, add='+')
            self.spin.bind("<<Increment>>", self._do_on_increment)
            self.spin.bind("<<Decrement>>", self._do_on_decrement)
            self.spin.bind("<ButtonRelease-1>", self._spin_selected, add='+')

    def _update_value(self, name, index, mode):
        if self.entry_method:
            self.spin.event_generate("<Return>")

    def _spin_selected(self, event=None):
        self._check_user_value()
        self.spin.event_generate('<Return>')

    def _do_on_increment(self, event=None):
        self._do_upon_clicking_arrows("up")
        return "break"

    def _do_on_decrement(self, event=None):
        self._do_upon_clicking_arrows("down")
        return "break"

    def _do_upon_clicking_arrows(self, direction):

        if direction == 'up':
            if self.type == 'float':
                if float(self.get()) >= self.end:
                    value = self.end
                else:
                    value = min(float(self.end), float(self.get()) + self.increment)
                self.set(float(value))

            else:
                if int(self.get()) >= self.end:
                    value = self.end
                else:
                    value = min(self.end, int(self.get()) + self.increment)
                self.set(int(value))

        else:
            if self.type == 'float':
                if float(self.get()) <= self.start:
                    value = self.start
                else:
                    value = max(float(self.start), float(self.get()) - self.increment)
                self.set(float(value))

            else:
                if int(self.get()) <= self.start:
                    value = self.start
                else:
                    value = max(self.start, int(self.get()) - self.increment)
                self.set(int(value))

    def _check_user_value(self, event=None):
        self.update()
        try:
            current = float(self.variable.get().replace(',', '.'))
        except ValueError:
            current = float(self.start)

        if current < self.start:
            current = self.start
        elif current > self.end:
            current = self.end

        if self.type == 'int':
            self.set(str(int(current)))
        else:
            self.set(str(current))

    def enable(self):
        self.label.config(style='TLabel')
        self.spin.config(state='normal')

        if not str(self.get()):
            if self.initial_value is not None:
                self.set(self.initial_value)
            else:
                self.set(self.start)
            self._check_user_value()

    def disable(self):
        self.set('')
        self.label.config(style='secondary.TLabel')
        self.spin.config(state='disabled')

    def readonly(self):
        self.label.config(style='TLabel')
        self.spin.config(state='readonly')

    def get(self):
        return self.variable.get()

    def set(self, value):
        if value in (None, ''):
            new_value = self.start

        elif isfloat(value):
            value = float(value)
            if value < self.start:
                new_value = self.start
            elif value > self.end:
                new_value = self.end
            else:
                new_value = value

        else:
            new_value = self.start

        if self.type == 'int':
            value = str(int(new_value))
        else:
            value = str(round(float(new_value), self.precision))

        if self.trace_variable:
            self.variable.trace_remove('write', self.cb_name)
            self.variable.set(value)
            self.cb_name = self.variable.trace_add("write", self._update_value)
        else:
            self.variable.set(value)


class LabelEntryUnit (ttk.Frame):
    """
    Compound widget, with a label, an entry field, and a combobox with applicable units (metric and imperial).
    Parameters:
        parent: parent widget
        label_text: label text value
        label_anchor: anchor position for the text within the label
        label_width: minimum width of the label
        entry_value: initial value to show at the entry (if any)
        entry_width: entry width in number of characters
        entry_method: method to associate with the entry events
        combobox_unit: unit system for the entry
        combobox_unit_width: width of the combobox in characters
        combobox_unit_conversion: boolean, if set to True converts the entry value when the unit is changed
        font: font to be used in the label and for the entry
        precision: number of decimal points to show to the user
    Methods for the user:
        disable(): turns the whole widget 'off'
        enable(): turns the whole widget 'on'
        readonly(): turn the whole widget 'readonly' (non-editable)
        lock_unit(): does not allow the unit combobox to change
        unlock_unit(): unlocks the unit combobox allowing change
        activate_self_conversion(): turns the widget in a unit converter
        deactivate_self_conversion(): deactivates the conversion feature

        get_entry(): gets the current value from the entry widget only
        set_entry(value): sets a value to the entry widget only
        get_unit(): gets the current value from the unit combobox only
        set_unit(value): sets a value to the unit combobox only
        get(): gets the current value and current unit
        set(value, unit): sets a value and an unit

        get_metric_value(): gets the current value and unit converted to the equivalent metric unit
        get_imperial_value(): gets the current value and unit converted to the equivalent imperial unit
        convert_to_metric(): converts the current shown value to the equivalent metric unit
        convert_to_imperial(): converts the current shown value to the equivalent imperial unit

        (almost) Static Methods: return (Value, Unit)
        convert_data_to_metric(value, unit): converts the given pair to the equivalent metric unit
        convert_data_to_imperial(value, unit): converts the given pair to the equivalent imperial unit
        convert_to_given_unit((old_value, old_unit), new_unit): converts the given pair to the given unit
    Internal Classes:
        NoUnitCombo: ('-')
        TemperatureCombo: ('°C', '°F')
        LengthCombo: ('mm', 'cm', 'm', 'in')
        AreaCombo: ('mm²', 'cm²', 'm²', 'in²')
        PressureCombo: ('kPa', 'bar', 'kgf/cm²', 'MPa', 'atmosphere', 'ksi', 'psi')
        StressCombo: ('MPa', 'GPa', 'x10³ ksi', 'psi', 'ksi')
        ForceCombo: ('N', 'kN', 'kgf', 'lbf')
        MomentCombo: ('N.m', 'kN.m', 'kgf.m', 'lbf.ft')
        EnergyCombo: ('joule', 'ft-lbf')
        ToughnessCombo: ('MPa.√m', 'N/mm^(3/2)', 'ksi.√in')
        JIntegralCombo: ('joule/m²', 'ft-lbf/ft²')
        ThermalExpansionCombo: ('10e-6/°C', '10e-6/°F')
    """

    class NoUnitCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('-',)
            self.variable = tk.StringVar(value='-')
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

    class TemperatureCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('°C', '°F')
            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

    class LengthCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('mm', 'cm', 'm', 'in')
            self.conversion_values = (1, 10, 1000, 25.4)

            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

    class AreaCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('mm²', 'cm²', 'm²', 'in²')
            self.conversion_values = (1, 100, 1000000, 645.16)

            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

    class PressureCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('kPa', 'bar', 'kgf/cm²', 'MPa', 'atmosphere', 'ksi', 'psi')
            self.conversion_values = (1, 100, 98.0665, 1000, 101.325, 689.4757, 6.894757)

            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

    class StressCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('MPa', 'GPa', 'x10³ ksi', 'psi', 'ksi')
            self.conversion_values = (1, 1000, 6894.757, 0.006894757, 6.894757)
            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

    class ForceCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('N', 'kN', 'kgf', 'lbf')
            self.conversion_values = (1, 1000, 9.80665, 4.448222)
            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

    class MomentCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('N.m', 'kN.m', 'kgf.m', 'lbf.ft')
            self.conversion_values = (1, 1000, 9.80665, 1.35582)
            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

    class EnergyCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('joule', 'ft-lbf')
            self.conversion_values = (1, 1.355818)
            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

    class ToughnessCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('MPa.√m', 'N/mm^(3/2)', 'ksi.√in')
            self.conversion_values = (1, 0.031621553, 1.0988015)
            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

    class JIntegralCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('joule/m²', 'ft-lbf/ft²')
            self.conversion_values = (1, 14.5939)
            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

    class ThermalExpansionCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('10e-6/°C', '10e-6/°F')
            self.conversion_values = (1, 0.55556)
            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

    # Dictionary that correlates the desired unit to the appropriate class
    unit_dict = {
        'none': NoUnitCombo,
        'temperature': TemperatureCombo,
        'length': LengthCombo,
        'area': AreaCombo,
        'pressure': PressureCombo,
        'stress': StressCombo,
        'force': ForceCombo,
        'moment': MomentCombo,
        'energy': EnergyCombo,
        'toughness': ToughnessCombo,
        'j-integral': JIntegralCombo,
        'thermal expansion': ThermalExpansionCombo
    }

    # List which identifies unit as SI or Custom. Their position in list guides its conversion units.
    metric_unit_list = \
        ('mm', 'cm',  'm',          # LengthCombo
         'mm²', 'cm²', 'm²',        # AreaCombo
         'kPa', 'kPa', 'bar', 'kgf/cm²', 'MPa', 'atmosphere',  # PressureCombo
         'GPa',                     # StressCombo
         'N', 'kN', 'kgf',          # ForceCombo
         'N.m', 'kN.m', 'kgf.m',    # MomentCombo
         '-',                       # NoUnitCombo
         'N/mm^(3/2)', 'MPa.√m',    # ToughnessCombo
         'joule',                   # EnergyCombo
         'joule/m²',                # JIntegralCombo
         '10e-6/°C',                # Thermal Expansion
         )
    imperial_unit_list = \
        ('in', 'in', 'in',
         'in²', 'in²', 'in²',
         'psi', 'ksi', 'ksi', 'ksi', 'ksi', 'psi',
         'x10³ ksi',
         'lbf', 'lbf', 'lbf',
         'lbf.ft', 'lbf.ft', 'lbf.ft',
         '-',
         'ksi.√in', 'ksi.√in',
         'ft-lbf',
         'ft-lbf/ft²',
         '10e-6/°F')

    # List with the conversion values from imperial to metric
    conversion = \
        (25.4, 2.54, 0.0254,
         645.16, 6.4516, 0.00064516,
         6.894757, 6894.757, 68.94757, 70.30696, 6.894757, 0.06804596,
         6.894757e6,
         4.448222, 0.004448222, 0.4535924,
         1.35582, 0.00135582, 0.1382552,
         1,
         34.7485, 1.0988,
         1.355818,
         14.5939,
         0.55556)

    # imperial_unit_list[index] * conversion[index] => metric_unit_list[index]

    def __init__(self, parent,
                 label_text='Label:', label_anchor='e', label_width=None,
                 entry_value='', entry_width=None, entry_method=None,
                 combobox_unit=None, combobox_unit_width=8, combobox_unit_conversion=False,
                 font=None, precision=2, trace_variable=False):

        # Parent class initialization
        super().__init__(parent)

        # Entry validation for numbers
        validate_numbers = self.register(float_only)

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=0)
            self.columnconfigure(2, weight=0)

        # Label configuration
        if True:
            self.label = ttk.Label(self, text=label_text, anchor=label_anchor)
            self.label.grid(row=0, column=0, sticky='ew', padx=2)

            if label_width:
                self.label['width'] = label_width
            if font:
                self.label.config(font=font)

        # Entry configuration
        if True:
            self.precision = precision
            self.trace_variable = trace_variable
            self.entry_variable = tk.StringVar(value=entry_value)
            self.entry = ttk.Entry(self, textvariable=self.entry_variable, justify='center')
            self.entry.grid(row=0, column=1, sticky='ew', padx=2)

            if entry_width:
                self.entry['width'] = entry_width

            if font:
                self.entry.config(font=font)

            # Restrict numeric values
            if True:
                if not isfloat(entry_value):
                    self.entry_variable.set('')
                self.entry.config(validate='all', validatecommand=(validate_numbers, '%d', '%P', '%S'))

        # Unit combobox configuration
        if True:
            if not combobox_unit:
                combobox_unit = 'none'

            local_class = LabelEntryUnit.unit_dict.get(combobox_unit.lower(), None)
            if not local_class:
                raise Exception('Unit not found in current units dictionary.')

            self.combobox_unit_conversion = combobox_unit_conversion
            self.combobox_unit_width = combobox_unit_width
            self.unit_combo = local_class(self, self.combobox_unit_width)
            self.unit_combo.grid(row=0, column=2, sticky='ew', padx=2)
            self.last_unit = self.unit_combo.values[0]
            self.combobox_variable = self.unit_combo.variable
            self.is_locked = False

        # Bind methods
        if True:
            if self.trace_variable:
                self.cb_name = self.entry_variable.trace_add("write", self._update_value)
            self.entry_method = entry_method
            self.entry.bind("<FocusOut>", self._adjust_value)
            if self.entry_method:
                self.entry.bind("<Return>", self.entry_method, add='+')

            if not self.combobox_unit_conversion:
                self.unit_combo.bind("<<ComboboxSelected>>", entry_method, add='+')
            else:
                self.unit_combo.bind("<<ComboboxSelected>>", self._convert_to_selected_unit, add='+')

    def _update_value(self, name, index, mode):
        if self.entry_method:
            self.entry.event_generate("<Return>")

    def _adjust_value(self, event):
        value = self.get_entry()
        if isfloat(value):
            if self.trace_variable:
                self.entry_variable.trace_remove('write', self.cb_name)
                self.entry_variable.set("%0.*f" % (self.precision, float(value)))
                self.cb_name = self.entry_variable.trace_add("write", self._update_value)
            else:
                self.entry_variable.set("%0.*f" % (self.precision, float(value)))
        if self.entry_method:
            self.entry.event_generate("<Return>")

    # Widget state methods ---------------------------------------------------------------------------------------------
    def enable(self):
        self.unlock_unit()
        self.label.config(style='TLabel')
        self.entry.config(state='normal')
        self.unit_combo.config(state='readonly', values=self.unit_combo.values)

    def disable(self):
        self.unlock_unit()

        self.set_entry('')
        self.combobox_variable.set('')
        self.label.config(style='secondary.TLabel')
        self.entry.config(state='disabled')
        self.unit_combo.config(state='disabled')

    def readonly(self):
        self.unlock_unit()
        self.label.config(style='TLabel')
        self.entry.config(state='readonly')
        if not self.combobox_unit_conversion:
            self.unit_combo.config(state='readonly', values=[])
        else:
            self.unit_combo.config(state='readonly', values=self.unit_combo.values)

    def lock_unit(self):
        if not self.get_unit():
            return
        self.unit_combo.config(state='readonly', values=[], style='TLabel',
                               width=self.combobox_unit_width+4)
        self.is_locked = True

    def unlock_unit(self):
        self.unit_combo.config(state='readonly', values=self.unit_combo.values, style='TCombobox',
                               width=self.combobox_unit_width)
        self.is_locked = False

    def activate_self_conversion(self):
        self.unlock_unit()
        self.enable()
        self.entry.config(state='readonly')
        self.combobox_unit_conversion = True
        if self.entry_method:
            self.unit_combo.unbind("<<ComboboxSelected>>")
        self.unit_combo.bind("<<ComboboxSelected>>", self._convert_to_selected_unit)

    def deactivate_self_conversion(self):
        self.enable()
        self.combobox_unit_conversion = False
        self.unit_combo.unbind("<<ComboboxSelected>>")
        if self.entry_method:
            self.unit_combo.bind("<<ComboboxSelected>>", self.entry_method)

    # Widget set and get methods ---------------------------------------------------------------------------------------
    def get_entry(self):
        return self.entry_variable.get()

    def set_entry(self, value):
        if str(self.entry.cget('state')) == 'disabled':
            return

        if value == '':
            if self.trace_variable:
                self.entry_variable.trace_remove('write', self.cb_name)
                self.entry_variable.set(value)
                self.cb_name = self.entry_variable.trace_add("write", self._update_value)
            else:
                self.entry_variable.set(value)
            return
        elif not(isfloat(value)):
            return

        else:
            if self.trace_variable:
                self.entry_variable.trace_remove('write', self.cb_name)
                self.entry_variable.set("%0.*f" % (self.precision, float(value)))
                self.cb_name = self.entry_variable.trace_add("write", self._update_value)
            else:
                self.entry_variable.set("%0.*f" % (self.precision, float(value)))

    def get_unit(self):
        return self.combobox_variable.get()

    def set_unit(self, unit):
        if str(self.unit_combo.cget('state')) == 'disabled':
            return

        if self.is_locked:
            return

        if unit in list(self.unit_combo.values):
            self.combobox_variable.set(unit)
            self.last_unit = unit
        else:
            self.combobox_variable.set(self.unit_combo.values[0])
            self.last_unit = self.unit_combo.values[0]

    def get(self):
        return self.get_entry(), self.get_unit()

    def set(self, value, unit=None):
        self.set_entry(value)
        if unit:
            self.set_unit(unit)

    # Widget conversion methods ----------------------------------------------------------------------------------------
    def get_metric_value(self):
        """
        Returns the current value converted to the equivalent metric unit.
        The selected metric unit is the first from the combobox values.
        """

        if isinstance(self.unit_combo, LabelEntryUnit.NoUnitCombo):
            return self.get_entry(), '-'

        if isinstance(self.unit_combo, LabelEntryUnit.TemperatureCombo):
            if str(self.get_unit()) == '°F':
                if not self.get_entry():
                    return '', '°C'
                else:
                    return 5 * (float(self.get_entry()) - 32) / 9, '°C'
            return self.get_entry(), '°C'

        index = self.unit_combo.values.index(self.get_unit())
        if not self.get_entry():
            return '', self.unit_combo.values[0]
        else:
            return float(self.get_entry()) * self.unit_combo.conversion_values[index], self.unit_combo.values[0]

    def get_imperial_value(self):
        """
        Returns the current value converted to the equivalent imperial unit.
        The selected imperial unit is the last from the combobox values.
        """

        if isinstance(self.unit_combo, LabelEntryUnit.NoUnitCombo):
            return self.get_entry(), '-'

        if isinstance(self.unit_combo, LabelEntryUnit.TemperatureCombo):
            if str(self.get_unit()) == '°C':
                if not self.get_entry():
                    return '', '°F'
                else:
                    return 9 * float(self.get_entry())/5 + 32, '°F'
            return self.get_entry(), '°F'

        index = self.unit_combo.values.index(self.get_unit())
        if not self.get_entry():
            return '', self.unit_combo.values[-1]
        else:
            last_value = self.get_entry()
            intermediary_value = float(last_value) * self.unit_combo.conversion_values[index]
            new_value = intermediary_value / self.unit_combo.conversion_values[-1]
            return new_value, self.unit_combo.values[-1]

    def convert_to_metric(self):
        """ Convert 'self' to metric """
        if self.is_locked:
            return
        new_value, new_unit = self.get_metric_value()
        self.set(new_value, new_unit)

    def convert_to_imperial(self):
        """ Convert 'self' to imperial """
        if self.is_locked:
            return
        new_value, new_unit = self.get_imperial_value()
        self.set(new_value, new_unit)

    @staticmethod
    def convert_data_to_metric(value, unit):
        """
        Convert any given data (value, unit) to metric.
        Uses the main conversion lists for the operation.
        """

        if unit == '-':
            return None, None

        elif unit == '°F':
            if not value:
                new_value = ''
            else:
                new_value = 5 * (float(value) - 32) / 9
            return new_value, '°C'

        else:
            if unit not in LabelEntryUnit.metric_unit_list:
                index = LabelEntryUnit.imperial_unit_list.index(unit)
                if not value:
                    new_value = ''
                else:
                    new_value = float(value)*LabelEntryUnit.conversion[index]
                return new_value, LabelEntryUnit.metric_unit_list[index]
            return value, unit

    @staticmethod
    def convert_data_to_imperial(value, unit):
        """
        Convert any given data (value, unit) to imperial.
        Uses the main conversion lists for the operation.
        """
        if unit == '-':
            return None, None

        elif unit == '°C':
            if not value:
                new_value = ''
            else:
                new_value = 9 * (float(value) / 5) + 32
            return new_value, '°F'

        else:
            if unit not in LabelEntryUnit.imperial_unit_list:
                index = LabelEntryUnit.metric_unit_list.index(unit)
                if not value:
                    new_value = ''
                else:
                    new_value = float(value) / LabelEntryUnit.conversion[index]
                return new_value, LabelEntryUnit.imperial_unit_list[index]
            return value, unit

    def convert_to_given_unit(self, old_data, given_unit):
        """
        Method to convert a given data to a new unit.
        """

        last_value = old_data[0]
        last_unit = old_data[1]
        new_unit = given_unit

        if isinstance(self.unit_combo, LabelEntryUnit.NoUnitCombo):
            return last_value, last_unit

        elif isinstance(self.unit_combo, LabelEntryUnit.TemperatureCombo):
            if last_unit == new_unit:
                return last_value, last_unit

            else:
                if new_unit == '°F':
                    if not last_value:
                        new_value = ''
                    else:
                        new_value = 9 * (float(last_value) / 5) + 32
                    return new_value, '°F'
                else:
                    if not last_value:
                        new_value = ''
                    else:
                        new_value = 5 * (float(last_value) - 32) / 9
                    return new_value, '°C'

        else:
            if last_unit == new_unit:
                return last_value, last_unit

            else:
                old_index = self.unit_combo.values.index(last_unit)
                new_index = self.unit_combo.values.index(new_unit)
                if not last_value:
                    new_value = ''
                else:
                    # Convert from old index to index 1
                    intermediary_value = float(last_value) * self.unit_combo.conversion_values[old_index]

                    # Convert from index 1 to new index
                    new_value = intermediary_value / self.unit_combo.conversion_values[new_index]

                return new_value, new_unit

    def _convert_to_selected_unit(self, event=None):
        """
        Method to convert the value everytime a unit is changed.
        """

        last_value = self.get_entry()
        new_unit = self.get_unit()
        last_unit = self.last_unit

        if isinstance(self.unit_combo, LabelEntryUnit.NoUnitCombo):
            pass

        elif isinstance(self.unit_combo, LabelEntryUnit.TemperatureCombo):
            if last_unit == new_unit:
                pass
            else:
                if new_unit == '°F':
                    if not last_value:
                        new_value = ''
                    else:
                        new_value = 9 * (float(last_value) / 5) + 32
                    self.last_unit = '°F'
                    self.set(new_value, '°F')
                else:
                    if not last_value:
                        new_value = ''
                    else:
                        new_value = 5 * (float(last_value) - 32) / 9
                    self.last_unit = '°C'
                    self.set(new_value, '°C')

        else:
            if last_unit == new_unit:
                pass
            else:
                old_index = self.unit_combo.values.index(last_unit)
                new_index = self.unit_combo.values.index(new_unit)
                if not last_value:
                    new_value = ''
                else:
                    # Convert from old index to index 1
                    intermediary_value = float(last_value) * self.unit_combo.conversion_values[old_index]

                    # Convert from index 1 to new index
                    new_value = intermediary_value / self.unit_combo.conversion_values[new_index]

                self.last_unit = new_unit
                self.set(new_value, new_unit)


class LabelEntryButton (ttk.Frame):
    """
    Create a compound widget, with a label, an entry field and a button within a frame.
    Input:
        parent: parent widget
        label_text: label text value
        label_anchor: anchor position for the text within the label
        label_width: minimum width of the label
        entry_value: initial value to show at the entry (if any)
        entry_numeric: whether the entry accepts only numbers
        entry_width: entry width in number of characters
        entry_method: method to associate with the entry events
        entry_max_char: maximum number of characters in the entry field
        button_text: string to be shown on the button
        button_width: width of the button in characters
        button_method: method to bind to the button
        font: font to be used for the label, the entry and the button
    Methods for the user:
        set(value): sets a value to the entry widget
        get(): gets the current value from the entry widget
        disable(): turns the whole widget 'off'
        enable(): turns the whole widget 'on'
        readonly(): turn the whole widget 'readonly' (non-editable)
    """

    def __init__(self, parent,
                 label_text='label:', label_anchor='e', label_width=None,
                 entry_value='', entry_numeric=False, entry_width=None,
                 entry_max_char=None, entry_method=None,
                 button_text='', button_width=None, button_method=None,
                 font=None, precision=2, trace_variable=False):

        # Parent class initialization
        super().__init__(parent)

        # Entry validation for numbers
        validate_numbers = self.register(float_only)
        validate_chars = self.register(max_chars)
        self.entry_numeric = entry_numeric
        self.entry_max_chars = entry_max_char
        self.precision = precision
        self.trace_variable = trace_variable

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=0)
            self.columnconfigure(2, weight=0)

        # Label configuration
        if True:
            self.label = ttk.Label(self, text=label_text, anchor=label_anchor)
            self.label.grid(row=0, column=0, sticky='ew', padx=2)

            if label_width:
                self.label['width'] = label_width
            if font:
                self.label.config(font=font)

        # Entry configuration
        if True:
            self.variable = tk.StringVar(value=entry_value)
            self.entry = ttk.Entry(self, textvariable=self.variable, justify='center')
            self.entry.grid(row=0, column=1, sticky='ew', padx=2)

            if entry_width:
                self.entry['width'] = entry_width

            if font:
                self.entry.config(font=font)

            # Restrict numeric values
            if entry_numeric:
                if not isfloat(entry_value):
                    self.variable.set('')
                self.entry.config(validate='all', validatecommand=(validate_numbers, '%d', '%P', '%S', entry_max_char))

            # Restrict max characters
            elif entry_max_char:
                entry_value = str(entry_value[:entry_max_char])
                self.variable.set(entry_value)
                self.entry.config(validate='all', validatecommand=(validate_chars, '%d', '%P', entry_max_char))

        # Button configuration
        if True:
            self.button = ttk.Button(self, text=button_text, width=button_width)
            self.button.grid(row=0, column=2, sticky='ew', padx=2)

        # Bind methods
        if True:
            self.button_method = button_method
            if button_method:
                self.button.configure(command=button_method)
            if self.trace_variable:
                self.cb_name = self.variable.trace_add("write", self._update_value)
            self.entry_method = entry_method
            self.entry.bind("<FocusOut>", self._adjust_value, add='+')
            if entry_method:
                self.entry.bind("<Return>", entry_method)

    def _update_value(self, name, index, mode):
        if self.entry_method:
            self.entry.event_generate("<Return>")

    def _adjust_value(self, event):
        value = self.get()
        if isfloat(value):
            if self.trace_variable:
                self.variable.trace_remove('write', self.cb_name)
                self.variable.set("%0.*f" % (self.precision, float(value)))
                self.cb_name = self.variable.trace_add("write", self._update_value)
            else:
                self.variable.set("%0.*f" % (self.precision, float(value)))
        if self.entry_method:
            self.entry.event_generate("<Return>")

    def enable(self):
        self.label.config(style='TLabel')
        self.entry.config(state='normal')
        self.button.state(["!disabled"])

    def disable(self):
        self.set('')
        self.label.config(style='secondary.TLabel')
        self.entry.config(state='disabled')
        self.button.state(["disabled"])

    def readonly(self):
        self.label.config(style='TLabel')
        self.entry.config(state='readonly')
        self.button.state(["!disabled"])

    def get(self):
        return self.variable.get()

    def set(self, value):
        if str(self.entry.cget('state')) == 'disabled':
            return
        if self.entry_numeric:
            if value == '':
                if self.trace_variable:
                    self.variable.trace_remove('write', self.cb_name)
                    self.variable.set(value)
                    self.cb_name = self.variable.trace_add("write", self._update_value)
                else:
                    self.variable.set(value)
            elif isfloat(value):
                if self.trace_variable:
                    self.variable.trace_remove('write', self.cb_name)
                    self.variable.set("%0.*f" % (self.precision, float(value)))
                    self.cb_name = self.variable.trace_add("write", self._update_value)
                else:
                    self.variable.set("%0.*f" % (self.precision, float(value)))
            else:
                return

        else:
            if self.entry_max_chars:
                value = str(value)[:self.entry_max_chars]
            if self.trace_variable:
                self.variable.trace_remove('write', self.cb_name)
                self.variable.set(value)
                self.cb_name = self.variable.trace_add("write", self._update_value)
            else:
                self.variable.set(value)


class LabelComboButton (ttk.Frame):
    """
    Create a compound widget, with a label, a combobox and a button within a ttk Frame.
    Input:
        parent: parent widget
        label_text: label text value
        label_anchor: anchor position for the text within the label
        label_width: minimum width of the label
        combo_value: initial value to show at the combo box (if any)
        combo_list: list of values to be shown at the combobox
        combo_width: combobox width in number of characters
        combo_method: method to associate when combobox is selected
        button_text: string to be shown on the button
        button_width: width of the button in characters
        button_method: method to bind to the button
        font: font to be used for the label, the entry and the button
    Methods for the user:
        set(value): sets a value to the entry widget
        get(): gets the current value from the entry widget
        disable(): turns the whole widget 'off'
        enable(): turns the whole widget 'on'
        readonly(): turn the whole widget 'readonly' (non-editable)
        set_combo_values(values): sets the combobox values after it has been created
    """

    def __init__(self, parent,
                 label_text='Label:', label_anchor='e', label_width=None,
                 combo_value='', combo_list=('No values informed',), combo_width=None, combo_method=None,
                 button_text='', button_width=None, button_method=None,
                 font=None):

        # Parent class initialization
        super().__init__(parent)

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=0)
            self.columnconfigure(2, weight=0)

        # Label configuration
        if True:
            self.label = ttk.Label(self, text=label_text, anchor=label_anchor)
            self.label.grid(row=0, column=0, sticky='ew', padx=2)

            if label_width:
                self.label['width'] = label_width
            if font:
                self.label.config(font=font)

        # Combobox configuration
        if True:
            self.combo_list = combo_list
            self.variable = tk.StringVar(value=combo_value)
            self.combobox = ttk.Combobox(self, textvariable=self.variable, justify='center',
                                         values=combo_list, state='readonly')
            self.combobox.grid(row=0, column=1, sticky='ew', padx=2)

            if combo_width:
                self.combobox['width'] = combo_width

        # Button configuration
        if True:
            self.button = ttk.Button(self, text=button_text, width=button_width)
            self.button.grid(row=0, column=2, sticky='ew', padx=2)

        # Bind methods
        if combo_method:
            self.combobox.bind('<<ComboboxSelected>>', combo_method, add='+')
        if button_method:
            self.button.configure(command=button_method)

    def enable(self):
        self.label.config(style='TLabel')
        self.combobox.config(state='readonly', values=self.combo_list)
        self.button.state(["!disabled"])

    def disable(self):
        self.variable.set('')
        self.label.config(style='secondary.TLabel')
        self.combobox.config(state='disabled')
        self.button.state(["disabled"])

    def readonly(self):
        self.label.config(style='TLabel')
        self.combobox.config(state='readonly', values=[])
        self.button.state(["!disabled"])

    def get(self):
        return self.variable.get()

    def set(self, value):
        if str(self.combobox.cget('state')) == 'disabled':
            return
        if value in self.combo_list:
            self.variable.set(value)
        else:
            self.variable.set('')

    def set_combo_values(self, values):
        self.combo_list = values
        self.combobox.config(values=values)