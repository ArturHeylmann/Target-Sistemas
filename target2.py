#Fibonacci
a = -1
try:
    while a < 0: #Garante que o usuario passe um valor positivo
        a = int(input("Digite um numero:"))
except ValueError: #Garante que o usuario passe valores numericos inteiros
    print("Somente valores inteiros")

sequencia = []
j1 = 0
j2 = 1
for i in range(a):
    placeholder = j2
    j2 = j1 + j2
    sequencia.append(j2)
    j1 = placeholder

if a in sequencia:
    print("O valor digitado esta na sequencia de Fibonacci.")
else:
    print("O valor nao se encontra na sequencia.")
