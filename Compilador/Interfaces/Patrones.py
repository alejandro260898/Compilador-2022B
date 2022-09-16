from Compilador.Interfaces.TipoSimbolo import TipoSimbolo

class Patrones:
    PATRON_BLANCOS =        "^\s"
    PATRON_IDENTIFICADOR =	"^[a-zA-Z][a-zA-Z0-9]*"
    PATRON_ENTERO =         "^[0-9]+[0-9]*"
    PATRON_REAL =           "^[0-9]+[.][0-9]+"
    PATRON_CADENA =         "^\"[a-zA-Z0-9\s]*\""
    PATRON_TIPO =           "^(void|int|float|char|string|boolean)"
    PATRON_OP_SUM =         "^[+-]"
    PATRON_OP_MUL =         "^[*\/]"
    PATRON_OP_RELAC =       "^[<>]=?"
    PATRON_OP_OR =          "^\|\|"
    PATRON_OP_AND =         "^&&"
    PATRON_OP_NOT =         "^!"
    PATRON_OP_IGUALDAD =    "^[!=]="
    PATRON_PUNTO_COMA =     "^;"
    PATRON_COMA =           "^,"
    PATRON_PARENTESIS_DER = "^\("
    PATRON_PARENTESIS_IZQ = "^\)"
    PATRON_LLAVE_DER =      "^\{"
    PATRON_LLAVE_IZQ =      "^\}"
    PATRON_IGUAL =          "^="
    PATRON_IF =             "^if"
    PATRON_WHILE =          "^while"
    PATRON_RETURN =         "^return"
    PATRON_ELSE =           "^else"
    PATRON_PESOS =          "^\$"
    
    PATRONES = {
        -1:                         PATRON_BLANCOS,       
        TipoSimbolo.TIPO:	        PATRON_TIPO,          
        TipoSimbolo.IF:             PATRON_IF,            
        TipoSimbolo.ELSE:           PATRON_ELSE,          
        TipoSimbolo.WHILE:          PATRON_WHILE,         
        TipoSimbolo.RETURN:         PATRON_RETURN,        
        TipoSimbolo.IDENTIFICADOR:  PATRON_IDENTIFICADOR, 
        TipoSimbolo.CADENA:         PATRON_CADENA,        
        TipoSimbolo.REAL:           PATRON_REAL,          
        TipoSimbolo.ENTERO:         PATRON_ENTERO,        
        TipoSimbolo.OP_SUM:         PATRON_OP_SUM,        
        TipoSimbolo.OP_MUL:         PATRON_OP_MUL,        
        TipoSimbolo.IGUAL:          PATRON_IGUAL,         
        TipoSimbolo.OP_IGUALDAD:    PATRON_OP_IGUALDAD,   
        TipoSimbolo.OP_RELAC:       PATRON_OP_RELAC,      
        TipoSimbolo.OP_AND:         PATRON_OP_AND,        
        TipoSimbolo.OP_OR:          PATRON_OP_OR,         
        TipoSimbolo.OP_NOT:         PATRON_OP_NOT,        
        TipoSimbolo.PARENTESIS_DER: PATRON_PARENTESIS_DER,
        TipoSimbolo.PARENTESIS_IZQ: PATRON_PARENTESIS_IZQ,
        TipoSimbolo.LLAVE_DER:      PATRON_LLAVE_DER,     
        TipoSimbolo.LLAVE_IZQ:      PATRON_LLAVE_IZQ,     
        TipoSimbolo.PUNTO_COMA:     PATRON_PUNTO_COMA,    
        TipoSimbolo.COMA:           PATRON_COMA,          
        TipoSimbolo.PESOS:          PATRON_PESOS,         
    }