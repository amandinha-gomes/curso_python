nome = 'rodrigo de souza modesto ornellas'
altura_metros = 1.70
peso = 60

imc = peso / altura_metros ** 2 #peso / (altura x altura)

#"f-strings: formatação"
linha_1 = f'{nome} tem {altura_metros:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é {imc:.2f}'

print(linha_1)
print(linha_2)
