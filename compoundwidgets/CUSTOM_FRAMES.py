import ttkbootstrap as ttk
import tkinter as tk
from .MESSAGE_BOX_WIDGETS import Tooltip


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
            self.parent = parent
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

        # Delegate content geometry methods from container frame
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

        self.container.bind("<Map>",  self._update, "+")
        self.container.bind("<Configure>", self._update, '+')
        self.container.bind("<<MapChild>>", self._update, '+')
        self.bind("<<MapChild>>", self._update, "+")
        self.bind("<Configure>", self._update, '+')

    def _update(self, event=None):
        self.update_idletasks()

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
        self.parent.event_generate("<Configure>")

    def expand_frame(self):
        if not self.disabled:
            self.collapse_button.configure(text='-')
            self.rowconfigure(1, weight=1)
            self.content_grid()
            self.parent.event_generate("<Configure>")

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
            self.container.rowconfigure(0, weight=0)  # Internal Title
            self.container.rowconfigure(1, weight=1)  # Main content
            self.container.columnconfigure(0, weight=0)  # Left Title
            self.container.columnconfigure(1, weight=1)  # Main content

        # Expansion frame + label
        if True:
            self.title_frame = ttk.Frame(self.container, bootstyle=style)
            self.title_frame.grid(row=0, column=0, rowspan=2, sticky='nsew')
            self.title_frame.columnconfigure(0, weight=1)
            self.title_frame.rowconfigure(0, weight=0)
            self.title_frame.rowconfigure(1, weight=1)
            self.title_frame.bind('<ButtonRelease-1>', self.check_collapse)

            broken_title = '\n'.join(title.upper())
            style = f'{style}.Inverse.TLabel'
            self.label = ttk.Label(self.title_frame, text=broken_title, anchor='n', justify='center', style=style)
            self.label.grid(row=1, column=0, sticky='nsew')
            self.label.bind('<ButtonRelease-1>', self.check_collapse)

            self.collapse_button = ttk.Label(self.title_frame, text='-', style='primary.TButton',
                                             font=title_font, width=3, padding=0, bootstyle=self.label_style,
                                             anchor='center', justify='center',)
            self.collapse_button.grid(row=0, column=0, sticky='nsew')
            self.collapse_button.bind('<ButtonRelease-1>', self.check_collapse)

            Tooltip(self.title_frame, text=title)
            Tooltip(self.collapse_button, text=title)

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

        self.container.bind("<Map>", self._update, "+")
        self.container.bind("<Configure>", self._update, '+')
        self.container.bind("<<MapChild>>", self._update, '+')
        self.bind("<<MapChild>>", self._update, "+")
        self.bind("<Configure>", self._update, '+')

    def _update(self, event=None):
        self.update_idletasks()

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
        self.label.configure(style='secondary.Inverse.TLabel')

    def enable(self):
        self.disabled = False
        self.title_frame.configure(bootstyle=self.style)
        self.collapse_button.configure(bootstyle=self.label_style)
        self.label.configure(style=f'{self.style}.Inverse.TLabel')

