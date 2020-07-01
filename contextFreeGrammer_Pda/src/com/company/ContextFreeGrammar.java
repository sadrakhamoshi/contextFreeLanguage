package com.company;

import jdk.jshell.spi.ExecutionControl;

import java.util.ArrayList;
import java.util.Hashtable;
import java.util.List;

public class ContextFreeGrammar {
    private boolean isChomskyForm;
    private boolean isDeleteTrash;
    private boolean isGreibachNormalForm;

    public String initialize;
    private Integer variableNum;
    private List<String> terminals;
    public Hashtable<String, List<Rules>> transitions;

    public ContextFreeGrammar() {
        transitions = new Hashtable<>();
    }

    public void setTerminals(String terminals) {
        this.terminals.add(terminals);
    }

    public List<String> getTerminals() {
        return terminals;
    }

    public Integer getVariableNum() {
        return variableNum;
    }

    public void setVariableNum(Integer variableNum) {
        this.variableNum = variableNum;
    }

    public void setChomskyForm(boolean chomskyForm) {
        isChomskyForm = chomskyForm;
    }

    public boolean isChomskyForm() {
        return this.isChomskyForm;
    }

    public void setDeleteTrash(boolean deleteTrash) {
        isDeleteTrash = deleteTrash;
    }

    public boolean isDeleteTrash() {
        return isDeleteTrash;
    }

    public void setGreibachNormalForm(boolean greibachNormalForm) {
        isGreibachNormalForm = greibachNormalForm;
    }

    public boolean isGreibachNormalForm() {
        return isGreibachNormalForm;
    }

    //method deleteTrash is here


    //method isGeneratedByGrammar

    public boolean isGeneratedByGrammar(String input, ContextFreeGrammar grammar) {

        ChomskyForm c = new ChomskyForm();
        c.isChomskyNormalForm(grammar);
        if (!c.isChomskyForm) {
            String t = c.convertToChomsky(grammar);
        }

        Boolean result = CYK_Algoorithm(input, grammar);
        return result;
    }

    private Boolean CYK_Algoorithm(String input, ContextFreeGrammar grammar) {
        String[] inputs = input.split(":");
        Integer length = inputs.length;

        List<String>[][] table = new List[length][length];


        grammar.transitions.forEach((key, rules) -> {

            for (int i = 0; i < length; i++) {
                String tmp = inputs[i];
                for (int j = 0; j < rules.size(); j++) {
                    if (rules.get(j).name.contains(tmp)) {
                        if (table[0][i] == null)
                            table[0][i] = new ArrayList<>();
                        if (!table[0][i].contains(key))
                            table[0][i].add(key);
                        break;
                    }
                }
            }
        });


        for (int row = 1; row < length; row++) {

            for (int column = 0; column < length - row; column++) {

                int k = column;
                for (int i = 0; i < row - 1; i++) {
                    if (table[i][column].size() == 0 || table[row - 1 - i][column + 1 + i].size() == 0) {
                        continue;
                    } else {
                        for (int j = 0; j < table[i][column].size(); j++) {
                            for (int l = 0; l < table[row - i - 1][column + i + 1].size(); l++) {
                                String tmp = "<" + table[i][column].get(j) + ">" + "<" + table[row - i - 1][column + i + 1].get(l) + ">";

                                int finalColumn = column;
                                int finalRow = row;

                                grammar.transitions.forEach((key, rules) -> {

                                    for (int m = 0; m < rules.size(); m++) {
                                        if (rules.get(m).name.contains(tmp)) {
                                            if (table[finalRow][finalColumn] == null)
                                                table[finalRow][finalColumn] = new ArrayList<>();
                                            table[finalRow][finalColumn].add(key);
                                            break;
                                        }
                                    }
                                });
                            }
                        }
                    }
                }
            }
        }
        for (int i = 0; i < table[0][length - 1].size(); i++) {
            if (table[0][length - 1].get(i).contains(grammar.initialize))
                return true;
        }
        return false;
    }

}
//    int k = j;
//                    for (int i = 0; i < row - 1; i++) {
//
//        if (table[i][k].size() == 0 || table[j - i + 1][column + i + 1].size() == 0)
//        }
//for (int j = column; j < length - 1 - row; j++) {
//
//        for (int i = 0; i < row - 1; i++) {
//        if(table[i][j].size()==0||table[row-1-i][j+i].size()==0)
//        }
//        }