from tipos import TIPOS_P

class Instruccion:
    '''Clase abstracta'''


class Imprimir(Instruccion):
    def __init__(self,lista):
        self.lista = lista
    
class DeclaracionImplicita(Instruccion):
    def __init__(self,id,valor,const=False,tipo=TIPOS_P.VOID,linea=0,columna=0):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.const= const
        self.linea=linea
        self.columna=columna

class DeclaracionExplicita(Instruccion):
    def __init__(self,id,valor,tipo,const=False,linea=0,columna=0):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.const= const
        self.linea=linea
        self.columna=columna

class Asignacion(Instruccion):
    def __init__(self,id,valor,linea=0,columna=0):
        self.id = id
        self.valor = valor
        self.linea=linea
        self.columna=columna

class controlFlujo(Instruccion):
    '''Clase Abstracta para flujo de control'''

class inst_if(controlFlujo):
    def __init__(self,cond,instruccionesIf,instruccionesElse):
        self.cond = cond
        self.instruccionesIf = instruccionesIf
        self.instruccionesElse=instruccionesElse

class inst_while(controlFlujo):
    def __init__(self,cond,instrucciones):
        self.cond = cond
        self.instrucciones = instrucciones
        
class inst_for(controlFlujo):
    def __init__(self,instruccion1,cond,instruccion2,instruccion_verdadero):
        self.instruccion1 = instruccion1
        self.cond = cond
        self.instruccion2 = instruccion2
        self.instruccion_verdadero = instruccion_verdadero

        