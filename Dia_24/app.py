from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Incrementador(BoxLayout):
    pass
class Teste(App):
    def build(self):
        return Incrementador()
    
Teste().run()