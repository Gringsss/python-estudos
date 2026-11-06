# Cada bloco abaixo é independente: pode copiar e colar so o que precisar.

# =============================
# 1. Nota com validação
# =============================

class Avaliacao:
    def __init__(self, nome, disciplina, nota=0):
        self.nome = nome
        self.disc = disciplina
        self._nota = 0
        self.nota = nota

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print('Nota inválida')

a1 = Avaliacao('Ana', 'Matemática', 8)
print(a1.nota)          # 8
a1.nota = 15            # imprime "Nota inválida"
print(a1.nota)          # continua 9.5
a2 = Avaliacao('Bruno', 'História', 12)   # imprime "Nota inválida"
print(a2.nota)          # 0, porque o valor inválido foi recusado na criação

# =============================
# 2. Termostato com limites
# =============================

class Termostato:
    MINIMA = 16
    MAXIMA = 30

    def __init__(self, temperatura=24):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor % 0.5 != 0:
            raise ValueError('A temperatura deve variar de 0.5 em 0.5')
        if not self.MINIMA <= valor <= self.MAXIMA:
            raise ValueError(f'A temperatura deve ficar entre {self.MINIMA} e {self.MAXIMA}')
        self.__temperatura = valor

    @property
    def temperatura_formatada(self):
        return f'{self.__temperatura}°C'

t = Termostato()
print(t.temperatura_formatada)
t.temperatura = 22.5
print(t.temperatura_formatada)
t.temperatura = 40 

# =============================
# 3. Dados protegidos com senha
# =============================

class Diario:
    def __init__(self, senha):
        self.__senha = senha
        self.__segredos = []

    def escrever(self, msg):
        if isinstance(msg, str) and msg.strip():
            self.__segredos.append(msg.strip())

    def ler(self, senha=None):
        if senha != self.__senha:
            raise PermissionError('Senha inválida')
        if not self.__segredos:
            return 'O diário está vazio'
        return '\n'.join(f'{i}. {s}' for i, s in enumerate(self.__segredos, start=1))

d1 = Diario('1234')

print(d1.ler('1234'))   # O diário está vazio

d1.escrever('Hoje foi um bom dia')
d1.escrever('Preciso estudar Python')
d1.escrever('   ')      # ignorado, só tem espaços
d1.escrever(123)        # ignorado, não é texto

print(d1.ler('1234'))
# 1. Hoje foi um bom dia
# 2. Preciso estudar Python

try:
    d1.ler('0000')
except PermissionError as erro:
    print(f'Erro: {erro}')   # Erro: Senha inválida

try:
    print(d1.__segredos)
except AttributeError:
    print('Não dá para acessar direto de fora')

# =============================
# 4. Carteira com saldo protegido
# =============================

class Carteira:
    def __init__(self, valor: int|float = 0):
        self.__saldo = valor

    def __str__(self):
        return f"Você tem R${self.__saldo:,.2f} de saldo"
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        raise PermissionError("Você não tem autorização para alterar")
    
    def __eq__(self, outro):
        if not isinstance(outro, Carteira):
            return NotImplemented
        return self.__saldo == outro.__saldo

    def __iadd__(self, valor: int|float):
        self.__saldo = self.__saldo + valor
        return self

c1 = Carteira(100)
c2 = Carteira(100)
c3 = Carteira()

print(c1)                  # Você tem R$100.00 de saldo
print(c3)                  # Você tem R$0.00 de saldo
print(c1.saldo)            # 100

try:
    c1.saldo = 500
except PermissionError as erro:
    print(f'Erro: {erro}')  # Erro: Você não tem autorização para alterar

try:
    c1.saldo += 10
except PermissionError as erro:
    print(f'Erro: {erro}')  # mesmo erro

print(c1 == c2)            # True

c1 += 50
print(c1)                  # Você tem R$150.00 de saldo
print(c1 == c2)            # False

c2 += 50
print(c1 == c2)            # True

c3 += 25.5
print(c3)                  # Você tem R$25.50 de saldo