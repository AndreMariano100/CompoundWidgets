import tkinter as tk
import tkinter.ttk as ttk


def float_only(action, value, text, max_length=None):
    """ Checks that only float related characters are accepted as input """

    permitted = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '-']
    if action == '1':
        if max_length:
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
        print(len(value))
        print(max_length)
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
        self.label.config(style='primary.TButton')

    def deselect(self, event=None):
        if str(self.label.cget('state')) == 'disabled':
            return
        self.color_canvas.config(bg=self.deselected_color)
        self.label.config(style='secondary.TButton')


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
        self.label.config(style='primary.TButton')

    def deselect(self):
        if str(self.label.cget('state')) == 'disabled':
            return
        self.color_canvas_1.config(bg=self.deselected_color)
        self.color_canvas_2.config(bg=self.bg_color)
        self.label.config(style='secondary.TButton')

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
        self.label.config(style='primary.TButton')

    def deselect(self):
        self.color_canvas.config(bg=self.deselected_color)
        self.label.config(style='secondary.TButton')

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
                 label_width=30,
                 entry_value='',
                 entry_numeric=False,
                 entry_width=10,
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
            self.label = ttk.Label(self, text=label_text, anchor=label_anchor, width=label_width)
            self.label.grid(row=0, column=0, sticky='ew', padx=2)

        # Entry
        if True:
            self.variable = tk.StringVar(value=entry_value)
            self.entry = ttk.Entry(self, textvariable=self.variable, justify='center', width=entry_width)
            self.entry.grid(row=0, column=1, sticky='ew', padx=2)

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
        return self.variable.get()

    def set_entry(self, value):
        self.variable.set(value)

    def get_unit(self):
        return self.unit_combo.get()

    def set_unit(self, value):
        self.unit_combo.set(value)

    def get(self):
        return self.variable.get(), self.unit_combo.get()

    def set(self, value, unit):
        self.variable.set(value)
        if unit in list(self.unit_combo.cget('values')):
            self.unit_combo.set(value)
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
                 label_width=10,
                 combo_value='',
                 combo_list=('No values informed',),
                 combo_width=20,
                 combo_method=None):

        # Parent class initialization
        super().__init__(parent)

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=0)

        # Label configuration
        if True:
            self.label = ttk.Label(self, text=label_text, anchor=label_anchor, width=label_width)
            self.label.grid(row=0, column=0, sticky='ew', padx=2)

        # Combo box configuration
        if True:
            self.combo_list = combo_list
            self.variable = tk.StringVar(value=combo_value)
            self.combobox = ttk.Combobox(self, textvariable=self.variable, justify='center', width=combo_width,
                                         values=combo_list, state='readonly')
            self.combobox.grid(row=0, column=1, sticky='ew', padx=2)

        # Bind method
        if True:
            self.combobox.bind('<<ComboboxSelected>>', combo_method)

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
                 label_width=10,
                 entry_numeric=False,
                 entry_width=20,
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
            self.label = ttk.Label(self, text=label_text, anchor=label_anchor, width=label_width)
            self.label.grid(row=0, column=0, sticky='ew', padx=2)

        # Entry
        if True:
            self.variable = tk.StringVar(value=entry_value)
            self.entry = ttk.Entry(self, textvariable=self.variable, justify='center', width=entry_width)
            self.entry.grid(row=0, column=1, sticky='ew', padx=2)

        # Restrict numeric values
        if entry_numeric:
            self.entry.config(validate='all', validatecommand=(validate_numbers, '%d', '%P', '%S', entry_max_char))

        # Restrict max characters
        elif entry_max_char:
            self.entry.config(validate='all', validatecommand=(validate_chars, '%d', '%P', entry_max_char))

        # Bind method
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
                 label_width=20,
                 text_value='',
                 text_width=20,
                 text_height=3,
                 text_method=None):

        # Parent class initialization
        super().__init__(parent)

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=0)
            self.columnconfigure(1, weight=1)
            self.columnconfigure(2, weight=0)

        # Label
        if True:
            self.label = ttk.Label(self, text=label_text, anchor=label_anchor, width=label_width)
            self.label.grid(row=0, column=0, sticky='ne', padx=2, pady=2)

        # Text
        if True:
            self.text = tk.Text(self, width=text_width, height=text_height, wrap=tk.WORD)
            self.text.grid(row=0, column=1, sticky='nsew', padx=2, pady=2)
            self.set(text_value)

        # Scroll bar
        if True:
            y_scroll = ttk.Scrollbar(self, orient='vertical', command=self.text.yview)
            y_scroll.grid(row=0, column=2, sticky='ns')
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

    def disable(self):
        self.label.config(style='secondary.TLabel')
        self.text.config(state='disabled')

    def get(self):
        return str(self.text.get('1.0', tk.END)).rstrip('\n')

    def set(self, value):
        self.text.delete('1.0', tk.END)
        self.text.insert('1.0', value)


