from PIL import Image, ImageTk, ImageFilter
import json


# Entry validation methods ---------------------------------------------------------------------------------------------
def float_only(action, value, text, max_length=None):
    """ Checks that only float related characters are accepted as input """

    permitted = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '-']

    if action == '1':
        if str(max_length) != 'None':
            if len(value) > int(max_length):
                return False
        if value == '.' and text == '.':
            return False
        elif value == '-' and text == '-':
            return True
        elif text in permitted:
            try:
                float(value)
                return True
            except ValueError:
                return False
        else:
            return False
    else:
        return True


def int_only(action, value, text, max_length=None):
    """ Checks that only int related characters are accepted as input """

    permitted = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']

    if action == '1':
        if str(max_length) != 'None':
            if len(value) > int(max_length):
                return False
        if value == '-' and text == '-':
            return True
        elif text in permitted:
            try:
                int(value)
                return True
            except ValueError:
                return False
        else:
            return False
    else:
        return True


def max_chars(action, value, max_length):
    """ Checks for the maximum number of characters """
    if action == '1':
        if len(value) > int(max_length):
            return False
    return True


# File methods ---------------------------------------------------------------------------------------------------------
def open_image(file_name: str, size_x: int, size_y: int, maximize: bool = False, blur: bool = False) -> ImageTk:
    """
    Function to open an image file and to adjust its dimensions as specified

    Input:  file_name - full path to the image
            size_x - final horizontal size of the image
            size_y - final vertical size of the image
            maximize -  if True enlarges the image to fit the dimensions,
                        else if reduces the image to fit the dimensions
            blur - whether to apply a blur filter to the image

    Return: tk_image - ImageTK to be inserted on a widget
    """

    image_final_width = size_x
    image_final_height = size_y
    image_file_name = file_name

    pil_image = Image.open(image_file_name)
    w, h = pil_image.size

    if maximize:
        final_scale = min(h / image_final_height, w / image_final_width)
    else:
        final_scale = max(h / image_final_height, w / image_final_width)

    width_final = int(w / final_scale)
    height_final = int(h / final_scale)
    final_pil_image = pil_image.resize((width_final, height_final), Image.LANCZOS)
    final_pil_image = final_pil_image.convert('RGBA')
    if blur:
        final_pil_image = final_pil_image.filter(ImageFilter.BoxBlur(5))

    tk_image = ImageTk.PhotoImage(final_pil_image)

    return tk_image


def read_json_file(file_path):
    """ Given the file path, reads the json file and returns the data """
    try:
        with open(file_path, 'r') as file_object:
            data = json.load(file_object)
    except (IOError, FileNotFoundError):
        raise Exception(f'Error reading JSON file {file_path}')
    except PermissionError:
        raise Exception(f'Permission error reading JSON file {file_path}')
    except Exception:
        raise Exception(f'Unknown error while trying to read file {file_path}')
    else:
        return data


# Math methods ---------------------------------------------------------------------------------------------------------
def isfloat(number):
    """ Fast check whether a value is a float """

    if not str(number):
        return False
    try:
        float(number)
        return True
    except (ValueError, TypeError):
        return False


def is_list_of_floats(list_of_values):
    """ Fast check whether all values on a list are float """

    for value in list_of_values:
        if not isfloat(value):
            return False
    return True


def interpolate(x_value, x0, x1, y0, y1):
    """
    Obtains the y value for an interpolation.
    Input:
        x_value - X value of interest
        x0 - initial value ox X
        x1 - final value of X
        y0 - initial value of Y
        y1 - final value of Y
    Returns:
        Y value of interest
    """

    if not is_list_of_floats([x_value, x0, x1, y0, y1]):
        return None

    x_value = float(x_value)
    x0 = float(x0)
    x1 = float(x1)
    y0 = float(y0)
    y1 = float(y1)

    if x0 <= x_value <= x1:
        try:
            y_value = y0 + (x_value - x0) * (y1 - y0) / (x1 - x0)
        except ZeroDivisionError:
            return y0
        return y_value

    return None


def interpolate_x(x_value, x_series, y_series):
    """
    Obtains the y value for an interpolation.
    Input:
        x_value - X value of interest
        x_series - array of x values
        y_series - array of y values
    Returns:
        y_value - Y value of interest
    """
    if not x_value or not x_series or not y_series:
        return None

    if not hasattr(x_series, '__iter__') or not hasattr(y_series, '__iter__') or not isfloat(x_value):
        return None

    if x_value < x_series[0] or x_value > x_series[-1]:
        return None

    if len(x_series) != len(y_series):
        return None

    if x_value in x_series:
        return y_series[x_series.index(x_value)]

    index_after = 0
    for i, value in enumerate(x_series):
        if value > x_value:
            index_after = i
            break

    if index_after:
        x_interval = float(x_series[index_after]) - float(x_series[index_after - 1])
        y_interval = float(y_series[index_after]) - float(y_series[index_after - 1])
        x_progress = float(x_value) - float(x_series[index_after - 1])
        y_value = float(y_series[index_after - 1]) + x_progress * y_interval / x_interval
    else:
        y_value = None

    return y_value


