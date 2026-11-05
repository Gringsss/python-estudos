# Cada bloco abaixo é independente: pode copiar e colar so o que precisar.

# =============================
# 1. Utilizando inputs e format
# =============================

nome = input('Qual seu nome? ')
print('Olá {}! Prazer em te conhecer!'.format(nome))

# =============================
# 2. Utilizando bibliotecas nativas
# =============================
import random

a1 = input('1º Nome: ')
a2 = input('2º Nome: ')
a3 = input('3º Nome: ')
a4 = input('4º Nome: ')

lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(f'A sequência sorteada foi: {lista}')

# =============================
# 3. Calculando ano Bissexto (IF e ELSE)
# =============================
# Caso 1) É um número divisível por 4, mas não é divisível por 100.
# Caso 2) É um número divisível por 4, por 100 e por 400.

ano = int(input('Qual ano? '))

if ano % 4 == 0:
    if ano % 100 != 0:
        print('É bissexto!')
    else:
        if ano % 400 == 0:
            print('É bissexto!')
        elif ano % 400 != 0:
            print('Não é bissexto!')
else:
    print('Não é bissexto!')

# =============================
# 4. Calculando baseado na data do sistema
# =============================

from datetime import datetime
agora = datetime.now()
atual = agora.year()

ano = int(input('Qual seu ano de nascimento? '))

if 18 > (atual-ano):
    print(f'Faltam {18-(atual-ano)} ano(s) para você se alistar!')
elif (atual-ano) == 18:
    print('Está na hora de se alistar!')
elif 18 < (atual-ano):
    print(f'Já passou {(atual-ano)-18} ano(s) do seu alistamento!')