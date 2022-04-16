import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import os
from COMPOUND_WIDGETS import *



def screen_position(window, parent=None, delta_x=0, delta_y=0):
    """
    Defines the screen position for a given widget
    Input:
        window: widget (tk.Tk() or tk.TopLevel()) being positioned
        parent: reference to the screen positioning
        delta_x: additional distance relative to the center in the X direction (positive is right)
        delta_y: additional distance relative to the center in the Y direction (positive is down)
    Returns:
        position_string: string to be passed to the geometry manager to position the widget (self.geometry(string))
    """

    # Window (widget) Size
    if window.minsize()[0]:
        window_width = window.minsize()[0]
        window_height = window.minsize()[1]
    else:
        window_width = window.winfo_width()
        window_height = window.winfo_height()

    if parent:
        # Finds the parent position and center coordinates
        parent_x = parent.winfo_x()
        parent_y = parent.winfo_y()
        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()
        parent_center_x = int(parent_x + parent_width / 2)
        parent_center_y = int(parent_y + parent_height / 2)

        # Determines the new window start position (upper left)
        x_position = int(parent_center_x - window_width / 2) + int(delta_x)
        y_position = int(parent_center_y - window_height / 2) + int(delta_y)

    else:
        # Finds th screen size
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # Determines the new window start position (upper left)
        x_position = int((screen_width - window_width) / 2) + int(delta_x)
        y_position = int((screen_height - window_height) / 2) + int(delta_y)

    return f'{window_width}x{window_height}+{x_position}+{y_position}'


def open_image(file_name: str, size_x: int, size_y: int, maximize: bool = False) -> ImageTk:
    """
    Function to open an image file and to adjust its dimensions as specified
    Input:  file_name - full path to the image
            size_x - final horizontal size of the image
            size_y - final vertical size of the image
            maximize -  if True enlarges the image to fit the dimensions,
                        else if reduces the image to fit the dimensions
    Return: tk_image - ImageTK to be inserted on a widget
    """
    image_final_width = size_x
    image_final_height = size_y
    pil_image = Image.open(file_name)
    w, h = pil_image.size
    if maximize:
        final_scale = min(h / image_final_height, w / image_final_width)
    else:
        final_scale = max(h / image_final_height, w / image_final_width)
    width_final = int(w / final_scale)
    height_final = int(h / final_scale)
    final_pil_image = pil_image.resize((width_final, height_final), Image.ANTIALIAS)
    final_pil_image = final_pil_image.convert('RGBA')
    tk_image = ImageTk.PhotoImage(final_pil_image)
    return tk_image


