from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from random import randrange

nomes = []

class MainApp(App):
    pass

class tela(BoxLayout):

    def novo(self):
        if not self.ids.inp.text:
            pass
        else:
            nomes.append(self.ids.inp.text)
            self.ids.inp.text = ''
            self.ids.lb3.text = str(nomes)

    def click(self):
        if not nomes:
            self.ids.lb.text = "  Nenhum para sortear\n Cadastre novos nomes"

        else:
            num_aleatorio = randrange(0, len(nomes))
            self.ids.lb.text = nomes[num_aleatorio]
            self.ids.lb2.text = self.ids.lb2.text + nomes[num_aleatorio] + " "
            del (nomes[num_aleatorio])
            self.ids.lb3.text = str(nomes)

janela = MainApp()
janela.run()

