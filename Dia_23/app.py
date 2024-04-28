from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Teste(App):
    def build(self):
        box = BoxLayout()
        #box = BoxLayout(orientation='vertical')
        button = Button(text='botão 1',font_size=30,on_release=self.incrementar)
        button2 = Button(text='botão 1')
        label = Label(text='texto 1')
        box.add_widget(button)
        box.add_widget(button2)
        box.add_widget(label)
        """
        
        box2 = BoxLayout()
        #box = BoxLayout(orientation='vertical')
        button3 = Button(text='botão 1')
        button4 = Button(text='botão 1')
        label2 = Label(text='texto 1')
        box.add_widget(button3)
        box.add_widget(button4)
        box.add_widget(label2)

        box.add_widget(box2)
        """
        return box
    
    def incrementar(self,button):
        button.text = 'soltei'
        # self.buttton.text = str(int(self.button.text)+1)
Teste().run()