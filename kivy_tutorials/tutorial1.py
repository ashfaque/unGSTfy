''' Basics of Kivy '''
# ? https://www.youtube.com/watch?v=Fe3lEsd-UJw

from kivy.app import App    # Main app, which will be inherited.
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)    # White background
Window.size = (330, 520)    # width, height, default size when window opens, but if changed by user manually, your applicaiton will be responsive.

class TutorialApp(App):    # Before `App` whatever you write in class name will be the title of your application in title bar.
    def build(self):    # Overriding `build` method of class App
        label = Label(
                    text='Hello Kivy'
                    , font_size="70sp"    # sp = screen pixels
                    , bold=True
                    , italic=True
                    , color=(1,0,0,1)    # (r,g,b,a), between 0-1, can have decimal values.
                )
        # return label

        btn = Button(
                text='Click Me'
                , size_hint=(0.3, 0.4)   # (x : width, y : height)
                , pos_hint={'center_x':0.5, 'center_y':0.5}    # Position hint, x:horizontal, y:vertical
                , font_size='40sp'
                , on_press=self.btn_clicked    # Can call a method
                , on_release=self.btn_released    # Can call a method
            )
        # return btn

        # img = Image(source="path_to_local_dir_img_file")
        img = AsyncImage(
                    source='https://cdn.pixabay.com/photo/2015/07/28/22/01/office-865091_960_720.jpg'    # Directly use image from internet
                    , size_hint=(None, None)    # By default kivy makes responsive apps, but if you want to give custom size, turn off the responsiveness.
                    , width=100
                    , height=50
                    , pos_hint={'center_x':0.5, 'center_y':0.5}    # Center your image to the screen if using 0.5, 0.5
                )
        return img

        # ? Now if you want to show more than one button or anything else, how will you show it??
        # ? We can't do return `img1, img2`, here comes `Layouts` into play. Like, BoxLayout, FloatLayout, GridLayout, etc.
        # ? Goto file, tutorial2.py for Layouts tutorial.

    def btn_clicked(self, btn):
        print('Button Clicked')

    def btn_released(self, btn):
        print('Button Released')

if __name__ == '__main__':
    TutorialApp().run()
