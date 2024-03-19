from tipos import TIPOS_P

class Instruccion:
    '''Clase abstracta'''


class Imprimir(Instruccion):
    def __init__(self,lista):
        self.lista = lista
    
class DeclaracionImplicita(Instruccion):
    def __init__(self,id,valor,tipo=TIPOS_P.VOID):
        self.id = id
        self.tipo = tipo
        self.valor = valor

class DeclaracionExplicita(Instruccion):
    def __init__(self,id,valor,tipo):
        self.id = id
        self.tipo = tipo
        self.valor = valor