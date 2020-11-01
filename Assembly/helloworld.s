STD_OUTPUT_HANDLE equ -11
%define NULL    dword 0

    extern  _GetStdHandle@4
    extern  _WriteFile@20
    extern  _ExitProcess@4

    global _main

    section .text

_main:
    ; local variable
bytesWritten equ -4
    mov     ebp, esp
    sub     esp, 4

    ; hStdOut = GetstdHandle(STD_OUTPUT_HANDLE)
    push    STD_OUTPUT_HANDLE
    call    _GetStdHandle@4
    mov     ebx, eax

    ; WriteFile(hstdOut, message, length(message),
    ;           &bytesWritten, null);
    push    NULL
    lea     eax, [ebp + bytesWritten]
    push    eax
    push    (message_end - message)
    push    message
    push    ebx
    call    _WriteFile@20

    ; ExitProcess(0)
    push    0
    call    _ExitProcess@4

    ; never here
    hlt
message:
    db      'Hello, World', 10
message_end: