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

        boolean result;

        if (grammar.isChomskyForm) {
            result = DpCheck(input, grammar);
        } else {
            result = notDpCheck(input, grammar);
        }
        return result;
    }

    private boolean DpCheck(String input, ContextFreeGrammar grammar) {
        return false;
    }

    private boolean notDpCheck(String input, ContextFreeGrammar grammar) {
        for (int i = 0; i < input.length(); i++) {

        }
        return false;
    }
}
