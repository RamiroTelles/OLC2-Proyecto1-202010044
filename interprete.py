
from expresiones import *
from instrucciones import *
from simbolos import *
from tipos import TIPOS_P,TIPOS_Simbolos
from errores import error
import copy

listaErrores =[]
SalidaConsola = ""
global TSReporte
TSReporte = TablaSimbolos()

def ejec_instrucciones(instrucciones,TS,save=True):
    
    for inst in instrucciones:
        if save:

            if isinstance(inst,Imprimir): ejec_Imprimir(inst,TS)
            elif isinstance(inst,DeclaracionExplicita): ejec_declaracion_explicita(inst,TS)
            elif isinstance(inst,DeclaracionImplicita): ejec_declaracion_implicita(inst,TS)
            elif isinstance(inst,Asignacion): ejec_Asignacion(inst,TS)
            elif isinstance(inst,controlFlujo): #ejec_controlFlujo(inst,TS)
                tupla=ejec_controlFlujo(inst,TS)
                if tupla!=None:
                    return tupla
                    #pass
            elif isinstance(inst,guardar_func): pass
                
        else:
            if isinstance(inst,guardar_func): ejec_Guardar_Func(inst,TS)
        #else: print('Error: instruccion no valida')
        

def ejec_Imprimir(inst,TS):
    global SalidaConsola
    for exp in inst.lista:
        #print('>> ', ejec_expresion(exp,TS))
        result = ejec_expresion(exp,TS)
        SalidaConsola += "> "
        SalidaConsola += str(result)
        SalidaConsola += "\n"
    

def ejec_expresion(exp,TS):
    if isinstance(exp,ExpresionAritmetica):
        return resolver_expresionAritmetica(exp,TS)
    elif isinstance(exp,ExpresionRelacional):
        return resolver_expresionRelacional(exp,TS)
    elif isinstance(exp,ExpresionDobleComilla):
        return exp.cad[1:len(exp.cad)-1]
    elif isinstance(exp,ExpresionComillaSimple):
        return exp.cad[1:len(exp.cad)-1]
    elif isinstance(exp,ExpresionBoleana):
        return resolver_expresionBoleana(exp,TS)
    elif isinstance(exp,ExpresionTernaria):
        return resolver_expresionTernaria(exp,TS)
    elif isinstance(exp,ExpresionID):
        return resolver_expresionId(exp,TS)
    elif isinstance(exp,call_func):
        tupla =ejec_Funcion(exp,TS)
        if tupla!=None:
            return tupla[1]
        
    elif isinstance(exp,ExpresionNull):
        return None
    else :
        return None
    
 

def resolver_expresionAritmetica(expNum,TS):
    if isinstance(expNum,ExpresionBinaria):
        exp1 = ejec_expresion(expNum.exp1,TS)
        exp2 = ejec_expresion(expNum.exp2,TS)

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

def resolver_expresionId(expId,TS):
    exp_id =  TS.obtener(expId.id)
    if exp_id== None:
        listaErrores.append(error("Se quiere usar valor null con variable "+expId.id,0,0,"Semantico"))
        print("Se quiere usar valor null con variable "+expId.id)
        return
    return exp_id.valor


def ejec_declaracion_explicita(inst,TS):
    exp = ejec_expresion(inst.valor,TS)

    if TS.obtener(inst.id)!=None:
        print("Ya declarada variable "+inst.id)
        listaErrores.append(error("Ya declarada variable "+inst.id,0,0,"Semantico"))
        return
    try:
        if inst.tipo==TIPOS_P.ENTERO:
            exp= int(exp)
        elif inst.tipo==TIPOS_P.FLOAT:
            exp= float(exp)
        elif inst.tipo==TIPOS_P.CADENA:
            exp= str(exp)
        elif inst.tipo==TIPOS_P.CHAR:
            exp= str(exp)
        elif inst.tipo==TIPOS_P.BOOLEAN:
            exp= bool(exp)
        
    except:
        print("Error, "+inst.id+" No se puede asignar un tipo de variable diferente")
        listaErrores.append(error(inst.id+" No se puede asignar un tipo de variable diferente",0,0,"Semantico"))

    if inst.const == True:
        if exp==None:
            print("No asigno valor a const "+inst.id)
            listaErrores.append(error("No asigno valor a const "+inst.id,0,0,"Semantico"))
            return
        else:
            simbolo = Simbolos(id=inst.id,tipo_simbolo=TIPOS_Simbolos.CONSTANTE,tipo=inst.tipo,valor=exp,ambito=TS.ambito,linea=inst.linea,columna=inst.columna)
    else:
        simbolo = Simbolos(id=inst.id,tipo_simbolo=TIPOS_Simbolos.VARIABLE,tipo=inst.tipo,valor=exp,ambito=TS.ambito,linea=inst.linea,columna=inst.columna)
        
    TS.agregar(simbolo)
    
    TSReporte.agregar(simbolo)

