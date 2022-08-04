'''Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).
Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará
o erro e continuará perguntando até que um valor correto seja preenchido.

Passos:
    Criar função para calcular idade
    Obter nome e idade do usuário
    Criar condicionais e tratamentos de erros para o ano informado pelo usuário
    informar nome e a idade que completou ou completará em 2022'''

#função
def calculoidade(anonasc):
    idade=2022-anonasc
    return idade


#programa
continuar=True
nome = str(input('Digite o seu nome: '))
while(continuar):
    try:
        anonasc=int(input('Digite o ano de nascimento: '))
        if (1922<anonasc<=2021):
            print(f'{nome} tem {calculoidade(anonasc)} anos')
            continuar=False
        else:
            print('Digite um ano entre 1922 e 2021')
    except:
        print('Digite um número válido!')
#fimdoprograma