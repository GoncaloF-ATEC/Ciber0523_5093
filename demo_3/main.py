from Pessoa import Pessoa, cao
from math import pow
'''
p1 = Pessoa(2, "ana", 10)
p2 = Pessoa(4, "João", 10, "email@sapo.pt")
print("--" * 10)
print(p1)
print(p2)
print("--" * 10)

f = p1 + p2

f.nome = "joão"

print("--" * 10)
print(p1.filhos)
print(p2.filhos)
print("--" * 10)

f = p1 + p2

f.nome = "Maria"

print("--" * 10)
print(p1.filhos)
print(p2.filhos)




p3 = Pessoa(8, "ana", 10)
p4 = Pessoa(16, "João", 10, "email@sapo.pt")

f2 = p3 + p4

print("--" * 10)
print(p3.filhos)
print(p4.filhos)

f2.nome = "João"
print("--" * 10)
print("--" * 10)

f3 = f + f2

print("--" * 10)
print(p1)

'''
ListaPessoas = []

_next = True


'''

2
4
8
16
36
26


** -> elevado 
pow(2, listSize) - Elevado <-  from math import pow

'''


print("ssa".isalpha())
print("    ".isalpha())

#print(2 ** 0)
def calcId(list_size:int = 0) -> int:
    return  int(pow(2, list_size))

while _next:
    nome = input("nome: ")
    while not nome.isalpha():
        print("o nome não pode ser deixado em branco")
        nome = input("nome: ")

    idade = input("idade: ")
    while not  idade.isnumeric():
        print("a idade tem de ser um valor inteiro")
        idade = input("idade: ")


    p = Pessoa(calcId(ListaPessoas.__len__()), nome, int(idade))

    ListaPessoas.append(p)
    _next = int(input("sair?: (0 = sair) ")) ## podia esta melhor



for p in ListaPessoas:

    print(f"id:{p.id} nome: {p.nome}, numero de filhos: {len(p.filhos)}")


