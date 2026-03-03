import os

def limpar_tela():
    os.system ('cls')

def plural_palavra(contador):
    if contador == 1:
        return "palavra"
    else:
        return "palavras"

def verificar_frase(frase):
    #Usando o "isistance" eu estou falando o seguinte para a máquina
    #"Ei máquina, verifque se a variavel 'frase' é do tipo string, se não
    # for do tipo string, o resultado será um TypeError, ou seja um erro de tipo"
    if not isinstance(frase, str):
        raise TypeError('A frase deve conter letras válidas pelo sistema.')
    
def voltar_menu():
    input ('Pressione qualquer tecla para voltar ao menu principal...')
    main()
    



def total_de_palavras():
    print('Olá você está em um programa de aprendizagem de python')
    frase = input('Digite uma frase : ')
    verificar_frase(frase)
    contador_de_frase = len(frase.split())

    print(f'a frase: "{frase}" tem o total de {contador_de_frase} {plural_palavra(contador_de_frase)}.')


def main():
    limpar_tela()
    total_de_palavras()
    ##voltar_menu()


if __name__ == "__main__":
    main()