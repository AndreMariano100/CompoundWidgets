import tkinter as tk
import tkinter.ttk as ttk


class CollapsableFrame(ttk.Frame):
    """
    Creates a collapsable frame
    Input:
        parent - container for the frame
        open_start - whether the frame initiates open or closed
    Attributes:
        title_label - use to configure the local title: CollapsableFrame.title_label.config(text='My Title')
        widgets_frame - use as container for the widgets: widget(CollapsableFrame.widget_frame, option=value).grid()
    """

    def __init__(self, parent, open_start=True, **kwargs):

        # Initialization
        if True:
            super().__init__(parent, **kwargs)
            self.master = parent.winfo_toplevel()
            self.style = self.master.style

            self.rowconfigure(0, weight=0)
            if open_start:
                self.rowconfigure(1, weight=1)
            else:
                self.rowconfigure(1, weight=0)
            self.columnconfigure(0, weight=1)
            self.configure(style='primary.TFrame')

        # Title Frame
        if True:
            self.title_frame = ttk.Frame(self, style='primary.TFrame')
            self.title_frame.grid(row=0, column=0, sticky='nsew')
            self.title_frame.rowconfigure(0, weight=1)
            self.title_frame.columnconfigure(0, weight=1)
            self.title_frame.columnconfigure(1, weight=0)

        # Widgets at Title Frame
        if True:
            self.title_label = ttk.Label(self.title_frame, style='primary.Inverse.TLabel', font=('Helvetica', 10),
                                         padding=5)
            self.title_label.grid(row=0, column=0, sticky='nsew')
            self.title_label.bind('<ButtonRelease-1>', self.check_collapse)

            if open_start:
                text = '-'
            else:
                text = '+'

            self.collapse_button = ttk.Label(self.title_frame, text=text, style='primary.TButton',
                                             font=('OpenSans', 12, 'bold'), width=3, padding=0)
            self.collapse_button.grid(row=0, column=1, sticky='nsew', padx=5)
            self.collapse_button.bind('<ButtonRelease-1>', self.check_collapse)

        # Widget Frame
        if True:
            self.widgets_frame = ttk.Frame(self)
            self.widgets_frame.grid(row=1, column=0, sticky='nsew', padx=1, pady=1)
            self.widgets_frame.rowconfigure(0, weight=1)
            self.widgets_frame.columnconfigure(0, weight=1)

            if not open_start:
                self.widgets_frame.grid_remove()

        # Start Status Adjust
        if True:
            if not open_start:
                self.collapse_button.event_generate('<ButtonRelease-1>')

    def check_collapse(self, event):

        widget_under_cursor = event.widget.winfo_containing(event.x_root, event.y_root)
        if widget_under_cursor != event.widget:
            return

        if self.collapse_button.cget('text') == '-':
            self.collapse_frame()
        else:
            self.expand_frame()

    def collapse_frame(self):
        self.collapse_button.configure(text='+')
        self.rowconfigure(1, weight=0)
        self.widgets_frame.grid_remove()

    def expand_frame(self):
        self.collapse_button.configure(text='-')
        self.rowconfigure(1, weight=1)
        self.widgets_frame.grid()

    def is_collapsed(self):
        if self.collapse_button.cget('text') == '-':
            return False
        return True


class ScrollableFrame(ttk.Frame):
    """
    Creates the frame with vertical scroll bar
    Attributes:
        self.widgets_frame - frame for the widgets
    Methods:
        on_canvas_configure(event, required_height) - call to update the canvas vertical size
    """

    def __init__(self, parent, **kwargs):

        # Initialization
        if True:
            super().__init__(parent, **kwargs)
            self.master = parent.winfo_toplevel()
            self.style = self.master.style

            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=0)
            self.rowconfigure(0, weight=1)

        # Scroll Canvas \ Scroll Bar \ Main Frame
        if True:
            # Scroll canvas
            self.scroll_canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0)
            self.scroll_canvas.grid(row=0, column=0, sticky='nsew')
            self.scroll_canvas.bind("<Configure>", self.on_canvas_configure)

            # Scroll bar
            y_scroll = ttk.Scrollbar(self, orient='vertical', command=self.scroll_canvas.yview)
            y_scroll.grid(row=0, column=1, sticky='nsew')

            # Frame for the widgets
            self.widgets_frame = ttk.Frame(self.scroll_canvas, padding=10, style='light.TFrame')
            self.widgets_frame.grid(sticky='nsew')
            self.widgets_frame.bind("<Configure>",
                                 lambda e: self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox("all")))

            # Putting the frame on the canvas
            self.frame_id = self.scroll_canvas.create_window((0, 0), window=self.widgets_frame, anchor='nw')
            self.scroll_canvas.configure(yscrollcommand=y_scroll.set)

            # Binding the MouseWheel event
            self.bind_all("<MouseWheel>", self._on_mousewheel)

    def on_canvas_configure(self, event, required_height=0):

        self.update()
        required_height = 40
        for widget in self.widgets_frame.winfo_children():
            required_height += widget.winfo_reqheight()

        height = max(event.height, required_height, self.winfo_height())
        width = max(event.width, self.winfo_width() - 10)
        self.scroll_canvas.itemconfigure(self.frame_id, width=width, height=height)

    def _on_mousewheel(self, event):
        self.scroll_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


# Local test of the frames
if __name__ == '__main__':
    import tkinter as tk
    from ttkbootstrap import Style

    root = tk.Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=0)
    root.rowconfigure(1, weight=1)
    root.minsize(300, 200)
    root.style = Style(theme='flatly')

    frame = CollapsableFrame(root)
    frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    ttk.Label(frame.widgets_frame, text='This is a collapsable frame', padding=50).grid(row=0, column=0, sticky='nsew')

    frame = ScrollableFrame(root)
    frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    ttk.Label(frame.widgets_frame, text='This is a scrollable frame', padding=50).grid(row=0, column=0, sticky='nsew')

    root.mainloop()
