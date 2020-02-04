# Exemplo 4 - Convertendo tipos
num1 = int(input("Digite um número:"))  # Recebe o valor e converte para int
num2 = int(input("Digite um número:"))  # Recebe o valor e converte para int
soma = num1 + num2
print("A soma dos dois números é ", soma)
print("{} + {} = {}" .format(num1, num2, soma))
'''OBS: Podemos utilizar .format para faciltar o nosso print, podendo marcar
a posição onde aparecerá a variavel com abre e fecha chaves {} subistituindo 
isto:  print(num1,"+", num2, "=", soma)
Por isto: print("{} + {} = {}" .format(num1, num2, soma)) '''
