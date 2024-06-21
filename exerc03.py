# Exercício 3: Verificação de Ano bissexto

ano = int(input('Digite um ano: ' ))
if ano % 4 == 0:
    print('O ano é BISSEXTO')
else:
    print('O ano NÃO é BISSEXTO')