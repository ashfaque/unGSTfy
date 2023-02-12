''' More layouts in Kivy '''

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout

class Tutorial5App(App):
    def build(self):
        ''' AnchorLayout '''
        a_layout = AnchorLayout(
                            # anchor_x='right'    # Horizontal
                            # , anchor_y='bottom'    # Vertical
                            anchor_x='left'    # Horizontal
                            , anchor_y='top'    # Vertical
        )

        btn1 = Button(
                    text='Ashfaque '
                    , size_hint=(None, None)
                    , width='100sp'
            )

        a_layout.add_widget(btn1)

        # return a_layout

        ''' FloatLayout'''
        f_layout = FloatLayout()

        btn2 = Button(
                    text='Ashfaque '
                    , size_hint=(None, None)
                    , width='100sp'
                    , pos_hint={'center_x': 0.5, 'center_y': 0.8}    # You can place any element using FloatLayout anywhere on the screen randomly, unlike Box or Grid Layouts.
            )

        f_layout.add_widget(btn2)

        # return f_layout

        ''' PageLayout'''
        p_layout = PageLayout()

        btn3 = Button(
                    text='Ashfaque '
                    , size_hint=(None, None)
                    , width='100sp'
                    , pos_hint={'center_x': 0.5, 'center_y': 0.8}    # You can place any element using FloatLayout anywhere on the screen randomly, unlike Box or Grid Layouts.
            )
        btn4 = Button(
                    text='Alam '
                    , size_hint=(None, None)
                    , width='100sp'
                    , pos_hint={'center_x': 0.5, 'center_y': 0.8}    # You can place any element using FloatLayout anywhere on the screen randomly, unlike Box or Grid Layouts.
            )

        p_layout.add_widget(btn3)
        p_layout.add_widget(btn4)

        return p_layout


if __name__ == '__main__':
    Tutorial5App().run()
