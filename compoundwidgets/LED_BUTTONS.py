import tkinter as tk
import tkinter.ttk as ttk


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

    def __init__(self, parent, label_text='Label', label_width=10, label_method=None, font=None):

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
            if font:
                self.label.config(font=font)

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

    def __init__(self, parent, label_text='Label', label_width=10, label_method=None, font=None):

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
            if font:
                self.label.config(font=font)

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
        font: label font
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

    def __init__(self, parent, label_text='Label', label_width=10, label_method=None, control_variable=None, font=None):

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
            if font:
                self.label.config(font=font)

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
