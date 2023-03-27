import tkinter as tk
import tkinter.ttk as ttk


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


class LedButton (ttk.Frame):
    """
    Create a compound widget, with a color canvas (left) and a label (right).
    The master (application top level) shall have a ttkbootstrap Style defined.
    Input:
        parent: container in which the widgets will be created
        label_text: string to be shown on the label
        label_width: width of the label im characters
        label_method: method to bind to the label
    Methods:
        enable method:
            enables the widgets (state='normal')
        disable method:
            disables the widgets (state='disabled')
        select method:
            changes the color of the canvas to the selected one
        deselect method:
            changes the color of the canvas to the deselected one
    """

    def __init__(self, parent, label_text='Label', label_width=10, label_method=None):

        # Parent class initialization
        super().__init__(parent)
        self.label_method = label_method

        # Gets the current style from the top level container
        style = parent.winfo_toplevel().style

        # Gets the active/inactive colors from the style
        if True:
            self.selected_color = style.colors.info
            self.deselected_color = style.colors.fg
            self.disable_color = style.colors.light

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=0)
            self.columnconfigure(1, weight=1)

        # Canvas
        if True:
            self.color_canvas = tk.Canvas(self, bd=0, width=10, height=0, highlightthickness=0)
            self.color_canvas.grid(row=0, column=0, sticky='nsew')
            self.color_canvas.configure(background=self.deselected_color)

        # Label
        if True:
            self.label = ttk.Label(self, text=label_text, anchor='w', style='secondary.TButton', padding=2,
                                   width=label_width)
            self.label.grid(row=0, column=1, sticky='nsew')

        # Bind mouse button click event
        self.color_canvas.bind('<Button-1>', self.select)
        self.label.bind('<Button-1>', self.select)
        self.color_canvas.bind('<ButtonRelease-1>', self.check_hover)
        self.label.bind('<ButtonRelease-1>', self.check_hover)

    def check_hover(self, event):
        """ Checks whether the mouse is still over the widget before calling the assigned method """

        if str(self.label.cget('state')) == 'disabled':
            return

        self.deselect()
        current_widget = event.widget.winfo_containing(event.x_root, event.y_root)
        if current_widget == event.widget:
            self.label_method(event)

    def enable(self):
        self.color_canvas.config(bg=self.deselected_color)
        self.label.config(state='normal')

    def disable(self):
        self.color_canvas.config(bg=self.disable_color)
        self.label.config(state='disabled')

    def select(self, event=None):
        if str(self.label.cget('state')) == 'disabled':
            return
        self.color_canvas.config(bg=self.selected_color)
        # self.label.config(style='primary.TButton')

    def deselect(self, event=None):
        if str(self.label.cget('state')) == 'disabled':
            return
        self.color_canvas.config(bg=self.deselected_color)
        # self.label.config(style='secondary.TButton')


