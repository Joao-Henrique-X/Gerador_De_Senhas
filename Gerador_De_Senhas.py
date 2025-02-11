from random import choice
import string

def gerar_senha(tamanho):
    
    if tamanho <= 4:
        return "As senhas precisam ter mais de 4 caracteres"
    else:
        remover = str.maketrans("","",string.whitespace)
        texto_completo = str.translate(string.printable, remover)
        senha = ""
        senha += choice(string.punctuation)
        senha += choice(string.ascii_letters)
        senha += choice(string.digits)
        for i in range(tamanho - 3):
            caractere = choice(texto_completo)
            senha += caractere
        return senha
           
tamanho = int(input("Digite o tamanho da Senha: "))
print(gerar_senha(tamanho))