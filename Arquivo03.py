nomes=["ygor","gol","mister","ronaldo","beie"]
nome= input("digite o nome que voce que encontrar: ")
for i in range(len(nomes)):
    if nome == nomes[i] :
        print(f"achei o nome {nome} na posição {i}")
    else:
        print("nome não encontrado.")


