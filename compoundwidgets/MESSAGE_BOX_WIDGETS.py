import tkinter as tk
import tkinter.ttk as ttk


class OkCancelBox(tk.Toplevel):
    """
    Creates a OK/CANCEL message box with the same style as the main application
    Input:
        parent: widget over which the progress bar will be positioned
        message = text to be shown as an alert to the user
    """

    def __init__(self, parent, message):

        # Configuration
        if True:
            super().__init__(parent)
            self.minsize(350, 150)
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=1)
            self.rowconfigure(0, weight=1)
            self.rowconfigure(1, weight=0)
            self.overrideredirect(True)
            self.config(padx=10, pady=10, bd=1, relief='raised')
            self.lift()

        # Widgets
        if True:
            self.control_var = tk.IntVar(value=0)
            label = ttk.Label(self, text=message, anchor='center', justify='center', padding=10, wraplength=300)
            label.grid(row=0, column=0, columnspan=2, sticky='nsew')

            ok_button = ttk.Button(self, text="OK", command=lambda: self.adjust_var(1), width=10,
                                   style='success.TButton')
            ok_button.grid(row=1, column=0, sticky='nsew', padx=30, pady=(0, 10))

            cancel_button = ttk.Button(self, text="Cancel", command=lambda: self.adjust_var(0), width=10,
                                       style='danger.TButton')
            cancel_button.grid(row=1, column=1, sticky='nsew', padx=30, pady=(0, 10))

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

    def adjust_var(self, option):
        self.control_var.set(option)
        self.destroy()

    def show(self):
        self.deiconify()
        self.wait_window()
        value = self.control_var.get()
        return value


class YesNoBox(tk.Toplevel):
    """
    Creates a Yes/No message box with the same style as the main application
    Input:
        parent: widget over which the progress bar will be positioned
        message = text to be shown as a question to the user
    """

    def __init__(self, parent, message):

        # Configuration
        if True:
            super().__init__(parent)
            self.minsize(350, 150)
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=1)
            self.rowconfigure(0, weight=1)
            self.rowconfigure(1, weight=0)
            self.overrideredirect(True)
            self.config(padx=10, pady=10, bd=1, relief='raised')
            self.lift()

        # Widgets
        if True:
            self.control_var = tk.IntVar(value=0)
            label = ttk.Label(self, text=message, anchor='center', justify='center', padding=10, wraplength=300)
            label.grid(row=0, column=0, columnspan=2, sticky='nsew')

            yes_button = ttk.Button(self, text="YES", command=lambda: self.adjust_var(1), width=10,
                                    style='success.TButton')
            yes_button.grid(row=1, column=0, sticky='nsew', padx=30, pady=(0, 10))

            no_button = ttk.Button(self, text="NO", command=lambda: self.adjust_var(0), width=10,
                                   style='danger.TButton')
            no_button.grid(row=1, column=1, sticky='nsew', padx=30, pady=(0, 10))

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

    def adjust_var(self, option):
        self.control_var.set(option)
        self.destroy()

    def show(self):
        self.deiconify()
        self.wait_window()
        value = self.control_var.get()
        return value


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

        # Message
        if True:
            label = ttk.Label(self, text=message, padding=10, wraplength=300)
            label.grid(row=0, column=0, sticky='nsew')

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


class WarningBox(tk.Toplevel):
    """ Creates a message box with the same style as the main application """

    def __init__(self, parent, message):

        # Configuration
        if True:
            super().__init__(parent)
            self.minsize(350, 150)
            self.columnconfigure(0, weight=1)
            self.rowconfigure(0, weight=1)
            self.rowconfigure(1, weight=0)
            self.overrideredirect(True)
            self.config(padx=10, pady=10, bd=1, relief='raised')
            self.lift()

        # Widgets
        if True:
            label = ttk.Label(self, text=message, anchor='center', justify='center', padding=10, wraplength=300)
            label.grid(row=0, column=0, sticky='nsew')

            ok_button = ttk.Button(self, text="OK", command=lambda: self.destroy(), width=10,
                                   style='danger.TButton')
            ok_button.grid(row=1, column=0, sticky='nsew', padx=30, pady=(0, 10))

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

    def show(self):
        self.deiconify()
        self.wait_window()
        return


class SuccessBox(tk.Toplevel):
    """ Creates a message box with the same style as the main application """

    def __init__(self, parent, message):

        # Configuration
        if True:
            super().__init__(parent)
            self.minsize(350, 150)
            self.columnconfigure(0, weight=1)
            self.rowconfigure(0, weight=1)
            self.rowconfigure(1, weight=0)
            self.overrideredirect(True)
            self.config(padx=10, pady=10, bd=1, relief='raised')
            self.lift()

        # Widgets
        if True:
            label = ttk.Label(self, text=message, anchor='center', justify='center', padding=10, wraplength=300)
            label.grid(row=0, column=0, sticky='nsew')

            ok_button = ttk.Button(self, text="OK", command=lambda: self.destroy(), width=10,
                                   style='success.TButton')
            ok_button.grid(row=1, column=0, sticky='nsew', padx=30, pady=(0, 10))

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

    def show(self):
        self.deiconify()
        self.wait_window()
        return


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
