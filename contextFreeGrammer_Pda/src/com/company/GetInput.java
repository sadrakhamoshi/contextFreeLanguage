package com.company;

import java.util.Scanner;

public class GetInput {

    public static void setGrammarFromInput(ContextFreeGrammar grammar) {
        Scanner scanner = new Scanner(System.in);
        Scanner scanner1 = new Scanner(System.in);
        grammar.setVariableNum(scanner.nextInt());
        boolean getInput = true;
        for (int i = 0; i < grammar.getVariableNum(); i++) {
            String input=scanner1.nextLine();
            String splitedByFlash[]=input.split("->");
            String variable=splitedByFlash[0];
            String transition=splitedByFlash[1];


        }
    }
}
