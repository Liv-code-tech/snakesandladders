import random

from kivy import Config
from kivy.app import App
from kivy.graphics import Line, Color
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


class GameBoard(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rollDie = 0
        self.playerPosition = 0
        self.playerName = ""
        self.allPlayers = []
        self.counter = 0
        self.allButtons = []
        self.buttonSize = dp(62)
        self.halfButtonSize = self.buttonSize/2
        self.generate_ladders()
        self.generate_snakes()

        for yAxis in range(0, 8):
            for xAxis in range(0, 8):
                self.counter += 1
                if yAxis % 2 == 0:
                    self.square = Button(text=str(self.counter), size_hint=(None, None),
                                    size=(self.buttonSize, self.buttonSize),
                                    pos=(xAxis * self.buttonSize, yAxis * self.buttonSize),
                                    font_size=dp(35),
                                    font_name="snakefont.ttf")
                else:
                    self.square = Button(text=str(self.counter), size_hint=(None, None),
                                    size=(self.buttonSize, self.buttonSize),
                                    pos=((self.buttonSize * 7) - (xAxis * self.buttonSize), yAxis * self.buttonSize),
                                    font_size=dp(35),
                                    font_name="snakefont.ttf")

                self.square.bind(on_press=self.get_position)
                self.add_widget(self.square)
                self.allButtons.append(self.square)
        self.draw_snake()
        self.draw_ladder()

    def get_position(self, event):
        print(event.pos)

    def on_button_click(self):
        if self.playerPosition >= 63:
            return
        else:
            self.rollDie = random.randint(1, 6)
            self.allButtons[self.playerPosition].background_color = [1, 1, 1, 1]
            self.playerPosition += self.rollDie
            self.check_is_field_snake()
            self.check_is_field_ladder()
            print(self.playerPosition + 1)
        if self.playerPosition >= 63:
            print("YOU WON")
            self.ids.rollWin.text = str("You won! Game over.")
        else:
            self.allButtons[self.playerPosition].background_color = [1, 0, 0, 1]
            print("Button clicked")
            self.ids.currentRoll.text = str(self.rollDie)

    def generate_ladders(self):
        self.ladders = [[13 - 1, 44 - 1], [27 - 1, 47 - 1], [33 - 1, 51 - 1], [41 - 1, 57 - 1], [3 - 1, 30 - 1]]

    def generate_snakes(self):
        self.snakes = [[63-1, 35-1], [56-1, 15-1], [32-1, 12-1], [39-1, 6-1], [61-1, 23-1]]

    def draw_snake(self):
        for i, idx in enumerate(self.snakes):
            with self.canvas:
                Color(1, 0, 0, 0.5, mode="rgba")
                Line(points=(self.allButtons[self.snakes[i][0]].pos[0]+self.halfButtonSize,
                             self.allButtons[self.snakes[i][0]].pos[1]+self.halfButtonSize,
                             self.allButtons[self.snakes[i][1]].pos[0]+self.halfButtonSize,
                             self.allButtons[self.snakes[i][1]].pos[1]+self.halfButtonSize), width=4)

    def draw_ladder(self):
        for i, idx in enumerate(self.ladders):
            with self.canvas:
                Color(1, 1, 0, 0.5, mode="rgba")
                Line(points=(self.allButtons[self.ladders[i][0]].pos[0] + self.halfButtonSize,
                             self.allButtons[self.ladders[i][0]].pos[1] + self.halfButtonSize,
                             self.allButtons[self.ladders[i][1]].pos[0] + self.halfButtonSize,
                             self.allButtons[self.ladders[i][1]].pos[1] + self.halfButtonSize), width=4)

    def check_is_field_snake(self):
        for i, idx in enumerate(self.snakes):
            if self.playerPosition == self.snakes[i][0]:
                self.playerPosition = self.snakes[i][1]

    def check_is_field_ladder(self):
        for i, idx in enumerate(self.ladders):
            if self.playerPosition == self.ladders[i][0]:
                self.playerPosition = self.ladders[i][1]

    #add players to the game
    #widgets to allow user to input up to 6 players
    #inputtext section allows for 12 characters or less
    #once all added, players can select "add players"
    #if self.playerName != "":
    #self.allPlayers.append(self.playerName)
    #players have option to select "Start Game"


    #self.playerName = input(name, 12 characters or less)
    #if len(self.playerName) <= 12:
    #add playerName to allPlayers list
    #else:
    #print(must be 12 characters or less)
    #player must try again
    def add_players(self):
         for yAxisAddPlayers in range(2):
             for xAxisAddPlayers in range(3):
                 addSections = TextInput(text="Insert player: ", multiline=False,

                                         )
class CanvassLine(Widget):
    pass


class MainWidget(Widget):
    pass


class SnakesAndLaddersApp(App):
    pass


SnakesAndLaddersApp().run()
Config.set('graphics', 'width', '100')
