from Compilador.Interfaces.TipoSimbolo import TipoSimbolo

class Reducciones:
    R0  = 'r0'
    R1  = -1 
    R2  = -2
    R3  = -3
    R4  = -4
    R5  = -5
    R6  = -6
    R7  = -7
    R8  = -8
    R9  = -9
    R10 = -10
    R11 = -11
    R12 = -12
    R13 = -13
    R14 = -14 
    R15 = -15
    R16 = -16
    R17 = -17
    R18 = -18
    R19 = -19
    R20 = -20
    R21 = -21
    R22 = -22
    R23 = -23
    R24 = -24
    R25 = -25
    R26 = -26
    R27 = -27
    R28 = -28
    R29 = -29
    R30 = -30
    R31 = -31
    R32 = -32
    R33 = -33
    R34 = -34
    R35 = -35
    R36 = -36
    R37 = -37
    R38 = -38
    R39 = -39 
    R40 = -40 
    R41 = -41
    R42 = -42
    R43 = -43
    R44 = -44
    R45 = -45
    R46 = -46
    R47 = -47
    R48 = -48
    R49 = -49
    R50 = -50
    R51 = -51
    R52 = -52
    
    REDUCCIONES = {
        R1:  "<programa>",
        R2:  "<Definiciones>",
        R3:  "<Definiciones>",
        R4:  "<Definicion>",
        R5:  "<Definicion>",
        R6:  "<DefVar>",
        R7:  "<ListaVar>",
        R8:  "<ListaVar>",
        R9:  "<DefFunc>",
        R10: "<Parametros>",
        R11: "<Parametros>",
        R12: "<ListaParam>",
        R13: "<ListaParam>",
        R14: "<BloqFunc>",
        R15: "<DefLocales>",
        R16: "<DefLocales>",
        R17: "<DefLocal>",
        R18: "<DefLocal>",
        R19: "<Sentencias>",
        R20: "<Sentencias>",
        R21: "<Sentencia>",
        R22: "<Sentencia>",
        R23: "<Sentencia>",
        R24: "<Sentencia>",
        R25: "<Sentencia>",
        R26: "<Otro>",
        R27: "<Otro>",
        R28: "<Bloque>",
        R29: "<ValorRegresa>",
        R30: "<ValorRegresa>",
        R31: "<Argumentos>",
        R32: "<Argumentos>",
        R33: "<ListaArgumentos>",
        R34: "<ListaArgumentos>",
        R35: "<Termino>",
        R36: "<Termino>",
        R37: "<Termino>",
        R38: "<Termino>",
        R39: "<Termino>",
        R40: "<LlamadaFunc>",
        R41: "<SentenciaBloque>",
        R42: "<SentenciaBloque>",
        R43: "<Expresion>",
        R44: "<Expresion>",
        R45: "<Expresion>",
        R46: "<Expresion>",
        R47: "<Expresion>",
        R48: "<Expresion>",
        R49: "<Expresion>",
        R50: "<Expresion>",
        R51: "<Expresion>",
        R52: "<Expresion>",
    }
    
    POPS = {
        R1:  1,
        R2:  0,
        R3:  2,
        R4:  1,
        R5:  1,
        R6:  4,
        R7:  0,
        R8:  3, 
        R9:  6,
        R10: 0, 
        R11: 3, 
        R12: 0,
        R13: 4,
        R14: 3, 
        R15: 0,
        R16: 2,
        R17: 1,
        R18: 1,
        R19: 0,
        R20: 2,
        R21: 4, 
        R22: 6,
        R23: 5,
        R24: 3,
        R25: 2,
        R26: 0,
        R27: 2,
        R28: 3,
        R29: 0,
        R30: 1,
        R31: 0,
        R32: 2,
        R33: 0,
        R34: 3,
        R35: 1,
        R36: 1, 
        R37: 1, 
        R38: 1, 
        R39: 1, 
        R40: 4,
        R41: 1,
        R42: 1,
        R43: 3,
        R44: 2,
        R45: 2, 
        R46: 3, 
        R47: 3, 
        R48: 3, 
        R49: 3, 
        R50: 3, 
        R51: 3, 
        R52: 1, 
    }
    
    REDUCCIONES_ID = {
        R1:  TipoSimbolo.PESOS + 1,
        R2:  TipoSimbolo.PESOS + 2,
        R3:  TipoSimbolo.PESOS + 2,
        R4:  TipoSimbolo.PESOS + 3,
        R5:  TipoSimbolo.PESOS + 3,
        R6:  TipoSimbolo.PESOS + 4,
        R7:  TipoSimbolo.PESOS + 5,
        R8:  TipoSimbolo.PESOS + 5,
        R9:  TipoSimbolo.PESOS + 6,
        R10: TipoSimbolo.PESOS + 7,
        R11: TipoSimbolo.PESOS + 7,
        R12: TipoSimbolo.PESOS + 8,
        R13: TipoSimbolo.PESOS + 8,
        R14: TipoSimbolo.PESOS + 9,
        R15: TipoSimbolo.PESOS + 10,
        R16: TipoSimbolo.PESOS + 10,
        R17: TipoSimbolo.PESOS + 11,
        R18: TipoSimbolo.PESOS + 11,
        R19: TipoSimbolo.PESOS + 12,
        R20: TipoSimbolo.PESOS + 12,
        R21: TipoSimbolo.PESOS + 13,
        R22: TipoSimbolo.PESOS + 13,
        R23: TipoSimbolo.PESOS + 13,
        R24: TipoSimbolo.PESOS + 13,
        R25: TipoSimbolo.PESOS + 13,
        R26: TipoSimbolo.PESOS + 14,
        R27: TipoSimbolo.PESOS + 14,
        R28: TipoSimbolo.PESOS + 15,
        R29: TipoSimbolo.PESOS + 16,
        R30: TipoSimbolo.PESOS + 16,
        R31: TipoSimbolo.PESOS + 17,
        R32: TipoSimbolo.PESOS + 17,
        R33: TipoSimbolo.PESOS + 18,
        R34: TipoSimbolo.PESOS + 18,
        R35: TipoSimbolo.PESOS + 19,
        R36: TipoSimbolo.PESOS + 19,
        R37: TipoSimbolo.PESOS + 19,
        R38: TipoSimbolo.PESOS + 19,
        R39: TipoSimbolo.PESOS + 19,
        R40: TipoSimbolo.PESOS + 20,
        R41: TipoSimbolo.PESOS + 21,
        R42: TipoSimbolo.PESOS + 21,
        R43: TipoSimbolo.PESOS + 22,
        R44: TipoSimbolo.PESOS + 22,
        R45: TipoSimbolo.PESOS + 22,
        R46: TipoSimbolo.PESOS + 22,
        R47: TipoSimbolo.PESOS + 22,
        R48: TipoSimbolo.PESOS + 22,
        R49: TipoSimbolo.PESOS + 22,
        R50: TipoSimbolo.PESOS + 22,
        R51: TipoSimbolo.PESOS + 22,
        R52: TipoSimbolo.PESOS + 22,
    }