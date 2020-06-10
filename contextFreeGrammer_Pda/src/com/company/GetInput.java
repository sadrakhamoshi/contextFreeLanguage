package com.company;

import java.awt.font.GraphicAttribute;
import java.util.ArrayList;
import java.util.Scanner;

public class GetInput {

    public static void setGrammarFromInput(ContextFreeGrammar grammar) {
        Scanner scanner = new Scanner(System.in);
        Scanner scanner1 = new Scanner(System.in);
        grammar.setVariableNum(scanner.nextInt());
        boolean getInput = true;
        for (int i = 0; i < grammar.getVariableNum(); i++) {
            String input = scanner1.nextLine();
            String splitedByFlash[] = input.split("->");
            String variable = splitedByFlash[0];
            String transition = splitedByFlash[1];
            //get variable
            String current = "";
            if (variable.length() != 0) {
                String[] tmp = variable.split("<|>|\\s+");
                for (String str :
                        tmp) {
                    if (str.length() != 0) {
                        current = str;

                        if (current.equals("START"))
                            grammar.initialize = current;

                        if (!grammar.transitions.containsKey(str)) {
                            grammar.transitions.put(str, new ArrayList<>());
                        }
                    }
                }

            }
            //transitions
            String[] eachTrans = transition.split("\\|");

            ComputTransitions(current, grammar, eachTrans);
        }
    }

    private static void ComputTransitions(String key, ContextFreeGrammar grammar, String[] eachTrans) {
        for (int i = 0; i < eachTrans.length; i++) {
            //has variable
            if (eachTrans[i].contains("<")) {

                Rules rules = new Rules(eachTrans[i]);

                String[] splited = eachTrans[i].split("<|>");

                for (int j = 0; j < splited.length; j++) {
                    if (splited[j].length() != 0) {
                        //space
                        if (splited[j].equals(" ")) {
                            Pair pair = new Pair(" ", Rules.SPACE);
                            rules.setPairs(pair);
                        }
                        //is terminal
                        else if (Character.isLowerCase(splited[j].charAt(0))) {
                            Pair pair = new Pair(splited[j], Rules.TERMINAL);
                            rules.setPairs(pair);
                        }
                        //is variable
                        else {
                            Pair pair = new Pair(splited[j], Rules.VARIABLE);
                            rules.setPairs(pair);
                        }
                    }
                }
                grammar.transitions.get(key).add(rules);
            }
            //don't have variable
            else {
                Rules rules = new Rules(eachTrans[i]);
                //space
                if (eachTrans[i].equals(" ")) {
                    Pair pair = new Pair(" ", Rules.SPACE);
                    rules.setPairs(pair);
                } else {
                    rules.setPairs(new Pair(eachTrans[i], Rules.TERMINAL));
                }
                grammar.transitions.get(key).add(rules);
            }
        }
    }
}
