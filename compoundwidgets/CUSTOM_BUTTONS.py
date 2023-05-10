import ttkbootstrap as ttk
from .SCRIPTS import *
import os

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), 'IMAGES'))


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