class CheckLedButton (ttk.Frame):
    """
    Create a compound widget, with a color canvas (left) and a label (right).
    The master (application top level) shall have a ttkbootstrap Style defined.
    This button remains ON until once again selected
    Input:
        parent: container in which the widgets will be created
        label_text: string to be shown on the label
        label_width: width of the label im characters
        label_method: method to bind to the label
    Methods:
        enable method:
            enables the widgets (state='normal')
        disable method:
            disables the widgets (state='disabled')
        select method:
            changes the color of the canvas to the selected one
        deselect method:
            changes the color of the canvas to the deselected one
        is_selected:
            checks whether the button is currently selected
    """

    def __init__(self, parent, label_text='Label', label_width=10, label_method=None):

        # Parent class initialization
        super().__init__(parent)
        self.label_method = label_method

        # Gets the current style from the top level container
        style = parent.winfo_toplevel().style

        # Gets the active/inactive colors from the style
        if True:
            self.selected_color = style.colors.info
            self.deselected_color = style.colors.fg
            self.disable_color = style.colors.light
            self.bg_color = style.colors.secondary

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=0)
            self.columnconfigure(1, weight=0)
            self.columnconfigure(2, weight=1)

        # Canvas
        if True:
            self.color_canvas_1 = tk.Canvas(self, bd=0, width=10, height=0, highlightthickness=0)
            self.color_canvas_1.grid(row=0, column=0, sticky='nsew', padx=(1, 0))
            self.color_canvas_1.configure(background=self.deselected_color)

            self.color_canvas_2 = tk.Canvas(self, bd=0, width=10, height=0, highlightthickness=0)
            self.color_canvas_2.grid(row=0, column=1, sticky='nsew', padx=(0, 1))
            self.color_canvas_2.configure(background=self.bg_color)

        # Label
        if True:
            self.label = ttk.Label(self, text=label_text, anchor='w', style='secondary.TButton', padding=2,
                                   width=label_width)
            self.label.grid(row=0, column=2, sticky='nsew')

        # Bind method
        self.color_canvas_1.bind('<ButtonRelease-1>', self.check_hover)
        self.color_canvas_2.bind('<ButtonRelease-1>', self.check_hover)
        self.label.bind('<ButtonRelease-1>', self.check_hover)

    def check_hover(self, event):
        """ Checks whether the mouse is still over the widget before releasing the assigned method """

        if str(self.label.cget('state')) == 'disabled':
            return

        widget_under_cursor = event.widget.winfo_containing(event.x_root, event.y_root)

        if widget_under_cursor in (self.color_canvas_1, self.color_canvas_2, self.label):
            if self.is_selected():
                self.deselect()
            else:
                self.select()
                self.label_method(event)

    def enable(self):
        self.color_canvas_1.config(bg=self.deselected_color)
        self.color_canvas_2.config(bg=self.bg_color)
        self.label.config(state='normal')

    def disable(self):
        self.color_canvas_1.config(bg=self.disable_color)
        self.color_canvas_2.config(bg=self.bg_color)
        self.label.config(state='disabled')

    def select(self):
        if str(self.label.cget('state')) == 'disabled':
            return
        self.color_canvas_1.config(bg=self.bg_color)
        self.color_canvas_2.config(bg=self.selected_color)
        # self.label.config(style='primary.TButton')

    def deselect(self):
        if str(self.label.cget('state')) == 'disabled':
            return
        self.color_canvas_1.config(bg=self.deselected_color)
        self.color_canvas_2.config(bg=self.bg_color)
        # self.label.config(style='secondary.TButton')

    def is_selected(self):
        if self.color_canvas_2.cget('bg') == self.selected_color:
            return True
        else:
            return False


class RadioLedButton(ttk.Frame):
    """
    Create a compound widget, with a color canvas and a label.
    The set of instance with the same control variable will work as radio buttons.
    Input:
        parent: container in which the widgets will be created
        label_text: string to be shown on the label
        label_width: width of the label im characters
        label_method: method to bind to the label
        control_variable: variable that will group the buttons for "radio button" like operation
    Methods:
        enable method:
            enables the widgets (state='normal')
        disable method:
            disables the widgets (state='disabled')
        select method:
            changes the color of the canvas to the selected one
        deselect method:
            changes the color of the canvas to the deselected one
        is_selected:
            checks whether the button is currently selected
    """

    control_variable_dict = {}

    def __init__(self, parent, label_text='Label', label_width=10, label_method=None, control_variable=None):

        super().__init__(parent)
        self.label_method = label_method
        self.control_variable = control_variable

        if control_variable in RadioLedButton.control_variable_dict:
            RadioLedButton.control_variable_dict[control_variable].append(self)
        else:
            RadioLedButton.control_variable_dict[control_variable] = [self]

        # Gets the current style from the top level container
        style = parent.winfo_toplevel().style

        # Gets the active/inactive colors from the style
        if True:
            self.selected_color = style.colors.info
            self.deselected_color = style.colors.fg
            self.disabled_color = style.colors.light

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=0)
            self.columnconfigure(1, weight=1)

        # Canvas
        if True:
            self.color_canvas = tk.Canvas(self, bd=0, width=10, height=0, highlightthickness=0)
            self.color_canvas.grid(row=0, column=0, sticky='nsew')
            self.color_canvas.configure(background=self.deselected_color)

        # Label
        if True:
            self.label = ttk.Label(self, text=label_text, anchor='w', justify='left', style='secondary.TButton',
                                   padding=1, width=label_width)
            self.label.grid(row=0, column=1, sticky='nsew')

        self.color_canvas.bind('<ButtonRelease-1>', self.check_hover)
        self.label.bind('<ButtonRelease-1>', self.check_hover)

    def check_hover(self, event):
        if str(self.label.cget('state')) == 'disabled':
            return

        widget_under_cursor = event.widget.winfo_containing(event.x_root, event.y_root)
        if widget_under_cursor not in (self.color_canvas, self.label):
            return

        for widget in list(self.control_variable_dict[self.control_variable]):
            if str(widget) == str(event.widget.winfo_parent()):
                widget.select()
                self.label_method(event)
            else:
                widget.deselect()

    def select(self):
        self.color_canvas.config(bg=self.selected_color)
        # self.label.config(style='primary.TButton')

    def deselect(self):
        self.color_canvas.config(bg=self.deselected_color)
        # self.label.config(style='secondary.TButton')

    def enable(self):
        self.color_canvas.config(bg=self.deselected_color)
        self.label.config(state='normal')

    def disable(self):
        self.color_canvas.config(bg=self.disabled_color)
        self.label.config(state='disabled')

    def is_selected(self):
        if self.color_canvas.cget('bg') == self.selected_color:
            return True
        return False


