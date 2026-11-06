# Cada bloco abaixo é independente: pode copiar e colar so o que precisar.

# =============================
# 1. Herança de classe
# =============================

class Pessoa:

    def __init__(self, nome='', idade=0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

class Aluno(Pessoa):
    def __init__(self, nome='', idade=0, curso='', turma=''):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'{self.nome} acabou de fazer matrícula!')

a1 = Aluno(nome='Bruna', idade=16, curso='Técnico em Agropecuária', turma='T04')
a1.fazer_matricula()

# =============================
# 2. Herança com classe abstrata
# =============================

from abc import ABC, abstractmethod
from math import pi

class Poligono(ABC):
    def __init__(self, lado=0, raio=0):
        self.qtd_lados = lado
        self.raio = raio

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Circulo(Poligono):
    def __init__(self, raio=0):
        super().__init__(lado=0, raio=raio)

    def area(self):
        valor = pi * self.raio ** 2
        print(f'Área = {valor:.2f}')
        return valor

    def perimetro(self):
        valor = 2 * pi * self.raio
        print(f'Perímetro = {valor:.2f}')
        return valor

p1 = Circulo(5)
p1.area()
p1.perimetro()

# =============================
# 3. Herança abstrata para cálculo de fretes
# =============================

from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, dist):
        super().__init__()
        self.distancia = dist

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    def __init__(self, dist):
        super().__init__(dist)
        self.fator = 0.5
        self.frete = dist * self.fator

    def calc_frete(self):
        return f'R${self.frete:.2f}'


class Caminhao(Transporte):
    def __init__(self, dist):
        super().__init__(dist)
        self.fator = 1.2
        self.frete = dist * self.fator

    def calc_frete(self):
        return f'R${self.frete:.2f}'

dist = float(input('Quantos KM de distância? '))
f1 = Moto(dist)
print(f'Frete de {type(f1).__name__} em {dist}KM = {f1.calc_frete()}')
f2 = Caminhao(dist)
print(f'Frete de {type(f2).__name__} em {dist}KM = {f2.calc_frete()}')