import tkinter as tk
import ttkbootstrap as ttk
from .SCRIPTS import *


class LabelCompoundWidget(ttk.Frame):
    """
    Compound Widget base Widget
    Other widgets will combine the Label widget with other input widgets.
    Parameters:
        parent: parent widget
        label_text: label text string
        label_anchor: anchor position for the text within the label
        label_width: minimum width of the label
        label_justify: multiline string alignment
        label_font: font to be used for the label
        sided: whether the label and the widget are positioned on the same line vs. in the same column
    """

    def __init__(self, parent, label_text='Label:', label_anchor='e', label_width=None,
                 label_justify=None, label_font=None, sided=True, **kwargs):

        # Parent class initialization
        super().__init__(parent, **kwargs)

        # Frame configuration
        if True:
            self.sided = sided
            if self.sided:
                self.rowconfigure(0, weight=1)
                self.columnconfigure(0, weight=1)
                self.columnconfigure(1, weight=0)
            else:
                self.rowconfigure(0, weight=1)
                self.rowconfigure(1, weight=1)
                self.columnconfigure(0, weight=1)

        # Label configuration
        if True:
            self.label = ttk.Label(self, text=label_text, anchor=label_anchor)
            self.label.grid(row=0, column=0, sticky='nsew', padx=2)

            if label_width:
                self.label['width'] = label_width
            if label_font:
                self.label.config(font=label_font)
            if label_justify:
                self.label.config(justify=label_justify)

        # Additional configuration: no label text
        if not label_text:
            self.set_label_text(label_text)

    def set_label_text(self, label_text):
        """ Sets a new string to the label """

        if not label_text:
            self.label.grid_remove()
            if self.sided:
                self.columnconfigure(0, weight=0)
            else:
                self.rowconfigure(0, weight=0)
        else:
            self.label.grid()
            self.label.config(text=label_text)
            if self.sided:
                self.columnconfigure(0, weight=1)
            else:
                self.rowconfigure(0, weight=1)


class LabelCombo(LabelCompoundWidget):
    """
    Compound widget, with a label and a combobox within a frame.
    Base frame and label widget inherited from LabelCompoundWidget.
    Specific Parameters:
        combo_value: initial value to show at the combobox (if any)
        combo_list: list of values to be shown at the combobox
        combo_width: combo box minimum width
        combo_method: method to associate when combobox is selected
    Methods for the user:
        enable(): turns the whole widget 'on'
        disable(): turns the whole widget 'off'
        readonly(): turn the whole widget 'readonly' (non-editable)
        get(): returns the current value from the combobox widget
        set(value): sets a value to the combobox widget
        get_combo_values: return the current available values form the combobox
        set_combo_values(values): sets the combobox values after it has been created
    """

    def __init__(self, parent, label_text='Label:', label_anchor='e', label_width=None,
                 label_justify=None, label_font=None, sided=True,
                 combo_value='', combo_list=('No values informed',), combo_width=None, combo_method=None, **kwargs):

        # Parent class initialization
        super().__init__(parent, label_text, label_anchor, label_width, label_justify, label_font, sided, **kwargs)

        # Combobox configuration
        if True:
            self.combo_list = combo_list
            self.variable = tk.StringVar(value=combo_value)
            self.combobox = ttk.Combobox(self, textvariable=self.variable, justify='center',
                                         values=combo_list, state='readonly')
            if sided:
                self.combobox.grid(row=0, column=1, sticky='nsew', padx=2)
            else:
                self.combobox.grid(row=1, column=0, sticky='nsew', padx=2, pady=(2, 0))

            if combo_width:
                self.combobox['width'] = combo_width

        # Bind method to the combobox
        if combo_method:
            self.combobox.bind('<<ComboboxSelected>>', combo_method, add='+')

    def enable(self):
        self.label.config(style='TLabel')
        self.combobox.config(state='readonly', values=self.combo_list, takefocus=1)

    def disable(self):
        self.variable.set('')
        self.label.config(style='secondary.TLabel')
        self.combobox.config(state='disabled', takefocus=0)

    def readonly(self):
        self.label.config(style='TLabel')
        self.combobox.config(state='readonly', values=[], takefocus=0)

    def get(self):
        return self.variable.get()

    def set(self, value):
        if str(self.combobox.cget('state')) == 'disabled':
            return
        if value in self.combo_list:
            self.variable.set(value)
        else:
            self.variable.set('')

    def get_combo_values(self):
        return self.combo_list

    def set_combo_values(self, values):
        self.combo_list = values
        self.combobox.config(values=values)


