from Pessoa import Pessoa, PessoaC, Morada

print("--"*10)
print("--"*10)

#dataclass

m = Morada("rua 1", '40', "234")
p = Pessoa("Gonçalo", 37, "teste@sapo.pt", m)
p2 = Pessoa(
    nome="Gonçalo",
    idade=37,
    email="teste@sapo.pt",
    morada=Morada("rua 1", '40', "234"))

print(p2)
'''
Pessoa(
    nome='Gonçalo', 
    idade=37, 
    email='teste@sapo.pt', 
    morada=Morada(
        rua='rua 1', 
        porta='40', 
        apt='234'
    )
)
'''
pc = PessoaC("Gonçalo", 37, "teste@sapo.pt")
print(pc)




print("--"*10)
print("--"*10)
def teste(p:Pessoa, pc:PessoaC):
    p.nome = "João"
    pc.nome = "João"


print(f"p.nome = {p.nome}")
print(f"pc.nome = {pc.nome}")
print("--"*10)

teste(p, pc)

print(f"p.nome = {p.nome}")
print(f"pc.nome = {pc.nome}")