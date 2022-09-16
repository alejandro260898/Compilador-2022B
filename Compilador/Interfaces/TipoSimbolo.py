class TipoSimbolo:
    NOM_IDENTIDICADORES = "ID'S"
    NOM_NUM_REALES =      "REALES"
    NOM_NUM_ENTEROS =     "ENTEROS"
    NOM_ERRORES =         "ERRORES"
    
    ERROR =          -1
    IDENTIFICADOR =	 0
    ENTERO =         1
    REAL =           2
    CADENA =         3
    TIPO =           4
    OP_SUM =         5
    OP_MUL =         6
    OP_RELAC =       7
    OP_OR =          8
    OP_AND =         9
    OP_NOT =         10
    OP_IGUALDAD =    11
    PUNTO_COMA =     12
    COMA =           13
    PARENTESIS_DER = 14
    PARENTESIS_IZQ = 15
    LLAVE_DER =      16
    LLAVE_IZQ =      17
    IGUAL =          18
    IF =             19
    WHILE =          20
    RETURN =         21
    ELSE =           22
    PESOS =          23

    
    SIMBOLOS = {
        ERROR:          "error",
        IDENTIFICADOR:	"identificador",
        ENTERO:         "entero",
        REAL:           "real",
        CADENA:         "cadena",
        TIPO:           "tipo",
        OP_SUM:         "opSuma",
        OP_MUL:         "opMul",
        OP_RELAC:       "opRelac",
        OP_OR:          "opOr",
        OP_AND:         "opAnd",
        OP_NOT:         "opNot",
        OP_IGUALDAD:    "opIgualdad",
        PUNTO_COMA:     ";",
        COMA:           ",",
        PARENTESIS_DER: "(",
        PARENTESIS_IZQ: ")",
        LLAVE_DER:      "{",
        LLAVE_IZQ:      "}",
        IGUAL:          "=",
        IF:             "if",
        WHILE:          "while",
        RETURN:         "return",
        ELSE:           "else",
        PESOS:          "$",
    }