import ttkbootstrap as ttk
from .SCRIPTS import *
import os

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), 'IMAGES'))


class CompoundButton(ttk.Button):
    """ Base widget for the compound buttons """

    def __init__(self, parent, *args, style=None, language='en', width=10, **kwargs):
        super().__init__(parent, *args, width=width, compound='right', **kwargs)

        # Style definition
        if True:
            self.style_list = (
                'danger', 'warning', 'info', 'success',
                'secondary', 'primary', 'light', 'dark'
            )
            if style:
                if style not in self.style_list:
                    self.style = 'primary'
                else:
                    self.style = style
            else:
                self.style = 'primary'

        self.language = language
        self.width = width
        self.disabled = False
        self.set_style(self.style)

    def check_size(self):
        self.update_idletasks()
        if self.winfo_reqwidth() > self.winfo_width():
            self.configure(width=f'{self.winfo_reqwidth()}p')

        if self.cget('text') == 'Copiar para àrea de transferência\t':
            print(self.winfo_reqwidth(), self.winfo_width())

    def disable(self):
        self.disabled = True
        self.configure(state='disabled')

    def enable(self):
        self.disabled = False
        self.configure(state='normal')

    def set_style(self, bootstyle):
        if bootstyle not in self.style_list:
            return
        self.style = bootstyle
        if self.disabled:
            return
        self.configure(bootstyle=bootstyle)


class YesButton(CompoundButton):
    def __init__(self, parent, *args, style='success', language='en', width=10, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'yes.png')
        tk_image = open_image(file_name=image_path, size_x=20, size_y=20, maximize=True)

        if language == 'br':
            text = 'SIM\t'
        else:
            text = 'YES\t'

        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()


class NoButton(CompoundButton):
    def __init__(self, parent, *args, style='danger', language='en', width=10, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'no.png')
        tk_image = open_image(file_name=image_path, size_x=20, size_y=20)

        if language == 'br':
            text = 'NÃO\t'
        else:
            text = 'NO\t'

        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()


class OKButton(CompoundButton):
    def __init__(self, parent, *args, style='success', language='en', width=10, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'yes.png')
        tk_image = open_image(file_name=image_path, size_x=20, size_y=20, maximize=True)

        self.configure(text='OK\t', image=tk_image)
        self.image = tk_image
        self.check_size()


class CancelButton(CompoundButton):
    def __init__(self, parent, *args, language='en', style='danger', width=10,  **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'no.png')
        tk_image = open_image(file_name=image_path, size_x=20, size_y=20)

        if language == 'br':
            text = 'CANCELAR'
        else:
            text = 'CANCEL\t'

        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()


class ClearButton(CompoundButton):
    def __init__(self, parent, *args, language='en', style='warning', width=10, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'clear.png')
        tk_image = open_image(file_name=image_path, size_x=20, size_y=20, maximize=True)

        if language == 'br':
            text = 'LIMPAR\t'
        else:
            text = 'CLEAR\t'

        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()


class SaveButton(CompoundButton):
    def __init__(self, parent, *args, style='primary', language='en', width=10, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'save.png')
        tk_image = open_image(file_name=image_path, size_x=20, size_y=20)

        if language == 'br':
            text = 'SALVAR\t'
        else:
            text = 'SAVE\t'

        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()


class CalculateButton(CompoundButton):
    def __init__(self, parent, *args, style='primary', language='en', width=15, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'calculate.png')
        tk_image = open_image(file_name=image_path, size_x=20, size_y=20)

        if language == 'br':
            text = 'CALCULAR\t'
        else:
            text = 'CALCULATE\t'

        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()


