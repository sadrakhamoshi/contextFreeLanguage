package com.company;

import javax.xml.namespace.QName;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class DeleteTrash {

    public boolean nullTrash;
    public boolean unitTrash;
    public boolean uselessTrash;

    public DeleteTrash() {
        nullTrash = unitTrash = uselessTrash = false;
    }


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
                                v.get(i).name = v.get(i).name.replace("<" + key + ">", "");
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

        grammar.transitions.forEach((key, rules) -> {

            Integer size = rules.size();
            for (int i = 0; i < rules.size(); i++) {

                if (rules.get(i).pairs.size() == 1) {
                    if (rules.get(i).pairs.get(0).type == Rules.VARIABLE) {
                        unitTrash = true;
                        DeleteUnitTrash(grammar, key, i, rules.get(i).pairs.get(0).member);
                        i--;
                    }
                }
            }
        });
    }

    private void DeleteUnitTrash(ContextFreeGrammar grammar, String key, int idx, String unitName) {
        grammar.transitions.get(key).remove(idx);
        grammar.transitions.forEach((k, rules) -> {

            Integer size = rules.size();
            //each rule
            for (int i = 0; i < rules.size(); i++) {
                if (rules.get(i).name.contains(key)) {

                    if (grammar.transitions.get(key).size() != 0) {

                        if (rules.get(i).pairs.size() == 1 && k.equals(unitName)) {
                            //do nothing
                        } else {
                            Rules rules1 = new Rules(rules.get(i).name.replace(key, unitName));
                            for (Pair p :
                                    rules.get(i).pairs) {
                                //not unit
                                if (!p.member.equals(key)) {
                                    rules1.pairs.add(new Pair(p.member, p.type));
                                }
                                //unit parameter
                                else {
                                    rules1.pairs.add(new Pair(unitName, p.type));
                                }
                            }
                            rules.add(rules1);
                        }
                    }
                    //only has one transition
                    else {
                        if (rules.get(i).pairs.size() == 1 && k.equals(unitName)) {
                            rules.remove(i);
                        } else {
                            rules.get(i).name = rules.get(i).name.replace(key, unitName);
                            for (Pair p :
                                    rules.get(i).pairs) {
                                if (p.member.equals(key)) {
                                    p.member = unitName;
                                }
                            }
                        }
                    }
                }
            }
        });
    }

    public void checkForUselessTrash(ContextFreeGrammar grammar) {
        List<String> useFulVariables = new ArrayList<>();
        useFulVariables.addAll(stepOneForFindUseFulVariables(grammar));  // step1
        useFulVariables = stepTwoForFindUseFulVariables(grammar, useFulVariables);  // step2
        removeUseLessVariablesAndRules(grammar, useFulVariables);
        removeNonReachableVariables(grammar);
    }

    private List<String> stepOneForFindUseFulVariables(ContextFreeGrammar grammar) {
        List<String> fullTerminalVariables = new ArrayList<>();
        grammar.transitions.forEach((k, v) -> {
            List<Rules> rules = grammar.transitions.get(k);
            for (int i = 0; i < rules.size(); i++) {
                Boolean isFullTerminal = true;
                for (int j = 0; j < rules.get(i).pairs.size(); j++) {
                    if (rules.get(i).pairs.get(j).type == Rules.VARIABLE)
                        isFullTerminal = false;
                }

                if (isFullTerminal == true) {
                    fullTerminalVariables.add(k);
                    break;
                }
            }
        });

        return fullTerminalVariables;
    }

    private List<String> stepTwoForFindUseFulVariables(ContextFreeGrammar grammar, List<String> usefulVariables) {
        Integer oldSize;
        do {
            oldSize = usefulVariables.size();
            // ?????????????
            grammar.transitions.forEach((k, v) -> {
                List<Rules> rules = grammar.transitions.get(k);

                if (!usefulVariables.contains(k)) {
                    for (int i = 0; i < rules.size(); i++) {
                        List<Pair> pairList = rules.get(i).pairs;

                        Boolean isOk = true;
                        for (Pair p :
                                pairList) {
                            if (p.type == Rules.VARIABLE) {
                                if (!usefulVariables.contains(p.member))
                                    isOk = false;
                            }
                        }
                        if (isOk) {
                            usefulVariables.add(k);
                            break;
                        }
                    }
                }
            });

        } while (oldSize != usefulVariables.size());

        return usefulVariables;
    }

    private void removeUseLessVariablesAndRules(ContextFreeGrammar grammar, List<String> useFulVariables) {
        List<String> variablesShouldBeRemoved = new ArrayList<>();
        grammar.transitions.forEach((k, rules) -> {
            List<Rules> rulesShouldBeRemoved = new ArrayList<>();

            if (!useFulVariables.contains(k))
                variablesShouldBeRemoved.add(k);
            else {
                for (int i = 0; i < rules.size(); i++) {
                    var rule = rules.get(i);
                    Boolean isOk = true;
                    for (int j = 0; j < rule.pairs.size(); j++) {
                        if (!useFulVariables.contains(rule.pairs.get(j).member)
                                && rule.pairs.get(j).type == Rules.VARIABLE) {
                            isOk = false;
                            break;
                        }
                    }
                    if (!isOk)
                        rulesShouldBeRemoved.add(rule);
                }

            }
            for (int i = 0; i < rulesShouldBeRemoved.size(); i++)
                rules.remove(rulesShouldBeRemoved.get(i));
        });

        for (int i = 0; i < variablesShouldBeRemoved.size(); i++)
            grammar.transitions.remove(variablesShouldBeRemoved.get(i));
    }

    private void removeNonReachableVariables(ContextFreeGrammar grammar) {
        List<String> reachableVariables = new ArrayList<>();
        reachableVariables.add(grammar.initialize);

        int oldSize;
        do {
            oldSize = reachableVariables.size();
            grammar.transitions.forEach((k, rules) -> {
                if (reachableVariables.contains(k)) {
                    for (Rules rule : rules) {
                        for (int j = 0; j < rule.pairs.size(); j++) {
                            if (rule.pairs.get(j).type == Rules.VARIABLE)
                                if (!reachableVariables.contains(rule.pairs.get(j).member))
                                    reachableVariables.add(rule.pairs.get(j).member);
                        }
                    }
                }
            });
        } while (oldSize != reachableVariables.size());

        List<String> shouldBeRemoved = new ArrayList<>();
        grammar.transitions.forEach((k, v) -> {
            if (!reachableVariables.contains(k))
                shouldBeRemoved.add(k);
        });


        for (var s : shouldBeRemoved) {
            grammar.transitions.remove(s);
        }

    }
}
