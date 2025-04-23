import tkinter as tk
import ttkbootstrap as ttk


class CheckLedButton(ttk.Frame):
    """
    Compound widget, with a color canvas (left) and a label (right).
    Input:
        parent: container for the frame
        label_text: string to be shown on the label
        label_width: width of the label im characters
        label_method: method to bind to the label
        style: bootstyle (color style)
        font: font for the label
        active_led_color: color for the selected state
        inactive_led_color: color for the unselected state
        relief: boolean, apply or not the relief
    User Methods:
        enable method(): enables the widgets (state='normal')
        disable method(): disables the widgets (state='disabled')
        is_disabled(): check whether the widget is currently disabled
        is_selected(): check whether the widget is currently selected
    """

    def __init__(self, parent, label_text='Label', label_width=10, label_method=None,
                 style='default', font=None,
                 active_led_color=None, inactive_led_color=None, relief=True):

        # Parent class initialization
        super().__init__(parent)
        self.parent = parent

        # Style definition
        if True:
            try:
                all_colors = parent.winfo_toplevel().style.colors
            except AttributeError:
                self.active_led_color = '#18bc9c'
                self.inactive_led_color = '#e74c3c'
                self.bg_led_color = '#7B8A8B'
                self.disabled_led_color = '#ECF0F1'
            else:
                self.active_led_color = all_colors.success
                self.inactive_led_color = all_colors.danger
                self.bg_led_color = all_colors.dark
                self.disabled_led_color = all_colors.light

            label_style_list = (
                'danger', 'warning', 'info', 'success', 'secondary', 'primary', 'light', 'dark', 'default',
                'inverse-danger', 'inverse-warning', 'inverse-info', 'inverse-success', 'inverse-secondary',
                'inverse-primary', 'inverse-light', 'inverse-dark', 'inverse-default'
            )
            if style not in label_style_list:
                self.style = 'default'
            else:
                self.style = style

            if active_led_color:
                self.active_led_color = active_led_color
            if inactive_led_color:
                self.inactive_led_color = inactive_led_color

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=0)
            self.columnconfigure(1, weight=1)

        # Canvas configuration
        if True:
            self.relief = relief
            self.color_canvas = tk.Canvas(self, bd=0, width=10, height=0, highlightthickness=0)
            self.color_canvas.grid(row=0, column=0, sticky='nsew')
            self.color_canvas.configure(background=self.inactive_led_color)
            if self.relief:
                self.color_canvas.config(relief='raised', borderwidth=1)

        # Label configuration
        if True:
            self.label = ttk.Label(self, text=label_text, anchor='w', bootstyle=self.style, width=label_width,
                                   padding=(5, 0, 0, 0))
            self.label.grid(row=0, column=1, sticky='nsew')
            if font:
                self.label.config(font=font)

        # Bind method
        if label_method and callable(label_method):
            self.label_method = label_method
        else:
            self.label_method = None
        self.color_canvas.bind('<ButtonRelease-1>', self._check_hover)
        self.label.bind('<ButtonRelease-1>', self._check_hover)

    def _check_hover(self, event):
        """ Checks whether the mouse is still over the widget before calling the assigned method """

        if str(self.label.cget('state')) == 'disabled':
            return

        widget_under_cursor = event.widget.winfo_containing(event.x_root, event.y_root)
        if widget_under_cursor in (self.color_canvas, self.label):
            if self.is_selected():
                self.deselect()
            else:
                self.select()
                if self.label_method:
                    self.label_method(event)

    def select(self, event=None):
        """ Canvas (led) color control """

        if str(self.label.cget('state')) == 'disabled':
            return
        self.color_canvas.config(bg=self.active_led_color)
        if self.relief:
            self.color_canvas.config(relief='sunken')

    def deselect(self, event=None):
        """ Canvas (led) color control """

        if str(self.label.cget('state')) == 'disabled':
            return
        self.color_canvas.config(bg=self.inactive_led_color)
        if self.relief:
            self.color_canvas.config(relief='raised')

    def enable(self):
        """ Enables the widget """

        self.label.config(state='normal')
        self.label.config(bootstyle=self.style)
        self.deselect()

    def disable(self):
        """ Disables the widget """

        self.color_canvas.config(bg=self.disabled_led_color)
        self.label.config(state='disabled')
        self.label.config(bootstyle='secondary')
        if self.relief:
            self.color_canvas.config(relief='raised')

    def is_selected(self):
        if self.color_canvas.cget('bg') == self.active_led_color:
            return True
        else:
            return False

    def is_disabled(self):
        if str(self.label.cget('state')) == 'disabled':
            return True
        return False