def ejec_declaracion_implicita(inst,TS):
    exp = ejec_expresion(inst.valor,TS)
    if TS.obtener(inst.id)!=None:
        print("Ya declarada variable "+inst.id)
        listaErrores.append(error("Ya declarada variable "+inst.id,0,0,"Semantico"))
        return

    if inst.const == True:
        if exp==None:
            print("No asigno valor a const "+inst.id)
            listaErrores.append(error("No asigno valor a const "+inst.id,0,0,"Semantico"))
            return
        else:
            simbolo = Simbolos(id=inst.id,tipo_simbolo=TIPOS_Simbolos.CONSTANTE,tipo=inst.tipo,valor=exp,ambito=TS.ambito,linea=inst.linea,columna=inst.columna)
    else:
        simbolo = Simbolos(id=inst.id,tipo_simbolo=TIPOS_Simbolos.VARIABLE,tipo=inst.tipo,valor=exp,ambito=TS.ambito,linea=inst.linea,columna=inst.columna)
    TS.agregar(simbolo)
    
    TSReporte.agregar(simbolo)

def ejec_Asignacion(inst,TS):
    
    exp = ejec_expresion(inst.valor,TS)
    simbolo = TS.obtener(inst.id)
    
    if simbolo== None:
        print("No se encontro variable "+inst.id)
        listaErrores.append(error("No se encontro variable "+inst.id,0,0,"Semantico"))
        return

    if simbolo.tipo_simbolo==TIPOS_Simbolos.CONSTANTE:
        print("No se puede asignar a Constante "+inst.id)
        listaErrores.append(error("No se puede asignar a Constante "+inst.id,0,0,"Semantico"))
        return

    try:
        if simbolo.tipo==TIPOS_P.ENTERO:
            exp= int(exp)
        elif simbolo.tipo==TIPOS_P.FLOAT:
            exp= float(exp)
        elif simbolo.tipo==TIPOS_P.CADENA:
            exp= str(exp)
        elif simbolo.tipo==TIPOS_P.CHAR:
            exp= str(exp)
        elif simbolo.tipo==TIPOS_P.BOOLEAN:
            exp= bool(exp)
    except:
        print("Error, "+inst.id+" No se puede asignar un tipo de variable diferente")
        listaErrores.append(error(inst.id+" No se puede asignar un tipo de variable diferente",0,0,"Semantico"))
    TS.actualizar(inst.id,exp)
    
    TSReporte.actualizar(inst.id,exp)


def ejec_controlFlujo(inst,TS):
    if isinstance(inst,inst_if): 
        tupla = ejec_If(inst,TS)
        if tupla != None:
            return tupla

    elif isinstance(inst,inst_while): return ejec_While(inst,TS)
    elif isinstance(inst,inst_for): return ejec_For(inst,TS)
    elif isinstance(inst,inst_switch): return ejec_Switch(inst,TS)
    elif isinstance(inst,call_func): ejec_Funcion(inst,TS)
    elif isinstance(inst,inst_Continue): 
        if('While' in TS.ambito or 'For' in TS.ambito):
            return inst,None
        else:
            print("Sentencia continue fuera de un Ciclo")
            listaErrores.append(error("Sentencia continue fuera de un Ciclo",0,0,"Semantico"))
    elif isinstance(inst,inst_Break): 
       
        
        if('While' in TS.ambito or 'For' in TS.ambito or 'Switch' in TS.ambito):
            return inst,None
        else:
            print("Sentencia break fuera de flujo de control valido")
            listaErrores.append(error("Sentencia break fuera de flujo de control valido",0,0,"Semantico"))
    elif isinstance(inst,inst_Return):
        return inst,ejec_expresion(inst.valor,TS) 
    
