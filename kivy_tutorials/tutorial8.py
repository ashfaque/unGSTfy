''' Builder method in Kivy, Same file KV Language '''

from kivy.app import App
from kivy.lang import Builder

mydoc = """
Label:
    text: "Welcome to Tutorial 8"
"""

class Tutorial8App(App):
    def build(self):
        # bldr = Builder.load_string(mydoc)
        # return bldr

        bldr = Builder.load_file('Welcome.kv')
        return bldr

if __name__ == '__main__':
    Tutorial8App().run()
