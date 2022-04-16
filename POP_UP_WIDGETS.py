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
            bg_color = parent.winfo_toplevel().style.colors.primary
            self.minsize(350, 150)
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=1)
            self.rowconfigure(0, weight=1)
            self.rowconfigure(1, weight=0)
            self.overrideredirect(True)
            self.config(bg=bg_color, padx=10, pady=10)

        # Widgets
        if True:
            self.control_var = tk.IntVar(value=0)
            label = ttk.Label(self, text=message, anchor='center', justify='center', padding=10,
                              style='primary.Inverse.TLabel', wraplength=300)
            label.grid(row=0, column=0, columnspan=2, sticky='nsew')

            cancel_button = ttk.Button(self, text="Cancel", command=lambda: self.adjust_var(0), width=10,
                                       style='danger.TButton')
            cancel_button.grid(row=1, column=0, sticky='nsew', padx=30, pady=(0, 10))

            ok_button = ttk.Button(self, text="OK", command=lambda: self.adjust_var(1), width=10,
                                   style='success.TButton')
            ok_button.grid(row=1, column=1, sticky='nsew', padx=30, pady=(0, 10))

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
            bg_color = parent.winfo_toplevel().style.colors.primary
            self.minsize(350, 150)
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=1)
            self.rowconfigure(0, weight=1)
            self.rowconfigure(1, weight=0)
            self.overrideredirect(True)
            self.config(bg=bg_color, padx=10, pady=10)

        # Widgets
        if True:
            self.control_var = tk.IntVar(value=0)
            label = ttk.Label(self, text=message, anchor='center', justify='center', padding=10,
                              style='primary.Inverse.TLabel')
            label.grid(row=0, column=0, columnspan=2, sticky='nsew')

            no_button = ttk.Button(self, text="NO", command=lambda: self.adjust_var(0), width=10,
                                   style='danger.TButton')
            no_button.grid(row=1, column=0, sticky='nsew', padx=30, pady=(0, 10))

            yes_button = ttk.Button(self, text="YES", command=lambda: self.adjust_var(1), width=10,
                                    style='success.TButton')
            yes_button.grid(row=1, column=1, sticky='nsew', padx=30, pady=(0, 10))

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
        update_bar(): updates the progress bar
    """

    def __init__(self, parent, message='Processing...', final_value=100):

        # self configuration
        if True:
            super().__init__()
            self.minsize(350, 100)
            self.columnconfigure(0, weight=1)
            self.rowconfigure(0, weight=1)
            self.overrideredirect(True)
            self.lift()

        # Base Frame /  Background Frame
        if True:
            background_frame = ttk.Frame(self, style='secondary.TFrame', padding=1)
            background_frame.grid(row=0, column=0, sticky='nsew')
            background_frame.columnconfigure(0, weight=1)
            background_frame.rowconfigure(0, weight=1)

            base_frame = ttk.Frame(background_frame)
            base_frame.grid(row=0, column=0, sticky='nsew')
            base_frame.columnconfigure(0, weight=1)
            base_frame.rowconfigure(0, weight=1)
            base_frame.rowconfigure(1, weight=0)

        # Message
        if True:
            label = ttk.Label(base_frame, text=message)
            label.grid(row=0, column=0, sticky='nsew', padx=10, pady=2)

        # Progress bar
        if True:
            self.final_value = final_value
            initial_value = 0
            self.progress_var = tk.DoubleVar(value=initial_value/self.final_value)
            progress_bar = ttk.Progressbar(base_frame, variable=self.progress_var,
                                           maximum=1, orient=tk.HORIZONTAL)
            progress_bar.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

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

    def update_bar(self, value):
        self.progress_var.set(value/self.final_value)
        self.update_idletasks()


class WarningBox(tk.Toplevel):
    """ Creates a message box with the same style as the main application """

    def __init__(self, parent, message):

        # Configuration
        if True:
            super().__init__(parent)
            bg_color = parent.winfo_toplevel().style.colors.primary
            self.minsize(350, 150)
            self.columnconfigure(0, weight=1)
            self.rowconfigure(0, weight=1)
            self.rowconfigure(1, weight=0)
            self.overrideredirect(True)
            self.config(bg=bg_color, padx=10, pady=10)
            self.lift()

        # Widgets
        if True:
            label = ttk.Label(self, text=message, anchor='center', justify='center', padding=10,
                              style='primary.Inverse.TLabel')
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


class Tooltip:
    """ It creates a tooltip for a given widget as the mouse goes on it. """

    def __init__(self, widget, *, bg='#FFFF8B', pad=(5, 3, 5, 3), text='widget info',
                 wait_time=500, wrap_length=250):

        self.master = widget.winfo_toplevel()
        self.style = self.master.style
        self.bg_color = bg
        self.fg_color = 'black'
        self.style.configure('custom.TLabel', background=self.bg_color, foreground=self.fg_color)
        self.wait_time = wait_time
        self.wrap_length = wrap_length
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.onEnter)
        self.widget.bind("<Leave>", self.onLeave)
        self.widget.bind("<ButtonPress>", self.onLeave)
        self.pad = pad
        self.id = None
        self.top_level = None

    def onEnter(self, event=None):
        self.schedule()

    def onLeave(self, event=None):
        self.unschedule()
        self.hide()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.wait_time, self.show)

    def unschedule(self):
        id_ = self.id
        self.id = None
        if id_:
            self.widget.after_cancel(id_)

    def show(self):

        def tip_pos_calculator(widget, label, *, tip_delta=(10, 5), pad=(5, 3, 5, 3)):
            w = widget
            s_width, s_height = w.winfo_screenwidth(), w.winfo_screenheight()
            width, height = (pad[0] + label.winfo_reqwidth() + pad[2],
                             pad[1] + label.winfo_reqheight() + pad[3])
            mouse_x, mouse_y = w.winfo_pointerxy()

            x1, y1 = mouse_x + tip_delta[0], mouse_y + tip_delta[1]
            x2, y2 = x1 + width, y1 + height

            x_delta = x2 - s_width
            if x_delta < 0:
                x_delta = 0
            y_delta = y2 - s_height
            if y_delta < 0:
                y_delta = 0

            offscreen = (x_delta, y_delta) != (0, 0)

            if offscreen:

                if x_delta:
                    x1 = mouse_x - tip_delta[0] - width

                if y_delta:
                    y1 = mouse_y - tip_delta[1] - height

            offscreen_again = y1 < 0  # out on the top

            if offscreen_again:
                # No further checks will be done.

                # TIP:
                # A further mod might automagically augment the
                # wraplength when the tooltip is too high to be
                # kept inside the screen.
                y1 = 0

            return x1, y1

        # creates a top level window
        self.top_level = tk.Toplevel(self.widget)
        self.top_level.wm_overrideredirect(True)
        self.top_level.rowconfigure(0, weight=1)
        self.top_level.columnconfigure(0, weight=1)
        self.top_level.configure(bg=self.style.colors.primary)

        label = ttk.Label(self.top_level, text=self.text, justify="left",
                          wraplength=self.wrap_length, style='custom.TLabel')
        label.grid(row=0, column=0, sticky='nsew', padx=1, pady=1)

        x, y = tip_pos_calculator(self.widget, label)

        self.top_level.wm_geometry("+%d+%d" % (x, y))

    def hide(self):
        if self.top_level:
            self.top_level.destroy()
        self.top_level = None


if __name__ == '__main__':

    from ttkbootstrap import Style
    import os

    # Root
    if True:
        root = tk.Tk()
        root.iconbitmap(default=os.path.join(os.getcwd(), 'IMAGES', 'engineering.ico'))
        root.title('Local Root for Testing')
        root.style = Style(theme='flatly')
        root.minsize(200, 50)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(2, weight=1)

    # Ok/CANCEL Message Box
    if True:
        def show_ok_cancel_box():
            answer = OkCancelBox(root, message='This is a OK / Cancel message box.\nTest the answers!').show()
            if answer:
                print('Selected OK')
            else:
                print('Selected Cancel')

        button = ttk.Button(root, text='OK / CANCEL Message Box', command=show_ok_cancel_box)
        button.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

    # Yes/No Message Box
    if True:
        def show_yes_no_box():
            answer = YesNoBox(root, message='This is a Yes / No message box.\nTest the answers!').show()
            if answer:
                print('Selected Yes')
            else:
                print('Selected No')

        button = ttk.Button(root, text='Yes / No Message Box', command=show_yes_no_box)
        button.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

    # Progress Bar
    if True:
        import time

        def show_progress_bar():
            p_bar = ProgressBar(root, message='Showing progress bar...', final_value=100)
            for i in range(100):
                time.sleep(0.02)
                p_bar.update_bar(i)
            p_bar.destroy()

        button = ttk.Button(root, text='Progress Bar', command=show_progress_bar)
        button.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)

    # Warning Box
    if True:
        def show_warning_box():
            WarningBox(root, message='This is a Warning box!').show()

        button = ttk.Button(root, text='Warning Box', command=show_warning_box)
        button.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)

    # Tool tip
    if True:
        button = ttk.Button(root, text='Tool Tip')
        button.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
        tool_tip_text = "This is a sample help text, that will be shown on a pop up window in the form of a tool tip"
        Tooltip(button, text=tool_tip_text, wrap_length=200)

    root.mainloop()
