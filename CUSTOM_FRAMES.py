import tkinter as tk
import tkinter.ttk as ttk
from CUSTOM_BUTTONS import *
from COMPOUND_WIDGETS import LabelCombo


# Collapsable Frame Class ----------------------------------------------------------------------------------------------
class CollapsableFrame(ttk.Frame):
    """
    Creates a collapsable frame
    Input:
        parent - container for the frame
        open_start - whether the frame initiates open or closed
    Attributes:
        title_label - use to configure the local title: CollapsableFrame.title_label.config(text='My Title')
        widget_frame - use as container for the widgets: widget(CollapsableFrame.widget_frame, option=value).grid()
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
            self.widget_frame = ttk.Frame(self)
            self.widget_frame.grid(row=1, column=0, sticky='nsew', padx=1, pady=1)
            self.widget_frame.rowconfigure(0, weight=1)
            self.widget_frame.columnconfigure(0, weight=1)

            if not open_start:
                self.widget_frame.grid_remove()

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
        self.widget_frame.grid_remove()

    def expand_frame(self):
        self.collapse_button.configure(text='-')
        self.rowconfigure(1, weight=1)
        self.widget_frame.grid()

    def is_collapsed(self):
        if self.collapse_button.cget('text') == '-':
            return False
        return True


# Regular Frame Class --------------------------------------------------------------------------------------------------
class RegularFrame(ttk.Frame):
    """
    Creates a non collapsable frame
    Input:
        parent - container for the frame
    Attributes:
        title_label - use to configure the local title: RegularFrame.title_label.config(text='My Title')
        widget_frame - use as container for the widgets: widget(RegularFrame.widget_frame, option=value).grid()
    """

    def __init__(self, parent, **kwargs):

        # Initialization
        if True:
            super().__init__(parent, **kwargs)
            self.master = parent.winfo_toplevel()
            self.style = self.master.style

            self.columnconfigure(0, weight=1)
            self.rowconfigure(0, weight=0)
            self.rowconfigure(1, weight=1)
            self.configure(style='primary.TFrame')

        # Title
        if True:
            self.title_label = ttk.Label(self, style='primary.Inverse.TLabel', font=('Helvetica', 10), padding=5)
            self.title_label.grid(row=0, column=0, sticky='nsew')

        # Widget Frame
        if True:
            self.widgets_frame = ttk.Frame(self)
            self.widgets_frame.grid(row=1, column=0, sticky='nsew', padx=1, pady=1)
            self.widgets_frame.rowconfigure(0, weight=1)
            self.widgets_frame.columnconfigure(0, weight=1)


# Scrollable Frame -----------------------------------------------------------------------------------------------------
class ScrollableFrame(ttk.Frame):
    """
    Creates the frame with vertical scroll bar
    Attributes:
        self.main_frame - frame for the widgets
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
            self.main_frame = ttk.Frame(self.scroll_canvas, padding=10, style='light.TFrame')
            self.main_frame.grid(sticky='nsew')
            self.main_frame.bind("<Configure>",
                                 lambda e: self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox("all")))

            # Putting the frame on the canvas
            self.frame_id = self.scroll_canvas.create_window((0, 0), window=self.main_frame, anchor='nw')
            self.scroll_canvas.configure(yscrollcommand=y_scroll.set)

            # Binding the MouseWheel event
            self.bind_all("<MouseWheel>", self._on_mousewheel)

    def on_canvas_configure(self, event, required_height=0):

        self.update()
        required_height = 40
        for widget in self.main_frame.winfo_children():
            required_height += widget.winfo_reqheight()

        height = max(event.height, required_height, self.winfo_height())
        width = max(event.width, self.winfo_width() - 10)
        self.scroll_canvas.itemconfigure(self.frame_id, width=width, height=height)

    def _on_mousewheel(self, event):
        self.scroll_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


# Frame for loading previous calculations performed --------------------------------------------------------------------
class PreviousCalculationFrame(ttk.Frame):

    def __init__(self, parent, combo_list=(), combo_method=None,
                 add_new_method=None, edit_method=None, remove_method=None):
        super().__init__(parent)
        self.combo_list = combo_list
        self.master = parent.winfo_toplevel()
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=0)

        self.previous_calculation_combo = LabelCombo(self, label_text='Selecionar Cálculo:',
                                                     combo_width=50, combo_method=combo_method,
                                                     combo_list=self.combo_list)
        self.previous_calculation_combo.grid(row=0, column=0, sticky='ew')

        self.add_analysis_button = AddToReport(self, command=add_new_method)
        self.add_analysis_button.grid(row=0, column=1, sticky='ew', padx=(10, 0))

        self.edit_analysis_button = EditReport(self, command=edit_method)
        self.edit_analysis_button.grid(row=0, column=2, sticky='ew', padx=10)

        self.remove_analysis_button = RemoveFromReport(self, command=remove_method)
        self.remove_analysis_button.grid(row=0, column=3, sticky='ew', padx=(0, 10))

    def disable(self):
        self.previous_calculation_combo.disable()
        self.add_analysis_button['state'] = 'disabled'
        self.edit_analysis_button['state'] = 'disabled'
        self.remove_analysis_button['state'] = 'disabled'

    def enable(self):
        self.previous_calculation_combo.enable()
        self.add_analysis_button['state'] = 'normal'
        self.edit_analysis_button['state'] = 'normal'
        self.remove_analysis_button['state'] = 'normal'


