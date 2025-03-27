grammar MiGramatica;

// Regla principal: múltiples sentencias
programa: (sentencia ';')+ EOF ;

// Sentencias posibles
sentencia
    : forStmt
    | asignacion
    ;

// Regla para `for`
forStmt
    : 'for' '(' inicializacion ';' condicion ';' actualizacion ')' '{' (sentencia (';')?)* '}' # ForLoop
    ;

// Inicialización del `for` (Ej: i = 0)
inicializacion
    : ID '=' expresion
    ;

// Condición dentro del `for` (Ej: i < 10)
condicion
    : ID op=('>' | '<' | '==' | '!=') INT
    ;

// Actualización del `for` (Ej: i = i + 1)
actualizacion
    : ID '=' expresion
    ;

// Asignaciones generales con `;`
asignacion
    : ID '=' expresion ';' # Assign
    ;

// Expresiones matemáticas
expresion
    : expresion op=('*'|'/') expresion 
    | expresion op=('+'|'-') expresion 
    | INT                           
    | ID                                 
    | '(' expresion ')'                
    ;

// Reglas léxicas
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;  
INT : [0-9]+ ;                  

// Corrección de espacios en blanco
WS  : [ \t\r\n\u00A0]+ -> skip ; 

// Fragmentos auxiliares (opcional)
fragment DIGIT  : [0-9] ;
fragment LETTER : [a-zA-Z_] ;