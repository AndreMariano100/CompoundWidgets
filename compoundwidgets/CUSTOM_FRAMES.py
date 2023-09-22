import ttkbootstrap as ttk
import tkinter as tk


class CollapsableFrame(ttk.Frame):
    """
    Creates a vertically collapsable frame
    Parameters:
        parent: container for the frame
        title: title of the frame
        open_start: boolean, whether the frame initiates opened or closed
        style: bootstyle (color style)
        disabled: boolean, whether the frame is disabled at start
    """

    def __init__(self, parent, title='Frame Title', title_font=('OpenSans', 12),
                 open_start=True, style='primary', disabled=False, **kwargs):

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

        # Main container
        if True:
            self.style = style
            self.container = ttk.Frame(parent, bootstyle=style)
            self.container.columnconfigure(0, weight=1)
            self.container.rowconfigure(0, weight=1)
            self.container.rowconfigure(1, weight=1)

        # Title frame @ main container
        if True:
            self.title_frame = ttk.Frame(self.container, bootstyle=style)
            self.title_frame.grid(row=0, column=0, sticky='nsew')
            self.title_frame.rowconfigure(0, weight=1)
            self.title_frame.columnconfigure(0, weight=1)
            self.title_frame.columnconfigure(1, weight=0)

            self.title_label = ttk.Label(self.title_frame, font=title_font, padding=5, text=title,
                                         bootstyle=self.label_style)
            self.title_label.grid(row=0, column=0, sticky='nsew')
            self.title_label.bind('<ButtonRelease-1>', self.check_collapse)

            self.collapse_button = ttk.Label(self.title_frame, text='-', font=title_font, width=2,
                                             padding=0, bootstyle=self.label_style)
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

        # if hasattr(parent, 'yview') and callable(parent.yview):
        #     self.bind("<Configure>", lambda _: parent.yview())

        # Collapsed start adjust
        if not open_start:
            self.collapse_frame()

        # Status flag: disabled / enabled
        if disabled:
            self.collapse_frame()
            self.disabled = True
            self.disable()
        else:
            self.disabled = False
            self.enable()

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
        if not self.disabled:
            self.collapse_button.configure(text='-')
            self.rowconfigure(1, weight=1)
            self.content_grid()

    def is_collapsed(self):
        if self.collapse_button.cget('text') == '-':
            return False
        return True

    def disable(self):
        self.collapse_frame()
        self.disabled = True
        local_style = 'secondary'
        local_label_style = self.label_style_dict.get(local_style)
        self.container.configure(bootstyle=local_style)
        self.title_frame.configure(bootstyle=local_style)
        self.title_label.configure(bootstyle=local_label_style)
        self.collapse_button.configure(bootstyle=local_label_style)

    def enable(self):
        self.disabled = False
        self.container.configure(bootstyle=self.style)
        self.title_frame.configure(bootstyle=self.style)
        self.title_label.configure(bootstyle=self.label_style)
        self.collapse_button.configure(bootstyle=self.label_style)


class VCollapsableFrame(ttk.Frame):
    """
    Creates a horizontally collapsable frame
    Parameters:
        parent: container for the frame
        title: title of the frame
        open_start: boolean, whether the frame initiates opened or closed
        style: bootstyle (color style)
        disabled: boolean, whether the frame is disabled at start
    """

    def __init__(self, parent, title='Frame Title', title_font=('OpenSans', 12),
                 open_start=True, style='primary', disabled=False, **kwargs):

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

        # Main container
        if True:
            self.container = ttk.Frame(parent)
            self.container.rowconfigure(0, weight=0)
            self.container.rowconfigure(1, weight=1)
            self.container.columnconfigure(0, weight=0)
            self.container.columnconfigure(1, weight=1)

        # Expansion frame + label
        if True:
            self.title_frame = ttk.Frame(self.container, bootstyle=style)
            self.title_frame.grid(row=0, column=0, rowspan=2, sticky='nsew')
            self.title_frame.columnconfigure(0, weight=1)
            self.title_frame.rowconfigure(0, weight=0)
            self.title_frame.rowconfigure(1, weight=1)
            self.title_frame.bind('<ButtonRelease-1>', self.check_collapse)

            self.collapse_button = ttk.Label(self.title_frame, text='-', style='primary.TButton',
                                             font=title_font, width=3, padding=0, bootstyle=self.label_style,
                                             anchor='center', justify='center',)
            self.collapse_button.grid(row=0, column=0, sticky='nsew')
            self.collapse_button.bind('<ButtonRelease-1>', self.check_collapse)

        # Title for the frame
        if True:
            self.title_label = ttk.Label(self.container, font=title_font, padding=5, text=title,
                                         bootstyle=self.label_style)
            self.title_label.grid(row=0, column=1, sticky='new', padx=(1, 0))
            self.title_label.bind('<ButtonRelease-1>', self.check_collapse)

        # Self initialization
        if True:
            self.base_frame = ttk.Frame(self.container, bootstyle=style, padding=1)
            self.base_frame.grid(row=1, column=1, sticky='nsew', padx=(1, 0))
            self.base_frame.columnconfigure(0, weight=1)
            self.base_frame.rowconfigure(0, weight=1)

            super().__init__(self.base_frame, **kwargs)
            self.grid(row=0, column=0, sticky='nsew')
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

        # Status flag: disabled / enabled
        if disabled:
            self.collapse_frame()
            self.disabled = True
            self.disable()
        else:
            self.disabled = False
            self.enable()

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
        self.title_label.grid_remove()
        self.base_frame.grid_remove()

    def expand_frame(self):
        if not self.disabled:
            self.collapse_button.configure(text='-')
            self.rowconfigure(1, weight=1)
            self.content_grid()
            self.title_label.grid()
            self.base_frame.grid()

    def is_collapsed(self):
        if self.collapse_button.cget('text') == '-':
            return False
        return True

    def disable(self):
        self.collapse_frame()
        self.disabled = True
        local_style = 'secondary'
        local_label_style = self.label_style_dict.get(local_style)
        self.title_frame.configure(bootstyle=local_style)
        self.collapse_button.configure(bootstyle=local_label_style)

    def enable(self):
        self.disabled = False
        self.title_frame.configure(bootstyle=self.style)
        self.collapse_button.configure(bootstyle=self.label_style)


