# Cada bloco abaixo é independente: pode copiar e colar so o que precisar.

# =============================
# 1. Função para calcular área
# =============================

def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é {a}m²')

largura = float(input("Largura (metros): "))
comprimento = float(input("Comprimento (metros): "))

area(largura, comprimento)

# =============================
# 2. Função para validar a participação na votação
# =============================

from datetime import datetime

def voto(ano):
    idade = datetime.now().year - ano
    if idade < 18:
        print(f'Com {idade} anos: VOTO NEGADO.')
    elif idade >= 18 and idade <= 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    elif idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL.')

nasc = int(input('Em que ano você nasceu? '))
voto(nasc)

# =============================
# 3. Função para formatar mensagem
# =============================

def escreva(msg):
    tam = len(msg) + 4
    print('=' * tam)
    print(f'{msg:^{tam}}')
    print('=' * tam)

msg = input('Escreva uma mensagem para formatar: ')
escreva(msg)

# =============================
# 4. Função para sortear números
# =============================

from random import sample
from time import sleep

def sorteia():
    sorteados = []
    print('Sorteando 5 valores: ', end='')

    for i in range(5):
        sorteados.append(sample(1,10))
        print(sorteados[i], end=' ', flush=True)
        sleep(0.25)
    print('PRONTO!')
    return sorteados

numeros = sorteia()