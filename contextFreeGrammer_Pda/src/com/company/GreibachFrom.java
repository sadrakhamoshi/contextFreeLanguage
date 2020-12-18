package com.company;

import java.util.Iterator;
import java.util.List;
import java.util.Set;
import java.util.concurrent.atomic.AtomicReference;

public class GreibachFrom extends ContextFreeGrammar {


    public void convertToGreibach(ContextFreeGrammar grammar) {
        if (!grammar.isChomskyForm()) {
            ChomskyForm chomskyForm = new ChomskyForm();
            chomskyForm.convertToChomsky(grammar);
        }
        Boolean result = isGreibach(grammar);
    }

    public Boolean isGreibach(ContextFreeGrammar grammar) {

        Iterator<List<Rules>> rules=grammar.transitions.values().iterator();

        while (rules.hasNext()){
            List<Rules> rule=rules.next();
            for (int i = 0; i < rule.size(); i++) {
                if(rule.get(i).pairs.get(0).type!=Rules.TERMINAL){
                    return false;
                }
                for (int j = 1; j < rule.get(i).pairs.size(); j++) {
                    if(rule.get(i).pairs.get(j).type!=Rules.VARIABLE)
                        return false;
                }
            }
        }
        return true;
    }
}
