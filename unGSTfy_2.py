import os
import sys

from kivy.app import App
# from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.screenmanager import (ScreenManager, Screen, NoTransition, SlideTransition, CardTransition, SwapTransition, FadeTransition, WipeTransition, FallOutTransition, RiseInTransition)
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.lang import Builder

mykv = """
Manager:
    FirstScreen:
        id: fscreen
    SecondScreen:
        id: sscreen

<FirstScreen>:
    name: 'firstscreen'
    GridLayout:
        cols: 2
        Label:
            id: amount_with_gst
            text: "Total Amount with GST"
            font_size: 30
            text_size: self.width, None
            halign: 'center'
        TextInput:
            id: amount_with_gst_input
            # text: ""
            font_size: 30
            text_size: self.width, None
            halign: 'left'
            input_filter: 'float'
            hint_text:'Total Amount with GST'
            write_tab: False
            multiline: False
            on_text: app.first_screen_process()

        Label:
            id: rate_of_gst
            text: "GST %"
            font_size: 30
            text_size: self.width, None
            halign: 'center'
        TextInput:
            id: rate_of_gst_input
            # text: ""
            font_size: 30
            text_size: self.width, None
            halign: 'left'
            input_filter: 'float'
            hint_text:'GST %'
            write_tab: False
            multiline: False
            on_text: app.first_screen_process()

        Label:
            id: amount_without_gst
            text: "Taxable Value"
            font_size: 30
            text_size: self.width, None
            halign: 'center'
        TextInput:
            id: amount_without_gst_output
            # text: ""
            font_size: 30
            text_size: self.width, None
            halign: 'left'
            input_filter: 'float'
            hint_text: 'Taxable Value'
            write_tab: False
            multiline: False
            background_color: (0,1,0,1)
            readonly: True

        Label:
            id: author_name
            text: "Created By: Ashfaque Alam"
            font_size: 20
            text_size: self.width, None
            halign: 'center'
        Button:
            text: '->'
            font_size: 50
            background_color: (1,0,0,1)
            on_release:
                app.root.current = "secondscreen"    # name: of SecondScreen
                root.manager.transition.direction = "left"


<SecondScreen>:
    name: 'secondscreen'
    GridLayout:
        cols: 2
        Label:
            id: amount_with_gst
            text: "Total Amount with GST"
            font_size: 30
            text_size: self.width, None
            halign: 'center'
        TextInput:
            id: amount_with_gst_input
            # text: ""
            font_size: 30
            text_size: self.width, None
            halign: 'left'
            input_filter: 'float'
            hint_text:'Total Amount with GST'
            write_tab: False
            multiline: False
            on_text: app.second_screen_process()

        Label:
            id: amount_without_gst
            text: "Taxable Value"
            font_size: 30
            text_size: self.width, None
            halign: 'center'
        TextInput:
            id: amount_without_gst_input
            # text: ""
            font_size: 30
            text_size: self.width, None
            halign: 'left'
            input_filter: 'float'
            hint_text: 'Taxable Value'
            write_tab: False
            multiline: False
            on_text: app.second_screen_process()

        Label:
            id: rate_of_gst
            text: "GST %"
            font_size: 30
            text_size: self.width, None
            halign: 'center'
        TextInput:
            id: rate_of_gst_output
            # text: ""
            font_size: 30
            text_size: self.width, None
            halign: 'left'
            input_filter: 'float'
            hint_text:'GST %'
            write_tab: False
            multiline: False
            background_color: (0,1,0,1)
            readonly: True

        Button:
            text: '<-'
            font_size: 50
            background_color: (1,0,0,1)
            on_release:
                app.root.current = "firstscreen"    # name: of FirstScreen
                root.manager.transition.direction = "right"
        Label:
            id: author_name_two
            text: "Created By: Ashfaque Alam"
            font_size: 20
            text_size: self.width, None
            halign: 'center'
"""

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

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class Manager(ScreenManager):
    pass



# class MainWidget(GridLayout):
#     pass


class unGSTfyApp(App):
    def build(self):
        screen_manager = Manager(transition = FadeTransition())

        screen_manager.add_widget(FirstScreen())
        screen_manager.add_widget(SecondScreen())

        # return screen_manager

        bldr = Builder.load_string(mykv)
        return bldr

    def first_screen_process(self):
        import re
        pattern = re.compile(r'[0-9.]+')

        amount_with_gst_input_str = self.root.get_screen('firstscreen').ids.amount_with_gst_input.text
        rate_of_gst_input_str = self.root.get_screen('firstscreen').ids.rate_of_gst_input.text

        amount_with_gst = amount_with_gst_input_str if amount_with_gst_input_str and re.fullmatch(pattern, amount_with_gst_input_str) else '0.0'
        rate_of_gst = rate_of_gst_input_str if rate_of_gst_input_str and re.fullmatch(pattern, rate_of_gst_input_str) else '0.0'

        amount_with_gst = amount_with_gst if amount_with_gst[0] != '.' else '0'+amount_with_gst
        rate_of_gst = rate_of_gst if rate_of_gst[0] != '.' else '0'+rate_of_gst

        amount_without_gst = (100 * float(amount_with_gst)) / (100 + float(rate_of_gst))

        self.root.get_screen('firstscreen').ids.amount_without_gst_output.text = str(round(amount_without_gst, 10))

    def second_screen_process(self):
        import re
        pattern = re.compile(r'[0-9.]+')

        amount_with_gst_input_str = self.root.get_screen('secondscreen').ids.amount_with_gst_input.text
        amount_without_gst_input_str = self.root.get_screen('secondscreen').ids.amount_without_gst_input.text

        amount_with_gst = amount_with_gst_input_str if amount_with_gst_input_str and re.fullmatch(pattern, amount_with_gst_input_str) else '0.0'
        amount_without_gst = amount_without_gst_input_str if amount_without_gst_input_str and re.fullmatch(pattern, amount_without_gst_input_str) else '0.0'

        amount_with_gst = amount_with_gst if amount_with_gst[0] != '.' else '0'+amount_with_gst
        amount_without_gst = amount_without_gst if amount_without_gst[0] != '.' else '0'+amount_without_gst

        rate_of_gst = ((float(amount_with_gst) / float(amount_without_gst)) - 1) * 100 if float(amount_with_gst) != 0.0 and float(amount_without_gst) != 0.0 else 0.0

        self.root.get_screen('secondscreen').ids.rate_of_gst_output.text = str(round(rate_of_gst, 10))

if __name__=='__main__':
    unGSTfyApp().run()

# Max recursion depth exceeded ERROR fix: https://github.com/kivy/kivy/issues/8074#issuecomment-1364595283
