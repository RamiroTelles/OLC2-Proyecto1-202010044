from enum import Enum

class OPERACION_ARITMETICA(Enum):
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4
    MODULO = 5

class OPERACION_REL(Enum):
    MAYOR_QUE = 1
    MENOR_QUE = 2
    IGUAL = 3
    NO_IGUAL = 4
    MAYORIGUAL =5
    MENORIGUAL=6

class OPERACION_LOGICA(Enum):
    AND=1
    OR=2
    NOT=3

class TIPOS_P(Enum):
    ENTERO=1
    FLOAT=2
    CADENA=3
    BOOLEAN=4
    CHAR=5


class ExpresionAritmetica:
    '''Clase Abstracta'''

class ExpresionBinaria(ExpresionAritmetica):
    def __init__(self,exp1,exp2,operador,tipo=TIPOS_P.ENTERO):
        self.exp1= exp1
        self.exp2 = exp2
        self.operador = operador
        self.tipo = tipo



class ExpresionNegativa(ExpresionAritmetica):
    def __init__(self,exp1,tipo=TIPOS_P.ENTERO):
        self.exp1= exp1
        self.tipo = tipo
        
class ExpresionEntero(ExpresionAritmetica):
    def __init__(self,exp1):
        self.exp1= exp1
        self.tipo = TIPOS_P.ENTERO
    
class ExpresionDecimal(ExpresionAritmetica):
    def __init__(self,exp1):
        self.exp1= exp1
        self.tipo = TIPOS_P.FLOAT

class ExpresionID():
    def __init__(self,id):
        self.id= id

class ExpresionBoleana:
    '''Clase Abstracta'''

class ExpresionRelacional(ExpresionBoleana):
    def __init__(self,exp1,exp2,operador):
        self.exp1= exp1
        self.exp2 = exp2
        self.operador = operador
        self.tipo = TIPOS_P.BOOLEAN

class ExpresionLogica(ExpresionBoleana):
    def __init__(self,exp1,exp2,operador):
        self.exp1= exp1
        self.exp2 = exp2
        self.operador = operador
        self.tipo = TIPOS_P.BOOLEAN  

class ExpresionNot(ExpresionBoleana):
    def __init__(self,exp1):
        self.exp1= exp1
        self.tipo = TIPOS_P.BOOLEAN

class Expresion_True_False(ExpresionBoleana):
    def __init__(self,exp1):
        self.exp1= exp1
        self.tipo = TIPOS_P.BOOLEAN
    
class ExpresionCadena:
    '''Clase Abstracta'''

class ExpresionDobleComilla(ExpresionCadena):
    def __init__(self, cad) :
        self.cad = cad
        self.tipo = TIPOS_P.CADENA

class ExpresionComillaSimple(ExpresionCadena):
    def __init__(self, cad) :
        self.cad =cad
        self.tipo = TIPOS_P.CHAR