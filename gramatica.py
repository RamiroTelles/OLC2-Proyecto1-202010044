

reservadas = {
    'console':'CONSOLE',
    'log':'LOG',
    'true':'TRUE',
    'false':'FALSE',
    'let':'LET',
    'number': 'NUMBER',
    'string': 'STRING',
    'if':'IF',
    'else' : 'ELSE',
    'function': 'FUNCTION',
    'interface': 'INTERFACE'
}

# Lista de tokens
tokens = [
   
    'PARIZQ',
    'PARDER',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'MODULO',
    'MAYOR',
    'MENOR',
    'MAYORIGUAL',
    'MENORIGUAL',
    'EQUIVALENTE',
    'DISTINTO',
    'NOT',
    'OR',
    'AND',
    'PUNTO',
    'PUNTOCOMA',
    'DOSPUNTOS',
    'INTERROGACION',
    'COMA',
    'CADENA',
    'ENTERO',
    'DECIMAL',
    'CARACTER',
    'COMMENTBLOCK'
 ] + list(reservadas.values())

t_CONSOLE   = r'console'
t_LOG       = r'log'
t_TRUE      = r'true'
t_FALSE     = r'false'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_MODULO    = r'%'
t_MAYOR     = r'>'
t_MENOR     = r'<'
t_MAYORIGUAL    = r'>='
t_MENORIGUAL    = r'<='
t_EQUIVALENTE   = r'=='
t_DISTINTO  = r'!='
t_NOT       = r'!'
t_OR        = r'\|\|'
t_AND       = r'&&' 
t_PUNTO    = r'\.'
t_PUNTOCOMA     = r';'
t_DOSPUNTOS     = r':'
t_INTERROGACION = r'\?'
t_COMA          = r','

def t_CADENA(t):
    r'\"(.+?)\"'
    try:
        t.value = str(t.value)
    except ValueError:
        print("Error %d", t.value)
        t.value = ''
    return t

def t_CARACTER(t):
    r'\'(.?)\''
    try:
        t.value = str(t.value)
    except ValueError:
        print("Error %d", t.value)
        t.value = ''
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

t_ignore = " \t"

t_ignore_COMMENTLINE = r'\/\/.*'

def t_ignore_COMMENTBLOCK(t):
    r'\/\*[^*]*\*+(?:[^/*][^*]*\*+)*\/'
    t.lexer.lineno += t.value.count('\n')  


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    
    print("Error Léxico '%s'" % t.value[0])
    t.lexer.skip(1)


from instrucciones import *
from expresiones import *
#Gramatica ------------------------------------------------------------------


def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t):
    '''instrucciones    : instrucciones instruccion'''
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_instruccion(t) :
    '''instruccion      : imprimir_instr'''
    t[0] = t[1]

def p_instruccion_console(t):
    '''imprimir_instr : CONSOLE PUNTO LOG PARIZQ lista_exp PARDER PUNTOCOMA'''
    t[0] = Imprimir(t[5])

def p_lista_exp1(t):
    '''lista_exp    : lista_exp COMA op_Ternario'''
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_exp2(t):
    '''lista_exp    : op_Ternario'''
    t[0]=[t[1]]

def p_op_Ternario1(t):
    '''op_Ternario  : exp_Or INTERROGACION exp_Or DOSPUNTOS exp_Or'''
    t[0] = ExpresionTernaria(t[1],t[3],t[5])

def p_op_Ternario2(t):
    '''op_Ternario  : exp_Or'''
    t[0] = t[1]

def p_exp_Or1(t):
    '''exp_Or   : exp_Or OR exp_And'''
    t[0] = ExpresionLogica(t[1],t[3],OPERACION_LOGICA.OR)


def p_exp_Or2(t):
    '''exp_Or   : exp_And'''
    t[0] = t[1]

def p_exp_And1(t):
    '''exp_And   : exp_And AND exp_Not'''
    t[0] = ExpresionLogica(t[1],t[3],OPERACION_LOGICA.AND)

def p_exp_And2(t):
    '''exp_And   : exp_Not'''
    t[0]=t[1]



def p_exp_Not1(t):
    '''exp_Not  : lNot exp_Comp'''
    if t[1]%2==0:
        t[0] = t[1]
    else:
        t[0]= ExpresionNot(t[2])

def p_expNot2(t):
    '''exp_Not  : exp_Comp'''
    t[0]=t[1]