if __name__ == '__main__':
    from ttkbootstrap import Style

    root = tk.Tk()
    root.style = Style()
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    # First frame, testing LedButtons
    if True:
        root.columnconfigure(0, weight=1)
        frame = ttk.LabelFrame(root, text='Regular Buttons')
        frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        frame.columnconfigure(0, weight=1)

        led_button_1 = LedButton(frame, label_text='First Button', label_width=20,
                                 label_method=lambda e: print('first led button'))
        led_button_1.grid(row=0, column=0, sticky='nsew', pady=(10, 0), padx=10)

        led_button_2 = LedButton(frame, label_text='Second Button', label_width=10,
                                 label_method=lambda e: print('second led button'))
        led_button_2.grid(row=1, column=0, sticky='nsew', pady=(10, 0), padx=10)

        led_button_3 = LedButton(frame, label_text='Third Button', label_width=15,
                                 label_method=lambda e: print('third led button'))
        led_button_3.grid(row=2, column=0, sticky='nsew', pady=10, padx=10)
        led_button_3.disable()

    # Second frame, testing the CheckLedButton
    if True:
        root.columnconfigure(1, weight=1)
        frame = ttk.LabelFrame(root, text='Check Buttons')
        frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

        frame.columnconfigure(0, weight=1)

        led_button_1 = CheckLedButton(frame, label_text='First Button', label_width=20,
                                      label_method=lambda e: print('first led button'))
        led_button_1.grid(row=0, column=0, sticky='nsew', pady=(10, 0), padx=10)

        led_button_2 = CheckLedButton(frame, label_text='Second Button', label_width=10,
                                      label_method=lambda e: print('second led button'))
        led_button_2.grid(row=1, column=0, sticky='nsew', pady=(10, 0), padx=10)

        led_button_3 = CheckLedButton(frame, label_text='Third Button', label_width=15,
                                      label_method=lambda e: print('third led button'))
        led_button_3.grid(row=2, column=0, sticky='nsew', pady=10, padx=10)
        led_button_3.disable()

    # Third frame, testing the RadioLedButton
    if True:
        root.columnconfigure(2, weight=1)
        frame = ttk.LabelFrame(root, text='Radio Buttons', padding=10)
        frame.grid(row=0, column=2, sticky='nsew', padx=10, pady=10)

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        all_buttons = []
        for i in range(3):
            led_button = RadioLedButton(frame, label_text=f'Button {i}', control_variable='first group',
                                        label_method=lambda e: print('first group'))
            led_button.grid(row=i, column=0, sticky='nsew', pady=(0, 10), padx=10)
            all_buttons.append(led_button)


        for i in range(3, 6):
            led_button = RadioLedButton(frame, label_text=f'Button {i}', control_variable='second group',
                                        label_method=lambda e: print('second group'))
            led_button.grid(row=i-3, column=1, sticky='nsew', pady=(0, 10), padx=10)
            all_buttons.append(led_button)

        all_buttons[0].select()
        all_buttons[3].select()

    # Fourth frame, testing LabelEntryUnits
    if True:
        def get_all_values(event):
            for w in all_label_entry_units:
                print('Separate data:', w.get_entry(), w.get_unit(), end=' / ')
                print('Altogether:', w.get(), end=' / ')
                print('Converted:', w.get_metric_value())

        root.columnconfigure(3, weight=1)
        frame = ttk.LabelFrame(root, text='Label-Entry-Units')
        frame.grid(row=0, column=3, sticky='nsew', padx=10, pady=10)

        frame.columnconfigure(0, weight=1)
        unit_options = ('temperature', 'length', 'pressure', 'stress', 'force', 'moment', 'none')

        all_label_entry_units = []
        for i, item in enumerate(unit_options):
            w = LabelEntryUnit(frame, label_text=str(item).capitalize(), label_width=20, entry_value='0',
                               entry_numeric=True, entry_width=10, entry_max_char=6, entry_method=get_all_values,
                               combobox_unit=item, combobox_unit_width=6)
            w.grid(row=i, column=0, sticky='nsew', pady=5, padx=10)
            all_label_entry_units.append(w)

        all_label_entry_units[-1].disable()
        all_label_entry_units[-2].readonly()

    # Fifth frame, testing LabelCombo
    if True:
        frame = ttk.LabelFrame(root, text='Label Combos')
        frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        frame.columnconfigure(0, weight=1)
        local_list = ('Label Combo 1', 'Label Combo 2', 'Label Combo 3', 'Label Combo 4')
        for i, item in enumerate(local_list):
            w = LabelCombo(frame, label_text=item, combo_list=local_list)
            w.grid(row=i, column=0, sticky='nsew')

    # Sixth frame, testing LabelEntry
    if True:
        frame = ttk.LabelFrame(root, text='Label Entries')
        frame.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)
        frame.columnconfigure(0, weight=1)
        local_list = ('Label Entry 1', 'Label Entry 2', 'Label Entry 3', 'Label Entry 4')
        for i, item in enumerate(local_list):
            w = LabelEntry(frame, label_text=item, entry_max_char=5)
            w.grid(row=i, column=0, sticky='nsew')

    # Seventh frame, testing LabelText
    if True:
        frame = ttk.LabelFrame(root, text='Label Text')
        frame.grid(row=1, column=2, columnspan=2, sticky='nsew', padx=10, pady=10)
        frame.columnconfigure(0, weight=1)
        local_list = ('Label Text 1', 'Label Text 2')
        for i, item in enumerate(local_list):
            w = LabelText(frame, label_text=item)
            w.grid(row=0, column=i, sticky='nsew')


    root.mainloop()