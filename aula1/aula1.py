'''

lista ≠ lista ligada



head -> valor | prt -> valor2 | prt -> valor3 | prt -> null

8.070055628195405e-07
1.458989572711289e-06
'''
import time

# array (listas)

# arr = [1, 20, 30, 4, 5, 6, 7, 8, 3, 3, 3, 3, 3, 3, 20, 30, 4, 5,
# 6, 7, 8, 3, 3, 3, 20, 30, 4, 5, 6, 7, 8, 3, 3, 3, 20, 30, 4, 5, 6, 7,
# 8, 3, 3, 3, 20, 30, 4, 5, 6, 7, 8, 3, 3, 3, 20, 30, 4, 5, 6, 7, 8, 3,
# 3, 3, 20, 30, 4, 5, 6, 7, 8, 3, 3, 3, 20, 30, 4, 5, 6, 7, 8, 3, 3, 3,
# 20, 30, 4, 5, 6, 7, 8, 3, 3, 3, 20, 30, 4, 5, 6, 7, 8, 3, 3, 3, 20, 30,
# 4, 5, 6, 7, 8, 3, 3, 3, 20, 30, 4, 5, 6, 7, 8, 3, 3, 3, 20, 30, 4, 5, 6,
# 7, 8, 3, 3, 3, 20, 30, 4, 5, 6, 7, 8, 3, 3, 3, 20, 30, 4, 5, 6, 7, 8, 3,
# 3, 3, 20, 30, 4, 5, 6, 7, 8, 3, 3, 3, 20, 30, 4, 5, 6, 7, 8, 3, 3, 3, 20,
# 30, 4, 5, 6, 7, 8, 3, 3, 3, 20, 30, 4, 5, 6, 7, 8, 3, 3, 3, 20, 30, 4, 5,
# 6, 7, 8, 3, 3, 3, 20, 30, 4, 5, 6, 7, 8, 3, 3, 3, 20, 30, 4, 5, 6, 7, 8, 3
# , 3, 3, 20, 30, 4, 5, 6, 7, 8, 3, 3, 3, 20, 30, 4, 5, 6, 7, 8, 3, 3, 3, 20,
# 30, 4, 5, 6, 7, 8, 3, 3, 3, 20, 30, 4, 5, 6, 7, 8, 3, 3, 3, 20, 30, 4, 5, 6,
# 7, 8, 3, 3, 3, 20, 30, 4, 5, 6, 7, 8, 3, 3, 3]

arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(arr)

tic = time.perf_counter()

arr.insert(2, -1)
arr.insert(2, -1)
arr.insert(2, -1)
arr.insert(2, -1)
toc = time.perf_counter()

# print(f" {toc - tic} ")

tic = time.perf_counter()

arr.append(20)

toc = time.perf_counter()
# print(f" {toc - tic} ")


print(arr)

print(arr.count(3))

s1 = len(arr)
s2 = arr.__len__()

arr.pop(0)  # del pos
arr.remove(-1)  # del value

print("rev")
print(arr)
arr.reverse()
print(arr)

print("sort")
# arr.append("teste")
print(arr)
arr.sort()
print(arr)

print(f"{2 > 3}")

print("-----------for------------")
print(arr)

for elm in arr:
    if elm % 2 == 0:
        print(elm)

print("-----------for------------")

# range(10) 0 -> 9
# range(5, 10) 5 -> 9

for i in range(len(arr)):
    print(f"na pos: {i} está o valor: {arr[i]}")

'''

for (int i = 0; i < 10; i++){ }

arr = []
set = {}
dict = {:}
'''
# set
print("-----------set------------")

var_que_vai_guardar_o_set_de_demo = {1, 2, 3, 4, 5}

for i in var_que_vai_guardar_o_set_de_demo:
    print(i)

print(var_que_vai_guardar_o_set_de_demo)

var_que_vai_guardar_o_set_de_demo.add(200)
print(var_que_vai_guardar_o_set_de_demo)

var_que_vai_guardar_o_set_de_demo.add(200)

print(var_que_vai_guardar_o_set_de_demo)


var_que_vai_guardar_o_set_de_demo.remove(5)
print(var_que_vai_guardar_o_set_de_demo)


def safe_remove(my_set:set, val):
    if my_set.__contains__(val):
        my_set.remove(val)
        return True
    else:
        print("o valor não esta no set")
        return False


safe_remove(var_que_vai_guardar_o_set_de_demo, 200)
print(var_que_vai_guardar_o_set_de_demo)

var_que_vai_guardar_o_set_de_demo.pop()
print(var_que_vai_guardar_o_set_de_demo)

for i in var_que_vai_guardar_o_set_de_demo:
    print(i)

print(10*'--'+'set'+10*'--')

set1 = {"oleo", "sal", "Polvilho doçe", "Polvilho Azedo", "Queijo", "Leite"}

set2 = {"Farinha", "sal", "Fermento", "Agua"}


print(set1.union(set2))

print(set1.difference(set2))
print(set2.difference(set1))

print(set1.intersection(set2))

print(set1.symmetric_difference(set2))

# dict
print(10*'--'+'Dicts'+10*'--')

dict = {"chave do 1 valor":"Value 1", "key2":"Value 2", "key3":"Value 3"}

print(dict)

dict["nova key"] = "novo value"

print(dict)

print(dict["chave do 1 valor"])
print(dict.get("chave do 1 valor"))

print(dict.__contains__("key2")) # verifica se a key existe

print("--"*10)
for elm in dict:
    print(elm) # keys

print("--"*10)

for elm in dict.values():
    print(elm) # valores


print("--"*10)

for elm in dict.keys():
    print(elm) # keys

print("--"*10)
print(dict)
for key_value_pair in dict.items():
    # ('key2',  'Value 2')
    print(f"key: {key_value_pair[0]},\t valor: {key_value_pair[1]}") # tuplo (key, value)


# tuplos
print(10*'--'+'tuplos'+10*'--')

tup = ("Gonçalo", 37, True)

print(tup)

for i in tup:
    print(i)
print("--"*10)

print(tup.__contains__(37))

print("--"*10)
print(tup[0])
print(tup[1])
print(tup[2])
print("--"*10)

# funcs
print(10*'--'+'funcs'+10*'--')


def calcular_media(lista_notas: list):
    total = sum(lista_notas)
    total_notas = len(lista_notas)

    if total_notas > 0:
        return total / total_notas

    return -1

def is_aprovado(lista_notas: list):
    media = calcular_media(lista_notas)

    if media >= 9.5:
        return True, media, "Aprovado"

    else:
        return False, media, "Não Aprovado"


lista_notas = []

while True:

    nota = input("Digite uma nota (para sair use um char): ")

    if nota.isnumeric():
        lista_notas.append(float(nota))
    else:
        break


status = is_aprovado(lista_notas)

print(status)



# dataclasses


# class
