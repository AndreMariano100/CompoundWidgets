import tkinter as tk
import ttkbootstrap as ttk


class LedButton (ttk.Frame):
    """
    Compound widget, with a color canvas (left) and a label (right).
    Input:
        parent: container for the frame
        label_text: string to be shown on the label
        label_width: width of the label im characters
        label_method: method to bind to the label
        style: bootstyle (color style)
        font: font for the label
        led_color: color for the active state
        bg color: color for the canvas background

    User Methods:
        enable method(): enables the widgets (state='normal')
        disable method(): disables the widgets (state='disabled')
        is_disabled(): check whether the widget is currently disabled
    """

    def __init__(self, parent, label_text='Label', label_width=10, label_method=None, style='primary', font=None,
                 led_color=None, bg_color=None):

        # Parent class initialization
        super().__init__(parent)

        # Style definition
        if True:
            self.label_style_dict = {
                'danger': 'inverse-danger',
                'warning': 'inverse-warning',
                'info': 'inverse-info',
                'success': 'inverse-success',
                'secondary': 'inverse-secondary',
                'primary': 'inverse-primary',
                'light': 'inverse-light',
                'dark': 'inverse-dark',
                'fg': 'inverse-fg',
                'bg': 'inverse-bg',
                'selectfg': 'inverse-selectfg',
                'selectbg': 'inverse-selectbg'
            }
            if style not in list(self.label_style_dict.keys()):
                self.style = 'primary'
            else:
                self.style = style

            self.label_style = self.label_style_dict.get(style)
            if led_color:
                self.led_color = led_color
            else:
                self.led_color = 'snow'
            if bg_color:
                self.bg_color = bg_color
            else:
                self.bg_color = 'gray30'
            self.disable_color = 'gray60'

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=0)
            self.columnconfigure(1, weight=1)
            self.configure(bootstyle=self.style)

        # Canvas configuration
        if True:
            self.color_canvas = tk.Canvas(self, bd=0, width=10, height=0, highlightthickness=0)
            self.color_canvas.grid(row=0, column=0, sticky='nsew')
            self.color_canvas.configure(background=self.bg_color)

        # Label configuration
        if True:
            self.label = ttk.Label(self, text=label_text, anchor='w', bootstyle=self.label_style, width=label_width)
            self.label.grid(row=0, column=1, sticky='nsew', padx=(5, 0))
            if font:
                self.label.config(font=font)

        # Bind method
        self.label_method = label_method
        self.color_canvas.bind('<Button-1>', self._select)
        self.label.bind('<Button-1>', self._select)
        self.color_canvas.bind('<ButtonRelease-1>', self._check_hover)
        self.label.bind('<ButtonRelease-1>', self._check_hover)

    def _check_hover(self, event):
        """ Checks whether the mouse is still over the widget before calling the assigned method """

        if str(self.label.cget('state')) == 'disabled':
            return

        self._deselect()
        current_widget = event.widget.winfo_containing(event.x_root, event.y_root)
        if current_widget == event.widget:
            self.label_method(event)

    def _select(self, event=None):
        """ Canvas (led) color control """
        if str(self.label.cget('state')) == 'disabled':
            return
        self.color_canvas.config(bg=self.led_color)

    def _deselect(self, event=None):
        """ Canvas (led) color control """
        if str(self.label.cget('state')) == 'disabled':
            return
        self.color_canvas.config(bg=self.bg_color)

    def enable(self):
        self.label.config(state='normal')
        self.color_canvas.config(bg=self.bg_color)
        self.config(bootstyle=self.style)
        self.label.config(bootstyle=self.label_style)

    def disable(self):
        self.label.config(state='disabled')
        self.color_canvas.config(bg=self.disable_color)
        self.config(bootstyle='secondary')
        self.label.config(bootstyle='inverse-secondary')

    def is_disabled(self):
        if str(self.label.cget('state')) == 'disabled':
            return True
        return False