def ejec_If(inst,TS):
    exp = ejec_expresion(inst.cond,TS)
    if exp:
        TablaLocal = TablaSimbolos(simbolos=TS.simbolos.copy(),ambito=TS.ambito +"_If")

        tupla = ejec_instrucciones(inst.instruccionesIf,TablaLocal)
        #TS.salida+= TablaLocal.salida
        
    else:
        TablaLocal = TablaSimbolos(simbolos=TS.simbolos.copy(),ambito=TS.ambito +"_If")

        tupla = ejec_instrucciones(inst.instruccionesElse,TablaLocal)
        #TS.salida+= TablaLocal.salida
    
    return tupla

def ejec_While(inst,TS):
    
    exp = ejec_expresion(inst.cond,TS)
    while exp:
        TablaLocal = TablaSimbolos(simbolos=TS.simbolos.copy(),ambito=TS.ambito +"_While")

        tupla = ejec_instrucciones(inst.instrucciones,TablaLocal)
        if tupla!=None:

            if isinstance(tupla[0],inst_Break):
                
                break
            if isinstance(tupla[0],inst_Return):
                
                return tupla

        exp = ejec_expresion(inst.cond,TS)
        #TS.salida+= TablaLocal.salida
    
        
    
    

def ejec_For(inst,TS):
    TablaLocal = TablaSimbolos(simbolos=TS.simbolos.copy(),ambito=TS.ambito +"_For")
    ejec_instrucciones(inst.instruccion1,TablaLocal)
    exp= ejec_expresion(inst.cond,TablaLocal)

    while exp:
        tupla = ejec_instrucciones(inst.instruccion_verdadero,TablaLocal)
        if tupla!=None:

            if isinstance(tupla[0],inst_Break):
                
                break
            if isinstance(tupla[0],inst_Return):
                
                return tupla
        ejec_instrucciones(inst.instruccion2,TablaLocal)
        exp = ejec_expresion(inst.cond,TablaLocal)
    #TS.salida+= TablaLocal.salida
        
def ejec_Switch(inst,TS):
    valorId = ejec_expresion(inst.id,TS)
    posDefault=-1
    contador=-1
    for i in range(len(inst.listaExpresiones)):
        exp= ejec_expresion(inst.listaExpresiones[i],TS)
        if exp==None:
            posDefault=i
        elif valorId== exp:
            contador=i

    TablaLocal = TablaSimbolos(simbolos=TS.simbolos.copy(),ambito=TS.ambito +"_Switch")
    if contador!=-1:
        for i in range(contador,len(inst.listaInst)):
            tupla = ejec_instrucciones(inst.listaInst[i],TablaLocal)
            
            if tupla!=None:

                if isinstance(tupla[0],inst_Break):
                    
                    break
                if isinstance(tupla[0],inst_Return):
                    
                    return tupla
    elif posDefault!=-1:
        for i in range(posDefault,len(inst.listaInst)):
            tupla = ejec_instrucciones(inst.listaInst[i],TablaLocal)
            
            if tupla!=None:

                if isinstance(tupla[0],inst_Break):
                    
                    break
                if isinstance(tupla[0],inst_Return):
                    
                    return tupla

    #TS.salida+= TablaLocal.salida

def ejec_Guardar_Func(inst,TS):
    sim =TS.obtener(inst.id)
    if sim!=None:
        if sim.tipo_simbolo==TIPOS_Simbolos.FUNCION:
            print("Ya declarada Funcion "+inst.id)
            listaErrores.append(error("Ya declarada Funcion "+inst.id,0,0,"Semantico"))
            return
    
    simbolo = Simbolos(id=inst.id,tipo_simbolo=TIPOS_Simbolos.FUNCION,tipo=inst.tipo,valor=None,ambito=TS.ambito,parametros=inst.listaParametros,instrucciones=inst.instrucciones)

    TS.agregar(simbolo)
    
    TSReporte.agregar(simbolo)


def ejec_Funcion(inst,TS):
    fun_ = TS.obtener(inst.id).instrucciones
    params_ = TS.obtener(inst.id).parametros
    TablaLocal = copy.deepcopy(TS)
    TablaLocal.ambito = inst.id
    for i in range(len(inst.listaParametros)):

        exp = ejec_expresion(inst.listaParametros[i], TablaLocal)

        

        TablaLocal.agregar(Simbolos(params_[i].id,TIPOS_Simbolos.VARIABLE,params_[i].tipo,exp,TablaLocal.ambito))
        
        

    tupla = ejec_instrucciones(fun_, TablaLocal)
    #print(tupla)
    if tupla!= None:
        return tupla