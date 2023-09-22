import tkinter as tk
import ttkbootstrap as ttk


class BaseTopLevelWidget(tk.Toplevel):
    """
    Basic TopLevel Widget for Message Boxes
    Input:
        parent: widget over which the progress bar will be positioned
        icon_path: path to the icon for the widget
        title: title message for the widget
        message = text to be shown as an alert to the user
    """

    def __init__(self, parent, icon_path, title, message):

        # Configuration
        if True:
            super().__init__(parent)
            self.iconbitmap(icon_path)
            self.title(title)
            self.minsize(250, 120)
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=0)
            self.columnconfigure(2, weight=0)
            self.rowconfigure(0, weight=1)
            self.rowconfigure(1, weight=0)
            self.rowconfigure(2, weight=0)
            self.lift()

        # Label configuration
        if True:
            self.label = ttk.Label(self, text=message, justify='left', padding=5)
            self.label.grid(row=0, column=0, columnspan=3, sticky='nsew')
            if self.label.winfo_reqwidth() > self.minsize()[0] - 50:
                self.minsize(self.label.winfo_reqwidth() + 20, 120)
                self.update()

        # Separator configuration
            separator = ttk.Separator(self, orient='horizontal', style='secondary.Horizontal.TSeparator')
            separator.grid(row=1, column=0, columnspan=3, sticky='nsew')

        # Determine relative position
        if True:
            position_x = parent.winfo_x()
            position_y = parent.winfo_y()
            height = parent.winfo_height()
            width = parent.winfo_width()

            local_height = self.minsize()[1]
            local_width = self.minsize()[0]

            final_position = (position_x + width / 2 - local_width / 2, position_y + height / 2 - local_height / 2)
            self.geometry('%dx%d+%d+%d' % (local_width, local_height, final_position[0], final_position[1]))
            self.grab_set()

        # Control variable
        self.control_var = tk.IntVar(value=0)

    def adjust_var(self, option):
        self.control_var.set(option)
        self.destroy()

    def show(self):
        self.deiconify()
        self.wait_window()
        value = self.control_var.get()
        return value


class OkCancelBox(BaseTopLevelWidget):
    """
    Creates a OK/CANCEL message box with the same style as the main application
    Input:
        parent: widget over which the progress bar will be positioned
        icon_path: path to the icon for the widget
        title: title message for the widget
        message: text to be shown as an alert to the user
        language: language for the buttons text
    """

    def __init__(self, parent, icon_path, title, message, language='en'):

        super().__init__(parent, icon_path, title, message)

        if language == 'br':
            cancel_text, ok_text = 'CANCELAR', 'OK'
        else:
            cancel_text, ok_text = 'CANCEL', 'OK'

        cancel_button = ttk.Button(self, text=cancel_text, command=lambda: self.adjust_var(0), width=8,
                                   style='secondary.TButton')
        cancel_button.grid(row=2, column=1, sticky='nsew', pady=5)

        ok_button = ttk.Button(self, text=ok_text, command=lambda: self.adjust_var(1), width=8,
                               style='primary.TButton')
        ok_button.grid(row=2, column=2, sticky='nsew', padx=5, pady=5)


class YesNoBox(BaseTopLevelWidget):
    """
    Creates a Yes/No message box with the same style as the main application
    Input:
        parent: widget over which the progress bar will be positioned
        icon_path: path to the icon for the widget
        title: title message for the widget
        message: text to be shown as an alert to the user
        language: language for the buttons text
    """

    def __init__(self, parent, icon_path, title, message, language='en'):

        super().__init__(parent, icon_path, title, message)

        if language == 'br':
            no_text, yes_text = 'NÃO', 'SIM'
        else:
            no_text, yes_text = 'NO', 'YES'

        no_button = ttk.Button(self, text=no_text, command=lambda: self.adjust_var(0), width=8,
                               style='secondary.TButton')
        no_button.grid(row=2, column=1, sticky='nsew', pady=5)
        yes_button = ttk.Button(self, text=yes_text, command=lambda: self.adjust_var(1), width=8,
                                style='primary.TButton')
        yes_button.grid(row=2, column=2, sticky='nsew', padx=5, pady=5)