class ScrollableFrame(ttk.Frame):
    """
    Creates a frame with a vertical and a horizontal scrollbar.
    Scrollbars will hide if the content fits the frame dimensions.
    Parameters:
        parent: container for the frame
        style: bootstyle (color style)
        bind_mouse_wheel: select whether to not bind mouse wheel events
    """

    def __init__(self, parent, style='TFrame', bind_mouse_wheel=True, **kwargs):

        # Main container
        self.container = ttk.Frame(parent)
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        # canvas
        self.canvas = tk.Canvas(self.container, borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky='nsew')

        # vertical scrollbar
        self.v_scroll = ttk.Scrollbar(self.container, command=self.canvas.yview, orient='vertical')
        self.v_scroll.grid(row=0, column=1, sticky='ns')

        # Horizontal scrollbar
        self.h_scroll = ttk.Scrollbar(self.container, command=self.canvas.xview, orient='horizontal')
        self.h_scroll.grid(row=1, column=0, sticky='ew')

        # Intermediary frame
        self.bottom_frame = ttk.Frame(self.canvas)
        self.bottom_frame.grid()
        self.bottom_frame.columnconfigure(0, weight=1)
        self.bottom_frame.rowconfigure(0, weight=1)
        self.bottom_frame.bind("<Configure>",
                               lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Canvas window objet
        self.window_id = self.canvas.create_window((0, 0), window=self.bottom_frame, anchor='nw')
        self.canvas.configure(yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set)

        # 'self' frame, that will receive all widgets
        super().__init__(self.bottom_frame, style=style, **kwargs)
        self.grid(row=0, column=0, sticky='nsew')

        # Mouse wheel bindings
        self.bind_mouse_wheel = bind_mouse_wheel
        if self.bind_mouse_wheel:
            self.container.bind("<Enter>", self._on_enter, "+")
            self.canvas.bind("<Enter>", self._on_enter, "+")
            self.v_scroll.bind("<Enter>", self._on_enter, "+")
            self.h_scroll.bind("<Enter>", self._on_enter, "+")
            self.bottom_frame.bind("<Enter>", self._on_enter, "+")
            self.bind("<Enter>", self._on_enter, "+")

            self.container.bind("<Leave>", self._on_leave, "+")
            self.canvas.bind("<Leave>", self._on_leave, "+")
            self.v_scroll.bind("<Leave>", self._on_leave, "+")
            self.h_scroll.bind("<Leave>", self._on_leave, "+")
            self.bottom_frame.bind("<Leave>", self._on_leave, "+")
            self.bind("<Leave>", self._on_leave, "+")

        # Configure bindings
        if True:
            self.container.bind("<Map>", self._update, "+")
            self.container.bind("<Configure>", self._update, '+')
            self.container.bind("<<MapChild>>", self._update, '+')
            self.bind("<<MapChild>>", self._update, "+")
            self.bind("<Configure>", self._update, '+')

        # delegate content geometry methods from container frame to 'self'
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
        """ Callback for when new widgets are gridded, or the frame has been configured """

        # Container size
        if True:
            self.container.update_idletasks()
            container_x_size = self.container.winfo_width()
            container_y_size = self.container.winfo_height()

        # Removes the vertical scroll if available height is bigger than required height
        if True:
            if self.h_scroll.winfo_ismapped():
                available_y_size = container_y_size - 11
            else:
                available_y_size = container_y_size

            if self.bottom_frame.winfo_reqheight() < available_y_size:
                expand_y = True
                self.v_scroll.grid_remove()
                available_width = container_x_size
                self.canvas.grid_configure(columnspan=2)
            else:
                expand_y = False
                self.v_scroll.grid()
                available_width = container_x_size - 11
                self.canvas.grid_configure(columnspan=1)

        # Removes the horizontal scroll if available width is bigger than required width
        if True:
            if self.v_scroll.winfo_ismapped():
                available_x_size = container_x_size - 11
            else:
                available_x_size = container_x_size

            if self.bottom_frame.winfo_reqwidth() < available_x_size:
                expand_x = True
                self.h_scroll.grid_remove()
                available_height = container_y_size
                self.canvas.grid_configure(rowspan=2)
            else:
                expand_x = False
                self.h_scroll.grid()
                available_height = container_y_size - 11
                self.canvas.grid_configure(rowspan=1)

        # Adjust the canvas dimensions
        final_width = max (available_width, self.bottom_frame.winfo_reqwidth())
        self.canvas.itemconfigure(self.window_id, width=final_width)

        final_height = max (available_height, self.bottom_frame.winfo_reqheight())
        self.canvas.itemconfigure(self.window_id, height=final_height)


class BorderFrame(ttk.Frame):
    """
    Creates a frame with a continuous border all around it.
    Parameters:
        parent: container for the frame
        border_width: width of the border (padding)
        border_style: color of the border (bootstyle)
        frame_style: main frame style (bootstyle)
    """

    def __init__(self, parent, border_width=1, border_style='secondary', frame_style='TFrame', **kwargs):

        # Main container
        if True:
            self.container = ttk.Frame(parent, style=border_style)
            self.container.rowconfigure(0, weight=1)
            self.container.columnconfigure(0, weight=1)

        # Self initialization
        if True:
            super().__init__(self.container, style=frame_style, **kwargs)

            if isinstance(border_width, tuple) or isinstance(border_width, list):
                pad_x = border_width[0:2]
                pad_y = border_width[2:4]
            else:
                pad_x = border_width
                pad_y = border_width

            self.grid(row=0, column=0, sticky='nsew', padx=pad_x, pady=pad_y)

        # Delegate content geometry methods from container frame
        _methods = vars(tk.Grid).keys()
        for method in _methods:
            if "grid" in method:
                # prefix content frame methods with 'content_'
                setattr(self, f"content_{method}", getattr(self, method))
                # overwrite content frame methods from container frame
                setattr(self, method, getattr(self.container, method))
