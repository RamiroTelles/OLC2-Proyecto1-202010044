
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
    elif isinstance(exp,ExpresionDobleComilla):
        return exp.cad
    elif isinstance(exp,ExpresionComillaSimple):
        return exp.cad
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


    