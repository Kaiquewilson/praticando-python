#Neste exercício bem simples, consiste em criar um programa que leia alguns números dado pelo
#usuário e mostre o resultado
#--------------------------------------------------------------------------------------------------#
#Entrada de dado:
# 1- receber um número digitado pelo usuário
# 2- Receber o segundo número digitado pelo usuário
# 3- Fazer a soma e mostra o resultado 
#--------------------------------------------------------------------------------------------------#
def somar(a,b):
    return a + b

print("Olá, seja-bem vindo(a) ao programa de soma de números!\n")

try:
    numero1 =  float(input("Digite o primeiro número: "))
    numero2 =  float(input("Digite o segundo número: "))
    resultado = somar(numero1, numero2)
    print(f"a soma dos números {numero1} e {numero2} é igual a {resultado}")

except ValueError:
    print("Ops, parece que você digitou um valor inválido. Por favor, digite apenas números.")