class LabelEntryUnit (ttk.Frame):
    """
    Creates a compound widget, with a label, an entry field, and a combobox with applicable units (metric and imperial).
    Input:
        parent: container in which the widgets will be created
        label_text: string to be shown on the label
        label_anchor: position of the text within the label
        label_width: width of the label in characters
        entry_value: initial value to show at the entry (if any)
        entry_numeric: whether the entry accepts only numbers
        entry_width: entry width in number of characters
        entry_method: method to associate when the entry events
        entry_max_char: maximum number of characters in the entry field
        combobox_unit: unit system for the entry
        combobox_unit_width: width of the combobox in characters
        combobox_unit_conversion: boolean, if set to True converts the entry value when the unit changes
    """

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

            self.values = ('mm', 'in')
            self.conversion_values = (1, 25.4)

            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

    class AreaCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('mm²', 'cm²', 'in²')
            self.conversion_values = (1, 100, 645.16)

            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

    class PressureCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('kPa', 'bar', 'kgf/cm²', 'MPa', 'ksi', 'psi')
            self.conversion_values = (1, 100, 98.0665, 1000, 689.4757, 6.894757)

            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

    class StressCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('MPa', 'GPa', 'ksi', 'x10³ ksi', 'psi')
            self.conversion_values = (1, 1000, 6.894757, 6894.757, 0.006894757)
            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

    class ForceCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('N', 'kgf', 'lbf')
            self.conversion_values = (1, 9.80665, 4.448222)
            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

    class MomentCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('N.m', 'kgf.m', 'lbf.ft')
            self.conversion_values = (1, 9.80665, 1.35582)
            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

    class NoUnitCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('-',)
            self.variable = tk.StringVar(value='-')
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

    class ToughnessCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('N/mm^(3/2)', 'MPa.√m', 'ksi.√in')
            self.conversion_values = (1, 31.6240, 34.7485)
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

    class JIntegralCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('joule/m²', 'ft-lbf/ft²')
            self.conversion_values = (1, 14.5939)
            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')


    unit_dict = {
        'temperature': TemperatureCombo,
        'area': AreaCombo,
        'length': LengthCombo,
        'pressure': PressureCombo,
        'stress': StressCombo,
        'force': ForceCombo,
        'moment': MomentCombo,
        'none': NoUnitCombo,
        'toughness': ToughnessCombo,
        'energy': EnergyCombo,
        'j-integral': JIntegralCombo
    }
    metric_unit_list = \
        ('mm',  #LengthCombo
         'mm²', 'cm²',  #AreaCombo
         'kPa', 'kPa', 'bar', 'kgf/cm²', 'MPa',  #PressureCombo
         'kPa', 'GPa',  # StressCombo
         'N', 'kgf',  #ForceCombo
         'N.m', 'kgf.m',  #MomentCombo
         '-',  #NoUnitCombo
         'N/mm^(3/2)', 'MPa.√m',  #ToughnessCombo
         'joule',  #EnergyCombo
         'joule/m²'  #JIntegralCombo
         )
    imperial_unit_list = \
        ('in',
         'in²', 'in²',
         'psi', 'ksi', 'ksi', 'ksi', 'ksi',
         'x10³ ksi', 'x10³ ksi',
         'lbf', 'lbf',
         'lbf.ft', 'lbf.ft',
         '-',
         'ksi.√in', 'ksi.√in',
         'ft-lbf',
         'ft-lbf/ft²')
    conversion = \
        (25.4,
         645.16, 6.4516,
         6.894757, 6894.757, 68.94757, 70.30696, 6.894757,
         6.894757e6, 6.894757,
         4.448222, 0.4535924,
         1.35582, 0.1382552,
         1,
         34.7485, 1.0988,
         1.355818,
         14.5939)

    def __init__(self, parent, label_text='Label:', label_anchor='e', label_width=None, entry_value='',
                 entry_numeric=False, entry_width=None, entry_max_char=None, entry_method=None, combobox_unit=None,
                 combobox_unit_width=8, combobox_unit_conversion=False):

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

        # Label
        if True:
            self.label = ttk.Label(self, text=label_text, anchor=label_anchor)
            self.label.grid(row=0, column=0, sticky='ew', padx=2)
            if label_width:
                self.label['width'] = label_width

        # Entry
        if True:
            self.variable = tk.StringVar(value=entry_value)
            self.entry = ttk.Entry(self, textvariable=self.variable, justify='center')
            self.entry.grid(row=0, column=1, sticky='ew', padx=2)

            if entry_width:
                self.entry['width'] = entry_width

        # Restrict numeric values
        if entry_numeric:
            self.entry.config(validate='all', validatecommand=(validate_numbers, '%d', '%P', '%S'))

        # Restrict maximum number of characters
        if entry_max_char:
            self.entry_max_char = entry_max_char
            self.entry.bind('<Key>', self.check_length)

        # Unit Combobox
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

        # Bind methods
        if True:
            self.entry.bind("<Return>", entry_method)
            self.entry.bind("<FocusOut>", entry_method)

            self.combobox_unit_conversion = combobox_unit_conversion
            if not self.combobox_unit_conversion:
                self.unit_combo.bind("<<ComboboxSelected>>", entry_method)
            else:
                self.unit_combo.bind("<<ComboboxSelected>>", self.convert_to_selected_unit)

    # Widget state methods ---------------------------------------------------------------------------------------------
    def enable(self):
        self.label.config(style='TLabel')
        self.entry.config(state='normal')
        self.unit_combo.config(state='readonly', values=self.unit_combo.values)

    def disable(self):
        self.label.config(style='secondary.TLabel')
        self.entry.config(state='disabled')
        self.unit_combo.config(state='disabled')

    def readonly(self):
        self.label.config(style='TLabel')
        self.entry.config(state='readonly')
        if not self.combobox_unit_conversion:
            self.unit_combo.config(state='readonly', values=[])
        else:
            self.unit_combo.config(state='readonly', values=self.unit_combo.values)

    def lock_unit(self):
        self.unit_combo.config(state='readonly', values=[], style='TLabel',
                               width=self.combobox_unit_width+4)

    def unlock_unit(self):
        self.unit_combo.config(state='readonly', values=self.unit_combo.values, style='TCombobox',
                               width=self.combobox_unit_width)

    def check_length(self, event):
        current = self.get_entry()
        if len(current) >= self.entry_max_char:
            self.set_entry(current[:int(self.entry_max_char)])

    # Widget set and get methods ---------------------------------------------------------------------------------------
    def get_entry(self):
        return self.variable.get()

    def set_entry(self, value):
        self.variable.set(value)

    def get_unit(self):
        return self.unit_combo.get()

    def set_unit(self, unit):
        if unit in list(self.unit_combo.values):
            self.unit_combo.set(unit)
            self.last_unit = unit
        else:
            self.unit_combo.set(self.unit_combo.values[0])
            self.last_unit = self.unit_combo.values[0]

    def get(self):
        return self.get_entry(), self.get_unit()

    def set(self, value, unit):
        self.variable.set(value)
        if unit in list(self.unit_combo.values):
            self.set_unit(unit)
            self.last_unit = unit
        else:
            self.unit_combo.set(self.unit_combo.values[0])
            self.last_unit = self.unit_combo.values[0]

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
            new_value = round(new_value, 8)
            return new_value, self.unit_combo.values[-1]

    def convert_to_metric(self):
        """ Convert 'self' to metric """

        new_value, new_unit = self.get_metric_value()
        self.set(new_value, new_unit)

    def convert_to_imperial(self):
        """ Convert 'self' to imperial """

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
                    new_value = round(float(value)*LabelEntryUnit.conversion[index], 8)
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
                    new_value = round(float(value) / LabelEntryUnit.conversion[index], 8)
                return new_value, LabelEntryUnit.imperial_unit_list[index]
            return value, unit

    def convert_to_selected_unit(self, event=None):
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
                        new_value = round(new_value, 8)
                    self.last_unit = '°F'
                    self.set(new_value, '°F')
                else:
                    if not last_value:
                        new_value = ''
                    else:
                        new_value = 5 * (float(last_value) - 32) / 9
                        new_value = round(new_value, 8)
                    self.last_unit = '°C'
                    self.set(new_value, '°C')

                print(f'New data: {new_value} {self.last_unit}')

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
                    new_value = round(new_value, 8)

                self.last_unit = new_unit
                self.set(new_value, new_unit)


