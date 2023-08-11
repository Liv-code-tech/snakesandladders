import random

from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix import button
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


class GameBoard(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.roll_die = 0
        self.player_position = 0
        self.counter = 0
        button_size = dp(62)
        for y_axis in range(0, 8):
            for x_axis in range(0, 8):
                self.counter += 1
                if y_axis % 2 == 0:
                    self.square = Button(text=str(self.counter), size_hint=(None, None),
                                    size=(button_size, button_size),
                                    pos=(x_axis * button_size, y_axis * button_size),
                                    font_size=dp(35),
                                    font_name="snakefont.ttf")
                else:
                    self.square = Button(text=str(self.counter), size_hint=(None, None),
                                    size=(button_size, button_size),
                                    pos=((button_size * 7) - (x_axis * button_size), y_axis * button_size),
                                    font_size=dp(35),
                                    font_name="snakefont.ttf")

                self.add_widget(self.square)

    def on_button_click(self):
        self.roll_die = random.randint(1, 6)
        self.player_position += self.roll_die
        
        print("Button clicked")
        self.ids.current_roll.text = str(self.roll_die)


class MainWidget(Widget):
    pass


class SnakesAndLaddersApp(App):
    pass


SnakesAndLaddersApp().run()
