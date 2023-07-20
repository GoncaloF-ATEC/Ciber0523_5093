from Pessoa import Pessoa, PessoaC

#dataclass

p = Pessoa("Gonçalo", 37, "teste@sapo.pt")
print(p)

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