class LabelCombo (ttk.Frame):
    """
    Create a compound widget, with a label and a combo box within a ttk Frame.
    Input:
        parent - container in which the widgets will be created
        label_text - string to be shown on the label
        label_anchor - position of the text within the label
        label_width: label width in number of characters
        combo_value - initial value to show at the combo box (if any)
        combo_list - list of values to be shown at the combo box
        combo_width: combo box width in number of characters
        combo_method: method to associate when combo box is selected
    Methods:
        enable method:
            enables the widgets (state='normal')
        disable method:
            disables the widgets (state='disabled')
        get method:
            gets the value from the combo box widget
        set method:
            sets the value to the combo box widget
    """

    def __init__(self, parent,
                 label_text='Label:',
                 label_anchor='e',
                 label_width=None,
                 combo_value='',
                 combo_list=('No values informed',),
                 combo_width=None,
                 combo_method=None,
                 combo_method_2=None):

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

        # Combobox configuration
        if True:
            self.combo_list = combo_list
            self.variable = tk.StringVar(value=combo_value)
            self.combobox = ttk.Combobox(self, textvariable=self.variable, justify='center',
                                         values=combo_list, state='readonly')
            self.combobox.grid(row=0, column=1, sticky='ew', padx=2)

            if combo_width:
                self.combobox['width'] = combo_width

        # Combobox bind to method
        if combo_method:
            self.combobox.bind('<<ComboboxSelected>>', combo_method, add='+')
        if combo_method_2:
            self.combobox.bind('<<ComboboxSelected>>', combo_method_2, add='+')

    def enable(self):
        self.label.config(style='TLabel')
        self.combobox.config(state='readonly', values=self.combo_list)

    def disable(self):
        self.label.config(style='secondary.TLabel')
        self.combobox.config(state='disabled')

    def readonly(self):
        self.label.config(style='TLabel')
        self.combobox.config(state='readonly', values=[])

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)


