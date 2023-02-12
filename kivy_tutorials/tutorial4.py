''' TextInput in Kivy '''

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Tutorial4App(App):
    def build(self):
        layout = BoxLayout(
                        orientation='vertical'
                        , padding='200sp'
                        , spacing='20sp'
        )

        self.email = TextInput(text='Enter your Email: ')
        self.password = TextInput(text='Enter your Password: ')
        self.submit=Button(text='Login', on_press=self.submit_btn)

        layout.add_widget(self.email)
        layout.add_widget(self.password)
        layout.add_widget(self.submit)

        return layout

    def submit_btn(self, obj):
        print(f"Your Email is: {self.email.text}")
        print(f"Your Password is: {self.password.text}")

if __name__ == '__main__':
    Tutorial4App().run()
