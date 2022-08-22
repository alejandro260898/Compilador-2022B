class ConstantesAnalizadorexico:
    NOM_IDENTIDICADORES = "ID´S"
    NOM_NUM_REALES = "REALES"
    NOM_NUM_ENTEROS = "ENTEROS"
    NOM_ERRORES = "ERRORES"
    ERROR = -1
    IDENTIFICADOR = 0
    ENTERO = 1
    REAL = 2
    CADENA = 3
    TIPO_DATO = 4 # void, float, int
    OP_SUMA = 5 # +, -
    OP_MULTIPLICACION = 6 # *, /
    OP_RELACIONAL = 7 # <, <=, >, >=
    OP_OR = 8 # ||
    OP_AND = 9 # &&
    OP_NOT = 10 # !
    OP_IGUALDAD = 11 # ==, !=
    SIGNO_PUNTO_COMA = 12
    SIGNO_COMA = 13
    SIGNO_PARRENTESIS_INICIO = 14
    SIGNO_PARRENTESIS_FIN = 15
    SIGNO_LLAVES_INICIO = 16
    SIGNO_LLAVES_FIN = 17
    SIGNO_IGUAL = 18
    IF = 19
    WHILE = 20
    RETURN = 21
    ELSE = 22
    SIGNO_PESOS = 23
    TOKENS = {
        IDENTIFICADOR: "ID",
        ENTERO: "Entero",
        REAL: "Real",
        CADENA: "Cadena",
        TIPO_DATO: "Tipo",
        OP_SUMA: "OpSuma",
        OP_MULTIPLICACION: "OpMul",
        OP_RELACIONAL: "OpRelac",
        OP_OR: "OpOR",
        OP_AND: "OpAND",
        OP_NOT: "OpNOT",
        OP_IGUALDAD: "OpIgualdad",
        SIGNO_PUNTO_COMA: ";",
        SIGNO_COMA: ",",
        SIGNO_PARRENTESIS_INICIO: "(",
        SIGNO_PARRENTESIS_FIN: ")",
        SIGNO_LLAVES_INICIO: "{",
        SIGNO_LLAVES_FIN: "}",
        SIGNO_IGUAL: "=",
        IF: "if",
        WHILE: "while",
        RETURN: "return",
        ELSE: "else",
        SIGNO_PESOS: "$"
    }