class LabelEntry (ttk.Frame):
    """
    Create a compound widget, with a label and an entry field.
    Input:
        parent: container in which the widgets will be created
        label_text: string to be shown on the label
        label_anchor - position of the text within the label
        label_width: label width in number of characters
        entry_value: initial value to show at the entry (if any)
        entry_numeric: whether the entry accepts only numbers
        entry_width: entry width in number of characters
        entry_method: method to associate when the entry events
        entry_max_char: maximum number of characters in the entry field
    Methods:
        enable method:
            enables the widgets (state='normal')
        disable method:
            disables the widgets (state='disabled')
        read_only method:
            disabled edition of the entry widget (state='readonly')
        get method:
            gets the value from the entry widget
        set method:
            sets the value to the entry widget
    """

    def __init__(self, parent,
                 label_text='label:',
                 label_anchor='e',
                 entry_value='',
                 label_width=None,
                 entry_numeric=False,
                 entry_width=None,
                 entry_max_char=None,
                 entry_method=None):

        # Parent class initialization
        super().__init__(parent)

        # Entry validation for numbers
        validate_numbers = self.register(float_only)
        validate_chars = self.register(max_chars)

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=0)

        # Label
        if True:
            self.label = ttk.Label(self, text=label_text, anchor=label_anchor)
            self.label.grid(row=0, column=0, sticky='ew', padx=2)

            if label_width:
                self.label['width'] = label_width

        # Entry
        if True:
            self.variable = tk.StringVar(value=entry_value)
            self.entry = ttk.Entry(self, textvariable=self.variable, justify='center')
            self.entry.grid(row=0, column=1, sticky='ew', padx=2)

            if entry_width:
                self.entry['width'] = entry_width

        # Restrict numeric values
        if entry_numeric:
            self.entry.config(validate='all', validatecommand=(validate_numbers, '%d', '%P', '%S', entry_max_char))

        # Restrict max characters
        elif entry_max_char:
            self.entry.config(validate='all', validatecommand=(validate_chars, '%d', '%P', entry_max_char))

        # Entry bind to method
        if True:
            self.entry.bind("<Return>", entry_method)
            self.entry.bind("<FocusOut>", entry_method)

    def enable(self):
        self.label.config(style='TLabel')
        self.entry.config(state='normal')

    def disable(self):
        self.label.config(style='secondary.TLabel')
        self.entry.config(state='disabled')

    def readonly(self):
        self.label.config(style='TLabel')
        self.entry.config(state='readonly')

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)