class CheckSwitchLedButton(ttk.Frame):
    """
    Compound widget, with a color canvas (left) and a label (right) which behaves as a Switch Check Button.
    Input:
        parent: container for the frame
        label_text: string to be shown on the label
        label_width: width of the label in characters
        label_method: method to bind to the label
        style: bootstyle for the label (color style)
        font: font for the label
        active_led_color: color for the selected state
        inactive_led_color: color for the unselected state
        relief: boolean, apply or not the relief
    User Methods:
        enable method(): enables the widgets (state='normal')
        disable method(): disables the widgets (state='disabled')
        is_disabled(): check whether the widget is currently disabled
        is_selected(): check whether the widget is currently selected
    """

    def __init__(self, parent, label_text='Label', label_width=10, label_method=None,
                 style='default', font=None,
                 active_led_color=None, inactive_led_color=None, relief=True):

        # Parent class initialization
        super().__init__(parent)
        self.parent = parent

        # Style definition
        if True:
            try:
                all_colors = parent.winfo_toplevel().style.colors
            except AttributeError:
                self.active_led_color = '#18bc9c'
                self.inactive_led_color = '#e74c3c'
                self.bg_led_color = '#7B8A8B'
                self.disabled_led_color = '#ECF0F1'
            else:
                self.active_led_color = all_colors.success
                self.inactive_led_color = all_colors.danger
                self.bg_led_color = all_colors.dark
                self.disabled_led_color = all_colors.light

            label_style_list = (
                'danger', 'warning', 'info', 'success', 'secondary', 'primary', 'light', 'dark', 'default',
                'inverse-danger', 'inverse-warning', 'inverse-info', 'inverse-success', 'inverse-secondary',
                'inverse-primary', 'inverse-light', 'inverse-dark', 'inverse-default'
            )
            if style not in label_style_list:
                self.style = 'default'
            else:
                self.style = style

            if active_led_color:
                self.active_led_color = active_led_color
            if inactive_led_color:
                self.inactive_led_color = inactive_led_color

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=0)
            self.columnconfigure(1, weight=0)
            self.columnconfigure(2, weight=1)

        # Canvas configuration
        if True:
            self.relief = relief
            self.color_canvas_1 = tk.Canvas(self, bd=0, width=10, height=0, highlightthickness=0)
            self.color_canvas_1.grid(row=0, column=0, sticky='nsew')
            self.color_canvas_1.configure(background=self.active_led_color)

            self.color_canvas_2 = tk.Canvas(self, bd=0, width=10, height=0, highlightthickness=0)
            self.color_canvas_2.grid(row=0, column=1, sticky='nsew')
            self.color_canvas_2.configure(background=self.bg_led_color)

            if self.relief:
                self.color_canvas_1.config(relief='raised', borderwidth=1)
                self.color_canvas_2.config(relief='sunken', borderwidth=1)

        # Label configuration
        if True:
            self.label = ttk.Label(self, text=label_text, anchor='w', bootstyle=self.style, width=label_width,
                                   padding=(5, 0, 0, 0))
            self.label.grid(row=0, column=2, sticky='nsew')
            if font:
                self.label.config(font=font)

        # Bind method
        if label_method and callable(label_method):
            self.label_method = label_method
        else:
            self.label_method = None
        self.color_canvas_1.bind('<ButtonRelease-1>', self._check_hover)
        self.color_canvas_2.bind('<ButtonRelease-1>', self._check_hover)
        self.label.bind('<ButtonRelease-1>', self._check_hover)

    def _check_hover(self, event):
        """ Checks whether the mouse is still over the widget before releasing the assigned method """

        if str(self.label.cget('state')) == 'disabled':
            return

        widget_under_cursor = event.widget.winfo_containing(event.x_root, event.y_root)
        if widget_under_cursor in (self.color_canvas_1, self.color_canvas_2, self.label):
            if self.is_selected():
                self.deselect()
            else:
                self.select()
                if self.label_method:
                    self.label_method(event)

    def select(self):
        """ Canvas (led) color control """

        if str(self.label.cget('state')) == 'disabled':
            return
        self.color_canvas_1.config(bg=self.active_led_color)
        self.color_canvas_2.config(bg=self.bg_led_color)

        if self.relief:
            self.color_canvas_1.config(relief='raised')
            self.color_canvas_2.config(relief='sunken')

    def deselect(self):
        """ Canvas (led) color control """

        if str(self.label.cget('state')) == 'disabled':
            return
        self.color_canvas_1.config(bg=self.bg_led_color)
        self.color_canvas_2.config(bg=self.inactive_led_color)

        if self.relief:
            self.color_canvas_1.config(relief='sunken')
            self.color_canvas_2.config(relief='raised')

    def enable(self):
        """ Enables the widget """

        self.label.config(state='normal')
        self.label.config(bootstyle=self.style)
        self.select()

    def disable(self):
        """ Disables the widget """

        self.color_canvas_1.config(bg=self.disabled_led_color)
        self.color_canvas_2.config(bg=self.bg_led_color)
        self.label.config(state='disabled')
        self.label.config(bootstyle='secondary')
        if self.relief:
            self.color_canvas_1.config(relief='raised')
            self.color_canvas_2.config(relief='sunken')

    def is_selected(self):
        if self.color_canvas_1.cget('bg') == self.active_led_color:
            return True
        else:
            return False

    def is_disabled(self):
        if str(self.label.cget('state')) == 'disabled':
            return True
        return False


