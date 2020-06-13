package com.company;

public class ChomskyForm extends ContextFreeGrammar {
    public boolean isChomskyForm;

    public ChomskyForm() {
        this.isChomskyForm = false;
    }

    public void isChomskyNormalForm(ContextFreeGrammar grammar) {
        grammar.transitions.forEach((key, rules) -> {
            for (int i = 0; i < rules.size(); i++) {
                //transition with length more than 2
                if (rules.get(i).pairs.size() > 2) {
                    isChomskyForm = false;
                    return;
                }
                if (rules.get(i).pairs.size() == 1) {
                    if (rules.get(i).pairs.get(0).type == Rules.VARIABLE) {
                        isChomskyForm = false;
                        return;
                    }
                } else {
                    if (rules.get(i).pairs.get(0).type * rules.get(i).pairs.get(1).type == 0) {
                        isChomskyForm = false;
                        return;
                    }
                }
            }
        });
        isChomskyForm = true;
    }

    public String convertToChomsky(ContextFreeGrammar grammar) {
        if (this.isChomskyForm)
            return "already is chomsky normal form";
        else {
            
        }
    }
}