# Application Model Frame ----------------------------------------------------------------------------------------------
class ModelFrame(ScrollableFrame):
    """
    Creates a model frame for the calculations
    Attributes:
        self.widgets_frame: parent for the upcoming widgets
        self.previous_calculation_frame: bind to enable / disable
        self.calculation_selection_combobox: bind to perform the calculation data update
        self.add_button: bind to add another calculation
        self.edit_button: bind to edit current calculation
        self.remove_button: bind to exclude current calculation
    Methods:
        set_analysis_id: sets the analysis ID
        set_calculation_id: sets the calculation ID
    """

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=0)   # Analysis ID
        self.main_frame.rowconfigure(1, weight=0)   # Calculus ID / Add / Edit / Remove
        self.main_frame.rowconfigure(2, weight=1)   # Calculus Data

        # Row 0 - Analysis ID
        if True:
            self.analysis_id = tk.StringVar(value='Identificação da Análise')
            self.title_label = ttk.Label(self.main_frame, textvariable=self.analysis_id, padding=5,
                                         style='primary.Inverse.TLabel', font=('Helvetica', 10), anchor='w')
            self.title_label.grid(row=0, column=0, sticky='ew')

        # Row 1 - Calculus ID Frame: Add / Edit / Exclude
        if True:

            self.calculus_id = tk.StringVar(value='Identificação do Cálculo')
            self.calculus_id_frame = CollapsableFrame(self.main_frame)
            self.calculus_id_frame.grid(row=1, column=0, sticky='ew', pady=10)

            self.calculus_id_frame.title_label['textvariable'] = self.calculus_id
            self.calculus_id_frame.collapse_button.bind(
                '<ButtonRelease-1>', lambda e: self.scroll_canvas.event_generate('<Configure>'), add='+')
            self.calculus_id_frame.title_label.bind(
                '<ButtonRelease-1>', lambda e: self.scroll_canvas.event_generate('<Configure>'), add='+')

            # Adds the Previous Calculation Frame
            self.previous_calculation_frame = PreviousCalculationFrame(self.calculus_id_frame.widget_frame)
            self.previous_calculation_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

            self.calculation_selection_combobox = self.previous_calculation_frame.previous_calculation_combo.combobox
            self.add_button = self.previous_calculation_frame.add_analysis_button
            self.edit_button = self.previous_calculation_frame.edit_analysis_button
            self.remove_button = self.previous_calculation_frame.remove_analysis_button

        # Row 2 - Calculus Details Frame
        if True:
            self.calculus_details_frame = RegularFrame(self.main_frame)
            self.calculus_details_frame.title_label['text'] = 'Detalhes do Cálculo'
            self.calculus_details_frame.grid(row=2, column=0, sticky='nsew')
            self.widgets_frame = self.calculus_details_frame.widgets_frame

    def set_analysis_id(self, text):
        self.analysis_id.set(text)

    def set_calculation_id(self, text):
        self.calculus_id.set(text)


# Application General Frame --------------------------------------------------------------------------------------------
class GeneralFrame(ttk.Frame):
    """
        Creates a non collapsable frame
        Input:
            parent - container for the frame
        Attributes:
            title_label - use to configure the local title: RegularFrame.title_label.config(text='My Title')
            widgets_frame - use as container for the widgets: widget(RegularFrame.widget_frame, option=value).grid()
            bottom_frame - use as container for action buttons
        """

    def __init__(self, parent, **kwargs):

        # Initialization
        if True:
            super().__init__(parent, **kwargs)
            self.master = parent.winfo_toplevel()
            self.style = self.master.style
            self.configure(style='light.TFrame', padding=10)
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=1)

            local_frame = ttk.Frame(self, style='primary.TFrame')
            local_frame.grid(row=0, column=0, sticky='nsew')
            local_frame.columnconfigure(0, weight=1)
            local_frame.rowconfigure(0, weight=0)
            local_frame.rowconfigure(1, weight=1)
            local_frame.rowconfigure(2, weight=0, minsize=40)

        # Title
        if True:
            self.title_label = ttk.Label(local_frame, style='primary.Inverse.TLabel',
                                         font=('Helvetica', 10), padding=10)
            self.title_label.grid(row=0, column=0, sticky='nsew')

        # Widget Frame
        if True:
            self.widgets_frame = ttk.Frame(local_frame)
            self.widgets_frame.grid(row=1, column=0, sticky='nsew', padx=1)
            self.widgets_frame.rowconfigure(0, weight=1)
            self.widgets_frame.columnconfigure(0, weight=1)

        # Bottom frame
        if True:
            self.bottom_frame = ttk.Frame(local_frame, style='primary.TFrame')
            self.bottom_frame.grid(row=2, column=0, sticky='nsew')


# Local test of the model frames
if __name__ == '__main__':
    import tkinter as tk
    from ttkbootstrap import Style

    root = tk.Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.minsize(900, 600)
    root.style = Style(theme='flatly')
    root.title('ModelFrame')
    frame = ModelFrame(root)
    frame.grid(row=0, column=0, sticky='nsew')

    root_2 = tk.Toplevel(root)
    root_2.columnconfigure(0, weight=1)
    root_2.rowconfigure(0, weight=1)
    root_2.minsize(900, 600)
    root_2.style = Style(theme='flatly')
    root_2.title('GeneralFrame')
    frame = GeneralFrame(root_2)
    frame.grid(row=0, column=0, sticky='nsew')


    root.mainloop()
