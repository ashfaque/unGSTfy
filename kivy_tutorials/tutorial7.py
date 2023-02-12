''' Pagination in Kivy, Forward and Back button '''

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager

class HomeScreen(Screen):
    ...

class FirstScreen(Screen):
    ...

class Manager(ScreenManager):
    ...

class Tutorial7App(App):
    def build(self):
        return

if __name__ == '__main__':
    Tutorial7App().run()
