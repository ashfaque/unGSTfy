import os
import sys

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

# https://www.youtube.com/watch?v=p3tSLatmGvU
# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
        # base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# NB: Anywhere you call an external file, wrap it around the resource_path
# Eg: add_file("path/to/img.png") becomes, add_file(resource_path("path/to/img.png"))

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class MainWidget(GridLayout):
    pass


class unGSTfyApp(App):
    def build(self):
        return MainWidget()

    def process(self):
        amount_with_gst = self.root.ids.amount_with_gst_input.text if self.root.ids.amount_with_gst_input.text else 0.0
        rate_of_gst = self.root.ids.rate_of_gst_input.text if self.root.ids.rate_of_gst_input.text else 0.0

        amount_without_gst = (100 * float(amount_with_gst)) / (100 + float(rate_of_gst))
        self.root.ids.amount_without_gst_output.text = str(amount_without_gst)

if __name__=='__main__':
    unGSTfyApp().run()

# Max recursion depth exceeded ERROR fix: https://github.com/kivy/kivy/issues/8074#issuecomment-1364595283
