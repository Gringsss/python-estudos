# Cada bloco abaixo é independente: pode copiar e colar so o que precisar.

# =============================
# 1. Loop FOR de contagem regressiva
# =============================

import time 

for t in range(10, 0, -1):
    print(f'Os fogos de artifício vão lançar em {t}')
    time.sleep(1)
print('KABOOOM')

# =============================
# 2. Loop FOR para maioridade
# =============================

from datetime import datetime
atual = datetime.now().year

print('Contador de maioridade (21+ anos)')

cont = 0
for c in range(0, 7):
    i = int(input('Digite o ano de nascimento: '))
    if atual-i >= 21:
        cont += 1

print(f'Quantidade de pessoas que atingiram a maioridade (21+): {cont}')

# =============================
# 3. Loop WHILE para acertar o número sorteado
# =============================

import random

sorteado = random.randint(1, 10)
cont = num = 0

while num != sorteado:
    num = int(input('Digite um número (1-10): '))
    cont += 1
print(f'Acertou! Você levou {cont} tentativas')

# =============================
# 4. Loop WHILE para simular um menu de opções
# =============================

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))

o=0
while o != 5:
    print('\n===Menu de operações===\n')
    print('[1] -> Somar')
    print('[2] -> Multiplicar')
    print('[3] -> Comaparar')
    print('[4] -> Números novos')
    print('[5] -> Sair do programa')

    o = int(input('\nOpção: '))

    if o == 1:
        print(f'A soma é {n1+n2}')
    if o == 2:
        print(f'A multiplicação é {n1*n2}')
    if o == 3:
        if n1 > n2:
            print(f'O número {n1} é maior!')
        elif n1 < n2:
            print(f'O número {n2} é maior!')
        else:
            print(f'O número números são iguais!')
    if o == 4:
        n1 = int(input('Número 1: '))
        n2 = int(input('Número 2: '))
print('===Programa encerrado===')

# =============================
# 5. Loop WHILE com True e break
# =============================

import random

n = s = cont = 0

while True:
    pc = random.randint(1, 100)
    n = int(input('Escolha um número: '))
    e = str(input('Par ou Ímpar?[P/I] ')).upper().strip()
    s = n + pc
    if e == 'P':
        if s % 2 == 0:
            cont += 1
            print(f'Você jogou {n} e o PC {pc}. O total deu {s}, deu Par!')
            print('Você ganhou!')
        else:
            print(f'Você jogou {n} e o PC {pc}. O total deu {s}, deu Ímpar!')
            print('Você perdeu!')
            break
    if e == 'I':
        if s % 2 == 1:
            cont += 1
            print(f'Você jogou {n} e o PC {pc}. O total deu {s}, deu Ímpar!')
            print('Você ganhou!')
        else:
            print(f'Você jogou {n} e o PC {pc}. O total deu {s}, deu Par!')
            print('Você perdeu!')
            break
print(f'Game Over! Você venceu {cont} vezes.')