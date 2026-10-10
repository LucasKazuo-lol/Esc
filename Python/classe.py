# decakaracao classe
class Minhaclasse:
    def __init__(self): #construtor
        # atributos
        self.nome = ""
        self.idade = 0
    # metods

    def aniversario(self):
        self.idade +=1

    def mensagem(self):
        return f"{self.nome} tem a idade de {self.idade}"
# declaracao objeto
g1 = Minhaclasse()
g1.nome = "lucas"
g1.idade = 18
g1.aniversario()
print(g1.mensagem())

g2 = Minhaclasse()
g2.nome = "Pedro"
g2.idade = 14
print(g2.mensagem())