class LabelEntry(LabelCompoundWidget):
    """
    Create a compound widget, with a label and an entry field within a frame.
    Base frame and label widget inherited from LabelCompoundWidget.
    Specific Parameters:
        entry_value: initial value to show at the entry (if any)
        entry_numeric: whether the entry accepts only numbers
        entry_width: entry width in number of characters
        entry_method: method to associate with the entry events
        entry_max_char: maximum number of characters in the entry field
    Methods for the user:
        enable(): turns the whole widget 'on'
        disable(): turns the whole widget 'off'
        readonly(): turn the whole widget 'readonly' (non-editable)
        get(): returns the current value from the entry widget
        set(value): sets a value to the entry widget
    """

    def __init__(self, parent, label_text='label:', label_anchor='e', label_width=None,
                 label_justify=None, label_font=None, sided=True,
                 entry_value='', entry_numeric=False, entry_width=None, entry_max_char=None,
                 entry_method=None, precision=2, trace_variable=False, **kwargs):

        # Parent class initialization
        super().__init__(parent, label_text, label_anchor, label_width, label_justify, label_font, sided, **kwargs)

        self.entry_numeric = entry_numeric
        self.entry_max_chars = entry_max_char
        self.entry_method = entry_method
        self.precision = precision
        self.trace_variable = trace_variable

        # Entry validation for numbers and max_char
        if True:
            validate_numbers = self.register(float_only)
            validate_chars = self.register(max_chars)

        # Entry configuration
        if True:
            self.variable = tk.StringVar(value=entry_value)
            self.entry = ttk.Entry(self, textvariable=self.variable, justify='center')
            if sided:
                self.entry.grid(row=0, column=1, sticky='nsew', padx=2)
            else:
                self.entry.grid(row=1, column=0, sticky='nsew', padx=2, pady=(2, 0))

            if entry_width:
                self.entry['width'] = entry_width
            if label_font:
                self.entry.config(font=label_font)

            # Restrict numeric values
            if entry_numeric:
                if not isfloat(entry_value):
                    self.variable.set('')
                self.entry.config(validate='all', validatecommand=(validate_numbers, '%d', '%P', '%S', entry_max_char))

            # Restrict max characters
            if entry_max_char and not entry_numeric:
                entry_value = str(entry_value[:entry_max_char])
                self.variable.set(entry_value)
                self.entry.config(validate='all', validatecommand=(validate_chars, '%d', '%P', entry_max_char))

        # Bind method
        if True:
            if self.trace_variable:
                self.cb_name = self.variable.trace_add("write", self._update_value)

            self.entry.bind("<FocusOut>", self._adjust_value, add='+')
            if self.entry_method:
                self.entry.bind("<Return>", self.entry_method, add='+')

    def _update_value(self, name, index, mode):
        """ Variable trace method. Calls the applicable method everytime the value changes """

        if self.entry_method:
            self.entry_method()

    def _adjust_value(self, event):
        """ Precision adjustment method. Called when 'focus' is taken away from the widget. """

        value = self.get()
        if self.entry_numeric:
            if isfloat(value):
                value = float(value)
                if self.trace_variable:
                    self.variable.trace_remove('write', self.cb_name)
                    self.variable.set(f'{value:.{self.precision}f}')
                    self.cb_name = self.variable.trace_add("write", self._update_value)
                else:
                    self.variable.set(f'{value:.{self.precision}f}')

        else:
            if self.trace_variable:
                self.variable.trace_remove('write', self.cb_name)
                self.variable.set(value)
                self.cb_name = self.variable.trace_add("write", self._update_value)
            else:
                self.variable.set(value)

        if self.entry_method:
            self.entry_method()

    def enable(self):
        self.label.config(style='TLabel')
        self.entry.config(state='normal', takefocus=1)

    def disable(self):
        self.set('')
        self.label.config(style='secondary.TLabel')
        self.entry.config(state='disabled', takefocus=0)

    def readonly(self):
        self.label.config(style='TLabel')
        self.entry.config(state='readonly', takefocus=0)

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
                value = float(value)
                if self.trace_variable:
                    self.variable.trace_remove('write', self.cb_name)
                    self.variable.set(f'{value:.{self.precision}f}')
                    self.cb_name = self.variable.trace_add("write", self._update_value)
                else:
                    self.variable.set(f'{value:.{self.precision}f}')
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


