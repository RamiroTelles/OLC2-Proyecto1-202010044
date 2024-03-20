from tipos import TIPOS_P

class Instruccion:
    '''Clase abstracta'''


class Imprimir(Instruccion):
    def __init__(self,lista):
        self.lista = lista
    
class DeclaracionImplicita(Instruccion):
    def __init__(self,id,valor,tipo=TIPOS_P.VOID,linea=0,columna=0):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.linea=linea
        self.columnna=columna

class DeclaracionExplicita(Instruccion):
    def __init__(self,id,valor,tipo,linea=0,columna=0):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.linea=linea
        self.columnna=columna