binclude "",offset,length



; Input: A - First number
;        B - Second number
; Output: A - Sum of the two numbers

ADD_TWO_NUMBERS:
    MOV C, A    ; Move the first number to register C
    ADD B       ; Add the second number to register A
    MOV A, C    ; Move the sum back to register A
    RET         ; Return from the subroutine