nota=[0,0,0,0,0]
soma=0
cont=0
for i in range(len(nota)):
    nota[i]= float(input(f"As nota do Aluno {i+1}: "))
for u in  range(len(nota)):
    soma=nota[u]+soma
media=soma/len(nota)
print(media)
for v in range(len(nota)):
    if nota[v]>=media:
        cont+=1
print(f"encontrei {cont} media {media}")




