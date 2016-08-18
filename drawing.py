from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ListProperty, StringProperty
from kivy.config import Config


class DrawingSpace(Button):
    current_project_color = ListProperty([.3, .5, .6, 1])
    current_shadow_color = ListProperty([1, 1, 1, 0.4])

    def __init__(self):
        super(DrawingSpace, self).__init__()
        self.selected_color_index = 0
        self.multi_line_height = 0  # This is to smooth out the toggle between shorten.
        self.colors = [
            (1, 0, 0, 1),
            (0, 1, 0, 1),
            (0, 0, 1, 1),
            (1, 1, 0, 1),
            (0, 1, 1, 1),
            (1, 0, 1, 1),
            (1, 1, 1, 1),
            (0, 0, 0, 1)
        ]

        # Return a list of only inherited label attributes

        self.tasktext = Label()
        self.add_widget(self.tasktext)
        self.tasktext.text = "This is a really long string for testing. We want the text to correctly align."
        self.tasktext.color = [0,0,0,1] # primary color
        self.tasktext.disabled_color = [0,0,0,.38] # disabled color
        self.tasktext.font_size = 18

        self.tasktext.halign = 'left'
        self.tasktext.valign = 'middle'
        self.tasktext.shorten_from = 'right'
        self.bind(size=self.size_change)

    def set_text(self, text):
        self.tasktext.text = text

    def cycle_colors(self):
        pass
        # if self.selected_color_index >= len(self.colors) - 1:
        #     print(len(self.colors))
        #     self.selected_color_index = 0
        # self.selected_color_index += 1
        # print(self.selected_color_index)
        # self.current_color = self.colors[self.selected_color_index]
        # self.tasktext.shorten = not self.tasktext.shorten

    def size_change(self, _object, size, short_padding=20):
        start = self.width*.07 + 5

        self.tasktext.width = self.width - start - 20
        self.tasktext.height = self.height
        self.tasktext.text_size = (self.width - start - 40, None)

        if not self.tasktext.shorten:
            self.multi_line_height = self.tasktext.texture_size[1] + short_padding

        if self.tasktext.texture_size[1] + short_padding >= self.height and not self.tasktext.shorten:
            self.tasktext.shorten = True
        elif self.multi_line_height < self.height:
            self.tasktext.shorten = False

        self.tasktext.x = self.x + start + 20
        self.tasktext.y = self.y


class DrawingApp(App):
    def build(self):
        return DrawingSpace()


if __name__ == '__main__':
    Config.set('graphics', 'width', '500')
    Config.set('graphics', 'height', '200')
    a = DrawingApp().run()


