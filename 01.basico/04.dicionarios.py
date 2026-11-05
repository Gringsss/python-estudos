# Cada bloco abaixo é independente: pode copiar e colar so o que precisar.

# =============================
# 1. Nota e situção de aluno com dicionário
# =============================

aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))

if aluno['media'] >= 6:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

print(f'Nome do aluno(a): {aluno["nome"]}')
print(f'A média foi {aluno["media"]}')
print(f'O aluno(a) foi {aluno["situacao"]}')

# =============================
# 2. Jogadores jogando dado e reordenados em um ranking (usando sub-dict)
# =============================

from random import sample
from time import sleep

jogador = {}

for v in range(1, 5):
    jogador[v] = {'dado': sample(range(1, 7), 1)}
    print(f'O Jogador {v+1} tirou: {jogador[v]["dado"][0]} no dado.')
    sleep(0.5)
print('=-'*20)

ranking = sorted(jogador.items(), key=lambda item: item[1]['dado'], reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: Jogador {(v[0])+1} com {v[1]["dado"][0]}.')
    sleep(0.5)

# =============================
# 3. Registro de Jogadores e partidas
# =============================

jogador = {}
jogador['nome'] = str(input('Nome do Jogador: '))
jogador['gols'] = []

ptd = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range(ptd):
    jogador['gols'].append(int(input(f'Quantos gols na partida {i+1}? ')))
jogador['total'] = sum(jogador['gols'])

print('=-'*20)
print(jogador)
print('=-'*20)

for c, v in jogador.items():
    print(f'O campo {c} tem o valor {v}.')
print('=-'*20)

print(f'O jogador {jogador["nome"]} jogou {ptd} partidas.')

for partida, gols in enumerate(jogador['gols']):
    print(f'Na partida {partida+1}, fez {gols} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

# =============================
# 4. Guardando dados com lista dentro de dicionário
# =============================

pessoas = {'pessoa': []}
somaidade = 0

while True:
    nome = input('Nome: ').strip()

    while True:
        sexo = input('Digite o seu sexo [M/F]: ').strip().upper()
        if sexo in ('M', 'F'):
            break
        print('Erro! Digite apenas M ou F.')

    while True:
        try:
            idade = int(input('Idade: '))
            if idade >= 0:
                break
            print('Idade inválida.')
        except ValueError:
            print('Por favor, introduza um número inteiro válido.')

    pessoas['pessoa'].append([nome, sexo, idade])
    somaidade += idade

    resp = ''
    while resp not in ('S', 'N'):
        resp = input('Quer continuar? [S/N]: ').strip().upper()
        if resp not in ('S', 'N'):
            print('Opção inválida! Digite apenas S ou N.')
            
    if resp == 'N':
        break

total_pessoas = len(pessoas['pessoa'])
media = somaidade / total_pessoas

print('=-' * 20)
print(f'Foram registadas {total_pessoas} pessoas.')
print(f'A média de idade é: {media:.2f}')

mulheres = [p[0] for p in pessoas['pessoa'] if p[1] == 'F']
if mulheres:
    print(f'Mulheres registadas: {", ".join(mulheres)}')
else:
    print('Nenhuma mulher encontrada nos registos.')

print('\nLista de pessoas que estão acima da idade média:')
for p in pessoas['pessoa']:
    if p[2] > media:
        print(f'Nome = {p[0]}; Sexo = {p[1]}; Idade = {p[2]}')