#Realizando repetição de texto com Python
def repeticao(texto, quantidade):
    return texto * quantidade
input_texto = input("Digite o texto que deseja repetir: ")
input_quantidade = int(input("Digite a quantidade de vezes que deseja repetir o texto: "))
resultado = repeticao(input_texto, input_quantidade)
print(resultado)