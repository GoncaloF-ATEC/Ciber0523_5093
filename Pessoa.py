from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    email: str

@dataclass
class Ponto:
    x: int
    y: int