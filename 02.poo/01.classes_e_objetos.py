# Cada bloco abaixo é independente: pode copiar e colar so o que precisar.

# =============================
# 1. Classe com descrição
# =============================

class Pessoa:
    '''
    Representa uma pessoa com nome e idade.

    Atributos:
        nome (str): nome da pessoa. Padrão: '(vazio)'.
        idade (int): idade em anos. Padrão: 0.

    Métodos:
        aniversario(): soma 1 ano à idade da pessoa.
    '''

    def __init__(self, nome='(vazio)', idade=0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f'{self.nome} tem {self.idade} anos de idade.'

p1 = Pessoa(nome='João', idade=34)
p1.aniversario()
print(p1)

# =============================
# 2. Classe de conta bancária
# =============================

class ContaBancaria:

    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta bancária de número {self.id} de {self.titular} com saldo de R${self.saldo:,.2f}.')

    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito de {valor:,.2f} na conta {self.id} autorizado.')

    def saque(self, valor):
        if valor > self.saldo:
            print(f'Saque NEGADO de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE.')
        else:
            self.saldo -= valor
            print(f'Saque de {valor:,.2f} na conta {self.id} autorizado.')

    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo.'

c1 = ContaBancaria(id=150, nome='Gabriela', saldo=4500)
c1.depositar(2500)
c1.saque(20000)
print(c1)

# =============================
# 3. Classe de livro interativo
# =============================

from time import sleep

class Livro:
    def __init__(self, title, paginas):
        self.titulo = title
        self.pag = paginas
        self.pag_atual = 1

        print(f'Você abriu o livro {self.titulo} e está na página {self.pag_atual}')

    def passa_pagina(self, qtd=1):
        cont = 0
        for _ in range(qtd):
            if not self.fim_livro():
                self.pag_atual += 1
                print(f'Pág{self.pag_atual} >', end=' ', flush=True)
                sleep(0.2)
                cont += 1
        paginas = 'página' if cont == 1 else 'páginas'
        print(f'Você avançou {cont} {paginas} e agora está na página {self.pag_atual}')
        if self.fim_livro():
            print(f'Você chegou no fim do livro {self.titulo}!')

    def fim_livro(self) -> bool:
        return self.pag_atual == self.pag

l1 = Livro(title='O Jogo infinito', paginas=300)
l1.passa_pagina(25)
l1.passa_pagina(100)
l1.passa_pagina(185)

# =============================
# 4. Classe de ficha Gamer
# =============================

class Gamer:
    def __init__(self, nome, nick):
        self.name = nome
        self.nick = nick
        self.jogos = []

    def add_favoritos(self, jogo):
        self.jogos.append(jogo)
        self.jogos.sort()

    def ficha(self):
        print(f'Nome real: {self.name}')
        print(f'Nickname: {self.nick}')
        print('Jogos favoritos:')
        for jogo in self.jogos:
            print(jogo)

j1 = Gamer(nome='Mariana Alves', nick='Mari_Maneira')
j1.add_favoritos('Minecraft')
j1.add_favoritos('God of War')
j1.add_favoritos('Fortnite')
j1.add_favoritos('Angry Birds')
j1.ficha()