class WarningBox(BaseTopLevelWidget):
    """
    Creates a message box with the same style as the main application
    Input:
        parent: widget over which the progress bar will be positioned
        icon_path: path to the icon for the widget
        title: title message for the widget
        message: text to be shown as an alert to the user
        language: language for the buttons text
    """

    def __init__(self, parent, icon_path, title, message, language='en'):

        super().__init__(parent, icon_path, title, message)

        self.label.config(style='danger.TLabel')
        ok_button = ttk.Button(self, text="OK", command=lambda: self.destroy(), width=8,
                               style='danger.TButton')
        ok_button.grid(row=2, column=2, sticky='nsew', padx=5, pady=5)


class SuccessBox(BaseTopLevelWidget):
    """
    Creates a message box with the same style as the main application
    Input:
        parent: widget over which the progress bar will be positioned
        icon_path: path to the icon for the widget
        title: title message for the widget
        message: text to be shown as an alert to the user
        language: language for the buttons text
    """

    def __init__(self, parent, icon_path, title, message, language='en'):

        super().__init__(parent, icon_path, title, message)
        ok_button = ttk.Button(self, text="OK", command=lambda: self.destroy(), width=8,
                               style='primary.TButton')
        ok_button.grid(row=2, column=2, sticky='nsew', padx=5, pady=5)


class ProgressBar(tk.Toplevel):
    """
    Creates a progress bar to follow the program tasks
    Input:
        parent: widget over which the progress bar will be positioned
        message: text to be shown above the progress bar
        final_value: number that represents the final value of the progress bar (100% value)
    Method:
        update_bar(value): updates the progress bar to the current value
    """

    def __init__(self, parent, message='Processing...', final_value=100):

        # self configuration
        if True:
            super().__init__(parent)
            self.minsize(350, 100)
            self.columnconfigure(0, weight=1)
            self.rowconfigure(0, weight=1)
            self.rowconfigure(1, weight=0)
            self.overrideredirect(True)
            self.config(padx=10, pady=10, bd=1, relief='raised')
            self.lift()

        # Label configuration
        if True:
            self.label = ttk.Label(self, text=message, justify='left', padding=10)
            self.label.grid(row=0, column=0, sticky='nsew')
            if self.label.winfo_reqwidth() > self.minsize()[0]:
                self.minsize(self.label.winfo_reqwidth() + 20, 100)
                self.update()

        # Progress bar
        if True:
            local_frame = ttk.Frame(self)
            local_frame.grid(row=1, column=0, sticky='nsew')
            local_frame.columnconfigure(0, weight=1)
            local_frame.rowconfigure(0, weight=1)

            self.final_value = final_value
            initial_value = 0
            self.progress_var = tk.DoubleVar(value=initial_value/self.final_value)
            progress_bar = ttk.Progressbar(local_frame, variable=self.progress_var, maximum=1, orient=tk.HORIZONTAL,
                                           style='info.Striped.Horizontal.TProgressbar')
            progress_bar.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        # Relative position
        if True:
            position_x = parent.winfo_x()
            position_y = parent.winfo_y()
            height = parent.winfo_height()
            width = parent.winfo_width()

            local_height = self.minsize()[1]
            local_width = self.minsize()[0]

            final_position = (position_x + width / 2 - local_width / 2, position_y + height / 2 - local_height / 2)
            self.geometry('%dx%d+%d+%d' % (local_width, local_height, final_position[0], final_position[1]))

            self.grab_set()

    def update_bar(self, value):
        self.progress_var.set(value/self.final_value)
        self.update_idletasks()


