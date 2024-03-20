
from expresiones import *
from instrucciones import *
from simbolos import *


def ejec_instrucciones(instrucciones,TS):
    for inst in instrucciones:
        if isinstance(inst,Imprimir): ejec_Imprimir(inst,TS)
        elif isinstance(inst,DeclaracionExplicita): ejec_declaracion_explicita(inst,TS)
        elif isinstance(inst,DeclaracionImplicita): ejec_declaracion_implicita(inst,TS)
        #else: print('Error: instruccion no valida')

def ejec_Imprimir(inst,TS):
    for exp in inst.lista:
        print('>> ', ejec_expresion(exp,TS))
    

def ejec_expresion(exp,TS):
    if isinstance(exp,ExpresionAritmetica):
        return resolver_expresionAritmetica(exp,TS)
    elif isinstance(exp,ExpresionRelacional):
        return resolver_expresionRelacional(exp,TS)
    elif isinstance(exp,ExpresionDobleComilla):
        return exp.cad
    elif isinstance(exp,ExpresionComillaSimple):
        return exp.cad
    elif isinstance(exp,ExpresionBoleana):
        return resolver_expresionBoleana(exp,TS)
    elif isinstance(exp,ExpresionTernaria):
        return resolver_expresionTernaria(exp,TS)
    else :
        print("Error: expresion no valida")
    
 

def resolver_expresionAritmetica(expNum,TS):
    if isinstance(expNum,ExpresionBinaria):
        exp1 = resolver_expresionAritmetica(expNum.exp1,TS)
        exp2 = resolver_expresionAritmetica(expNum.exp2,TS)

        if expNum.operador == OPERACION_ARITMETICA.MAS : return exp1 + exp2
        if expNum.operador == OPERACION_ARITMETICA.MENOS : return exp1 - exp2
        if expNum.operador == OPERACION_ARITMETICA.POR : return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO : return exp1 / exp2
        if expNum.operador == OPERACION_ARITMETICA.MODULO : return exp1 % exp2
    elif isinstance(expNum,ExpresionNegativa):
        return -resolver_expresionAritmetica(expNum.exp1,TS)
    elif isinstance(expNum,ExpresionEntero):
        return expNum.exp1
    elif isinstance(expNum,ExpresionDecimal):
        return expNum.exp1
    elif isinstance(expNum,ExpresionDobleComilla):
        return expNum.cad

def resolver_expresionRelacional(exp,TS):
    if isinstance(exp,ExpresionRelacional):
        exp1 = ejec_expresion(exp.exp1,TS)
        exp2 = ejec_expresion(exp.exp2,TS)

        if exp.operador == OPERACION_REL.MAYOR_QUE : return exp1 > exp2
        if exp.operador == OPERACION_REL.MENOR_QUE : return exp1 < exp2
        if exp.operador == OPERACION_REL.MAYORIGUAL : return exp1 >= exp2
        if exp.operador == OPERACION_REL.MENORIGUAL : return exp1 <= exp2
        if exp.operador == OPERACION_REL.IGUAL : return exp1 == exp2
        if exp.operador == OPERACION_REL.NO_IGUAL : return exp1 != exp2
    
def resolver_expresionBoleana(expBol,TS):
    if isinstance(expBol,ExpresionLogica):
        exp1 = ejec_expresion(expBol.exp1,TS)
        exp2 = ejec_expresion(expBol.exp2,TS)

        if expBol.operador == OPERACION_LOGICA.AND : return exp1 and exp2
        if expBol.operador == OPERACION_LOGICA.OR : return exp1 or exp2
    elif isinstance(expBol,ExpresionNot):
        return not ejec_expresion(expBol.exp1,TS)
    elif isinstance(expBol,Expresion_True_False):
        if expBol.exp1 == "true": return True
        if expBol.exp1 == "false" : return False

def resolver_expresionTernaria(expTer,TS):
    if ejec_expresion(expTer.exp1):
        return ejec_expresion(expTer.exp2,TS)
    return ejec_expresion(expTer.exp3,TS)

def ejec_declaracion_explicita(inst,TS):
    exp = ejec_expresion(inst.valor)
    simbolo = Simbolos(id=inst.id,tipo_simbolo=TIPOS_Simbolos.VARIABLE,tipo=inst.tipo,valor=exp,ambito=TS.ambito,linea=inst.linea,columna=inst.columna)
    TS.agregar(simbolo)

def ejec_declaracion_implicita(inst,TS):
    exp = ejec_expresion(inst.valor)
    simbolo = Simbolos(id=inst.id,tipo_simbolo=TIPOS_Simbolos.VARIABLE,tipo=inst.tipo,valor=exp,ambito=TS.ambito,linea=inst.linea,columna=inst.columna)
    TS.agregar(simbolo)