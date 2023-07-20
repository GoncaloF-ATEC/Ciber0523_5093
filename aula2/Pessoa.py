from dataclasses import dataclass

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


class PessoaC:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def ano_nasc(self):

        return 2023 - self.idade
