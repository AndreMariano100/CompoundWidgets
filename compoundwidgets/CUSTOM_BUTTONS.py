import ttkbootstrap as ttk
from PIL import Image, ImageTk
import os

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), 'IMAGES'))


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


class YesButton(ttk.Button):
    def __init__(self, *args, language='en', style='success', width=10, **kwargs):
        super().__init__(*args, **kwargs)
        image_path = os.path.join(ROOT_DIR, 'yes.png')
        tk_image = open_image(file_name=image_path, size_x=20, size_y=20, maximize=True)

        if language == 'br':
            text = 'SIM\t'
        else:
            text = 'YES\t'

        self.configure(text=text, bootstyle=style, width=width, image=tk_image, compound='right')
        self.image = tk_image


class NoButton(ttk.Button):
    def __init__(self, *args, language='en', style='danger', width=10, **kwargs):
        super().__init__(*args, **kwargs)
        image_path = os.path.join(ROOT_DIR, 'no.png')
        tk_image = open_image(file_name=image_path, size_x=20, size_y=20)

        if language == 'br':
            text = 'NÃO\t'
        else:
            text = 'NO\t'

        self.configure(text=text, bootstyle=style, width=width, image=tk_image, compound='right')
        self.image = tk_image


class OKButton(ttk.Button):
    def __init__(self, *args, language='en', style='success', width=10, **kwargs):
        super().__init__(*args, **kwargs)
        image_path = os.path.join(ROOT_DIR, 'yes.png')
        tk_image = open_image(file_name=image_path, size_x=20, size_y=20, maximize=True)

        self.configure(text='OK\t', bootstyle=style, width=width, image=tk_image, compound='right')
        self.image = tk_image


class CancelButton(ttk.Button):
    def __init__(self, *args, language='en', style='danger', width=10,  **kwargs):
        super().__init__(*args, **kwargs)
        image_path = os.path.join(ROOT_DIR, 'no.png')
        tk_image = open_image(file_name=image_path, size_x=20, size_y=20)

        if language == 'br':
            text = 'CANCELAR\t'
        else:
            text = 'CANCEL\t'

        self.configure(text=text, bootstyle=style, width=width, image=tk_image, compound='right')
        self.image = tk_image


class ClearButton(ttk.Button):
    def __init__(self, *args, language='en', style='warning', width=10, **kwargs):
        super().__init__(*args, **kwargs)
        image_path = os.path.join(ROOT_DIR, 'clear.png')
        tk_image = open_image(file_name=image_path, size_x=20, size_y=20, maximize=True)

        if language == 'br':
            text = 'LIMPAR\t'
        else:
            text = 'CLEAR\t'

        self.configure(text=text, bootstyle=style, width=width, image=tk_image, compound='right')
        self.image = tk_image


class SaveButton(ttk.Button):
    def __init__(self, *args, language='en', style='success', width=10, **kwargs):
        super().__init__(*args, **kwargs)
        image_path = os.path.join(ROOT_DIR, 'save.png')
        tk_image = open_image(file_name=image_path, size_x=20, size_y=20)

        if language == 'br':
            text = 'SALVAR\t'
        else:
            text = 'SAVE\t'

        self.configure(text=text, bootstyle=style, width=width, image=tk_image, compound='right')
        self.image = tk_image


class CalculateButton(ttk.Button):
    def __init__(self, *args, language='en', style='primary', width=15, **kwargs):
        super().__init__(*args, **kwargs)
        image_path = os.path.join(ROOT_DIR, 'calculate.png')
        tk_image = open_image(file_name=image_path, size_x=20, size_y=20)

        if language == 'br':
            text = 'CALCULAR\t'
        else:
            text = 'CALCULATE\t'

        self.configure(text=text, bootstyle=style, width=width, image=tk_image, compound='right')
        self.image = tk_image


class HelpButton(ttk.Button):
    def __init__(self, *args, language='en', style='secondary', width=10,  **kwargs):
        super().__init__(*args, **kwargs)
        image_path = os.path.join(ROOT_DIR, 'help.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        self.configure(bootstyle=style, width=width,  image=tk_image)
        self.image = tk_image


class BackButton(ttk.Button):
    def __init__(self, *args, language='en', style='primary', width=15, **kwargs):
        super().__init__(*args, **kwargs)
        image_path = os.path.join(ROOT_DIR, 'back.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        if language == 'br':
            text = 'VOLTAR\t\t'
        else:
            text = 'BACK\t\t'

        self.configure(text=text, bootstyle=style, width=width, image=tk_image, compound='right')
        self.image = tk_image


class AddToReport(ttk.Button):
    def __init__(self, *args, language='en', style='success', width=15,  **kwargs):
        super().__init__(*args, **kwargs)
        image_path = os.path.join(ROOT_DIR, 'add_to_form.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        if language == 'br':
            text = 'ADICIONAR\t'
        else:
            text = 'ADD\t\t'

        self.configure(text=text, bootstyle=style, width=width,  image=tk_image, compound='right')
        self.image = tk_image


class EditReport(ttk.Button):
    def __init__(self, *args, language='en', style='primary', width=15, **kwargs):
        super().__init__(*args, **kwargs)
        image_path = os.path.join(ROOT_DIR, 'edit_form.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        if language == 'br':
            text = 'EDITAR\t\t'
        else:
            text = 'EDIT\t\t'

        self.configure(text=text, bootstyle=style, width=width, image=tk_image, compound='right')
        self.image = tk_image


class RemoveFromReport(ttk.Button):
    def __init__(self, *args, language='en', style='danger', width=15, **kwargs):
        super().__init__(*args, **kwargs)
        image_path = os.path.join(ROOT_DIR, 'remove_from_form.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        if language == 'br':
            text = 'EXCLUIR\t\t'
        else:
            text = 'DELETE\t\t'

        self.configure(text=text, bootstyle=style, width=width, image=tk_image, compound='right')
        self.image = tk_image


class AddNewButton(ttk.Button):
    def __init__(self, *args, language='en', style='primary', width=15, **kwargs):
        super().__init__(*args, **kwargs)
        image_path = os.path.join(ROOT_DIR, 'add_new.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        self.configure(bootstyle=style, width=width, image=tk_image, padding=2)
        self.image = tk_image


class EraseButton(ttk.Button):
    def __init__(self, *args, language='en', style='danger', width=15, **kwargs):
        super().__init__(*args, **kwargs)
        image_path = os.path.join(ROOT_DIR, 'trash_can.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        self.configure(bootstyle=style, width=width, image=tk_image, padding=2)
        self.image = tk_image


class QuitButton(ttk.Button):
    def __init__(self, *args, language='en', style='danger', width=15, **kwargs):
        super().__init__(*args, **kwargs)
        image_path = os.path.join(ROOT_DIR, 'quit.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        if language == 'br':
            text = 'SAIR\t\t'
        else:
            text = 'EXIT\t\t'

        self.configure(text=text, bootstyle=style, width=width, image=tk_image, compound='right')
        self.image = tk_image
