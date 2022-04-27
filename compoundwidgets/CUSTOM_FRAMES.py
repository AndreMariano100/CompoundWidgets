import tkinter.ttk as ttk
import tkinter as tk


class CollapsableFrame(ttk.Frame):
    """
    Creates a collapsable frame
    Input:
        parent - container for the frame
        title - string for the title of the frame
        open_start - whether the frame initiates openned or closed

    Relevant Attributes:
        title_label - use to configure the local title: CollapsableFrame.title_label.config(text='My Title')
        widgets_frame - use as container for the widgets: widget(CollapsableFrame.widget_frame, option=value).grid()
    """

    def __init__(self, parent, title='', open_start=True, **kwargs):

        # Initialization
        if True:
            super().__init__(parent, **kwargs)
            self.title_string = title

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
                                         padding=5, text=self.title_string)
            self.title_label.grid(row=0, column=0, sticky='nsew')
            self.title_label.bind('<ButtonRelease-1>', self.check_collapse)

            self.collapse_button = ttk.Label(self.title_frame, text='-', style='primary.TButton',
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

        # Start status adjust
        if True:
            if not open_start:
                self.collapse_button['text'] = '+'
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

    def add_event(self, method):
        if callable(method):
            self.title_label.bind('<ButtonRelease-1>', method, add='+')
            self.collapse_button.bind('<ButtonRelease-1>', method, add='+')

        else:
            raise Exception(f'Method {method} is not callable')


class ScrollableFrame(ttk.Frame):
    """
    Creates the frame with vertical scroll bar
        Input:
        parent - container for the frame
    Attributes:
        self.widgets_frame - frame for the widgets
    Methods:
        adjust_scroll(event) - call to update the canvas vertical size
    """

    def __init__(self, parent, **kwargs):

        # Initialization
        if True:
            super().__init__(parent, **kwargs)
            self.parent = parent
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=0, minsize=10)
            self.rowconfigure(0, weight=1)
            self.rowconfigure(1, weight=0, minsize=10)

        # Scroll Canvas \ Scroll Bar \ Main Frame
        if True:
            # Scroll canvas
            self.scroll_canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0)
            self.scroll_canvas.grid(row=0, column=0, sticky='nsew')
            self.scroll_canvas.bind("<Configure>", self.adjust_scroll)

            # Scroll bar
            y_scroll = ttk.Scrollbar(self, orient='vertical', command=self.scroll_canvas.yview)
            y_scroll.grid(row=0, column=1, rowspan=2, sticky='nsew')
            x_scroll = ttk.Scrollbar(self, orient='horizontal', command=self.scroll_canvas.xview)
            x_scroll.grid(row=1, column=0, sticky='nsew')

            # Frame for the widgets
            self.widgets_frame = ttk.Frame(self.scroll_canvas, padding=10, style='light.TFrame')
            self.widgets_frame.grid(sticky='nsew')
            self.widgets_frame.bind("<Configure>",
                                    lambda e: self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox("all")))

            # Putting the frame on the canvas
            self.frame_id = self.scroll_canvas.create_window((0, 0), window=self.widgets_frame, anchor='nw')
            self.scroll_canvas.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

            # Binding the MouseWheel event
            self.bind_all("<MouseWheel>", self._on_mousewheel)

    def adjust_scroll(self, event):

        self.update()
        required_height = self.widgets_frame.winfo_reqheight()
        required_width = self.widgets_frame.winfo_reqwidth()

        final_width = max(required_width, self.winfo_width()) - 10
        final_height = max(required_height, self.winfo_height()) - 10
        self.scroll_canvas.itemconfigure(self.frame_id, width=final_width, height=final_height)
        self.scroll_canvas.configure(scrollregion=f'0 0 {final_width} {final_height}')

    def _on_mousewheel(self, event):
        self.scroll_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
