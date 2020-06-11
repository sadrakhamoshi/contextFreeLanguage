package com.company;

import java.util.ArrayList;
import java.util.List;

public class Variable {
    private String name;
    private List<String> terminals;
    private List<Variable> variables;

    public Variable(String name) {
        this.name = name;
    }

    public void setVariables(Variable variables) {
        if (this.variables == null)
            this.variables = new ArrayList<>();
        this.variables.add(variables);
    }

    public List<Variable> getVariables() {
        return variables;
    }

    public List<String> getTerminals() {
        return terminals;
    }

    public void setTerminals(String terminals) {
        if (this.terminals == null)
            this.terminals = new ArrayList<>();
        this.terminals.add(terminals);
    }

    public String getName() {
        return name;
    }
}
