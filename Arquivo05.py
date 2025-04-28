A=[0,0,0,0,0,0,0,0,0,0,0]
X=0
M=[0,0,0,0,0,0,0,0,0,0,0]
for i in range(len(A)):
    A[i]=int(input("Digite 10 núneros:"))
x=int(input("digite um numero :"))

for j in range(len(M)):
    M[j] =A[j]*X
print(A)
print(X)
print(M)