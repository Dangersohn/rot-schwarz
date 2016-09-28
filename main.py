from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file('rotschwarz.kv') #liest das Layout ein

class Rotschwarz(BoxLayout):
	pass
	#def build(selfe):
	#	self.orientation='vertical'
	#	self.spacing=0
	#	self.padding=5


class RotschwarzApp(App):
    def build(self):
        return Rotschwarz()


if __name__ == '__main__':
    RotschwarzApp().run()