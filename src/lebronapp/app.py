"""
My first app
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

# 76ers colors
Blue = "#006BB6"
Red = "#ED174C"
Navy = "#002B5C"
White = "#FFFFFF"

class LebronApp(toga.App):
    def startup(self):
        # Space at the top
        top_space = toga.Box(style = Pack(flex = 1, background_color = Navy))

        # Picture of LeBron
        lebron_pic = toga.ImageView(toga.Image("resources/Lebron.png"), style=Pack(width = 280, height = 325, background_color = Navy, margin = 10), )

        # Title
        title = toga.Label("LeBron James", style = Pack(font_size = 30, font_weight = "bold",
                                                      text_align = CENTER, color = White, background_color = Navy, margin = 10), )

        red_line = toga.Box(style = Pack(width = 120, height = 4, background_color = Red))

        # Subtitle
        subtitle = toga.Label("His career story", style = Pack(font_size = 14, text_align = CENTER,
                                                             color = White, background_color = Navy, margin = 10), )

        # The Start button
        button = toga.Button("Start", on_press = self.show_app_screen, style = Pack(color = White, background_color = Red, margin = 20), )

        # Space at the bottom
        bottom_space = toga.Box(style = Pack(flex = 1, background_color = Navy))

        self.splash_box = toga.Box(
            children = [top_space, lebron_pic, title, red_line, subtitle, button, bottom_space],
            style = Pack(direction = COLUMN, align_items = CENTER, background_color = Navy),
        )

        # The main app screen (blank)
        top_bar = toga.Box(style=Pack(height = 12, background_color = Red))

        # Work in progress message
        menu_top_space = toga.Box(style=Pack(flex = 1, background_color = Navy))
        menu_label = toga.Label("Work in progress", style=Pack(font_size = 20, font_weight = "bold",
                               text_align = CENTER, color = White, background_color = Navy, margin = 10), )
        menu_bottom_space = toga.Box(style=Pack(flex = 1, background_color = Navy))

        self.app_box = toga.Box(children=[top_bar, menu_top_space, menu_label, menu_bottom_space], style=Pack(direction = COLUMN, background_color = Navy))

        # Phone sized window
        self.main_window = toga.MainWindow(
            title = self.formal_name,
            size = (390, 760),
            resizable = False,
        )
        self.main_window.content = self.splash_box
        self.main_window.show()

    def show_app_screen(self, widget):
        # Run when start pressed
        self.main_window.content = self.app_box
def main():
    return LebronApp()