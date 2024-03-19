
from expresiones import *
from instrucciones import *



def ejec_instrucciones(instrucciones):
    for inst in instrucciones:
        if isinstance(inst,Imprimir): ejec_Imprimir(inst)
        else: print('Error: instruccion no valida')

def ejec_Imprimir(inst):
    for exp in inst.lista:
        print('>> ', ejec_expresion(exp))
    

def ejec_expresion(exp):
    if isinstance(exp,ExpresionAritmetica):
        return resolver_expresionAritmetica(exp)
    elif isinstance(exp,ExpresionRelacional):
        return resolver_expresionRelacional(exp)
    elif isinstance(exp,ExpresionDobleComilla):
        return exp.cad
    elif isinstance(exp,ExpresionComillaSimple):
        return exp.cad
    elif isinstance(exp,ExpresionBoleana):
        return resolver_expresionBoleana(exp)
    elif isinstance(exp,ExpresionTernaria):
        return resolver_expresionTernaria(exp)
    else :
        print("Error: expresion no valida")
    
 

def resolver_expresionAritmetica(expNum):
    if isinstance(expNum,ExpresionBinaria):
        exp1 = resolver_expresionAritmetica(expNum.exp1)
        exp2 = resolver_expresionAritmetica(expNum.exp2)

        if expNum.operador == OPERACION_ARITMETICA.MAS : return exp1 + exp2
        if expNum.operador == OPERACION_ARITMETICA.MENOS : return exp1 - exp2
        if expNum.operador == OPERACION_ARITMETICA.POR : return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO : return exp1 / exp2
        if expNum.operador == OPERACION_ARITMETICA.MODULO : return exp1 % exp2
    elif isinstance(expNum,ExpresionNegativa):
        return -resolver_expresionAritmetica(expNum.exp1)
    elif isinstance(expNum,ExpresionEntero):
        return expNum.exp1
    elif isinstance(expNum,ExpresionDecimal):
        return expNum.exp1
    elif isinstance(expNum,ExpresionDobleComilla):
        return expNum.cad

def resolver_expresionRelacional(exp):
    if isinstance(exp,ExpresionRelacional):
        exp1 = ejec_expresion(exp.exp1)
        exp2 = ejec_expresion(exp.exp2)

        if exp.operador == OPERACION_REL.MAYOR_QUE : return exp1 > exp2
        if exp.operador == OPERACION_REL.MENOR_QUE : return exp1 < exp2
        if exp.operador == OPERACION_REL.MAYORIGUAL : return exp1 >= exp2
        if exp.operador == OPERACION_REL.MENORIGUAL : return exp1 <= exp2
        if exp.operador == OPERACION_REL.IGUAL : return exp1 == exp2
        if exp.operador == OPERACION_REL.NO_IGUAL : return exp1 != exp2
    
def resolver_expresionBoleana(expBol):
    if isinstance(expBol,ExpresionLogica):
        exp1 = ejec_expresion(expBol.exp1)
        exp2 = ejec_expresion(expBol.exp2)

        if expBol.operador == OPERACION_LOGICA.AND : return exp1 and exp2
        if expBol.operador == OPERACION_LOGICA.OR : return exp1 or exp2
    elif isinstance(expBol,ExpresionNot):
        return not ejec_expresion(expBol.exp1)
    elif isinstance(expBol,Expresion_True_False):
        if expBol.exp1 == "true": return True
        if expBol.exp1 == "false" : return False

def resolver_expresionTernaria(expTer):
    if ejec_expresion(expTer.exp1):
        return ejec_expresion(expTer.exp2)
    return ejec_expresion(expTer.exp3)