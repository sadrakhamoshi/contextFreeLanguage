package com.company;

import java.util.Scanner;

public class GetInput {

    public static void setGrammarFromInput(ContextFreeGrammar grammar) {
        Scanner scanner = new Scanner(System.in);
        Scanner scanner1 = new Scanner(System.in);
        grammar.setVariableNum(scanner.nextInt());
        boolean getInput = true;
        for (int i = 0; i < grammar.getVariableNum(); i++) {
            String[] tmp = scanner1.nextLine().split("->");
            String var = tmp[0];
            grammar.initialize = var;
            if (!grammar.transitions.containsKey(var)) {
                grammar.transitions.put(var, new Variable(var));
            }

            String[] transition=tmp[1].split("[\\|\\s+]");

            for (int j = 0; j < transition.length; j++) {
                if(transition[j].length()!=0){
                    if(!transition[j].contains("<")){
                        grammar.setTerminals(transition[i]);
                        grammar.transitions.get(var).setTerminals(transition[j]);
                    }
                    
                }
            }

        }
    }
}
