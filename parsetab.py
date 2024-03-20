
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOLEAN CADENA CARACTER CHAR COMA COMMENTBLOCK CONSOLE CONST DECIMAL DISTINTO DIVIDIDO DOSPUNTOS ELSE ENTERO EQUIVALENTE FALSE FLOAT FUNCTION ID IF IGUAL INTERFACE INTERROGACION LLAVDER LLAVIZQ LOG MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MODULO NOT NULL NUMBER OR PARDER PARIZQ POR PUNTO PUNTOCOMA STRING TRUE VARinit            : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccion instruccion      : imprimir_instr\n                        | declaracion\n                        | asignacion\n                        | sIfsIf  : IF PARIZQ op_Ternario PARDER LLAVIZQ instrucciones sIf2sIf2  : LLAVDER ELSE sElsesIf2  : LLAVDERsElse    : LLAVIZQ instrucciones LLAVDERsElse    : sIfasignacion   : ID IGUAL op_Ternario PUNTOCOMA\n                    | ID MAS IGUAL op_Ternario PUNTOCOMA\n                    | ID MENOS IGUAL op_Ternario PUNTOCOMAdeclaracion  : tipoVar ID DOSPUNTOS tipo declaracion_explicitadeclaracion  : tipoVar ID declaracion_implicitadeclaracion_explicita    : PUNTOCOMAdeclaracion_explicita    : IGUAL op_Ternario PUNTOCOMAdeclaracion_implicita    : IGUAL op_Ternario PUNTOCOMAtipoVar  : VAR\n                | CONSTtipo : NUMBERtipo : FLOATtipo : STRINGtipo : BOOLEANtipo : CHARimprimir_instr : CONSOLE PUNTO LOG PARIZQ lista_exp PARDER PUNTOCOMAlista_exp    : lista_exp COMA op_Ternariolista_exp    : op_Ternarioop_Ternario  : exp_Or INTERROGACION exp_Or DOSPUNTOS exp_Orop_Ternario  : exp_Orexp_Or   : exp_Or OR exp_Andexp_Or   : exp_Andexp_And   : exp_And AND exp_Notexp_And   : exp_Notexp_Not  : lNot exp_Compexp_Not  : exp_ComplNot : lNot NOTlNot : NOTexp_Comp : exp_Sum_Menos EQUIVALENTE exp_Sum_Menos\n                | exp_Sum_Menos DISTINTO exp_Sum_Menosexp_Comp    : exp_relexp_rel  : exp_Sum_Menos MAYOR exp_Sum_Menos\n                | exp_Sum_Menos MENOR exp_Sum_Menos\n                | exp_Sum_Menos MAYORIGUAL exp_Sum_Menos\n                | exp_Sum_Menos MENORIGUAL exp_Sum_Menosexp_rel    : exp_Sum_Menosexp_Sum_Menos    : exp_Sum_Menos MAS exp_Mul_Div\n                        | exp_Sum_Menos MENOS exp_Mul_Divexp_Sum_Menos    : exp_Mul_Divexp_Mul_Div  : exp_Mul_Div POR exp_Parentesis\n                    | exp_Mul_Div DIVIDIDO exp_Parentesis\n                    | exp_Mul_Div MODULO exp_Parentesisexp_Mul_Div    : exp_Parentesisexp_Parentesis   : PARIZQ exp_Or PARDERexp_Parentesis   : exp_Negativoexp_Negativo : MENOS valorexp_Negativo : valorvalor    : ENTEROvalor    : CADENAvalor    : DECIMALvalor    : CARACTERvalor    : TRUE\n                | FALSEvalor    : NULLvalor    : ID'
    
