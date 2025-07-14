def dizerOi():
    print("olá, mundo")
dizerOi()

def saudacaoPersonalizada(nome):
    print(f"Olá, {nome}")
saudacaoPersonalizada("Nelson")
saudacaoPersonalizada("Pedro")

def saudacao(nome, saudar="Bom dia!"):
    print(f"{saudar} , {nome}")

saudacao("Maria")
saudacao("Bob", "Boa noite!")


num = int(input("Digite um número: "))
def parImpar(num):
    if num % 2 == 0:
        print(f"{num} é par")
    else:
        print(f"{num} é ímpar.")
parImpar(num)