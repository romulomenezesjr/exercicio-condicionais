""" Lista de exercícios sobre condicionais """

def questao01():
    """
    Escreva um programa que solicita
    um número ao usuário e determina se
    é positivo, negativo ou zero.
    """
    numero = int(input("Digite um número"))
    if numero > 0:
        print('positivo')
    elif numero < 0:
        print('negativo')
    else:
        print('zero')