class ScrollableFrame_old(ttk.Frame):
    """
    Creates a frame with a vertical scrollbar.
    Parameters:
        parent: container for the frame
        style: bootstyle (color style)
    """

    def __init__(self, master=None, style='TFrame', **kwargs):

        # content frame container
        self.container = ttk.Frame(master, bootstyle=style)
        self.container.bind("<Configure>", lambda _: self.yview())
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)
        self.container.columnconfigure(1, weight=0)

        # content frame
        super().__init__(self.container, bootstyle=style, **kwargs)
        self.place(rely=0.0, relwidth=1.0)

        # vertical scrollbar
        self.vscroll = ttk.Scrollbar(self.container, command=self.yview, orient='vertical')
        self.vscroll.pack(side='right', fill='y')

        # widget event binding
        self.container.bind("<Enter>", self._on_enter, "+")
        self.vscroll.bind("<Enter>", self._on_enter, "+")
        self.bind("<Enter>", self._on_enter, "+")

        self.container.bind("<Leave>", self._on_leave, "+")
        self.vscroll.bind("<Leave>", self._on_leave, "+")
        self.bind("<Leave>", self._on_leave, "+")

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
        self.container.bind_all("<MouseWheel>", self._on_mousewheel, "+")

    def _on_leave(self, event):
        """Callback for when the mouse leaves the widget."""
        self.container.unbind_all("<MouseWheel>")

    def _on_configure(self, event):
        """Callback for when the widget is configured"""
        self.yview()

    def _on_map(self, event):
        self.yview()

    def _on_mousewheel(self, event):
        """Callback for when the mouse wheel is scrolled."""
        delta = -int(event.delta / 30)
        self.yview_scroll(delta, 'units')


class ScrollableFrame(ttk.Frame):
    """
    Creates a frame with a vertical scrollbar.
    Parameters:
        parent: container for the frame
        style: bootstyle (color style)
    """

    def __init__(self, parent, style='TFrame', **kwargs):

        # Main container
        self.container = ttk.Frame(parent)
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)
        self.container.columnconfigure(1, weight=0)

        # canvas
        self.canvas = tk.Canvas(self.container, borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky='nsew')

        # vertical scrollbar
        self.vscroll = ttk.Scrollbar(self.container, command=self.canvas.yview, orient='vertical')
        self.vscroll.grid(row=0, column=1, sticky='ns')

        # intermediary frame
        self.bottom_frame = ttk.Frame(self.canvas, style=style)
        self.bottom_frame.grid(row=0, column=0, sticky='nsew')
        self.bottom_frame.columnconfigure(0, weight=1)
        self.bottom_frame.rowconfigure(0, weight=1)
        self.bottom_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.window_id = self.canvas.create_window((0, 0), window=self.bottom_frame, anchor='nw')
        self.canvas.configure(yscrollcommand=self.vscroll.set)

        # 'self' frame, that will receive all widgets
        super().__init__(self.bottom_frame, style=style, **kwargs)
        self.grid(row=0, column=0, sticky='nsew')

        # bindings
        if True:
            self.container.bind("<Enter>", self._on_enter, "+")
            self.canvas.bind("<Enter>", self._on_enter, "+")
            self.vscroll.bind("<Enter>", self._on_enter, "+")
            self.bottom_frame.bind("<Enter>", self._on_enter, "+")
            self.bind("<Enter>", self._on_enter, "+")

            self.container.bind("<Leave>", self._on_leave, "+")
            self.canvas.bind("<Leave>", self._on_leave, "+")
            self.vscroll.bind("<Leave>", self._on_leave, "+")
            self.bottom_frame.bind("<Leave>", self._on_leave, "+")
            self.bind("<Leave>", self._on_leave, "+")

            self.container.bind("<Map>", self._update, "+")
            self.bind("<<MapChild>>", self._update, "+")
            self.container.bind("<Configure>", self._update, '+')

        # delegate content geometry methods to container frame
        _methods = vars(tk.Grid).keys()
        for method in _methods:
            if "grid" in method:
                # prefix content frame methods with 'content_'
                setattr(self, f"content_{method}", getattr(self, method))
                # overwrite content frame methods from container frame
                setattr(self, method, getattr(self.container, method))

    def _on_enter(self, event):
        """Callback for when the mouse enters the widget."""
        self.container.bind_all("<MouseWheel>", self._on_mousewheel, "+")

    def _on_leave(self, event):
        """Callback for when the mouse leaves the widget."""
        self.container.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        """Callback for when the mouse wheel is scrolled."""
        delta = -int(event.delta / 30)
        self.canvas.yview_scroll(delta, 'units')

    def _update(self, event):
        """ Callback for when new widgets are gridded, of the frame has been configured """

        self.container.update()
        x_size = self.container.winfo_width()
        self.canvas.itemconfigure(self.window_id, width=x_size-11)