class LabelText(LabelCompoundWidget):
    """
    Compound widget, with a label and a text field within a frame.
    Base frame and label widget inherited from LabelCompoundWidget.
    Specific Parameters:
        text_width: text width in number of characters
        text_height: text width in number of lines
        text_method: method to associate when the text widget loosed focus
        text_value: initial value to show at the text (if any)
    Methods for the user:
        enable(): turns the whole widget 'on'
        disable(): turns the whole widget 'off'
        readonly(): turn the whole widget 'readonly' (non-editable)
        get(): returns the current text from the text widget
        set(text): sets a text to the text widget
    """

    def __init__(self, parent, label_text='Label:', label_anchor='e', label_width=None,
                 label_justify=None, label_font=None, sided=True,
                 text_value='', text_width=None, text_height=None, text_method=None, **kwargs):

        # Parent class initialization
        super().__init__(parent, label_text, label_anchor, label_width, label_justify, label_font, sided, **kwargs)

        # Local frame (text + scroll bar)
        if True:
            local_frame = ttk.Frame(self)
            local_frame.rowconfigure(0, weight=1)
            local_frame.columnconfigure(0, weight=1)
            local_frame.columnconfigure(1, weight=0)
            if sided:
                local_frame.grid(row=0, column=1, sticky='nsew', padx=2)
            else:
                local_frame.grid(row=1, column=0, sticky='nsew', padx=2, pady=(2, 0))

        # Text widget configuration
        if True:
            self.text = tk.Text(local_frame, wrap=tk.WORD, spacing1=2, padx=2, pady=2)
            self.text.grid(row=0, column=0, sticky='nsew')
            self.enabled_color = self.text.cget('fg')
            self.disabled_color = parent.winfo_toplevel().style.colors.secondary

            self.set(text_value)
            if text_width:
                self.text['width'] = text_width
            if text_height:
                self.text['height'] = text_height
            if label_font:
                self.text.config(font=label_font)

        # Scroll bar for the text widget
        if True:
            y_scroll = ttk.Scrollbar(local_frame, orient='vertical', command=self.text.yview)
            y_scroll.grid(row=0, column=1, sticky='ns')
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
        self.text.config(state='normal', fg=self.enabled_color, takefocus=1)

    def disable(self):
        self.label.config(style='secondary.TLabel')
        self.set('')
        self.text.config(state='disabled', fg=self.disabled_color, takefocus=0)

    def readonly(self):
        self.label.config(style='TLabel')
        self.text.config(state='disabled', fg=self.enabled_color, takefocus=0)

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


class LabelSpinbox(LabelCompoundWidget):
    """
    Create a compound widget, with a label and a spinbox within a frame.
    Base frame and label widget inherited from LabelCompoundWidget.
    Specific Parameters:
        entry_value: initial value to show at the entry (if any)
        entry_width: entry width in number of characters
        entry_method: method to associate with the entry events
        entry_type: whether the value will be a float or an integer
        spin_start: initial spinbox value
        spin_end: spinbox end_value
        spin_increment: spinbox increment
        spin_precision: number of decimal places to show for float type spinbox
    Methods for the user:
        enable(): turns the whole widget 'on'
        disable(): turns the whole widget 'off'
        readonly(): turn the whole widget 'readonly' (non-editable)
        get(): returns the current value from the spinbox widget
        set(value): sets a value to the spinbox widget
    """

    def __init__(self, parent, label_text='label:', label_anchor='e', label_width=None,
                 label_justify=None, label_font=None, sided=True,
                 entry_value=None, entry_width=None, entry_method=None, entry_type='float',
                 spin_start=0, spin_end=10, spin_increment=1, spin_precision=2,
                 trace_variable=False, **kwargs):

        # Parent class initialization
        super().__init__(parent, label_text, label_anchor, label_width, label_justify, label_font, sided, **kwargs)

        # Spinbox atributes initialization
        self.start = spin_start
        self.end = spin_end
        self.increment = spin_increment
        self.precision = spin_precision
        self.type = entry_type
        self.initial_value = entry_value
        self.trace_variable = trace_variable

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
            if sided:
                self.spin.grid(row=0, column=1, sticky='ew', padx=2)
            else:
                self.spin.grid(row=1, column=0, sticky='ew', padx=2, pady=(2, 0))

            if entry_width:
                self.spin['width'] = entry_width
            if label_font:
                self.spin.config(font=label_font)

        # Bind method
        if True:
            self.entry_method = entry_method
            if trace_variable:
                self.cb_name = self.variable.trace_add("write", self._update_value)
            if self.entry_method:
                self.spin.bind("<Return>", entry_method, add='+')
                self.spin.bind("<FocusOut>", entry_method, add='+')

            self.spin.bind("<Return>", self._check_user_value, add='+')
            self.spin.bind("<FocusOut>", self._check_user_value, add='+')
            self.spin.bind("<<Increment>>", self._on_increment)
            self.spin.bind("<<Decrement>>", self._on_decrement)
            self.spin.bind("<ButtonRelease-1>", self._spin_selected, add='+')
            self._increment_lock = False
            self._decrement_lock = False

    def _update_value(self, name, index, mode):
        current = self.variable.get()
        if isfloat(current):
            if self.entry_method:
                self.entry_method()
        else:
            self.spin.delete(self.spin.index("insert"), last='end')

    def _spin_selected(self, event=None):
        self._check_user_value()
        self.spin.event_generate('<Return>')

    # ------------------------------------------------------------------------------------------------------------------
    def _unlock_increment(self):
        self._increment_lock = False

    def _on_increment(self, event=None):
        if self._increment_lock:
            return "break"
        else:
            self._increment_lock = True
            self.after(200, self._unlock_increment)
            self.after(200, self._do_upon_clicking_arrows("up"))
        return "break"

    def _unlock_decrement(self):
        self._decrement_lock = False

    def _on_decrement(self, event=None):
        if self._decrement_lock:
            return "break"
        else:
            self._decrement_lock = True
            self.after(500, self._unlock_decrement)
            self.after(500, self._do_upon_clicking_arrows("down"))
        return "break"

    # ------------------------------------------------------------------------------------------------------------------
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
        self.spin.update()
        current = self.variable.get()
        if not current or current in ('.', '-'):
            return

        try:
            current = float(current)
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
        self.spin.config(state='normal', takefocus=1)

        if not str(self.get()):
            if self.initial_value is not None:
                self.set(self.initial_value)
            else:
                self.set(self.start)
            self._check_user_value()

    def disable(self):
        self.set('')
        self.label.config(style='secondary.TLabel')
        self.spin.config(state='disabled', takefocus=0)

    def readonly(self):
        self.label.config(style='TLabel')
        self.spin.config(state='readonly', takefocus=0)

    def get(self):
        value = self.variable.get()
        if not isfloat(value):
            return ''
        else:
            value = float(value)
            if self.type == 'float':
                return value
            else:
                return int(value)

    def set(self, value):
        if value in (None, ''):
            if self.trace_variable:
                self.variable.trace_remove('write', self.cb_name)
                self.variable.set('')
                self.cb_name = self.variable.trace_add("write", self._update_value)
            else:
                self.variable.set('')
            return

        if isfloat(value):
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