class Tooltip:
    """ It creates a tooltip for a given widget as the mouse goes on it. """

    def __init__(self, widget, text='widget info', bg='#FFFF8B', fg='black', wait_time=500, wrap_length=250):

        self.style = widget.winfo_toplevel().style
        self.style.configure('custom.TLabel', background=bg, foreground=fg)
        self.widget = widget
        self.text = text
        self.wait_time = wait_time
        self.wrap_length = wrap_length

        self.widget.bind("<Enter>", self._enter)
        self.widget.bind("<Leave>", self._leave)
        self.widget.bind("<ButtonPress>", self._leave)
        self.id = None
        self.top_level = None

    def _enter(self, event=None):
        self.schedule()

    def _leave(self, event=None):
        self.unschedule()
        self.hide()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.wait_time, self.show)

    def unschedule(self):
        if self.id:
            self.widget.after_cancel(self.id)
        self.id = None

    def show(self):

        def tip_pos_calculator(base_widget, selected_label):

            # Get the monitor's size
            total_width, total_height = base_widget.winfo_vrootwidth(), base_widget.winfo_vrootheight()

            # Tip label minimum size (plus offset)
            width, height = (selected_label.winfo_reqwidth() + 10, selected_label.winfo_reqheight() + 6)

            # Mouse position
            mouse_x, mouse_y = base_widget.winfo_pointerxy()

            # Top level initial and final positions
            x1, y1 = mouse_x + 10, mouse_y + 6
            x2, y2 = x1 + width, y1 + height

            # Checks for horizontal position
            if x2 > total_width:
                x1 -= (x2 - total_width)
            if x1 < 0:
                x1 = 30

            # Checks for vertical position
            if y2 > total_height:
                y1 -= (y2 - total_height)
            if y1 < 0:
                y1 = 30

            return x1, y1

        self.top_level = tk.Toplevel(self.widget)
        self.top_level.wm_overrideredirect(True)
        self.top_level.rowconfigure(0, weight=1)
        self.top_level.columnconfigure(0, weight=1)
        self.top_level.configure(bg=self.style.colors.primary)

        label = ttk.Label(self.top_level, text=self.text, justify="left",
                          wraplength=self.wrap_length, style='custom.TLabel')
        label.grid(row=0, column=0, sticky='nsew', padx=1, pady=1)

        x, y = tip_pos_calculator(self.widget, label)

        self.top_level.geometry(f'+{x}+{y}')

    def hide(self):
        if self.top_level:
            self.top_level.destroy()
        self.top_level = None


class TimedBox(tk.Toplevel):
    """
    TopLevel widget for timed message boxes.
    Input:
        parent = widget over which the progress bar will be positioned
        message = text to be shown as an alert to the user
        time = time in seconds for the pop-up window display
        style = color scheme for the window
    """

    def __init__(self, parent, message, time=1, style=None):

        # Configuration
        if True:
            super().__init__(parent)
            self.overrideredirect(True)
            self.total_time_ms = 1000 * time
            self.minsize(250, 120)
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=0)
            self.rowconfigure(0, weight=1)
            self.rowconfigure(1, weight=0)
            self.rowconfigure(2, weight=0)
            self.lift()
            style_dict = {
                'danger': ('danger.TLabel','danger.TButton', 'danger.Horizontal.TProgressbar'),
                'warning': ('warning.TLabel', 'warning.TButton', 'warning.Horizontal.TProgressbar'),
                'info': ('info.TLabel', 'info.TButton', 'info.Horizontal.TProgressbar'),
            }

        # Widgets
        if True:
            label_style, button_style, progress_bar_style = \
                style_dict.get(style, ('TLabel', 'TButton', 'TProgressbar'))
            label = ttk.Label(self, text=message, justify='left', style=label_style)
            label.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)

            self.progressbar_var = tk.DoubleVar(value=0)
            self.progressbar = ttk.Progressbar(self, maximum=self.total_time_ms, orient='horizontal',
                                               mode='determinate', style=progress_bar_style,
                                               variable=self.progressbar_var)
            self.progressbar.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=10)

            button = ttk.Button(self, text='CLOSE', style=button_style, command= lambda: self.destroy())
            button.grid(row=2, column=1, sticky='nsew', pady=10, padx=10)

            if label.winfo_reqwidth() > self.minsize()[0]:
                self.minsize(label.winfo_reqwidth() + 40, 120)
                self.update()

        # Determine relative position
        if True:
            position_x = parent.winfo_x()
            position_y = parent.winfo_y()
            height = parent.winfo_height()
            width = parent.winfo_width()

            local_height = self.minsize()[1]
            local_width = self.minsize()[0]

            final_position = (position_x + width / 2 - local_width / 2, position_y + height / 2 - local_height / 2)
            self.geometry('%dx%d+%d+%d' % (local_width, local_height, final_position[0], final_position[1]))
            self.grab_set()

    def update_progress_bar(self):

        step_number = 50
        step = int(self.total_time_ms / step_number)

        for i in range(step_number):
            self.after(step)
            self.progressbar_var.set((i + 1) * step)
            self.progressbar.update()
        self.destroy()


    def show(self):
        self.update()
        self.deiconify()
        self.update_progress_bar()
        return