_lr_action_items = {'CONSOLE':([0,2,3,4,5,6,7,14,23,59,83,84,86,102,103,104,109,110,112,114,115,117,118,119,120,121,],[8,8,-3,-4,-5,-6,-7,-2,-17,-13,-16,-18,-20,-14,-15,8,8,-28,-19,-8,-10,-9,8,-12,8,-11,]),'ID':([0,2,3,4,5,6,7,9,12,13,14,17,20,23,24,30,32,36,38,48,49,51,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,83,84,85,86,102,103,104,106,108,109,110,112,114,115,117,118,119,120,121,],[10,10,-3,-4,-5,-6,-7,16,-21,-22,-2,25,25,-17,25,25,-40,25,25,25,25,25,-13,25,25,25,-39,25,25,25,25,25,25,25,25,25,25,25,-16,-18,25,-20,-14,-15,10,25,25,10,-28,-19,-8,-10,-9,10,-12,10,-11,]),'IF':([0,2,3,4,5,6,7,14,23,59,83,84,86,102,103,104,109,110,112,114,115,116,117,118,119,120,121,],[11,11,-3,-4,-5,-6,-7,-2,-17,-13,-16,-18,-20,-14,-15,11,11,-28,-19,-8,-10,11,-9,11,-12,11,-11,]),'VAR':([0,2,3,4,5,6,7,14,23,59,83,84,86,102,103,104,109,110,112,114,115,117,118,119,120,121,],[12,12,-3,-4,-5,-6,-7,-2,-17,-13,-16,-18,-20,-14,-15,12,12,-28,-19,-8,-10,-9,12,-12,12,-11,]),'CONST':([0,2,3,4,5,6,7,14,23,59,83,84,86,102,103,104,109,110,112,114,115,117,118,119,120,121,],[13,13,-3,-4,-5,-6,-7,-2,-17,-13,-16,-18,-20,-14,-15,13,13,-28,-19,-8,-10,-9,13,-12,13,-11,]),'$end':([1,2,3,4,5,6,7,14,23,59,83,84,86,102,103,110,112,114,115,117,119,121,],[0,-1,-3,-4,-5,-6,-7,-2,-17,-13,-16,-18,-20,-14,-15,-28,-19,-8,-10,-9,-12,-11,]),'LLAVDER':([3,4,5,6,7,14,23,59,83,84,86,102,103,109,110,112,114,115,117,119,120,121,],[-3,-4,-5,-6,-7,-2,-17,-13,-16,-18,-20,-14,-15,115,-28,-19,-8,-10,-9,-12,121,-11,]),'PUNTO':([8,],[15,]),'IGUAL':([10,16,18,19,52,53,54,55,56,57,],[17,24,48,49,85,-23,-24,-25,-26,-27,]),'MAS':([10,25,33,35,37,39,40,41,42,43,44,45,46,47,76,90,91,92,93,94,95,96,97,98,99,100,101,],[18,-67,67,-51,-55,-57,-59,-60,-61,-62,-63,-64,-65,-66,-58,67,67,-49,-50,67,67,67,67,-52,-53,-54,-56,]),'MENOS':([10,17,20,24,25,30,32,33,35,37,38,39,40,41,42,43,44,45,46,47,48,49,51,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,85,90,91,92,93,94,95,96,97,98,99,100,101,106,108,],[19,36,36,36,-67,36,-40,68,-51,-55,36,-57,-59,-60,-61,-62,-63,-64,-65,-66,36,36,36,36,36,36,-39,36,36,36,36,36,36,36,36,36,36,36,-58,36,68,68,-49,-50,68,68,68,68,-52,-53,-54,-56,36,36,]),'PARIZQ':([11,17,20,21,24,30,32,38,48,49,51,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,85,106,108,],[20,38,38,51,38,38,-40,38,38,38,38,38,38,38,-39,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'LOG':([15,],[21,]),'DOSPUNTOS':([16,25,28,29,31,33,34,35,37,39,40,41,42,43,44,45,46,47,63,76,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,],[22,-67,-34,-36,-38,-48,-43,-51,-55,-57,-59,-60,-61,-62,-63,-64,-65,-66,-37,-58,108,-33,-35,-41,-42,-49,-50,-44,-45,-46,-47,-52,-53,-54,-56,]),'NOT':([17,20,24,30,32,38,48,49,51,60,61,62,64,85,106,108,],[32,32,32,64,-40,32,32,32,32,32,32,32,-39,32,32,32,]),'ENTERO':([17,20,24,30,32,36,38,48,49,51,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,85,106,108,],[41,41,41,41,-40,41,41,41,41,41,41,41,41,-39,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'CADENA':([17,20,24,30,32,36,38,48,49,51,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,85,106,108,],[42,42,42,42,-40,42,42,42,42,42,42,42,42,-39,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'DECIMAL':([17,20,24,30,32,36,38,48,49,51,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,85,106,108,],[43,43,43,43,-40,43,43,43,43,43,43,43,43,-39,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'CARACTER':([17,20,24,30,32,36,38,48,49,51,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,85,106,108,],[44,44,44,44,-40,44,44,44,44,44,44,44,44,-39,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'TRUE':([17,20,24,30,32,36,38,48,49,51,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,85,106,108,],[45,45,45,45,-40,45,45,45,45,45,45,45,45,-39,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'FALSE':([17,20,24,30,32,36,38,48,49,51,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,85,106,108,],[46,46,46,46,-40,46,46,46,46,46,46,46,46,-39,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'NULL':([17,20,24,30,32,36,38,48,49,51,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,85,106,108,],[47,47,47,47,-40,47,47,47,47,47,47,47,47,-39,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'NUMBER':([22,],[53,]),'FLOAT':([22,],[54,]),'STRING':([22,],[55,]),'BOOLEAN':([22,],[56,]),'CHAR':([22,],[57,]),'POR':([25,35,37,39,40,41,42,43,44,45,46,47,76,92,93,98,99,100,101,],[-67,73,-55,-57,-59,-60,-61,-62,-63,-64,-65,-66,-58,73,73,-52,-53,-54,-56,]),'DIVIDIDO':([25,35,37,39,40,41,42,43,44,45,46,47,76,92,93,98,99,100,101,],[-67,74,-55,-57,-59,-60,-61,-62,-63,-64,-65,-66,-58,74,74,-52,-53,-54,-56,]),'MODULO':([25,35,37,39,40,41,42,43,44,45,46,47,76,92,93,98,99,100,101,],[-67,75,-55,-57,-59,-60,-61,-62,-63,-64,-65,-66,-58,75,75,-52,-53,-54,-56,]),'EQUIVALENTE':([25,33,35,37,39,40,41,42,43,44,45,46,47,76,92,93,98,99,100,101,],[-67,65,-51,-55,-57,-59,-60,-61,-62,-63,-64,-65,-66,-58,-49,-50,-52,-53,-54,-56,]),'DISTINTO':([25,33,35,37,39,40,41,42,43,44,45,46,47,76,92,93,98,99,100,101,],[-67,66,-51,-55,-57,-59,-60,-61,-62,-63,-64,-65,-66,-58,-49,-50,-52,-53,-54,-56,]),'MAYOR':([25,33,35,37,39,40,41,42,43,44,45,46,47,76,92,93,98,99,100,101,],[-67,69,-51,-55,-57,-59,-60,-61,-62,-63,-64,-65,-66,-58,-49,-50,-52,-53,-54,-56,]),'MENOR':([25,33,35,37,39,40,41,42,43,44,45,46,47,76,92,93,98,99,100,101,],[-67,70,-51,-55,-57,-59,-60,-61,-62,-63,-64,-65,-66,-58,-49,-50,-52,-53,-54,-56,]),'MAYORIGUAL':([25,33,35,37,39,40,41,42,43,44,45,46,47,76,92,93,98,99,100,101,],[-67,71,-51,-55,-57,-59,-60,-61,-62,-63,-64,-65,-66,-58,-49,-50,-52,-53,-54,-56,]),'MENORIGUAL':([25,33,35,37,39,40,41,42,43,44,45,46,47,76,92,93,98,99,100,101,],[-67,72,-51,-55,-57,-59,-60,-61,-62,-63,-64,-65,-66,-58,-49,-50,-52,-53,-54,-56,]),'AND':([25,28,29,31,33,34,35,37,39,40,41,42,43,44,45,46,47,63,76,88,89,90,91,92,93,94,95,96,97,98,99,100,101,],[-67,62,-36,-38,-48,-43,-51,-55,-57,-59,-60,-61,-62,-63,-64,-65,-66,-37,-58,62,-35,-41,-42,-49,-50,-44,-45,-46,-47,-52,-53,-54,-56,]),'INTERROGACION':([25,27,28,29,31,33,34,35,37,39,40,41,42,43,44,45,46,47,63,76,88,89,90,91,92,93,94,95,96,97,98,99,100,101,],[-67,60,-34,-36,-38,-48,-43,-51,-55,-57,-59,-60,-61,-62,-63,-64,-65,-66,-37,-58,-33,-35,-41,-42,-49,-50,-44,-45,-46,-47,-52,-53,-54,-56,]),'OR':([25,27,28,29,31,33,34,35,37,39,40,41,42,43,44,45,46,47,63,76,77,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,113,],[-67,61,-34,-36,-38,-48,-43,-51,-55,-57,-59,-60,-61,-62,-63,-64,-65,-66,-37,-58,61,61,-33,-35,-41,-42,-49,-50,-44,-45,-46,-47,-52,-53,-54,-56,61,]),'PUNTOCOMA':([25,26,27,28,29,31,33,34,35,37,39,40,41,42,43,44,45,46,47,52,53,54,55,56,57,58,63,76,78,79,88,89,90,91,92,93,94,95,96,97,98,99,100,101,105,107,113,],[-67,59,-32,-34,-36,-38,-48,-43,-51,-55,-57,-59,-60,-61,-62,-63,-64,-65,-66,84,-23,-24,-25,-26,-27,86,-37,-58,102,103,-33,-35,-41,-42,-49,-50,-44,-45,-46,-47,-52,-53,-54,-56,110,112,-31,]),'PARDER':([25,27,28,29,31,33,34,35,37,39,40,41,42,43,44,45,46,47,50,63,76,77,81,82,88,89,90,91,92,93,94,95,96,97,98,99,100,101,111,113,],[-67,-32,-34,-36,-38,-48,-43,-51,-55,-57,-59,-60,-61,-62,-63,-64,-65,-66,80,-37,-58,101,105,-30,-33,-35,-41,-42,-49,-50,-44,-45,-46,-47,-52,-53,-54,-56,-29,-31,]),'COMA':([25,27,28,29,31,33,34,35,37,39,40,41,42,43,44,45,46,47,63,76,81,82,88,89,90,91,92,93,94,95,96,97,98,99,100,101,111,113,],[-67,-32,-34,-36,-38,-48,-43,-51,-55,-57,-59,-60,-61,-62,-63,-64,-65,-66,-37,-58,106,-30,-33,-35,-41,-42,-49,-50,-44,-45,-46,-47,-52,-53,-54,-56,-29,-31,]),'LLAVIZQ':([80,116,],[104,118,]),'ELSE':([115,],[116,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,104,118,],[2,109,120,]),'instruccion':([0,2,104,109,118,120,],[3,14,3,14,3,14,]),'imprimir_instr':([0,2,104,109,118,120,],[4,4,4,4,4,4,]),'declaracion':([0,2,104,109,118,120,],[5,5,5,5,5,5,]),'asignacion':([0,2,104,109,118,120,],[6,6,6,6,6,6,]),'sIf':([0,2,104,109,116,118,120,],[7,7,7,7,119,7,7,]),'tipoVar':([0,2,104,109,118,120,],[9,9,9,9,9,9,]),'declaracion_implicita':([16,],[23,]),'op_Ternario':([17,20,24,48,49,51,85,106,],[26,50,58,78,79,82,107,111,]),'exp_Or':([17,20,24,38,48,49,51,60,85,106,108,],[27,27,27,77,27,27,27,87,27,27,113,]),'exp_And':([17,20,24,38,48,49,51,60,61,85,106,108,],[28,28,28,28,28,28,28,28,88,28,28,28,]),'exp_Not':([17,20,24,38,48,49,51,60,61,62,85,106,108,],[29,29,29,29,29,29,29,29,29,89,29,29,29,]),'lNot':([17,20,24,38,48,49,51,60,61,62,85,106,108,],[30,30,30,30,30,30,30,30,30,30,30,30,30,]),'exp_Comp':([17,20,24,30,38,48,49,51,60,61,62,85,106,108,],[31,31,31,63,31,31,31,31,31,31,31,31,31,31,]),'exp_Sum_Menos':([17,20,24,30,38,48,49,51,60,61,62,65,66,69,70,71,72,85,106,108,],[33,33,33,33,33,33,33,33,33,33,33,90,91,94,95,96,97,33,33,33,]),'exp_rel':([17,20,24,30,38,48,49,51,60,61,62,85,106,108,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'exp_Mul_Div':([17,20,24,30,38,48,49,51,60,61,62,65,66,67,68,69,70,71,72,85,106,108,],[35,35,35,35,35,35,35,35,35,35,35,35,35,92,93,35,35,35,35,35,35,35,]),'exp_Parentesis':([17,20,24,30,38,48,49,51,60,61,62,65,66,67,68,69,70,71,72,73,74,75,85,106,108,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,98,99,100,37,37,37,]),'exp_Negativo':([17,20,24,30,38,48,49,51,60,61,62,65,66,67,68,69,70,71,72,73,74,75,85,106,108,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'valor':([17,20,24,30,36,38,48,49,51,60,61,62,65,66,67,68,69,70,71,72,73,74,75,85,106,108,],[40,40,40,40,76,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'tipo':([22,],[52,]),'lista_exp':([51,],[81,]),'declaracion_explicita':([52,],[83,]),'sIf2':([109,],[114,]),'sElse':([116,],[117,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','gramatica.py',160),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','gramatica.py',164),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',169),
  ('instruccion -> imprimir_instr','instruccion',1,'p_instruccion','gramatica.py',173),
  ('instruccion -> declaracion','instruccion',1,'p_instruccion','gramatica.py',174),
  ('instruccion -> asignacion','instruccion',1,'p_instruccion','gramatica.py',175),
  ('instruccion -> sIf','instruccion',1,'p_instruccion','gramatica.py',176),
  ('sIf -> IF PARIZQ op_Ternario PARDER LLAVIZQ instrucciones sIf2','sIf',7,'p_sIf1','gramatica.py',180),
  ('sIf2 -> LLAVDER ELSE sElse','sIf2',3,'p_sIf2_1','gramatica.py',183),
  ('sIf2 -> LLAVDER','sIf2',1,'p_sIf2_2','gramatica.py',186),
  ('sElse -> LLAVIZQ instrucciones LLAVDER','sElse',3,'p_sElse1','gramatica.py',189),
  ('sElse -> sIf','sElse',1,'p_sElse2','gramatica.py',192),
  ('asignacion -> ID IGUAL op_Ternario PUNTOCOMA','asignacion',4,'p_asignacion','gramatica.py',195),
  ('asignacion -> ID MAS IGUAL op_Ternario PUNTOCOMA','asignacion',5,'p_asignacion','gramatica.py',196),
  ('asignacion -> ID MENOS IGUAL op_Ternario PUNTOCOMA','asignacion',5,'p_asignacion','gramatica.py',197),
  ('declaracion -> tipoVar ID DOSPUNTOS tipo declaracion_explicita','declaracion',5,'p_declaracion1','gramatica.py',207),
  ('declaracion -> tipoVar ID declaracion_implicita','declaracion',3,'p_declaracion2','gramatica.py',216),
  ('declaracion_explicita -> PUNTOCOMA','declaracion_explicita',1,'p_declaracion_explicita1','gramatica.py',223),
  ('declaracion_explicita -> IGUAL op_Ternario PUNTOCOMA','declaracion_explicita',3,'p_declaracion_explicita2','gramatica.py',227),
  ('declaracion_implicita -> IGUAL op_Ternario PUNTOCOMA','declaracion_implicita',3,'p_declaracion_implicita','gramatica.py',232),
  ('tipoVar -> VAR','tipoVar',1,'p_tipoVar','gramatica.py',236),
  ('tipoVar -> CONST','tipoVar',1,'p_tipoVar','gramatica.py',237),
  ('tipo -> NUMBER','tipo',1,'p_tipoNumber','gramatica.py',242),
  ('tipo -> FLOAT','tipo',1,'p_tipoFloat','gramatica.py',246),
  ('tipo -> STRING','tipo',1,'p_tipoString','gramatica.py',250),
  ('tipo -> BOOLEAN','tipo',1,'p_tipoBoolean','gramatica.py',254),
  ('tipo -> CHAR','tipo',1,'p_tipoChar','gramatica.py',258),
  ('imprimir_instr -> CONSOLE PUNTO LOG PARIZQ lista_exp PARDER PUNTOCOMA','imprimir_instr',7,'p_instruccion_console','gramatica.py',262),
  ('lista_exp -> lista_exp COMA op_Ternario','lista_exp',3,'p_lista_exp1','gramatica.py',266),
  ('lista_exp -> op_Ternario','lista_exp',1,'p_lista_exp2','gramatica.py',271),
  ('op_Ternario -> exp_Or INTERROGACION exp_Or DOSPUNTOS exp_Or','op_Ternario',5,'p_op_Ternario1','gramatica.py',275),
  ('op_Ternario -> exp_Or','op_Ternario',1,'p_op_Ternario2','gramatica.py',279),
  ('exp_Or -> exp_Or OR exp_And','exp_Or',3,'p_exp_Or1','gramatica.py',283),
  ('exp_Or -> exp_And','exp_Or',1,'p_exp_Or2','gramatica.py',288),
  ('exp_And -> exp_And AND exp_Not','exp_And',3,'p_exp_And1','gramatica.py',292),
  ('exp_And -> exp_Not','exp_And',1,'p_exp_And2','gramatica.py',296),
  ('exp_Not -> lNot exp_Comp','exp_Not',2,'p_exp_Not1','gramatica.py',302),
  ('exp_Not -> exp_Comp','exp_Not',1,'p_expNot2','gramatica.py',309),
  ('lNot -> lNot NOT','lNot',2,'p_listaNot1','gramatica.py',313),
  ('lNot -> NOT','lNot',1,'p_listaNot2','gramatica.py',317),
  ('exp_Comp -> exp_Sum_Menos EQUIVALENTE exp_Sum_Menos','exp_Comp',3,'p_exp_Comp1','gramatica.py',321),
  ('exp_Comp -> exp_Sum_Menos DISTINTO exp_Sum_Menos','exp_Comp',3,'p_exp_Comp1','gramatica.py',322),
  ('exp_Comp -> exp_rel','exp_Comp',1,'p_exp_Comp2','gramatica.py',327),
  ('exp_rel -> exp_Sum_Menos MAYOR exp_Sum_Menos','exp_rel',3,'p_exp_rel1','gramatica.py',331),
  ('exp_rel -> exp_Sum_Menos MENOR exp_Sum_Menos','exp_rel',3,'p_exp_rel1','gramatica.py',332),
  ('exp_rel -> exp_Sum_Menos MAYORIGUAL exp_Sum_Menos','exp_rel',3,'p_exp_rel1','gramatica.py',333),
  ('exp_rel -> exp_Sum_Menos MENORIGUAL exp_Sum_Menos','exp_rel',3,'p_exp_rel1','gramatica.py',334),
  ('exp_rel -> exp_Sum_Menos','exp_rel',1,'p_exp_rel2','gramatica.py',341),
  ('exp_Sum_Menos -> exp_Sum_Menos MAS exp_Mul_Div','exp_Sum_Menos',3,'p_exp_sum_menos1','gramatica.py',345),
  ('exp_Sum_Menos -> exp_Sum_Menos MENOS exp_Mul_Div','exp_Sum_Menos',3,'p_exp_sum_menos1','gramatica.py',346),
  ('exp_Sum_Menos -> exp_Mul_Div','exp_Sum_Menos',1,'p_exp_Sum_Menos2','gramatica.py',352),
  ('exp_Mul_Div -> exp_Mul_Div POR exp_Parentesis','exp_Mul_Div',3,'p_exp_Mul_Div1','gramatica.py',357),
  ('exp_Mul_Div -> exp_Mul_Div DIVIDIDO exp_Parentesis','exp_Mul_Div',3,'p_exp_Mul_Div1','gramatica.py',358),
  ('exp_Mul_Div -> exp_Mul_Div MODULO exp_Parentesis','exp_Mul_Div',3,'p_exp_Mul_Div1','gramatica.py',359),
  ('exp_Mul_Div -> exp_Parentesis','exp_Mul_Div',1,'p_exp_Mul_Div2','gramatica.py',365),
  ('exp_Parentesis -> PARIZQ exp_Or PARDER','exp_Parentesis',3,'p_exp_Parentesis1','gramatica.py',369),
  ('exp_Parentesis -> exp_Negativo','exp_Parentesis',1,'p_exp_Parentesis2','gramatica.py',373),
  ('exp_Negativo -> MENOS valor','exp_Negativo',2,'p_exp_Negativo1','gramatica.py',377),
  ('exp_Negativo -> valor','exp_Negativo',1,'p_exp_Negativo2','gramatica.py',381),
  ('valor -> ENTERO','valor',1,'p_valorEntero','gramatica.py',386),
  ('valor -> CADENA','valor',1,'p_valorCadena','gramatica.py',390),
  ('valor -> DECIMAL','valor',1,'p_valorDecimal','gramatica.py',394),
  ('valor -> CARACTER','valor',1,'p_valorCaracter','gramatica.py',398),
  ('valor -> TRUE','valor',1,'p_valorBoolean','gramatica.py',402),
  ('valor -> FALSE','valor',1,'p_valorBoolean','gramatica.py',403),
  ('valor -> NULL','valor',1,'p_valorNull','gramatica.py',407),
  ('valor -> ID','valor',1,'p_valorId','gramatica.py',411),
]
