import tkinter as tk
import tkinter.ttk as ttk


class RadioLedButton(ttk.Frame):
    """
    Create a compound widget, with a color canvas and a label.
    The set of instance with the same control variable will work as radio buttons.
    Input:
        parent: container in which the widgets will be created
        label_text: string to be shown on the label
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

    def __init__(self, parent, label_text='Label', label_method=None, control_variable=None, font=('OpenSans', 12)):
        super().__init__(parent)
        self.label_text = label_text
        self.label_method = label_method
        self.control_variable = control_variable

        if control_variable in self.control_variable_dict:
            self.control_variable_dict[control_variable].append(self)
        else:
            self.control_variable_dict[control_variable] = [self]

        style = parent.winfo_toplevel().style
        self.selected_color = style.colors.info
        self.deselected_color = 'white'
        self.disabled_color = style.colors.light

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)

        self.color_canvas = tk.Canvas(self, bg=self.deselected_color, bd=0, width=10, height=0, highlightthickness=0)
        self.color_canvas.grid(row=0, column=0, sticky='nsew')

        self.label = ttk.Label(self, text=f'  {label_text}', anchor='w', justify='left', style='secondary.TButton',
                               padding=1, font=font)
        self.label.grid(row=0, column=1, sticky='nsew')

        if self.label_method:
            self.label.bind('<ButtonRelease-1>', self.check_hover)

    def check_hover(self, event):
        widget_under_cursor = event.widget.winfo_containing(event.x_root, event.y_root)
        if widget_under_cursor != event.widget:
            print('Other widget')
            return

        if self.label.cget('state') == 'disabled':
            print('Widget disabled')
            return

        for widget in list(self.control_variable_dict[self.control_variable]):
            if str(widget) == str(event.widget.winfo_parent()):
                widget.select()
            else:
                widget.deselect()

        self.label_method(event)

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
    Creates a compound widget, with a label and an entry field.
    Input:
        parent: container in which the widgets will be created
        label_text: string to be shown on the label
        label_anchor: position of the text within the label
        label_width: width of the label in characters
        entry_value: initial value to show at the entry (if any)
        entry_numeric: whether the entry accepts only numbers
        entry_width: entry width in number of characters
        entry_method: method to associate when the entry events
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
    """

    class LengthCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            length_list = ('mm', 'in')
            self.variable = tk.StringVar(value=length_list[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=length_list,
                           state='readonly')

        def get(self):
            return self.variable.get()

        def set(self, value):
            self.variable.set(value)

    class TemperatureCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.temperature_list = ('°C', '°F')
            self.variable = tk.StringVar(value=self.temperature_list[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.temperature_list,
                           state='readonly')

        def get(self):
            return self.variable.get()

        def set(self, value):
            if value in self.temperature_list:
                self.variable.set(value)

    class PressureCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.pressure_list = ('MPa', 'kgf/cm²', 'psi', 'bar', 'kPa', 'ksi')
            self.variable = tk.StringVar(value=self.pressure_list[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.pressure_list,
                           state='readonly')

        def get(self):
            return self.variable.get()

        def set(self, value):
            if value in self.pressure_list:
                self.variable.set(value)

    class StressCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.stress_list = ('MPa', 'GPa', 'ksi', 'psi')
            self.variable = tk.StringVar(value=self.stress_list[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.stress_list,
                           state='readonly')

        def get(self):
            return self.variable.get()

        def set(self, value):
            self.variable.set(value)

    class ForceCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.force_list = ('kgf', 'N', 'lbf')
            self.variable = tk.StringVar(value=self.force_list[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.force_list,
                           state='readonly')

        def get(self):
            return self.variable.get()

        def set(self, value):
            self.variable.set(value)

    class MomentCombo(ttk.Combobox):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.moment_list = ('kgf.m', 'N.m', 'lbf.ft')
            self.variable = tk.StringVar(value=self.moment_list[0])
            self.configure(textvariable=self.variable, justify='center', width=width, values=self.moment_list,
                           state='readonly')

    class NoUnitCombo(ttk.Label):
        def __init__(self, parent, width):
            super().__init__(parent)

            self.variable = tk.StringVar(value='none')
            self.configure(text=' ', width=width)

        def get(self):
            return self.variable.get()

        def set(self, value):
            self.variable.set(value)

    unit_dict = {'length': LengthCombo,
                 'temperature': TemperatureCombo,
                 'pressure': PressureCombo,
                 'stress': StressCombo,
                 'force': ForceCombo,
                 'moment': MomentCombo,
                 'none': NoUnitCombo
                 }

    def __init__(self, parent,
                 label_text='label:',
                 label_anchor='e',
                 label_width=30,
                 entry_value='',
                 entry_numeric=False,
                 entry_width=20,
                 method=None,
                 combobox_unit=None,
                 combobox_unit_width=8
                 ):

        # Parent class initialization
        super().__init__(parent)

        # Entry validation for numbers
        validate_numbers = self.register(self.float_only)

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

        # Unit Combobox
        if True:
            if not combobox_unit:
                combobox_unit = 'none'
            local_class = LabelEntryUnit.unit_dict.get(combobox_unit.lower(), None)
            my_error_string = 'Unit not found.'
            if not local_class:
                raise Exception(my_error_string)
            self.unit_combo = LabelEntryUnit.unit_dict.get(combobox_unit.lower(), None)(self, combobox_unit_width)
            self.unit_combo.grid(row=0, column=2, sticky='ew', padx=2)

        # Bind method
        if True:
            self.entry.bind("<Return>", method)
            self.entry.bind("<FocusOut>", method)
            self.unit_combo.bind("<<ComboboxSelected>>", method)

    def enable(self):
        self.label.config(style='TLabel')
        self.entry.config(state='normal')
        self.unit_combo.config(state='readonly')

    def disable(self):
        self.label.config(style='secondary.TLabel')
        self.entry.config(state='disabled')
        self.unit_combo.config(state='disabled')

    def readonly(self):
        self.label.config(style='TLabel')
        self.entry.config(state='readonly')
        self.unit_combo.config(state='readonly')

    def get_entry(self):
        return self.variable.get()

    def set_entry(self, value):
        self.variable.set(value)

    def get_unit(self):
        return self.unit_combo.get()

    def set_unit(self, value):
        self.unit_combo.set(value)

    @staticmethod
    def float_only(action, value, text):
        """ Checks that only float related characters are accepted as input """

        permitted = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '-']
        if action == '1':
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
            self.variable = tk.StringVar(value=combo_value)
            self.combobox = ttk.Combobox(self, textvariable=self.variable, justify='center', width=combo_width,
                                         values=combo_list, state='readonly')
            self.combobox.grid(row=0, column=1, sticky='ew', padx=2)

        # Bind method
        if True:
            self.combobox.bind('<<ComboboxSelected>>', combo_method)

    def enable(self):
        self.label.config(style='TLabel')
        self.combobox.config(state='readonly')

    def disable(self):
        self.label.config(style='secondary.TLabel')
        self.combobox.config(state='disabled')

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
                 entry_method=None):

        # Parent class initialization
        super().__init__(parent)

        # Entry validation for numbers
        validate_numbers = self.register(self.float_only)

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
            self.entry.config(validate='all', validatecommand=(validate_numbers, '%d', '%P', '%S'))

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

    @staticmethod
    def float_only(action, value, text):
        """ Checks that only float related characters are accepted as input """

        permitted = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '-']
        if action == '1':
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
                 text_method=None):

        # Parent class initialization
        super().__init__(parent)

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=0)
            self.columnconfigure(2, weight=0)

        # Label
        if True:
            self.label = ttk.Label(self, text=label_text, anchor=label_anchor, width=label_width)
            self.label.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)

        # text
        if True:
            self.text = tk.Text(self, width=text_width, height=2, wrap=tk.WORD)
            self.text.grid(row=0, column=1, sticky='nsew', padx=2, pady=2)
            self.set(text_value)

        # scroll bar
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


