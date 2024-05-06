#Uso do While (enquanto)

contador =1
while contador <= 10:
    print(contador)
    contador += 1


# contador =1 
while contador <=3:
    nota_1 = float(input('Digite a nota 1: '))
    nota_2 = float(input('Digite a nota 2: '))
    print(f'A média {(nota_1+nota_2/2)}')
    contador +=1


#Uso do For (para)

for contador in range( 1,11):
    print(contador)

#Uso do continue no For (salta para próxima)
for i in range(1,5):
    if i == 4:
        continue
    print(i)


# Uso do Break no For (interrompe a execução)

for i in range (1,8):
    if i == 5:
        break
    print(i)

#Desafio 1

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite um número: '))

for i in range(numero_1+1,numero_2):
    print(i)


#Desafio 2

bacteria_1 = 4
bacteria_2 = 10
dia = 0
taxa_1 = 0.03
taxa_2 = 0.015
while bacteria_1 <= bacteria_2:
    bacteria_1 *= 1 + taxa_1
    bacteria_2*= 1 + taxa_2

    dia +=11


#Desafio 3
for i in range(15):
    nota = float(input(f'insira uma nota {i}: '))
     
    while (nota < 0 ) or (nota > 5):
      nota = float(input(f'Nota inválida, insira novamente{i}: '))


print('verificação feita. Todas são válidas')


# Desafio 4

temperatura = float(input('Insira uma temperatura em celsius: '))

contadora = 0
soma = 0

while temperatura != -273:
    soma += temperatura

    contadora += 1

    temperatura = float(input('Insira uma temperatura em celsius: '))

media = soma / contadora
print(f' A média das temperaturas é {media}')  


# Desafio 5

numero = int(input('Insira um número'))

fatorial = 1


i = numero

while i > 0:
    fatorial *= i
    i -= 1
    
    
    
print(f' fatorial de {numero} é {fatorial}')

# Desafio 6

num = int(input('Digite um número inteiro'))

for i in range (1,11):
    resultado = num * i

    print( f'{num} x {i} = {resultado}')



    
    


    
    
    







    



 
    
    


