from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.config import Config


class DrawingSpace(Button):
    current_color = ObjectProperty((1, 1, 1, 1))

    def __init__(self):
        super(DrawingSpace, self).__init__()
        self.selected_color_index = 0
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

        self.tasktext = Label()
        self.add_widget(self.tasktext)
        self.tasktext.text = "This is a really long string for testing. We want the text to correctly align."
        self.tasktext.halign = 'left'
        self.tasktext.valign = 'middle'
        self.tasktext.shorten_from = 'right'
        self.bind(size=self.size_change)

    def cycle_colors(self):
        if self.selected_color_index >= len(self.colors) - 1:
            print(len(self.colors))
            self.selected_color_index = 0
        self.selected_color_index += 1
        print(self.selected_color_index)
        self.current_color = self.colors[self.selected_color_index]
        self.tasktext.shorten = not self.tasktext.shorten

    def size_change(self, _object, size):
        start = self.width*.05 + 5

        self.tasktext.width = self.width - start - 20
        self.tasktext.height = self.height
        self.tasktext.text_size = (self.width - start - 40, None)

        print("Text size:    {}".format(self.tasktext.text_size))
        print("Texture size: {}".format(self.tasktext.texture_size))
        if self.tasktext.texture_size[1] + 40 >= self.height and self.shorten == False:
            print("True")
            self.tasktext.shorten = True
        elif self.tasktext.shorten:
            self.tasktext.shorten = False
        self.tasktext.x = self.x + start + 20
        self.tasktext.y = self.y


class DrawingApp(App):
    def build(self):
        return DrawingSpace()


if __name__ == '__main__':
    Config.set('graphics', 'width', '500')
    Config.set('graphics', 'height', '200')
    DrawingApp().run()
