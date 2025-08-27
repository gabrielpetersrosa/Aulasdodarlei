print("odeio minha vida")
convidados_da_festa = ['Maria', 'João', 'Ana', 'Carlos']
status_presença = {}
print('--- Verificação da lista de convidados ---')
lista_de_chegadas = ['Maria', 'João', 'Ana', 'Carlos']
for pessoas in lista_de_chegadas:
    if pessoas in lista_de_chegadas:
        print(f'OLÁ, {pessoas}! Bem vindo à festa.')
        status_presença[pessoas] = "confirmado"

    else:
        print(f'Desculpe,{pessoas} seu nome não está na suruba')