class LabelEntryButton (ttk.Frame):
    """
    Create a compound widget, with a label, an entry field and a button.
    Input:
        parent: container in which the widgets will be created
        label_text: string to be shown on the label
        label_anchor - position of the text within the label
        label_width: label width in number of characters
        entry_value: initial value to show at the entry (if any)
        entry_numeric: whether the entry accepts only numbers
        entry_width: entry width in number of characters
        entry_method: method to associate when the entry events
        entry_max_char: maximum number of characters in the entry field
        button_text: string to be shown on the label
        button_width: width of the label im characters
        button_method: method to bind to the label
    Methods:
        enable method:
            enables the widgets (state='normal')
        disable method:
            disables the widgets (state='disabled')
        read_only method:
            disabled edition of the entry widget (state='readonly')
        get method:
            gets the value from the entry widget
        set method:
            sets the value to the entry widget
    """

    def __init__(self, parent,
                 label_text='label:',
                 label_anchor='e',
                 entry_value='',
                 label_width=None,
                 entry_numeric=False,
                 entry_width=None,
                 entry_max_char=None,
                 entry_method=None,
                 button_text='',
                 button_width=None,
                 button_method=None
    ):

        # Parent class initialization
        super().__init__(parent)

        # Entry validation for numbers
        validate_numbers = self.register(float_only)
        validate_chars = self.register(max_chars)

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=0)
            self.columnconfigure(2, weight=0)

        # Label
        if True:
            self.label = ttk.Label(self, text=label_text, anchor=label_anchor)
            self.label.grid(row=0, column=0, sticky='ew', padx=2)

            if label_width:
                self.label['width'] = label_width

        # Entry
        if True:
            self.variable = tk.StringVar(value=entry_value)
            self.entry = ttk.Entry(self, textvariable=self.variable, justify='center')
            self.entry.grid(row=0, column=1, sticky='ew', padx=2)

            if entry_width:
                self.entry['width'] = entry_width

            if entry_method:
                self.entry.bind("<Return>", entry_method)
                self.entry.bind("<FocusOut>", entry_method)

            if entry_numeric:
                self.entry.config(validate='all', validatecommand=(validate_numbers, '%d', '%P', '%S', entry_max_char))

            elif entry_max_char:
                self.entry.config(validate='all', validatecommand=(validate_chars, '%d', '%P', entry_max_char))

        # Button
        if True:
            self.button = ttk.Button(self, text=button_text, width=button_width)
            self.button.grid(row=0, column=2, sticky='ew', padx=2)

            if button_method:
                self.button.configure(command=button_method)

    def enable(self):
        self.label.config(style='TLabel')
        self.entry.config(state='normal')
        self.button.config(state='normal')

    def disable(self):
        self.label.config(style='secondary.TLabel')
        self.entry.config(state='disabled')
        self.button.config(state='disabled')

    def readonly(self):
        self.label.config(style='TLabel')
        self.entry.config(state='readonly')
        self.button.config(state='normal')

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)


