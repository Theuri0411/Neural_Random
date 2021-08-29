import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require("1.9.0")


class Neural_Random(App):

    def build(self):
        return BoxLayout()


neuralRandom = Neural_Random()
neuralRandom.run()
