# Escreva um programa que calcule a média de três números inteiros 10, 20 e 30, e exiba no console se a média é maior, menor ou igual a 20.

num1, num2, num3 = 10, 20, 30
media = (num1 + num2 + num3) / 3

if media > 20:
    print("Maior que 20")
elif media < 20:
    print("Menor que 20")
else:
    print("Igual a 20")