class LabelEntryUnit(LabelCompoundWidget):
    """
    Compound widget, with a label, an entry field, and a combobox with applicable units (metric and imperial).
    Base frame and label widget inherited from LabelCompoundWidget.
    Specific Parameters:
        entry_value: initial value to show at the entry (if any)
        entry_width: entry width in number of characters
        entry_method: method to associate with the entry events
        combobox_unit: unit system for the entry
        combobox_unit_width: width of the combobox in characters
        combobox_unit_conversion: boolean, if set to True converts the entry value when the unit is changed
        precision: number of decimal points to show to the user
    Methods for the user:
        enable(): turns the whole widget 'on'
        disable(): turns the whole widget 'off'
        readonly(): turn the whole widget 'readonly' (non-editable)
        is_disabled(): checks whether the widget is disabled
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
        TemperatureRateCombo: ('°C/s', '°C/min', '°C/hour', '°F/s', '°F/min', '°F/hour')
        LengthCombo: ('mm', 'cm', 'm', 'in')
        TimeCombo: ('s', 'min', 'hour', 'day', 'year')
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

    class TemperatureRateCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('°C/s', '°C/min', '°C/hour', '°F/s', '°F/min', '°F/hour')
            self.conversion_values = (1, 1/60, 1/3600, 1.8, 0.03, 0.0005)
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

    class TimeCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('s', 'min', 'hour', 'day', 'year')
            self.conversion_values = (1, 60, 3600, 86400, 3.1536e7)

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
            self.conversion_values = (1, 100, 98.0665, 1000, 101.325, 6894.757, 6.894757)

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
        'temperature rate': TemperatureRateCombo,
        'length': LengthCombo,
        'time': TimeCombo,
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

    # List which identifies unit as SI or Custom.
    # Their position in list guides its conversion constants.
    #       imperial_unit_list[index] * conversion[index] => metric_unit_list[index]
    # Temperature, Temperature Rate and time units are excluded from the lists.
    metric_unit_list = \
        ('°C/s', '°C/min', '°C/hour',                           # TemperatureRateCombo
         'mm', 'cm',  'm',                                      # LengthCombo
         'mm²', 'cm²', 'm²',                                    # AreaCombo
         'kPa', 'kPa', 'bar', 'kgf/cm²', 'MPa', 'atmosphere',   # PressureCombo
         'GPa',                                                 # StressCombo
         'N', 'kN', 'kgf',                                      # ForceCombo
         'N.m', 'kN.m', 'kgf.m',                                # MomentCombo
         '-',                                                   # NoUnitCombo
         'N/mm^(3/2)', 'MPa.√m',                                # ToughnessCombo
         'joule',                                               # EnergyCombo
         'joule/m²',                                            # JIntegralCombo
         '10e-6/°C',                                            # Thermal Expansion
         )
    imperial_unit_list = \
        ('°F/s', '°F/min', '°F/hour',
         'in', 'in', 'in',
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
        (0.55556, 0.55556, 0.55556,
         25.4, 2.54, 0.0254,
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

    def __init__(self, parent, label_text='label:', label_anchor='e', label_width=None,
                 label_justify=None, label_font=None, sided=True,
                 entry_value=None, entry_width=None, entry_method=None,
                 combobox_unit=None, combobox_unit_width=8, combobox_unit_conversion=False,
                 precision=2, trace_variable=False, **kwargs):

        # Parent class initialization
        super().__init__(parent, label_text, label_anchor, label_width, label_justify, label_font, sided, **kwargs)

        # Entry validation for numbers
        validate_numbers = self.register(float_only)

        # Local frame (text + scroll bar)
        if True:
            local_frame = ttk.Frame(self)
            local_frame.rowconfigure(0, weight=1)
            local_frame.columnconfigure(0, weight=1)
            local_frame.columnconfigure(1, weight=0)
            if sided:
                local_frame.grid(row=0, column=1, sticky='nsew', padx=2)
            else:
                local_frame.grid(row=1, column=0, sticky='nsew', padx=2, pady=(2, 0))

        # Entry configuration
        if True:
            self.parent = parent
            self.precision = precision
            self.trace_variable = trace_variable
            self.entry_method = entry_method
            self.entry_variable = tk.StringVar()
            if entry_value and isfloat(entry_value):
                value = float(entry_value)
                self.last_value = value
                if 0 < float(entry_value) < 1 / (10 ** (self.precision - 1)):
                    self.entry_variable.set(f'{value:.{self.precision}e}')
                else:
                    self.entry_variable.set(f'{value:.{self.precision}f}')
            self.entry = ttk.Entry(local_frame, textvariable=self.entry_variable, justify='center')
            self.entry.grid(row=0, column=0, sticky='nsew')

            if entry_width:
                self.entry['width'] = entry_width
            if label_font:
                self.entry.config(font=label_font)

            # Restrict numeric values
            if True:
                self.entry.config(validate='all', validatecommand=(validate_numbers, '%d', '%P', '%S'))

            self.last_value = entry_value

        # Unit combobox configuration
        if True:
            if not combobox_unit:
                combobox_unit = 'none'

            local_class = LabelEntryUnit.unit_dict.get(combobox_unit.lower(), None)
            if not local_class:
                raise Exception('Unit not found in current units dictionary.')

            self.combobox_unit_conversion = combobox_unit_conversion
            self.combobox_unit_width = combobox_unit_width
            self.unit_combo = local_class(local_frame, self.combobox_unit_width)
            self.unit_combo.grid(row=0, column=1, sticky='nsew', padx=(2, 0))
            self.last_unit = self.unit_combo.values[0]
            self.combobox_variable = self.unit_combo.variable
            self.is_locked = False

        # Bind methods
        if True:
            if self.trace_variable:
                self.cb_name = self.entry_variable.trace_add("write", self._update_value)

            # When leaving the widget adjust the precision
            self.entry.bind("<FocusOut>", self._adjust_value, add='+')

            # When 'enter' is selected, runs the applicable method
            if self.entry_method:
                self.entry.bind("<Return>", self.entry_method, add='+')

            if not self.combobox_unit_conversion:
                self.unit_combo.bind("<<ComboboxSelected>>", self.entry_method, add='+')
            else:
                self.unit_combo.bind("<<ComboboxSelected>>", self._convert_to_selected_unit, add='+')

    def _update_value(self, name, index, mode):
        """ Variable trace method. Calls the applicable method everytime the value changes """
        if self.entry_method:
            self.entry_method()

    def _adjust_value(self, event):
        """ Precision adjustment method. Called when 'focus' is taken away from the widget. """

        value = self.get_entry()
        if isfloat(value):
            value = float(value)
            if self.trace_variable:
                self.entry_variable.trace_remove('write', self.cb_name)
                if 0 < value < 1 / (10 ** (self.precision - 1)):
                    self.entry_variable.set(f'{value:.{self.precision}e}')
                else:
                    self.entry_variable.set(f'{value:.{self.precision}f}')
                self.cb_name = self.entry_variable.trace_add("write", self._update_value)
            else:
                if 0 < value < 1 / (10 ** (self.precision - 1)):
                    self.entry_variable.set(f'{value:.{self.precision}e}')
                else:
                    self.entry_variable.set(f'{value:.{self.precision}f}')

        else:
            if self.trace_variable:
                self.entry_variable.trace_remove('write', self.cb_name)
                self.entry_variable.set('')
                self.cb_name = self.entry_variable.trace_add("write", self._update_value)
            else:
                self.entry_variable.set('')

        if self.entry_method:
            self.entry_method()

    # Widget state methods ---------------------------------------------------------------------------------------------
    def enable(self):
        self.unlock_unit()
        self.label.config(style='TLabel')
        self.entry.config(state='normal', takefocus=1)
        self.unit_combo.config(state='readonly', values=self.unit_combo.values, takefocus=1)
        if not self.unit_combo.get():
            self.unit_combo.set(self.unit_combo.values[0])

    def disable(self):
        self.unlock_unit()
        self.set_entry('')
        self.combobox_variable.set('')
        self.label.config(style='secondary.TLabel')
        self.entry.config(state='disabled', takefocus=0)
        self.unit_combo.config(state='disabled', takefocus=0)

    def readonly(self):
        self.unlock_unit()
        self.label.config(style='TLabel')
        self.entry.config(state='readonly', takefocus=0)
        if not self.combobox_unit_conversion:
            self.unit_combo.config(state='readonly', values=[], takefocus=0)
        else:
            self.unit_combo.config(state='readonly', values=self.unit_combo.values, takefocus=1)

    def is_disabled(self):
        if str(self.entry.cget('state')) == 'disabled':
            return True
        return False

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
        self.last_value = self.get_entry()
        self.last_unit = self.combobox_variable.get()
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
        value = self.entry_variable.get()
        try:
            value = float(value)
        except ValueError:
            value = ''
        return value

    def set_entry(self, value, update_last_value=True):
        if str(self.entry.cget('state')) == 'disabled':
            return

        if value in ('', 'NA'):
            if update_last_value:
                self.last_value = 0
            if self.trace_variable:
                self.entry_variable.trace_remove('write', self.cb_name)
                self.entry_variable.set(value)
                self.cb_name = self.entry_variable.trace_add("write", self._update_value)
            else:
                self.entry_variable.set(value)
            return

        elif not(isfloat(value)):
            if update_last_value:
                self.last_value = 0

        else:
            value = float(value)
            if self.trace_variable:
                self.entry_variable.trace_remove('write', self.cb_name)
                if 0 < value < 1 / (10 ** (self.precision - 1)):
                    self.entry_variable.set(f'{value:.{self.precision}e}')
                else:
                    self.entry_variable.set(f'{value:.{self.precision}f}')
                self.cb_name = self.entry_variable.trace_add("write", self._update_value)
            else:
                if 0 < value < 1 / (10 ** (self.precision - 1)):
                    self.entry_variable.set(f'{value:.{self.precision}e}')
                else:
                    self.entry_variable.set(f'{value:.{self.precision}f}')

            if update_last_value:
                self.last_value = value

    def get_unit(self):
        return self.combobox_variable.get()

    def set_unit(self, unit, update_last_unit=True):
        if str(self.unit_combo.cget('state')) == 'disabled':
            return

        if self.is_locked:
            return

        if unit in list(self.unit_combo.values):
            if update_last_unit:
                self.last_unit = unit
            self.combobox_variable.set(unit)
        else:
            if update_last_unit:
                self.last_unit = self.unit_combo.values[0]
            self.combobox_variable.set(self.unit_combo.values[0])

    def get(self):
        return self.get_entry(), self.get_unit()

    def set(self, value, unit=None):
        self.set_entry(value)
        if unit:
            self.set_unit(unit)
        else:
            self.set_unit(self.get_unit())

    # Widget conversion methods ----------------------------------------------------------------------------------------
    def get_metric_value(self):
        """
        Returns the current value converted to the equivalent metric unit.
        The selected metric unit is the first from the combobox values.
        """

        if self.is_disabled():
            return '', ''

        if isinstance(self.unit_combo, LabelEntryUnit.NoUnitCombo):
            return self.get_entry(), '-'

        if isinstance(self.unit_combo, LabelEntryUnit.TemperatureCombo):
            if str(self.get_unit()) == '°F':
                if not str(self.get_entry()):
                    return '', '°C'
                else:
                    return 5 * (float(self.get_entry()) - 32) / 9, '°C'
            return self.get_entry(), '°C'

        index = self.unit_combo.values.index(self.get_unit())
        if not str(self.get_entry()):
            return '', self.unit_combo.values[0]
        else:
            return float(self.get_entry()) * self.unit_combo.conversion_values[index], self.unit_combo.values[0]

    def get_imperial_value(self):
        """
        Returns the current value converted to the equivalent imperial unit.
        The selected imperial unit is the last from the combobox values.
        """

        if self.is_disabled():
            return '', ''

        if isinstance(self.unit_combo, LabelEntryUnit.NoUnitCombo):
            return self.get_entry(), '-'

        if isinstance(self.unit_combo, LabelEntryUnit.TemperatureCombo):
            if str(self.get_unit()) == '°C':
                if not str(self.get_entry()):
                    return '', '°F'
                else:
                    return 9 * float(self.get_entry())/5 + 32, '°F'
            return self.get_entry(), '°F'

        index = self.unit_combo.values.index(self.get_unit())
        if not str(self.get_entry()):
            return '', self.unit_combo.values[-1]
        else:
            if isinstance(self.unit_combo, LabelEntryUnit.TimeCombo):
                final_index = 0
            else:
                final_index = -1
            last_value = self.get_entry()
            intermediary_value = float(last_value) * self.unit_combo.conversion_values[index]
            new_value = intermediary_value / self.unit_combo.conversion_values[final_index]

            return new_value, self.unit_combo.values[final_index]

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

        last_value = self.last_value
        last_unit = self.last_unit
        new_unit = self.get_unit()

        if isinstance(self.unit_combo, LabelEntryUnit.NoUnitCombo):
            pass

        elif isinstance(self.unit_combo, LabelEntryUnit.TemperatureCombo):
            if new_unit == last_unit:
                self.set_entry(last_value)
            else:
                if new_unit == '°F':
                    if not last_value:
                        new_value = ''
                    else:
                        new_value = 9 * (float(last_value) / 5) + 32

                    self.set_unit('°F', update_last_unit=False)
                    self.set_entry(new_value, update_last_value=False)
                else:
                    if not last_value:
                        new_value = ''
                    else:
                        new_value = 5 * (float(last_value) - 32) / 9
                    self.set_unit('°C', update_last_unit=False)
                    self.set_entry(new_value, update_last_value=False)

        else:
            if new_unit == last_unit:
                self.set_entry(last_value)
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

                self.set_unit(new_unit, update_last_unit=False)
                self.set_entry(new_value, update_last_value=False)


class LabelEntryButton(LabelCompoundWidget):
    """
    Create a compound widget, with a label, an entry field and a button within a frame.
    Base frame and label widget inherited from LabelCompoundWidget.
    Specific Parameters:
        entry_value: initial value to show at the entry (if any)
        entry_numeric: whether the entry accepts only numbers
        entry_width: entry width in number of characters
        entry_method: method to associate with the entry events
        entry_max_char: maximum number of characters in the entry field
        button_text: string to be shown on the button
        button_width: width of the button in characters
        button_method: method to bind to the button
    Methods for the user:
        enable(): turns the whole widget 'on'
        disable(): turns the whole widget 'off'
        readonly(): turn the whole widget 'readonly' (non-editable)
        get(): returns the current value from the entry widget
        set(value): sets a value to the entry widget
    """

    def __init__(self, parent, label_text='Label:', label_anchor='e', label_width=None,
                 label_justify=None, label_font=None, sided=True,
                 entry_value='', entry_numeric=False, entry_width=None,
                 entry_max_char=None, entry_method=None,
                 button_text='', button_width=None, button_method=None,
                 precision=2, trace_variable=False, **kwargs):

        # Parent class initialization
        super().__init__(parent, label_text, label_anchor, label_width, label_justify, label_font, sided, **kwargs)

        self.entry_numeric = entry_numeric
        self.entry_max_chars = entry_max_char
        self.entry_method = entry_method
        self.precision = precision
        self.trace_variable = trace_variable
        self.button_method = button_method

        # Entry validation for numbers
        if True:
            validate_numbers = self.register(float_only)
            validate_chars = self.register(max_chars)

        # Local frame (entry + button)
        if True:
            local_frame = ttk.Frame(self)
            local_frame.rowconfigure(0, weight=1)
            local_frame.columnconfigure(0, weight=1)
            local_frame.columnconfigure(1, weight=1)
            if sided:
                local_frame.grid(row=0, column=1, sticky='nsew', padx=2)
            else:
                local_frame.grid(row=1, column=0, sticky='nsew', padx=2, pady=(2, 0))

        # Entry configuration
        if True:
            self.variable = tk.StringVar(value=entry_value)
            self.entry = ttk.Entry(local_frame, textvariable=self.variable, justify='center')
            self.entry.grid(row=0, column=0, sticky='nsew')

            if entry_width:
                self.entry['width'] = entry_width

            if label_font:
                self.entry.config(font=label_font)

            # Restrict numeric values
            if entry_numeric:
                if not isfloat(entry_value):
                    self.variable.set('')
                self.entry.config(validate='all', validatecommand=(validate_numbers, '%d', '%P', '%S', entry_max_char))

            # Restrict max characters
            elif entry_max_char and not entry_numeric:
                entry_value = str(entry_value[:entry_max_char])
                self.variable.set(entry_value)
                self.entry.config(validate='all', validatecommand=(validate_chars, '%d', '%P', entry_max_char))

        # Button configuration
        if True:
            self.button = ttk.Button(local_frame, text=button_text, width=button_width)
            self.button.grid(row=0, column=1, sticky='nsew', padx=(2, 0))

        # Bind methods
        if True:
            if button_method:
                self.button.configure(command=button_method)
            if self.trace_variable:
                self.cb_name = self.variable.trace_add("write", self._update_value)
            self.entry.bind("<FocusOut>", self._adjust_value, add='+')
            if entry_method:
                self.entry.bind("<Return>", self.entry_method, add='+')

    def _update_value(self, name, index, mode):
        if self.entry_method:
            self.entry_method()

    def _adjust_value(self, event):

        value = self.get()
        if self.entry_numeric:
            if isfloat(value):
                value = float(value)
                if self.trace_variable:
                    self.variable.trace_remove('write', self.cb_name)
                    self.variable.set(f'{value:.{self.precision}f}')
                    self.cb_name = self.variable.trace_add("write", self._update_value)
                else:
                    self.variable.set(f'{value:.{self.precision}f}')
        else:
            if self.trace_variable:
                self.variable.trace_remove('write', self.cb_name)
                self.variable.set(value)
                self.cb_name = self.variable.trace_add("write", self._update_value)
            else:
                self.variable.set(value)

        if self.entry_method:
            self.entry_method()

    def enable(self):
        self.label.config(style='TLabel')
        self.entry.config(state='normal', takefocus=1)
        self.button.state(["!disabled"])

    def disable(self):
        self.set('')
        self.label.config(style='secondary.TLabel')
        self.entry.config(state='disabled', takefocus=0)
        self.button.state(["disabled"])

    def readonly(self):
        self.label.config(style='TLabel')
        self.entry.config(state='readonly', takefocus=0)
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
                value = float(value)
                if self.trace_variable:
                    self.variable.trace_remove('write', self.cb_name)
                    self.variable.set(f'{value:.{self.precision}f}')
                    self.cb_name = self.variable.trace_add("write", self._update_value)
                else:
                    self.variable.set(f'{value:.{self.precision}f}')
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


class LabelComboButton(LabelCompoundWidget):
    """
    Create a compound widget, with a label, a combobox and a button within a ttk Frame.
    Base frame and label widget inherited from LabelCompoundWidget.
    Specific Parameters:
        combo_value: initial value to show at the combo box (if any)
        combo_list: list of values to be shown at the combobox
        combo_width: combobox width in number of characters
        combo_method: method to associate when combobox is selected
        button_text: string to be shown on the button
        button_width: width of the button in characters
        button_method: method to bind to the button
    Methods for the user:
        enable(): turns the whole widget 'on'
        disable(): turns the whole widget 'off'
        readonly(): turn the whole widget 'readonly' (non-editable)
        get(): gets the current value from the entry widget
        set(value): sets a value to the entry widget
        get_combo_values: return the current available values form the combobox
        set_combo_values(values): sets the combobox values after it has been created
    """

    def __init__(self, parent, label_text='Label:', label_anchor='e', label_width=None,
                 label_justify=None, label_font=None, sided=True,
                 combo_value='', combo_list=('No values informed',), combo_width=None, combo_method=None,
                 button_text='', button_width=None, button_method=None, **kwargs):

        # Parent class initialization
        super().__init__(parent, label_text, label_anchor, label_width, label_justify, label_font, sided, **kwargs)

        # Local frame (combo + button)
        if True:
            local_frame = ttk.Frame(self)
            local_frame.rowconfigure(0, weight=1)
            local_frame.columnconfigure(0, weight=1)
            local_frame.columnconfigure(1, weight=1)
            if sided:
                local_frame.grid(row=0, column=1, sticky='nsew', padx=2)
            else:
                local_frame.grid(row=1, column=0, sticky='nsew', padx=2, pady=(2, 0))

        # Combobox configuration
        if True:
            self.combo_list = combo_list
            self.variable = tk.StringVar(value=combo_value)
            self.combobox = ttk.Combobox(local_frame, textvariable=self.variable, justify='center',
                                         values=combo_list, state='readonly')
            self.combobox.grid(row=0, column=0, sticky='nsew')

            if combo_width:
                self.combobox['width'] = combo_width

        # Button configuration
        if True:
            self.button = ttk.Button(local_frame, text=button_text, width=button_width)
            self.button.grid(row=0, column=1, sticky='nsew', padx=(2, 0))

        # Bind methods
        if combo_method:
            self.combobox.bind('<<ComboboxSelected>>', combo_method, add='+')
        if button_method:
            self.button.configure(command=button_method)

    def enable(self):
        self.label.config(style='TLabel')
        self.combobox.config(state='readonly', values=self.combo_list, takefocus=1)
        self.button.state(["!disabled"])

    def disable(self):
        self.variable.set('')
        self.label.config(style='secondary.TLabel')
        self.combobox.config(state='disabled', takefocus=0)
        self.button.state(["disabled"])

    def readonly(self):
        self.label.config(style='TLabel')
        self.combobox.config(state='readonly', values=[], takefocus=0)
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

    def get_combo_values(self):
        return self.combo_list

    def set_combo_values(self, values):
        self.combo_list = values
        self.combobox.config(values=values)
