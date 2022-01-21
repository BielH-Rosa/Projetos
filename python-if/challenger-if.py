print('Bem vindo ao desafio, deseja continuar?')
usuario = input()
if usuario == 'Sim' and 's':
    print('Continuing ...')
    print('Complete')
elif usuario == 'Não' and 'n':
    print('Exiting')
else:
    print('Por favor, tente de novo respondendo com Sim ou Não')
