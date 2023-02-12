''' KV Language, it's more like CSS but for python, follows MVT model '''

from kivy.app import App

class KVLanguageApp(App):
    def build(self):
        # There is a kvlanguage.kv file in this dir, it is using it.
        pass

if __name__ == '__main__':
    KVLanguageApp().run()
