from dataclasses import dataclass
from math import sqrt, pow
@dataclass
class Morada:
    rua: str
    porta: str
    apt: str

@dataclass
class Pessoa:
    nome: str
    idade: int
    email: str
    morada: Morada

@dataclass
class Ponto:
    x: int
    y: int

    def distance_to(self, pt2: 'Ponto'):
        x = pt2.x - self.x
        y = pt2.y - self.y
        return sqrt(pow(x, 2) + pow(y, 2))



class PessoaC:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def ano_nasc(self):
        # TODO: ir buscar o ano ao calendario
        return 2023 - self.idade


    #TODO: fazer a funcCool(self):
    # dadasdasdasdeqwewqe dsad
    def funcCool(self):
        pass


    #FIXME: a função retorna sempre 10
    def funcComErro(self,a ,b):
        soma = a + b
        return 10
