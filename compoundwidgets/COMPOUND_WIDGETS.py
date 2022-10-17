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
    Methods:
        enable method:
            enables the widgets (state='normal')
        disable method:
            disables the widgets (state='disabled')
        read_only method:
            disabled edition of the entry widget (state='readonly')
        get_entry method:
            gets the value from the entry widget
        set_entry method:
            sets the value to the entry widget
        get_unit method:
            gets the value from the unit widget
        set_unit method:
            sets the value from the unit widget
        get_metric_value:
            gets the value from the entry widget already converted for the metric (SI) unit
    """

    class TemperatureCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('°C', '°F')
            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

        def get(self):
            return self.variable.get()

        def set(self, value):
            if value in self.values:
                self.variable.set(value)

    class LengthCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('mm', 'in')
            self.conversion_values = (1, 25.4)

            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

        def get(self):
            return self.variable.get()

        def set(self, value):
            self.variable.set(value)

    class PressureCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('MPa', 'kgf/cm²', 'psi', 'bar', 'kPa', 'ksi')
            self.conversion_values = (1, 0.0980665, 0.006894757, 0.1, 0.001, 6.894757)
            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

        def get(self):
            return self.variable.get()

        def set(self, value):
            if value in self.values:
                self.variable.set(value)

    class StressCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('MPa', 'GPa', 'psi', 'ksi')
            self.conversion_values = (1, 1000, 0.006894757, 6.894757)
            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

        def get(self):
            return self.variable.get()

        def set(self, value):
            self.variable.set(value)

    class ForceCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.values = ('N', 'kgf', 'lbf')
            self.conversion_values = (1, 9.80665, 4.448222)
            self.variable = tk.StringVar(value=self.values[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.values,
                           state='readonly')

        def get(self):
            return self.variable.get()

        def set(self, value):
            self.variable.set(value)

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

        def get(self):
            return self.variable.get()

        def set(self, value):
            self.variable.set(value)

    unit_dict = {
        'temperature': TemperatureCombo,
        'length': LengthCombo,
        'pressure': PressureCombo,
        'stress': StressCombo,
        'force': ForceCombo,
        'moment': MomentCombo,
        'none': NoUnitCombo
    }

    def __init__(self, parent,
                 label_text='Label:',
                 label_anchor='e',
                 label_width=None,
                 entry_value='',
                 entry_numeric=False,
                 entry_width=None,
                 entry_max_char=None,
                 entry_method=None,
                 combobox_unit=None,
                 combobox_unit_width=8
                 ):

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

            self.unit_combo = local_class(self, combobox_unit_width)
            self.unit_combo.grid(row=0, column=2, sticky='ew', padx=2)

        # Bind method
        if True:
            self.entry.bind("<Return>", entry_method)
            self.entry.bind("<FocusOut>", entry_method)
            self.unit_combo.bind("<<ComboboxSelected>>", entry_method)

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
        self.unit_combo.config(state='readonly', values=[])

    def get_entry(self):
        return self.variable.get() or 0

    def set_entry(self, value):
        self.variable.set(value)

    def get_unit(self):
        return self.unit_combo.get()

    def set_unit(self, value):
        self.unit_combo.set(value)

    def get(self):
        return self.get_entry(), self.get_unit()

    def set(self, value, unit):
        self.variable.set(value)
        if unit in list(self.unit_combo.values):
            self.set_entry(value)
            self.set_unit(unit)
        else:
            raise Exception('Unit not found in current units dictionary.')

    def get_metric_value(self):

        if isinstance(self.unit_combo, LabelEntryUnit.NoUnitCombo):
            return self.get_entry(), '-'

        if isinstance(self.unit_combo, LabelEntryUnit.TemperatureCombo):
            if str(self.unit_combo.get()) == '°F':
                return 5 * (float(self.get_entry()) - 32) / 9, self.unit_combo.values[0]
            return self.get_entry(), self.unit_combo.values[0]

        index = self.unit_combo.values.index(self.get_unit())
        return float(self.get_entry()) * self.unit_combo.conversion_values[index], self.unit_combo.values[0]

    def check_length(self, event):
        current = self.get_entry()
        if len(current) >= self.entry_max_char:
            self.set_entry(current[:int(self.entry_max_char)])


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
            self.variable = tk.DoubleVar(value=spin_start)
            self.spin = ttk.Spinbox(self, textvariable=self.variable, justify='center',
                                    from_=spin_start, to=spin_end, increment=spin_increment)
            self.spin.grid(row=0, column=1, sticky='ew', padx=2)

            if entry_width:
                self.spin['width'] = entry_width

        # Bind method
        if True:
            self.spin.bind("<Return>", entry_method)
            self.spin.bind("<FocusOut>", entry_method)
            self.spin.bind("<<Increment>>", self._do_on_increment)
            self.spin.bind("<<Decrement>>", self._do_on_decrement)

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
            if self.get() >= self.end:
                self.set(self.end)

            else:
                self.set(self.get() + sign * self.increment)
        else:
            sign = -1
            if self.get() <= self.start:
                self.set(self.start)

            else:
                self.set(self.get() + sign * self.increment)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(round(value, self.precision))

