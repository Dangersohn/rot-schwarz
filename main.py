from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random


rot = 16
schwarz	 = 16

class TestApp(App):
	def build(self):
		layout = BoxLayout(orientation='vertical')
		# use a (r, g, b, a) tuple
		blue = (0, 0, 1.5, 2.5)
		red = (2.5, 0, 0, 1.5)

		self.btn =  Button(text='Karte ziehen', background_color=blue, font_size=120)
		self.btn.bind(on_press=self.callback)
		#self.label = Label(text="------------", font_size='50sp')
		layout.add_widget(self.btn)
		#layout.add_widget(self.label)
		return layout

	def callback(self, event):
		global rot
		global schwarz
		if  rot > 0 and schwarz > 0:
			self.btn.text= 'Karte ziehen'
			choice = random.randrange(1,3)
			#print(choice)
			if choice == 1:
				#self.label.text = "rot"
				self.btn.background_color = (2.5, 0, 0, 1.5)
				rot = rot - 1
			else:
				#self.label.text = "schwarz"
				self.btn.background_color = (0, 0, 0, 0)
				schwarz = schwarz - 1
		elif rot == 0 and schwarz == 0:
				self.btn.text='neue Runde'
				self.btn.background_color = (2, 2, 2, 2)
				rot = 16
				schwarz = 16
		elif rot > 0 and schwarz == 0:
			self.btn.background_color = (2.5, 0, 0, 1.5)
			rot = rot - 1
		elif schwarz > 0 and rot == 0:
			self.btn.background_color = (0, 0, 0, 0)
			schwarz = schwarz - 1

if __name__ == "__main__":
	TestApp().run()
