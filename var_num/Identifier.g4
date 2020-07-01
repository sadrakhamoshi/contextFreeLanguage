grammar Identifier;

start
    :Var
    |Num
    ;

Var: Variable;
Num: Number;

fragment Variable: ([a-zA-Z_]+[0-9]*[a-zA-Z_]*)+;
fragment Number: ([+-]?[0-9]+([.][0-9]+)?) | (('(')[+-]?[0-9]+([.][0-9]+)?(')'));

Newline: '\n' -> skip;