class LabelComboButton (ttk.Frame):
    """
    Create a compound widget, with a label and a combo box within a ttk Frame.
    Input:
        parent - container in which the widgets will be created
        label_text - string to be shown on the label
        label_anchor - position of the text within the label
        label_width: label width in number of characters
        combo_value - initial value to show at the combo box (if any)
        combo_list - list of values to be shown at the combo box
        combo_width: combo box width in number of characters
        combo_method: method to associate when combo box is selected
        button_text: string to be shown on the label
        button_width: width of the label im characters
        button_method: method to bind to the label
    Methods:
        enable method:
            enables the widgets (state='normal')
        disable method:
            disables the widgets (state='disabled')
        get method:
            gets the value from the combo box widget
        set method:
            sets the value to the combo box widget
    """

    def __init__(self, parent,
                 label_text='Label:',
                 label_anchor='e',
                 label_width=None,
                 combo_value='',
                 combo_list=('No values informed',),
                 combo_width=None,
                 combo_method=None,
                 combo_method_2=None,
                 button_text='',
                 button_width=None,
                 button_method=None
                 ):

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

        # Combobox configuration
        if True:
            self.combo_list = combo_list
            self.variable = tk.StringVar(value=combo_value)
            self.combobox = ttk.Combobox(self, textvariable=self.variable, justify='center',
                                         values=combo_list, state='readonly')
            self.combobox.grid(row=0, column=1, sticky='ew', padx=2)

            if combo_width:
                self.combobox['width'] = combo_width

        # Combobox bind to method
        if combo_method:
            self.combobox.bind('<<ComboboxSelected>>', combo_method, add='+')
        if combo_method_2:
            self.combobox.bind('<<ComboboxSelected>>', combo_method_2, add='+')

        # Button
        if True:
            self.button = ttk.Button(self, text=button_text, width=button_width)
            self.button.grid(row=0, column=2, sticky='ew', padx=2)

            if button_method:
                self.button.configure(command=button_method)

    def enable(self):
        self.label.config(style='TLabel')
        self.combobox.config(state='readonly', values=self.combo_list)
        self.button.config(state='normal')

    def disable(self):
        self.label.config(style='secondary.TLabel')
        self.combobox.config(state='disabled')
        self.button.config(state='disabled')

    def readonly(self):
        self.label.config(style='TLabel')
        self.combobox.config(state='readonly', values=[])
        self.button.config(state='normal')

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)


class LabelText (ttk.Frame):
    """
    Create a compound widget, with a label and a text field.
    Input:
        parent: container in which the widgets will be created
        label_text: string to be shown on the label
        label_width: label width in number of characters
        label_anchor: position of the text within the label
        text_value: initial value to show at the text (if any)
        text_width: text width in number of characters
        text_method: method to associate when the text events
    Methods:
        enable method:
            enables the widgets (state='normal')
        disable method:
            disables the widgets (state='disabled')
        get method:
            gets the value from the entry widget
        set method:
            sets the value to the entry widget
    """

    def __init__(self, parent,
                 label_text='label:',
                 label_anchor='e',
                 label_width=None,
                 text_value='',
                 text_width=None,
                 text_height=None,
                 text_method=None,
                 sided=True):

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
        # Label
        if True:
            self.label = ttk.Label(self, text=label_text, anchor=label_anchor)
            if sided:
                self.label.grid(row=0, column=0, sticky='ne', padx=2, pady=2)
            else:
                self.label.grid(row=0, column=0, columnspan=2,
                                sticky='nsew', padx=2, pady=2)
            if label_width:
                self.label['width'] = label_width

        # Text
        if True:
            self.text = tk.Text(self, height=text_height, wrap=tk.WORD)
            self.disabled_color = parent.winfo_toplevel().style.colors.secondary
            self.enabled_color = self.text.cget('fg')
            if sided:
                self.text.grid(row=0, column=1, sticky='nsew', padx=2, pady=2)
            else:
                self.text.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)

            self.set(text_value)
            if text_width:
                self.text['width'] = text_width
            if text_height:
                self.text['height'] = text_height

        # Scroll bar
        if True:
            y_scroll = ttk.Scrollbar(self, orient='vertical', command=self.text.yview)
            if sided:
                y_scroll.grid(row=0, column=2, sticky='ns')
            else:
                y_scroll.grid(row=1, column=1, sticky='ns')
            self.text.configure(yscrollcommand=y_scroll.set)
            self.text.bind('<MouseWheel>', self.on_mouse_wheel)
            y_scroll.bind('<MouseWheel>', self.on_mouse_wheel)

        # Bind method
        if True:
            self.text.bind("<Return>", text_method)
            self.text.bind("<FocusOut>", text_method)

    def on_mouse_wheel(self, event):
        self.text.yview_scroll(int(-1 * event.delta / 120), 'units')

    def enable(self):
        self.label.config(style='TLabel')
        self.text.config(state='normal')
        self.text.config(fg=self.enabled_color)

    def disable(self):
        self.label.config(style='secondary.TLabel')
        self.text.config(state='disabled')
        self.text.config(fg=self.disabled_color)

    def readonly(self):
        self.label.config(style='TLabel')
        self.text.config(state='disabled')
        self.text.config(fg=self.enabled_color)

    def get(self):
        return str(self.text.get('1.0', tk.END)).rstrip('\n')

    def set(self, value):
        state = self.text.cget('state')
        self.text.config(state='normal')
        self.text.delete('1.0', tk.END)
        self.text.insert('1.0', value)
        self.text.config(state=state)


