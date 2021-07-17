from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from functools import partial

class DB():
	db_clientes = [{'São Paulo': {'cliente1': {'nome': 'Agatha', 'idade': 18}, 'cliente2': {'nome': 'Mikaele', 'idade': 19}}, 'Rio de Janeiro': {'cliente1': {'nome': 'Fábio', 'idade': 20}, 'cliente2': {'nome': 'Junio', 'idade': 22}}}]
	
class TelaManager(ScreenManager):
	pass
	
class Screen1(Screen):
	def load(self, cidade):
		self.ids.box1.clear_widgets()
		screen2 = self.manager.ids.screen2
		db = DB().db_clientes
		if cidade == 'São Paulo':
			for i, i2 in db[0]['São Paulo'].items():
				self.ids.box1.add_widget(MyButton(screen2, i2['nome'], i2['idade']))
		elif cidade == 'Rio de Janeiro':
			for i, i2 in db[0]['Rio de Janeiro'].items():
				self.ids.box1.add_widget(MyButton(screen2, i2['nome'], i2['idade']))
	
class Screen2(Screen):
	def load(self, idade, *args):
		self.ids.box1.add_widget(Button(text=str(idade)))
		self.manager.current = 'screen2'
	
class MyButton(Button):
	def __init__(self, screen2, nome, idade, **kwargs):
		super(MyButton, self).__init__(**kwargs)
		
		self.text = nome
		self.idade = idade
		self.screen2 = screen2
		self.size_hint_y = None
		self.height = '300dp'
		
		self.bind(on_press = partial(self.screen2.load, self.idade))
	
class Test(App):
	def build(self):
		return TelaManager()
		
Test().run()