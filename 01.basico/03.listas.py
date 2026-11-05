# Cada bloco abaixo é independente: pode copiar e colar so o que precisar.

# =============================
# 1. Tabela de preços com lista
# =============================

lista = ('Pão', 5.00, 'Caderno', 15.90, 'Notebook', 3599.99)

print('-'*40)
print('Listagem de preços'.center(40))
print('-'*40)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:7.2f}')
print('-'*40)

# =============================
# 2. Adicionar números/itens em uma lista
# =============================

i = n = cont = 0
lista = []

while i is not 'N':
    n = int(input('Digite um número: '))
    lista.append(n)
    cont += 1
    
    i = str(input('Quer digitar mais? [S/N] ')).upper().strip()

lista.sort(reverse=True)

print(f'Você digitou {cont} valores.')
print(f'Os valores de forma decrescente são {lista}')

# =============================
# 3. Matriz usando lista
# =============================

matriz = list()

for linha in range(3):
    matriz.append([])
    for coluna in range(0, 3):
        n = int(input(f'Digite o nro em {linha}, {coluna}: '))
        matriz[linha].append(n)

for linha in range(0,3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]}]', end=' ')
    print()

# =============================
# 4. Lista dentro de outra lista registrando alunos e notas
# =============================

o = ''

lista = []

while 'N' not in o:
    pessoa = []
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    pessoa.append(nome)
    pessoa.append(n1)
    pessoa.append(n2)
    pessoa.append(media)
    lista.append(pessoa)

    o = str(input('Quer continuar? [S/N]: ')).upper().strip()
print('=-'*25)
for i in range(len(lista)):
    print(f'Nº {i} Nome: {lista[i][0]} Média: {lista[i][3]}')
print('=-'*25)

while True:
    idx = int(input('Mostrar as notas de qual aluno [Nº]? (99 para) '))

    if idx == 99:
        break

    print(f'As notas do {lista[idx][0]} são {lista[idx][1]} e {lista[idx][2]}')