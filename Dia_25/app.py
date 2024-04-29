from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Tarefas(BoxLayout):
    #keyword argument
    def __init__(self, tarefas=[], **kwargs):
        super().__init__()
        for tarefa in tarefas:
            self.add_widget(Label(text=tarefa, font_size=30))
    pass
class Teste(App):
    def build(self):
        return Tarefas(['Fazer Compras', 'Buscar Filho'],orientation='horizontal')
    
Teste().run()