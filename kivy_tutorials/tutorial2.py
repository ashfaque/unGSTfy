''' BoxLayouts in Kivy '''

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Tutorial2App(App):
    def build(self):
        layout = BoxLayout(
                        orientation='vertical'
                        # orientation='horizontal'
                        , spacing='10sp'    # Spacing between two elements in the Boxlayout
                        , padding='30sp'    # BoxLayout all 4 sides padding
        )
        btn1 = Button(text='Button 1')
        btn2 = Button(text='Button 2')

        # Adding multiple elements in the layout and finally only returning the layout
        layout.add_widget(btn1)
        layout.add_widget(btn2)

        return layout


if __name__ == '__main__':
    Tutorial2App().run()