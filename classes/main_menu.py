import pygame
import pygame_menu
from pygame_menu import sound
from pygame_menu.themes import Theme


class Menu:
    menu = None
    screen = None
    my_theme = None
    my_image = None
    sound = None

    def my_theme(self):
        font = pygame_menu.font.FONT_8BIT
        styl = pygame_menu.widgets.MENUBAR_STYLE_NONE
        my_theme = Theme(widget_font=font)
        my_theme.title_font_color = (255, 255, 255)
        my_theme.title_font = font
        my_theme.title_bar_style = styl
        my_theme.widget_border_color = (55, 25, 25)
        self.my_image = pygame_menu.baseimage.BaseImage(
            image_path='img/bckg.jpg',
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY
        )
        my_theme.background_color = self.my_image
        return my_theme

    def __init__(self, arg_screen, sound_path):
        self.menu = pygame_menu.Menu(600, 800, 'Shamboogeon',
                                     theme=self.my_theme())

        self.screen= arg_screen
        self.sound= pygame.mixer.Sound(sound_path)
        self.sound.play(-1)
        self.sound.set_volume(0.2)

    def add_button(self,name ,  action):
        self.menu.add_button(name, action, self.screen)

    def response(self,width,height):
        self.menu = pygame_menu.Menu(height, width, 'Shamboogeon',
                                     theme=self.my_theme())

        """ 
        engine = sound.Sound()
        engine.set_sound(sound.SOUND_TYPE_OPEN_MENU, 'img/drzwi_loch.ogg')
        self.menu.set_sound(engine, recursive=True)
        """





        


