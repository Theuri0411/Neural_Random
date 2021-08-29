import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require("1.9.0")


class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number (self):


class Neural_Random(App):

    def build(self):
        return BoxLayout()


neuralRandom = Neural_Random()
neuralRandom.run()
