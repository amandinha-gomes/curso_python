# Operador lógico "not"

# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

# if senha !=  '12345':   #diferente
#     print('senha incorreta')

if not senha:
    print('vc nao digitou nada')

print(not True)  # False
print(not False)  # True