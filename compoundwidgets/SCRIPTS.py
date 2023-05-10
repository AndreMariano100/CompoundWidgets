from PIL import Image, ImageTk


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


def max_chars(action, value, max_length):
    """ Checks for the maximum number of characters """
    if action == '1':
        if len(value) > int(max_length):
            return False
    return True


def isfloat(value):
    try:
        value = float(value)
    except ValueError:
        return False
    return True


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