def p_listaNot1(t):
    '''lNot : lNot NOT'''
    t[0]= t[1]+1

def p_listaNot2(t):
    '''lNot : NOT'''
    t[0]=1

def p_exp_Comp1(t):
    '''exp_Comp : exp_Sum_Menos EQUIVALENTE exp_Sum_Menos
                | exp_Sum_Menos DISTINTO exp_Sum_Menos'''
    if t[2] == '=='  : t[0] = ExpresionRelacional(t[1], t[3], OPERACION_REL.IGUAL)
    elif t[2] == '!=': t[0] = ExpresionRelacional(t[1], t[3], OPERACION_REL.NO_IGUAL)
    
def p_exp_Comp2(t):
    '''exp_Comp    : exp_rel'''
    t[0]=t[1]

def p_exp_rel1(t):
    '''exp_rel  : exp_Sum_Menos MAYOR exp_Sum_Menos
                | exp_Sum_Menos MENOR exp_Sum_Menos
                | exp_Sum_Menos MAYORIGUAL exp_Sum_Menos
                | exp_Sum_Menos MENORIGUAL exp_Sum_Menos'''
    if t[2] == '>'  : t[0] = ExpresionRelacional(t[1], t[3], OPERACION_REL.MAYOR_QUE)
    elif t[2] == '<': t[0] = ExpresionRelacional(t[1], t[3], OPERACION_REL.MENOR_QUE)
    elif t[2] == '>=': t[0] = ExpresionRelacional(t[1], t[3], OPERACION_REL.MAYORIGUAL)
    elif t[2] == '<=': t[0] = ExpresionRelacional(t[1], t[3], OPERACION_REL.MENORIGUAL)
    
def p_exp_rel2(t):
    '''exp_rel    : exp_Sum_Menos'''
    t[0]=t[1]

def p_exp_sum_menos1(t):
    '''exp_Sum_Menos    : exp_Sum_Menos MAS exp_Mul_Div
                        | exp_Sum_Menos MENOS exp_Mul_Div'''
    
    if t[2] == '+'  : t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS)
    elif t[2] == '-': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS)
    
def p_exp_Sum_Menos2(t):
    '''exp_Sum_Menos    : exp_Mul_Div'''
    t[0]=t[1]


def p_exp_Mul_Div1(t):
    '''exp_Mul_Div  : exp_Mul_Div POR exp_Parentesis
                    | exp_Mul_Div DIVIDIDO exp_Parentesis
                    | exp_Mul_Div MODULO exp_Parentesis'''
    if t[2] == '*'  : t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR)
    elif t[2] == '/': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)
    elif t[2] == '%': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MODULO)
    
def p_exp_Mul_Div2(t):
    '''exp_Mul_Div    : exp_Parentesis'''
    t[0]=t[1]

def p_exp_Parentesis1(t):
    '''exp_Parentesis   : PARIZQ exp_Or PARDER'''
    t[0] = t[2]

def p_exp_Parentesis2(t):
    '''exp_Parentesis   : exp_Negativo'''
    t[0]=t[1]

def p_exp_Negativo1(t):
    '''exp_Negativo : MENOS valor'''
    t[0]= ExpresionNegativa(t[2])

def p_exp_Negativo2(t):
    '''exp_Negativo : valor'''
    t[0]= t[1]


def p_valorEntero(t):
    '''valor    : ENTERO'''
    t[0]=ExpresionEntero(t[1])

def p_valorCadena(t):
    '''valor    : CADENA'''
    t[0]=ExpresionDobleComilla(t[1])

def p_valorDecimal(t):
    '''valor    : DECIMAL'''
    t[0]=ExpresionDecimal(t[1])

def p_valorCaracter(t):
    '''valor    : CARACTER'''
    t[0]=ExpresionComillaSimple(t[1])

def p_valorBoolean(t):
    '''valor    : TRUE
                | FALSE'''
    t[0]=Expresion_True_False(t[1])
    
    







def p_error(p):
    if p:
        
        print(f"Error de sintaxis en línea {p.lineno}, columna {p.lexpos}: Token inesperado '{p.value}'")
    else:
        
        print("Error de sintaxis")

import ply.lex as Lex
import ply.yacc as yacc
lexer = Lex.lex()
parser = yacc.yacc()

def parse(input) :
    return parser.parse(input)

    

