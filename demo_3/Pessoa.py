from dataclasses import dataclass, field


@dataclass
class Pessoa:
    id: int
    nome: str
    idade: int
    filhos: list['Pessoa']
    email: str = "sem email"

    def __init__(self, id:int, nome:str, idade:int, email: str =  "sem email"):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.email = email
        self.filhos = []

    def __eq__(lhs, rhs):
        return lhs.id == rhs.id

    def __le__(self, other): ##<=
        pass

    def __lt__(self, other): # <
        pass

    def __gt__(self, other): # >
        pass

    def __ge__(self, other): # >=
        pass

    def __add__(self, other): # +
        novoid = self.id + other.id
        filho = Pessoa(novoid, "sem nome", 0 )

        self.filhos.append(filho)
        other.filhos.append(filho)

        return  filho


@dataclass
class Ponto:

    x: int
    y: int
    p1: Pessoa

@dataclass
class cao:
    id: int
    nome: str

    def __eq__(lhs, rhs):
        return lhs.id != rhs.id