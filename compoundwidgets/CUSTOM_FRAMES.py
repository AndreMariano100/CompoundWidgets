import tkinter.ttk as ttk
import tkinter as tk


class CollapsableFrame(ttk.Frame):
    """
    Creates a collapsable frame
    Input:
        parent - container for the frame
        title - title of the frame
        open_start - whether the frame initiates opened or closed
    """

    def __init__(self, parent, title='Frame Title', open_start=True, **kwargs):

        # Main container
        if True:
            self.container = ttk.Frame(parent, style='primary.TFrame')
            self.container.columnconfigure(0, weight=1)
            self.container.rowconfigure(0, weight=1)
            self.container.rowconfigure(1, weight=1)

        # Title frame @ main container
        if True:
            title_frame = ttk.Frame(self.container, style='primary.TFrame')
            title_frame.grid(row=0, column=0, sticky='nsew')
            title_frame.rowconfigure(0, weight=1)
            title_frame.columnconfigure(0, weight=1)
            title_frame.columnconfigure(1, weight=0)

            title_label = ttk.Label(title_frame, style='primary.Inverse.TLabel', font=('OpenSans', 12),
                                    padding=5, text=title)
            title_label.grid(row=0, column=0, sticky='nsew')
            title_label.bind('<ButtonRelease-1>', self.check_collapse)

            self.collapse_button = ttk.Label(title_frame, text='-', style='primary.TButton',
                                             font=('OpenSans', 12, 'bold'), width=2, padding=0)
            self.collapse_button.grid(row=0, column=1, sticky='nsew')
            self.collapse_button.bind('<ButtonRelease-1>', self.check_collapse)

        # Self initialization
        if True:
            super().__init__(self.container, **kwargs)
            self.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=1)

        # Delegate content geometry methods to container frame
        _methods = vars(tk.Grid).keys()
        for method in _methods:
            if "grid" in method:
                # prefix content frame methods with 'content_'
                setattr(self, f"content_{method}", getattr(self, method))
                # overwrite content frame methods from container frame
                setattr(self, method, getattr(self.container, method))

        # Collapsed start adjust
        if not open_start:
            self.collapse_frame()

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
        self.content_grid_remove()

    def expand_frame(self):
        self.collapse_button.configure(text='-')
        self.rowconfigure(1, weight=1)
        self.content_grid()

    def is_collapsed(self):
        if self.collapse_button.cget('text') == '-':
            return False
        return True


class ScrollableFrame(ttk.Frame):
    """
    Creates a frame with a vertical scrollbar.
    Input:
        parent - container for the frame
    """

    def __init__(self, master=None, **kwargs):

        # content frame container
        self.container = ttk.Frame(master)
        self.container.bind("<Configure>", lambda _: self.yview())
        # self.container.propagate(False)
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)
        self.container.columnconfigure(1, weight=0)

        # content frame
        super().__init__(self.container, **kwargs)
        self.place(rely=0.0, relwidth=1.0)

        # vertical scrollbar
        self.vscroll = ttk.Scrollbar(self.container, command=self.yview, orient='vertical')
        self.vscroll.pack(side='right', fill='y')

        # widget event binding
        self.container.bind("<Enter>", self._on_enter, "+")
        self.container.bind("<Leave>", self._on_leave, "+")
        self.container.bind("<Map>", self._on_map, "+")
        self.bind("<<MapChild>>", self._on_map_child, "+")

        # delegate content geometry methods to container frame
        _methods = vars(tk.Pack).keys() | vars(tk.Grid).keys() | vars(tk.Place).keys()
        for method in _methods:
            if any(["pack" in method, "grid" in method, "place" in method]):
                # prefix content frame methods with 'content_'
                setattr(self, f"content_{method}", getattr(self, method))
                # overwrite content frame methods from container frame
                setattr(self, method, getattr(self.container, method))

    def yview(self, *args):
        """Update the vertical position of the content frame within the container.
        Parameters:
            *args (List[Any, ...]):
                Optional arguments passed to yview in order to move the
                content frame within the container frame.
        """
        if not args:
            first, _ = self.vscroll.get()
            self.yview_moveto(fraction=first)
        elif args[0] == "moveto":
            self.yview_moveto(fraction=float(args[1]))
        elif args[0] == "scroll":
            self.yview_scroll(number=int(args[1]), what=args[2])
        else:
            return

    def yview_moveto(self, fraction: float):
        """Update the vertical position of the content frame within the container.
        Parameters:
            fraction (float):
                The relative position of the content frame within the container.
        """
        base, thumb = self._measures()
        if fraction < 0:
            first = 0.0
        elif (fraction + thumb) > 1:
            first = 1 - thumb
        else:
            first = fraction
        self.vscroll.set(first, first + thumb)
        self.content_place(rely=-first * base)

    def yview_scroll(self, number: int, what: str):
        """Update the vertical position of the content frame within the
        container.

        Parameters:

            number (int):
                The amount by which the content frame will be moved
                within the container frame by 'what' units.

            what (str):
                The type of units by which the number is to be interpeted.
                This parameter is currently not used and is assumed to be
                'units'.
        """
        first, _ = self.vscroll.get()
        fraction = (number / 100) + first
        self.yview_moveto(fraction)

    def _measures(self):
        """Measure the base size of the container and the thumb size
        for use in the yview methods"""
        outer = self.container.winfo_height()
        inner = max([self.winfo_height(), outer])
        base = inner / outer
        if inner == outer:
            thumb = 1.0
        else:
            thumb = outer / inner
        return base, thumb

    def _on_map_child(self, event):
        """Callback for when a widget is mapped to the content frame."""
        if self.container.winfo_ismapped():
            self.yview()

    def _on_enter(self, event):
        """Callback for when the mouse enters the widget."""

        children = self.winfo_children()
        for widget in [self, *children]:
            bindings = widget.bind()
            if "<MouseWheel>" not in bindings:
                widget.bind("<MouseWheel>", self._on_mousewheel, "+")

    def _on_leave(self, event):
        """Callback for when the mouse leaves the widget."""
        children = self.winfo_children()
        for widget in [self, *children]:
            widget.unbind("<MouseWheel>")

    def _on_configure(self, event):
        """Callback for when the widget is configured"""
        self.yview()

    def _on_map(self, event):
        self.yview()

    def _on_mousewheel(self, event):
        """Callback for when the mouse wheel is scrolled."""
        delta = -int(event.delta / 30)
        self.yview_scroll(delta, 'units')
