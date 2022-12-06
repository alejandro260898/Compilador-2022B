; Galvan Ontiveros Francisco Alejandro 214090509
[BITS 64]

; sección de constantes
%define TAM_BYTE 1 
%define INICIO_ASCCI_NUM 48
%define TIPO_INT 1
%define SYS_EXIT 1
%define SYS_WRITE 4
%define INTERRUPT_KERNEL 80h
%define EXIT_SUCCESS 0

%macro printf 3
    mov eax, INICIO_ASCCI_NUM
    mov ebx, %3
    add eax, ebx
    mov [buffer_cad], eax
    mov byte [buffer_cad + TAM_BYTE], 10

    mov eax, SYS_WRITE
	mov ebx, 1
	mov ecx, %1
	mov edx, %2
	int INTERRUPT_KERNEL

    mov eax, SYS_WRITE
	mov ebx, 1
	mov ecx, buffer_cad
	mov edx, 2
	int INTERRUPT_KERNEL
%endmacro

; sección funciones
%macro suma 2
    xor eax, eax
    xor ebx, ebx

    mov eax, %1
    mov ebx, %2
    add eax, ebx
%endmacro

; sección de datos con valor definidos
SECTION .data
    print_1 db "c = "
    len_print_1 equ $-print_1

; sección de datos sin valor definidos
SECTION .bss
    buffer_cad resb 10
    c resd 1

; sección de definición de funciones
SECTION .text
    global main ; función principal main

main:
    push rbp ;guardar el puntero base
    
    suma 4, 2
    mov [c], eax

    printf print_1, len_print_1, [c]

    finPrograma:
    	mov	eax, SYS_EXIT
        mov	ebx, EXIT_SUCCESS
        int	INTERRUPT_KERNEL