class ModelTopLevel(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.style = self.master.style
        self.evaluation_dict = self.master.evaluation_dict
        self.unit_system = self.master.current_unit_system.get()

        self.title(self.master.title())
        self.minsize(300, 200)
        root_path = os.getcwd().split('MAIN')[0]
        image_path = os.path.join(root_path, 'MAIN_IMAGES')
        self.iconbitmap(os.path.join(image_path, 'petrobras.ico'))
        self.geometry(screen_position(self, self.master))
        self.grab_set()

    def show(self):
        self.deiconify()
        self.wait_window()
        return


class PressureConverter(ModelTopLevel):
    def __init__(self, master):

        # 'self' configuration
        if True:
            super().__init__(master)
            self.configure(bg=self.style.colors.primary)
            self.minsize(400, 250)
            self.resizable(0, 0)
            self.overrideredirect(True)

            self.columnconfigure(0, weight=1)
            self.rowconfigure(0, weight=0)
            self.rowconfigure(1, weight=1)
            self.rowconfigure(2, weight=0)

        # Current pressure unit
        if True:
            if self.master.current_unit_system.get() == 'Métrico (SI)':
                self.pressure_unit = tk.StringVar(value='kPa')
            else:
                self.pressure_unit = tk.StringVar(value='psi')

        # Title
        if True:
            root_path = os.getcwd().split('MAIN')[0]
            pressure_image_name = os.path.join(root_path, 'MAIN_WIDGETS', 'IMAGES', 'pressure.png')
            size = 20
            pressure_image = open_image(pressure_image_name, size_x=size, size_y=size)
            label = ttk.Label(self, text='  Pressure Conversion', anchor='center', justify='center', padding=10,
                              style='primary.Inverse.TLabel', image=pressure_image, compound='left',
                              font=('OpenSans', '14'))
            label.grid(row=0, column=0, sticky='nsew')
            label.image = pressure_image

        # Local frame
        if True:
            local_frame = ttk.Frame(self)
            local_frame.grid(row=1, column=0, sticky='nsew', padx=2)
            local_frame.columnconfigure(0, weight=1)
            local_frame.columnconfigure(1, weight=1)
            local_frame.rowconfigure(0, weight=1)
            local_frame.rowconfigure(1, weight=0)
            local_frame.rowconfigure(2, weight=1)

        # Input Pressure
        if True:
            self.pressure_entry = LabelEntry(local_frame, label_text=f'Original Pressure:', entry_value='',
                                             entry_numeric=True, entry_width=10, entry_method=self.calculate)
            self.pressure_entry.grid(row=0, column=0, sticky='ew', pady=10)

            # Pressure Units
            pressure_units_list = ('bar', 'kgf/cm²', 'kilopascal (kPa)', 'megapascal (MPa)', 'pascal (Pa)',
                                   'pound/foot²', 'pound/in² (psi)', '1000 pound/inch² (ksi)', 'atmosphere (atm)')
            self.selected_pressure_unit = tk.StringVar()

            self.pressure_unit_combo = ttk.Combobox(local_frame, textvariable=self.selected_pressure_unit,
                                                    justify='center', width=20, state='readonly',
                                                    values=pressure_units_list)
            self.pressure_unit_combo.grid(row=0, column=1, sticky='ew', padx=10)
            self.pressure_unit_combo.bind('<<ComboboxSelected>>', self.calculate)

        # Calculate Button
        if True:
            calculate_button = ttk.Button(local_frame, text="Convert to ...", command=self.calculate, width=20,
                                          style='secondary.TButton')
            calculate_button.grid(row=1, column=0, columnspan=2, sticky='ns', padx=30)

        # Output pressure
        if True:
            self.pressure_output = LabelEntry(local_frame, label_text=f'Equivalent Pressure:', entry_value='',
                                              entry_numeric=True, entry_width=10, entry_method=self.calculate)
            self.pressure_output.grid(row=2, column=0, sticky='ew', pady=10)
            self.pressure_output.readonly()

            # Pressure Output Units
            label = ttk.Label(local_frame, textvariable=self.pressure_unit, anchor='center')
            label.grid(row=2, column=1, sticky='ew', pady=10)

        # Buttons
        if True:
            local_frame = ttk.Frame(self, padding=10, style='primary.TFrame')
            local_frame.grid(row=2, column=0, sticky='nsew')
            local_frame.rowconfigure(0, weight=1)
            local_frame.columnconfigure(0, weight=1)
            local_frame.columnconfigure(1, weight=1)

            cancel_button = ttk.Button(local_frame, text="CANCEL", command=self.cancel, width=10,
                                       style='secondary.TButton')
            cancel_button.grid(row=0, column=0, sticky='nsew', padx=30)

            ok_button = ttk.Button(local_frame, text="OK", command=self.ok, width=10,
                                   style='secondary.TButton')
            ok_button.grid(row=0, column=1, sticky='nsew', padx=30)

        self.answer = None

    # Top Level Handling Methods ---------------------------------------------------------------------------------------
    def calculate(self, event=0):
        units = ('bar', 'kgf/cm²', 'kilopascal (kPa)', 'megapascal (MPa)', 'pascal (Pa)',
                 'pound/foot²', 'pound/in² (psi)', '1000 pound/inch² (ksi)', 'atmosphere (atm)')
        convert_to_kpa = (100, 98.0665, 1, 1000, 0.001, 0.04788026, 6.894757, 6894.757, 101.325)
        convert_to_psi = (14.50377, 14.22334, 0.1450377, 145.0377, 0.0001450377, 0.006944444, 1, 1000, 14.69595)

        selected_unit = self.selected_pressure_unit.get()
        selected_value = self.pressure_entry.get()

        if not selected_value or not selected_unit:
            return

        index = units.index(selected_unit)
        if self.pressure_unit.get() == 'kPa':
            self.pressure_output.set(f'{float(selected_value) * convert_to_kpa[index]:.2f}')
        else:
            self.pressure_output.set(f'{float(selected_value) * convert_to_psi[index]:.2f}')

    def cancel(self):
        self.answer = None
        self.destroy()

    def ok(self):
        current_value = self.pressure_output.get()
        if not current_value:
            self.answer = None
        else:
            self.answer = float(current_value)
        self.destroy()

    def show(self):
        self.deiconify()
        self.wait_window()
        return self.answer

