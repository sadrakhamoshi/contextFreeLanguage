package com.company;

import javax.xml.namespace.QName;
import java.util.Iterator;

public class DeleteTrash {

    public boolean nullTrash;
    public boolean unitTrash;
    public boolean uselessTrash;


    public void checkForNullTrash(ContextFreeGrammar grammar) {
        grammar.transitions.forEach((key, value) -> {
            for (int i = 0; i < value.size(); i++) {
                if (value.get(i).name.contains("lamda")) {
                    nullTrash = true;
                    DeleteLambda(grammar, key, i);
                }
            }
        });
    }

    private void DeleteLambda(ContextFreeGrammar grammar, String key, int idx) {
        grammar.transitions.get(key).remove(idx);
        grammar.transitions.forEach((k, v) -> {
            //through the one variable
            Integer size = v.size();
            for (int i = 0; i < size; i++) {

                if (v.get(i).name.contains(key)) {
                    //key has only lambda transition
                    if (grammar.transitions.get(key).size() == 0) {
                        for (int j = 0; j < v.get(i).pairs.size(); j++) {
                            if (v.get(i).pairs.get(j).member.equals(key)) {
                                v.get(i).pairs.remove(j);
                                v.get(i).name=v.get(i).name.replace("<" + key + ">", "");
                            }
                        }
                    } else {
                        Rules rules = new Rules(v.get(i).name.replace("<" + key + ">", ""));
                        for (Pair p :
                                v.get(i).pairs) {
                            if (!p.member.equals(key)) {
                                Pair tmp = new Pair(p.member, p.type);
                                rules.pairs.add(tmp);
                            }
                        }
                        v.add(rules);
                    }
                }
            }
        });
    }

    public void checkForUnitTrash(ContextFreeGrammar grammar) {

    }

    public void checkForUselessTrash(ContextFreeGrammar grammar) {

    }
}
