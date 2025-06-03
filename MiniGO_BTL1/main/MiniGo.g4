grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language = Python3;
}

program: 'votien'+ EOF;

// ! ---------------- LEXER DEADLINE PASS 13 TEST CASE 23:59 16/1 ----------------------- */

//TODO Keywords 3.3.2 pdf
IF: 'if';

//TODO Operators 3.3.3 pdf
ADD: '+';

//TODO Separators 3.3.4 pdf
LPAREN: '(';

//TODO Identifiers 3.3.1 pdf
ID: [a-zA-Z_];

//TODO Literals 3.3.5 pdf
INT_LIT: [0-9];

//TODO skip 3.1 and 3.2 pdf
WS: [ \t\f\r\n]+ -> skip; // skip spaces, tabs 

//TODO ERROR pdf BTL1 + lexererr.py
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING:
	'U' {
    raise UncloseString(self.text[1:-2])
};
ILLEGAL_ESCAPE:
	'I' {
    raise IllegalEscape(self.text[1:])
};

//! ---------------- LEXER ----------------------- */