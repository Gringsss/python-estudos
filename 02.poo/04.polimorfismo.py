# Cada bloco abaixo é independente: pode copiar e colar so o que precisar.

# =============================
# 1. Classe abstrata e polimorfismo
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

class Quadrado(Poligono):
    def __init__(self, lado=0):
        super().__init__(lado=4, raio=0)
        self.lado = lado

    def area(self):
        valor = self.lado ** 2
        print(f'Área = {valor:.2f}cm²')
        return valor

    def perimetro(self):
        valor = 4 * self.lado
        print(f'Perímetro = {valor:.2f}cm')
        return valor

class Circulo(Poligono):
    def __init__(self, raio=0):
        super().__init__(lado=0, raio=raio)

    def area(self):
        valor = pi * self.raio ** 2
        print(f'Área = {valor:.2f}cm²')
        return valor

    def perimetro(self):
        valor = 2 * pi * self.raio
        print(f'Perímetro = {valor:.2f}cm')
        return valor

q = Quadrado(4)
q.area()          # Área = 16.00cm²
q.perimetro()     # Perímetro = 16.00cm

c = Circulo(5)
c.area()          # Área = 78.54cm²
c.perimetro()     # Perímetro = 31.42cm

formas = [Quadrado(3), Circulo(2)]
for forma in formas:
    forma.area()  # mesmo comando, cada classe calcula do seu jeito

# =============================
# 2. Duck typing
# =============================

class Porta:
    def abrir(self):
        print("Girar a maçaneta")

class Empresa:
    def abrir(self):
        print("Registre um CNPJ")

class Ovo:
    def abrir(self):
        print("Quebre a casca")

class Pedra:
    pass

def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except AttributeError:
        print(f"Não consegui abrir {objeto.__class__.__name__}")

for objeto in [Porta(), Empresa(), Ovo(), Pedra()]:
    tentar_abrir(objeto)

# =============================
# 3. Herança com propriedade validada
# =============================

from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self, nome: str, ext:str, tam: int):
        self.nome = nome
        self._extensao = None
        self.tamanho = tam
        self.extensao = ext

    @abstractmethod
    def abrir(self):
        print(f"Abrindo o arquivo '{self.nome_completo}'")

    @property
    def nome_completo(self):
        return f"{self.nome}.{self.extensao} ({self.tamanho / 1_000_000:.2f}MB)"
    
    @property
    def extensao(self):
        return self._extensao
    
    @extensao.setter
    def extensao(self, ext:str):
        formatos = ['pdf', 'doc']
        ext = ext.lower().strip()
        if ext in formatos:
            self._extensao = ext
        else:
            raise ValueError("O formato do arquivo não é suportado")

class PDF(Arquivo):
    def __init__(self, nome, tam):
        super().__init__(nome, 'pdf', tam)
    def abrir(self):
        print(f"Abrindo o arquivo '{self.nome_completo}' no Adobe Reader")

class DOC(Arquivo):
    def __init__(self, nome, tam):
        super().__init__(nome, 'doc', tam)
    def abrir(self):
        print(f"Abrindo o arquivo '{self.nome_completo}' no Microsoft Word")

def abrir_arquivo(arquivo):
    arquivo.abrir()

p = PDF('relatorio', 2_500_000)
d = DOC('contrato', 800_000)

abrir_arquivo(p)   # Abrindo o arquivo 'relatorio.pdf (2.50MB)' no Adobe Reader
abrir_arquivo(d)   # Abrindo o arquivo 'contrato.doc (0.80MB)' no Microsoft Word

p.extensao = ' PDF '
print(p.extensao)  # pdf (o setter tira espaços e passa para minúsculo)

try:
    p.extensao = 'txt'
except ValueError as erro:
    print(f'Erro: {erro}')   # Erro: O formato do arquivo não é suportado

# =============================
# 4. Polimorfismo na exportação de dados
# =============================

import json
import xml.etree.ElementTree as ET

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class XML:
    def exportar(self, dados):
        print("Exportando dados para XML")
        nome = dados[0].__class__.__name__.lower()
        pai = ET.Element("dados")
        for item in dados:
            filho = ET.SubElement(pai, nome)
            for chave, valor in item.__dict__.items():
                neto = ET.SubElement(filho, chave)
                neto.text = str(valor)
        ET.indent(pai, space="\t")
        txt = ET.tostring(pai, encoding="unicode", xml_declaration=True)
        return txt            # retorna apenas no terminal

class JSON:
    def exportar(self, dados):
        print("Exportando dados para JSON")
        lista = []
        for item in dados:
            lista.append(item.__dict__)
        with open("dados.json", "w", encoding="utf-8") as f:
            json.dump(lista, f, ensure_ascii=False, indent=4)
        return "Arquivo dados.json criado"

def exportar_dados(formato, dados):
    print(formato.exportar(dados))

usuarios = [
    Usuario('Ana', 'ana@email.com'),
    Usuario('Bruno', 'bruno@email.com'),
]

exportar_dados(XML(), usuarios)
exportar_dados(JSON(), usuarios)