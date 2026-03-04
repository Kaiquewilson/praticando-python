import os

def limpar_tela():
    os.system ('cls')

def plural_palavra(contador):
    if contador == 1:
        return "palavra"
    else:
        return "palavras"

def verificar_frase(texto):
    #Nessa etapa, o código precisa ter um padrão, visto que isso facilita a verificação das palvras.
    #Já que no código "Padrão" é diferente de "padrão", o código não reconheceria as palavras como iguais, por isso, é necessário colocar tudo em minúsculo.

    #essa implementação também nos ajuda a criar um contador de repetição de pavras.
    texto = texto.lower()
    caracteres = ".,:;/?-!@#$%¨&*()_+=|<>"
    for char in caracteres:
        texto = texto.replace(char, "")
        #o que eu acabei de fazer aqui?
        #Primeiro eu criei uma especie de "lista" de caracteres, que são os caracteres
        #  que eu quero remover da minha frase, depois, eu utilizei um loop "for" para percorrer cada caractere dessa lista e utilizei o método 
        # "replace" para substituir cada caractere por uma string vazia, ou seja, removendo esses caracteres da minha frase.
    return texto

    
def voltar_menu():
    input ('Pressione qualquer tecla para voltar ao menu principal...')
    main()
    



def total_de_palavras():
    print('Olá você está em um programa de aprendizagem de python')
 #-------------------------------------------------------------------------------------------------------------
    frase = input("""OBS: o programa não inclui caracteres especiais, apenas letras e números.
                  
Dgite uma frase para contar o número de palavras: """)
 #-------------------------------------------------------------------------------------------------------------
    frase = verificar_frase(frase)
    contador_de_frase = len(frase.split())

    print(f'a frase: "{frase}" tem o total de {contador_de_frase} {plural_palavra(contador_de_frase)}.')


def main():
    limpar_tela()
    total_de_palavras()
    ##voltar_menu()


if __name__ == "__main__":
    main()