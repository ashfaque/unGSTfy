''' GridLayout in Kivy, more like a 2D table '''

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class Tutorial3App(App):
    def build(self):
        # layout = GridLayout(rows=2)    # Only two rows will be there, and fit all elements in these two rows
        # layout = GridLayout(cols=2)    # Only two columns will be there, and fit all elements in these two columns
        layout = GridLayout(cols=2
                            , row_force_default=True    # TODO: Don't know what it does
                            , row_default_height=40
                )
        btn1 = Button(text='Button 1')
        btn2 = Button(text='Button 2')
        btn3 = Button(text='Button 3')
        btn4 = Button(text='Button 4')
        btn5 = Button(text='Button 5')

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout.add_widget(btn5)

        return layout

if __name__ == '__main__':
    Tutorial3App().run()