# Widget methods -------------------------------------------------------------------------------------------------------
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


def pprint(_dict, tab=0, break_list=False):
    if not isinstance(_dict, dict):
        raise TypeError('Local method pprint works only with dictionaries')
    tab = tab
    space = tab * ' '
    for k, v in _dict.items():
        k = str(k).replace('\n', ' ')
        print(f'{space}{k}', end=': ')
        if type(v) in (int, float, complex, bool, str):
            v = str(v).replace('\n', ' ')
            print(v)
        elif type(v) in (list, tuple, range, set, frozenset):
            if break_list:
                print()
                for v2 in v:
                    print(f'{space}  {v2}')
            else:
                for i in range(len(v)):
                    if i != len(v) - 1:
                        print(v[i], end=' / ')
                    else:
                        print(v[i])
        elif type(v) == dict:
            print()
            new_tab = tab + 4
            pprint(v, new_tab, break_list)


def retrieve_description(_dict, tab=0, list_break=False):

    tab = tab
    final_text = ''
    engineering_units = ('-', '°C', '°F',
                         '°C/s', '°C/min', '°C/hour', '°F/s', '°F/min', '°F/hour',
                         'mm', 'cm', 'm', 'in', 's', 'min', 'hour', 'day', 'year',
                         'mm²', 'cm²', 'm²', 'in²',
                         'kPa', 'bar', 'kgf/cm²', 'MPa', 'atmosphere', 'ksi', 'psi',
                         'GPa', 'x10³ ksi', 'N', 'kN', 'kgf', 'lbf',
                         'N.m', 'kN.m', 'kgf.m', 'lbf.ft', 'joule', 'ft-lbf',
                         'MPa.√m', 'N/mm^(3/2)', 'ksi.√in', 'joule/m²', 'ft-lbf/ft²',
                         '10e-6/°C', '10e-6/°F')
    for k, v in _dict.items():
        final_text += tab * '\t' + f'{k}: '
        if type(v) in (int, float, complex, bool, str):
            final_text += f'{v}\n'

        elif type(v) in (list, tuple, range, set, frozenset):
            if list_break:
                final_text += '\n'
                for item in v:
                    final_text += (tab + 1) * '\t' + str(item) + '\n'
            else:
                str_v = [str(item) for item in v]
                if len(str_v) == 2 and str_v[1] in engineering_units:
                    final_text += ' '.join(str_v) + '\n'
                else:
                    final_text += '/'.join(str_v) + '\n'
        elif type(v) == dict:
            final_text += '\n'
            final_text += retrieve_description(v, tab + 1, list_break=list_break)
        if tab == 0:
            final_text += '\n'

    return final_text


# Conversion methods ---------------------------------------------------------------------------------------------------
def convert_temperature(f_temperature=None, c_temperature=None):
    """ Temperature conversion: °F <-> °C"""

    if f_temperature is not None:
        if isinstance(f_temperature, tuple):
            f_temperature = f_temperature[0]
        return round(5 * (f_temperature - 32) / 9, 3), '°C'

    if c_temperature is not None:
        if isinstance(c_temperature, tuple):
            c_temperature = c_temperature[0]
        return round(9 * c_temperature / 5 + 32, 3), '°F'


def convert_stress(ksi_stress=None, mpa_stress=None):
    """ Stress conversion:  ksi <-> MPa """

    if ksi_stress is not None:
        if isinstance(ksi_stress, tuple):
            ksi_stress = ksi_stress[0]
        return round(ksi_stress * 6.894757, 3), 'MPa'

    if mpa_stress is not None:
        if isinstance(mpa_stress, tuple):
            mpa_stress = mpa_stress[0]
        return round(mpa_stress / 6.894757, 3), 'ksi'


def convert_pressure(psi_pressure=None, kpa_pressure=None):
    """ Stress conversion: psi <-> kPa"""

    if psi_pressure is not None:
        if isinstance(psi_pressure, tuple):
            psi_pressure = psi_pressure[0]
        return round(psi_pressure * 6.894757, 3), 'kPa'

    if kpa_pressure is not None:
        if isinstance(kpa_pressure, tuple):
            kpa_pressure = kpa_pressure[0]
        return round(kpa_pressure / 6.894757, 3), 'psi'


def convert_length(in_length=None, mm_length=None):
    """ Length conversion: in <-> mm """

    if in_length is not None:
        if isinstance(in_length, tuple):
            in_length = in_length[0]
        return round(in_length * 25.4, 3), 'mm'

    if mm_length is not None:
        if isinstance(mm_length, tuple):
            mm_length = mm_length[0]
        return round(mm_length / 25.4, 3), 'in'
