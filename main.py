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
        self.all_buttons = []
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
                self.all_buttons.append(self.square)

    def on_button_click(self):
        self.roll_die = random.randint(1, 6)
        self.all_buttons[self.player_position].background_color = [1, 1, 1, 1]
        self.player_position += self.roll_die
        if self.player_position >= 63:
            self.ids.roll_win.text = str("You won! Game over.")
        else:
            self.all_buttons[self.player_position].background_color = [1, 0, 0, 1]
            print("Button clicked")
            self.ids.current_roll.text = str(self.roll_die)

    def snake(self,):
        snake_head = self.player_position
        if snake_head == 20:
            snake_tail = 10
        elif snake_head == 43:
            snake_tail = 13
        elif snake_head == 38:
            snake_tail = 14
        self.player_position = snake_tail

    def ladder(self, ladder_bottom, ladder_top):
        if self.player_position == ladder_bottom:
            self.player_position = ladder_top

class MainWidget(Widget):
    pass


class SnakesAndLaddersApp(App):
    pass


SnakesAndLaddersApp().run()