class HelpButton(CompoundButton):
    def __init__(self, parent, *args, language='en', style='secondary', width=3,  **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'help.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        self.configure(image=tk_image)
        self.image = tk_image
        self.check_size()


class BackButton(CompoundButton):
    def __init__(self, parent, *args, style='danger', language='en', width=15, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)
        image_path = os.path.join(ROOT_DIR, 'back.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        if language == 'br':
            text = 'VOLTAR\t\t'
        else:
            text = 'BACK\t\t'

        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()


class AddToReport(CompoundButton):
    def __init__(self, parent, *args, language='en', style='success', width=15,  **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)
        image_path = os.path.join(ROOT_DIR, 'add_to_form.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        if language == 'br':
            text = 'ADICIONAR\t'
        else:
            text = 'ADD\t\t'

        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()


class EditReport(CompoundButton):
    def __init__(self, parent, *args, style='primary', language='en', width=15, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)
        image_path = os.path.join(ROOT_DIR, 'edit_form.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        if language == 'br':
            text = 'EDITAR\t\t'
        else:
            text = 'EDIT\t\t'

        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()


class RemoveFromReport(CompoundButton):
    def __init__(self, parent, *args, style='danger', language='en', width=15, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'remove_from_form.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        if language == 'br':
            text = 'EXCLUIR\t\t'
        else:
            text = 'DELETE\t\t'

        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()


class AddNewButton(CompoundButton):
    def __init__(self, parent, *args, style='success', language='en', width=1, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'add_new.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        self.configure(image=tk_image)
        self.image = tk_image
        self.check_size()


class EraseButton(CompoundButton):
    def __init__(self, parent, *args, style='danger', language='en', width=1, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'trash_can.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        self.configure(image=tk_image)
        self.image = tk_image
        self.check_size()


class QuitButton(CompoundButton):
    def __init__(self, parent, *args, style='danger', language='en', width=15, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'quit.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        if language == 'br':
            text = 'SAIR\t\t'
        else:
            text = 'EXIT\t\t'

        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()


class ClipBoardButton(CompoundButton):
    def __init__(self, parent, *args, style='primary', language='en', width=20, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'copy_to_clipboard.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        if language == 'br':
            text = 'Copiar para àrea de transferência\t'
        else:
            text = 'Copy to Clipboard\t'
        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()


class NextButton(CompoundButton):
    def __init__(self, parent, *args, style='primary', language='en', width=15, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'right_arrow.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        if language == 'br':
            text = 'Próximo\t\t'
        else:
            text = 'NEXT\t\t'

        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()


class PreviousButton(CompoundButton):
    def __init__(self, parent, *args, style='primary', language='en', width=15, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'left_arrow.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        if language == 'br':
            text = 'Anterior\t\t'
        else:
            text = 'PREVIOUS\t'

        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()


class UpButton(CompoundButton):
    def __init__(self, parent, *args, style='primary', language='en', width=15, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'up_arrow.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        if language == 'br':
            text = 'Acima\t\t'
        else:
            text = 'ABOVE\t\t'

        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()


class DownButton(CompoundButton):
    def __init__(self, parent, *args, style='primary', language='en', width=15, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'down_arrow.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        if language == 'br':
            text = 'Abaixo\t\t'
        else:
            text = 'BELOW\t\t'

        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()


class SearchButton(CompoundButton):
    def __init__(self, parent, *args, style='primary', language='en', width=15, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'search.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        if language == 'br':
            text = 'Procurar\t\t'
        else:
            text = 'SEARCH\t\t'

        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()


class HomeButton(CompoundButton):
    def __init__(self, parent, *args, style='primary', language='en', width=15, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'home.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        if language == 'br':
            text = 'Início\t\t'
        else:
            text = 'HOME\t\t'

        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()


class MainMenuButton(CompoundButton):
    def __init__(self, parent, *args, style='primary', language='en', width=15, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'burguer_menu.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        if language == 'br':
            text = 'Menu\t\t'
        else:
            text = 'MENU\t\t'

        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()


class AppsMenuButton(CompoundButton):
    def __init__(self, parent, *args, style='primary', language='en', width=15, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'apps_menu.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        if language == 'br':
            text = 'Menu\t\t'
        else:
            text = 'MENU\t\t'

        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()


class ConfigurationButton(CompoundButton):
    def __init__(self, parent, *args, style='primary', language='en', width=20, **kwargs):
        super().__init__(parent, *args, style=style, language=language, width=width, **kwargs)

        image_path = os.path.join(ROOT_DIR, 'configuration.png')
        tk_image = open_image(file_name=image_path, size_x=30, size_y=20)

        if language == 'br':
            text = 'Configurações\t\t'
        else:
            text = 'CONFIGURATION\t\t'

        self.configure(text=text, image=tk_image)
        self.image = tk_image
        self.check_size()