class LabelSpinbox(ttk.Frame):
    """
        Create a compound widget, with a label and a Spinbox.
        Input:
            parent: container in which the widgets will be created
            label_text: string to be shown on the label
            label_anchor - position of the text within the label
            label_width: label width in number of characters
            entry_width: entry width in number of characters
            entry_method: method to associate when the entry events
            entry_type: whether the value will be a float or an integer
            spin_start: initial value
            spin_end: end_value
            spin_increment: increment
        Methods:
            enable method:
                enables the widgets (state='normal')
            disable method:
                disables the widgets (state='disabled')
            read_only method:
                disabled edition of the entry widget (state='readonly')
            get method:
                gets the value from the entry widget
            set method:
                sets the value to the entry widget
        """

    def __init__(self, parent,
                 label_text='label:',
                 label_anchor='e',
                 label_width=None,
                 entry_width=None,
                 entry_method=None,
                 entry_type='float',
                 spin_start=0,
                 spin_end=10,
                 spin_increment=1,
                 spin_precision=1
                 ):

        # Parent class initialization
        super().__init__(parent)
        self.increment = spin_increment
        self.start = spin_start
        self.end = spin_end
        self.precision = spin_precision
        self.type = entry_type

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=0)

        # Label
        if True:
            self.label = ttk.Label(self, text=label_text, anchor=label_anchor)
            self.label.grid(row=0, column=0, sticky='ew', padx=2)

            if label_width:
                self.label['width'] = label_width

        # Spinbox
        if True:
            if self.type == 'float':
                value = spin_start
            else:
                value = int(spin_start)
                self.increment = int(self.increment)
                self.start = int(self.start)
                self.end = int(self.end)

            self.variable = tk.StringVar(value=str(value))

            self.spin = ttk.Spinbox(self, textvariable=self.variable, justify='center', command=self.spin_selected,
                                    from_=self.start, to=self.end, increment=self.increment)
            self.spin.grid(row=0, column=1, sticky='ew', padx=2)

            if entry_width:
                self.spin['width'] = entry_width

        # Bind method
        if True:
            self.spin.bind("<Return>", entry_method)
            self.spin.bind("<FocusOut>", entry_method)
            self.spin.bind("<<Increment>>", self._do_on_increment)
            self.spin.bind("<<Decrement>>", self._do_on_decrement)
            self.spin.bind("<ButtonRelease-1>", self.spin_selected, add='+')

    def spin_selected(self, event=None):
        self.update()
        current = float(self.variable.get().replace(',', '.'))
        if current < self.start:
            current = self.start
        elif current > self.end:
            current = self.end

        if self.type == 'int':
            self.variable.set(int(current))
        else:
            self.variable.set(current)
        self.spin.event_generate('<Return>')

    def enable(self):
        self.label.config(style='TLabel')
        self.spin.config(state='normal')

    def disable(self):
        self.label.config(style='secondary.TLabel')
        self.spin.config(state='disabled')

    def readonly(self):
        self.label.config(style='TLabel')
        self.spin.config(state='readonly')

    def _do_on_increment(self, *args, **kwargs):
        self.do_upon_clicking_arrows("up")
        return "break"

    def _do_on_decrement(self, *args, **kwargs):
        self.do_upon_clicking_arrows("down")
        return "break"

    def do_upon_clicking_arrows(self, direction):

        if direction == 'up':
            sign = 1
            if self.type == 'float':
                if float(self.get()) >= self.end:
                    self.set(self.end)

                else:
                    self.set(float(self.get()) + sign * self.increment)
            else:
                if int(self.get()) >= self.end:
                    self.set(int(self.end))

                else:
                    self.set(int(self.get()) + sign * self.increment)
        else:
            sign = -1
            if self.type == 'float':
                if float(self.get()) <= self.start:
                    self.set(self.start)

                else:
                    self.set(float(self.get()) + sign * self.increment)
            else:
                if int(self.get()) <= self.start:
                    self.set(int(self.start))

                else:
                    self.set(int(self.get()) + sign * self.increment)

    def get(self):
        return self.variable.get()

    def set(self, value):
        if self.type == 'int':
            self.variable.set(int(value))
        else:
            self.variable.set(round(value, self.precision))