class LedButton (ttk.Frame):
    """
    Create a compound widget, with a color canvas and a label.
    Input:
        parent: container in which the widgets will be created
        label_text: string to be shown on the label
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

    def __init__(self, parent, label_text='Label', label_method=None):

        # Parent class initialization
        super().__init__(parent)
        self.label_text = label_text
        self.label_method = label_method

        # Gets the current style from the top level container
        style = parent.winfo_toplevel().style

        # Gets the active/inactive colors from the style
        if True:
            self.selected_color = style.colors.info
            self.deselected_color = 'white'
            self.disable_color = style.colors.light

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=0)
            self.columnconfigure(1, weight=1)

        # Canvas
        if True:
            self.color_canvas = tk.Canvas(self, bg=self.deselected_color, bd=0, width=10,
                                          height=0, highlightthickness=0)
            self.color_canvas.grid(row=0, column=0, sticky='nsew')

        # Label
        if True:
            self.label = ttk.Label(self, text=label_text, anchor='w', justify='left', style='secondary.TButton',
                                   padding=2)
            self.label.grid(row=0, column=1, sticky='nsew')

        # Bind method
        if self.label_method:
            self.label.bind('<ButtonRelease-1>', self.check_hover)

    def check_hover(self, event):
        """ Checks whether the mouse is still over the widget before releasing the assigned method """

        widget_under_cursor = event.widget.winfo_containing(event.x_root, event.y_root)
        if widget_under_cursor != event.widget:
            return
        if self.label.cget('state') == 'disabled':
            return
        self.label_method(event)

    def enable(self):
        self.color_canvas.config(bg=self.deselected_color)
        self.label.config(state='normal')

    def disable(self):
        self.color_canvas.config(bg=self.disable_color)
        self.label.config(state='disabled')

    def select(self):
        self.color_canvas.config(bg=self.selected_color)
        self.label.config(style='primary.TButton')

    def deselect(self):
        self.color_canvas.config(bg=self.deselected_color)
        self.label.config(style='secondary.TButton')

    def is_selected(self):
        if self.color_canvas.cget('bg') == self.selected_color:
            return True
        else:
            return False
