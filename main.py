from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

#from kivymd.theming import ThemeManager
#from kivymd.textfields.MDTextField import MDTextField 
#from kivymd.label.MDLabel import MDLabel 
#from kivymd.button.MDRaisedButton import MDRaisedButton 

def isqrt(n):
  x = n
  y = (x + n // x) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

def calculate_ferma(n, verbose=False):
    a = isqrt(n) # int(ceil(n**0.5))
    b2 = a*a - n
    b = isqrt(n) # int(b2**0.5)
    count = 0
    while b*b != b2:
        if verbose:
            print('Trying: a=%s b2=%s b=%s' % (a, b2, b))
        a = a + 1
        b2 = a*a - n
        b = isqrt(b2) # int(b2**0.5)
        count += 1
    p=a+b
    q=a-b
    #assert n == p * q
    return {'number_1': str(p),
	        'number_2': str(q)}


class Container(GridLayout):
	def calculate(self):
		try:
			initial_number = int(self.text_input.text)
		except:
			initial_number = 0
		
		numbers = calculate_ferma(initial_number)
		self.number_1.text = numbers.get('number_1')
		self.number_2.text = numbers.get('number_2')


class MyApp(App):
	#theme_cls = ThemeManager()
	#title = "RTS Lab 3.1 Vorotyntsev"

	def build(self):
		#self.theme_cls.theme_style = 'Light'
		return Container()

if __name__=='__main__':
	MyApp().run()
