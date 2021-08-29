import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require("2.0.0")


class Neural_Random(App):

    def build(self):
        return Label(text="Neural Random")


neuralRandom = Neural_Random()
neuralRandom.run()
