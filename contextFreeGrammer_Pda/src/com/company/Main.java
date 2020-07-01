package com.company;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        // write your code here
        ContextFreeGrammar grammar = new ContextFreeGrammar();
        GetInput.setGrammarFromInput(grammar);

        Boolean result = grammar.isGeneratedByGrammar("b:a:a:b:a", grammar);

//        ChomskyForm chomskyForm=new ChomskyForm();
//
//        chomskyForm.isChomskyNormalForm(grammar);
//        chomskyForm.condition();
//        if(!chomskyForm.isChomskyForm)
//            chomskyForm.convertToChomsky(grammar);
//
//        grammar.transitions.forEach((k, rules) -> {
//            System.out.print(k + " -> ");
//            for (var rule : rules) {
//                for (var p : rule.pairs) {
//                    if (p.type == Rules.VARIABLE)
//                        System.out.print("<" + p.member + ">");
//                    else
//                        System.out.print(p.member);
//                }
//                System.out.print(" | ");
//            }
//            System.out.print("\n");
//        });
    }
}