class CheckLedButton (ttk.Frame):
    """
    Compound widget, with a color canvas (left) and a label (right) which behaves as a Check Button.
    Input:
        parent: container for the frame
        label_text: string to be shown on the label
        label_width: width of the label im characters
        label_method: method to bind to the label
        style: bootstyle (color style)
        font: font for the label
        led_color: color for the active state
        unselect_color: color for the inactive state
        bg color: color for the canvas background
    User Methods:
        enable method(): enables the widgets (state='normal')
        disable method(): disables the widgets (state='disabled')
        is_disabled(): check whether the widget is currently disabled
        is_selected(): check whether the widget is currently selected
    """

    def __init__(self, parent, label_text='Label', label_width=10, label_method=None, style='primary', font=None,
                 led_color=None, bg_color=None, unselect_color=None):

        # Parent class initialization
        super().__init__(parent)

        # Style definition
        if True:
            self.label_style_dict = {
                'danger': 'inverse-danger',
                'warning': 'inverse-warning',
                'info': 'inverse-info',
                'success': 'inverse-success',
                'secondary': 'inverse-secondary',
                'primary': 'inverse-primary',
                'light': 'inverse-light',
                'dark': 'inverse-dark',
            }
            if style not in list(self.label_style_dict.keys()):
                self.style = 'primary'
            else:
                self.style = style

            self.label_style = self.label_style_dict.get(style)

            if led_color:
                self.led_color = led_color
            else:
                self.led_color = 'snow'

            if bg_color:
                self.bg_color = bg_color
            else:
                self.bg_color = 'gray30'

            if unselect_color:
                self.unselect_color = unselect_color
            else:
                self.unselect_color = 'gray30'

            self.disable_color = 'gray40'

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=0)
            self.columnconfigure(1, weight=0)
            self.columnconfigure(2, weight=1)
            self.configure(bootstyle=self.style)

        # Canvas configuration
        if True:
            self.color_canvas_1 = tk.Canvas(self, bd=0, width=10, height=0, highlightthickness=0)
            self.color_canvas_1.grid(row=0, column=0, sticky='nsew')
            self.color_canvas_1.configure(background=self.led_color)

            self.color_canvas_2 = tk.Canvas(self, bd=0, width=10, height=0, highlightthickness=0)
            self.color_canvas_2.grid(row=0, column=1, sticky='nsew')
            self.color_canvas_2.configure(background=self.bg_color)

        # Label configuration
        if True:
            self.label = ttk.Label(self, text=label_text, anchor='w', bootstyle=self.label_style, width=label_width)
            self.label.grid(row=0, column=2, sticky='nsew', padx=(5, 0))
            if font:
                self.label.config(font=font)

        # Bind method
        self.label_method = label_method
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
                self._deselect()
            else:
                self._select()
            self.label_method(event)

    def _select(self):
        if str(self.label.cget('state')) == 'disabled':
            return
        self.color_canvas_1.config(bg=self.led_color)
        self.color_canvas_2.config(bg=self.bg_color)

    def _deselect(self):
        if str(self.label.cget('state')) == 'disabled':
            return
        self.color_canvas_1.config(bg=self.bg_color)
        self.color_canvas_2.config(bg=self.unselect_color)

    def enable(self):
        self.color_canvas_1.config(bg=self.led_color)
        self.color_canvas_2.config(bg=self.bg_color)
        self.label.config(state='normal')
        self.config(bootstyle=self.style)
        self.label.config(bootstyle=self.label_style)

    def disable(self):
        self.color_canvas_1.config(bg=self.disable_color)
        self.color_canvas_2.config(bg=self.bg_color)
        self.label.config(state='disabled')
        self.config(bootstyle='secondary')
        self.label.config(bootstyle='inverse-secondary')

    def is_selected(self):
        if self.color_canvas_2.cget('bg') == self.bg_color:
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
        led_color: color for the active state
        bg color: color for the canvas background
    User Methods:
        enable method(): enables the widgets (state='normal')
        disable method(): disables the widgets (state='disabled')
        is_disabled(): check whether the widget is currently disabled
        is_selected(): check whether the widget is currently selected
    """

    control_variable_dict = {}

    def __init__(self, parent, label_text='Label', label_width=10, label_method=None, style='primary',
                 control_variable=None, font=None, led_color=None, bg_color=None):

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
            self.label_style_dict = {
                'danger': 'inverse-danger',
                'warning': 'inverse-warning',
                'info': 'inverse-info',
                'success': 'inverse-success',
                'secondary': 'inverse-secondary',
                'primary': 'inverse-primary',
                'light': 'inverse-light',
                'dark': 'inverse-dark',
                'fg': 'inverse-fg',
                'bg': 'inverse-bg',
                'selectfg': 'inverse-selectfg',
                'selectbg': 'inverse-selectbg'
            }
            if style not in list(self.label_style_dict.keys()):
                self.style = 'primary'
            else:
                self.style = style

            self.label_style = self.label_style_dict.get(style)
            if led_color:
                self.led_color = led_color
            else:
                self.led_color = 'snow'
            if bg_color:
                self.bg_color = bg_color
            else:
                self.bg_color = 'gray30'
            self.disable_color = 'gray60'

        # Frame configuration
        if True:
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=0)
            self.columnconfigure(1, weight=1)
            self.configure(bootstyle=self.style)

        # Canvas configuration
        if True:
            self.color_canvas = tk.Canvas(self, bd=0, width=10, height=0, highlightthickness=0)
            self.color_canvas.grid(row=0, column=0, sticky='nsew')
            self.color_canvas.configure(background=self.bg_color)

        # Label configuration
        if True:
            self.label = ttk.Label(self, text=label_text, anchor='w', bootstyle=self.label_style, width=label_width)
            self.label.grid(row=0, column=1, sticky='nsew', padx=(5, 0))
            if font:
                self.label.config(font=font)

        # Bind method
        self.label_method = label_method
        self.color_canvas.bind('<ButtonRelease-1>', self._check_hover)
        self.label.bind('<ButtonRelease-1>', self._check_hover)

    def _check_hover(self, event):
        """ Checks whether the mouse is still over the widget before calling the assigned method """

        if str(self.label.cget('state')) == 'disabled':
            return

        widget_under_cursor = event.widget.winfo_containing(event.x_root, event.y_root)
        if widget_under_cursor not in (self.color_canvas, self.label):
            return

        for widget in list(self.control_variable_dict[self.control_variable]):
            if str(widget) == str(event.widget.winfo_parent()):
                widget._select()
                self.label_method(event)
            else:
                widget._deselect()

    def _select(self):
        if str(self.label.cget('state')) == 'disabled':
            return
        self.color_canvas.config(bg=self.led_color)

    def _deselect(self):
        if str(self.label.cget('state')) == 'disabled':
            return
        self.color_canvas.config(bg=self.bg_color)

    def enable(self):
        self.color_canvas.config(bg=self.bg_color)
        self.label.config(state='normal')
        self.config(bootstyle=self.style)
        self.label.config(bootstyle=self.label_style)

    def disable(self):
        self.color_canvas.config(bg=self.disable_color)
        self.label.config(state='disabled')
        self.config(bootstyle='secondary')
        self.label.config(bootstyle='inverse-secondary')

    def is_selected(self):
        if self.color_canvas.cget('bg') == self.led_color:
            return True
        return False

    def is_disabled(self):
        if str(self.label.cget('state')) == 'disabled':
            return True
        return False