class RadioLedButton(ttk.Frame):
    """
    Compound widget, with a color canvas and a label, which behaves as Radio Buttons.
    Input:
        parent: container for the frame
        label_text: string to be shown on the label
        label_width: width of the label im characters
        label_method: method to bind to the label
        style: bootstyle (color style)
        control_variable: variable that will group the buttons for "radio button" like operation
        font: label font
        active_led_color: color for the selected state
        inactive_led_color: color for the unselected state
        relief: boolean, apply or not the relief
    User Methods:
        enable method(): enables the widgets (state='normal')
        disable method(): disables the widgets (state='disabled')
        is_disabled(): check whether the widget is currently disabled
        is_selected(): check whether the widget is currently selected
    """

    control_variable_dict = {}

    def __init__(self, parent, label_text='Label', label_width=10, label_method=None,
                 style='default', control_variable=None, font=None, switch_type=False,
                 active_led_color=None, inactive_led_color=None, relief=True):

        # Parent class initialization
        super().__init__(parent)

        # Control variable
        self.control_variable = control_variable
        if control_variable in RadioLedButton.control_variable_dict:
            RadioLedButton.control_variable_dict[control_variable].append(self)
        else:
            RadioLedButton.control_variable_dict[control_variable] = [self]

        # Style definition
        if True:
            try:
                all_colors = parent.winfo_toplevel().style.colors
            except AttributeError:
                self.active_led_color = '#18bc9c'
                self.inactive_led_color = '#e74c3c'
                self.bg_led_color = '#7B8A8B'
                self.disabled_led_color = '#ECF0F1'
            else:
                self.active_led_color = all_colors.success
                self.inactive_led_color = all_colors.danger
                self.bg_led_color = all_colors.dark
                self.disabled_led_color = all_colors.light

            label_style_list = (
                'danger', 'warning', 'info', 'success', 'secondary', 'primary', 'light', 'dark', 'default',
                'inverse-danger', 'inverse-warning', 'inverse-info', 'inverse-success', 'inverse-secondary',
                'inverse-primary', 'inverse-light', 'inverse-dark', 'inverse-default'
            )
            if style not in label_style_list:
                self.style = 'default'
            else:
                self.style = style

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=1)

        # Buttons configuration
        if switch_type:
            self.b = CheckSwitchLedButton(self, label_text=label_text, label_width=label_width,
                                          label_method=self._check_hover, style=self.style, font=font,
                                          active_led_color=active_led_color, inactive_led_color=inactive_led_color,
                                          relief=relief)
            self.b.deselect()
        else:
            self.b = CheckLedButton(self, label_text=label_text, label_width=label_width,
                                    label_method=self._check_hover, style=self.style, font=font,
                                    active_led_color=active_led_color, inactive_led_color=inactive_led_color,
                                    relief=relief)
        self.b.grid(row=0, column=0, sticky='nsew')

        # Bind methods
        if label_method and callable(label_method):
            self.label_method = label_method
        else:
            self.label_method = None
        self.b.bind('<ButtonRelease-1>', self._check_hover, add='+')

    def _check_hover(self, event):
        """ Checks whether the mouse is still over the widget before calling the assigned method """

        if str(self.b.label.cget('state')) == 'disabled':
            return

        for widget in list(RadioLedButton.control_variable_dict[self.control_variable]):
            if str(widget) == str(self):
                widget.select()
                if self.label_method:
                    self.label_method(event)
            else:
                widget.deselect()

    def select(self):
        self.b.select()

    def deselect(self):
        self.b.deselect()

    def enable(self):
        self.b.enable()
        self.b.deselect()

    def disable(self):
        self.b.disable()

    def is_selected(self):
        return self.b.is_selected()

    def is_disabled(self):
        return self.b.is_disabled()
