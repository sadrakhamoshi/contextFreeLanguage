package com.company;

import java.util.ArrayList;
import java.util.Hashtable;
import java.util.List;

public class ChomskyForm extends ContextFreeGrammar {

    public boolean isChomskyForm;

    public void condition() {
        System.out.println(isChomskyForm + "");
    }

    public ChomskyForm() {
        this.isChomskyForm = true;
    }

    public void isChomskyNormalForm(ContextFreeGrammar grammar) {

        grammar.transitions.forEach((key, rules) -> {
            if (isChomskyForm) {
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
            }
        });
    }

    public String convertToChomsky(ContextFreeGrammar grammar) {
        if (this.isChomskyForm)
            return "already is chomsky normal form";
        else {
            checkStart(grammar, grammar.transitions.get("START"));

            Step1(grammar);
            Step2(grammar);
            return "successful";
        }
    }

    private void Step2(ContextFreeGrammar grammar) {
        int idx = 0;
        List<Hashtable<String, List<Rules>>> list = new ArrayList<>();
        grammar.transitions.forEach((name, rules) -> {
            for (int i = 0; i < rules.size(); i++) {
                Hashtable<String, List<Rules>> hashtable = new Hashtable<>();
                if (rules.get(i).pairs.size() > 2) {
                    LowerVariable(name, grammar, hashtable, rules, idx);
                    list.add(hashtable);
                    break;
                }
            }
        });
        for (int i = 0; i < list.size(); i++) {
            grammar.transitions.putAll(list.get(i));
        }
    }

    private void LowerVariable(String name, ContextFreeGrammar grammar, Hashtable<String, List<Rules>> hashtable, List<Rules> rules, int idx) {


        for (int i = 0; i < rules.size(); i++) {
            if (rules.get(i).pairs.size() > 2) {
                Rules tmp = rules.get(i);
                rules.remove(i);

                Rules rules1 = new Rules("<" + tmp.pairs.get(0).member + ">" + "<X" + idx + ">");
                rules1.pairs.add(tmp.pairs.get(0));
                rules1.pairs.add(new Pair("X" + idx, Rules.VARIABLE));
                rules.add(i, rules1);


                String[] tmp1 = new String[tmp.pairs.size() - 2];
                for (int j = 0; j < tmp1.length; j++) {
                    tmp1[j] = "X" + idx;
                    idx++;
                }

                //iterate through the pairs
                for (int j = 0; j < tmp.pairs.size() - 3; j++) {
                    hashtable.put(tmp1[j], new ArrayList<>());
                    Rules rules2 = new Rules("<" + tmp.pairs.get(j + 1).member + ">" + "<" + tmp1[j + 1] + ">");
                    rules2.pairs.add(new Pair(tmp.pairs.get(j + 1).member, Rules.VARIABLE));
                    rules2.pairs.add(new Pair(tmp1[j + 1], Rules.VARIABLE));
                    hashtable.get(tmp1[j]).add(rules2);
                }
                hashtable.put(tmp1[tmp1.length - 1], new ArrayList<>());
                Rules rules2 = new Rules("<" + tmp.pairs.get(tmp.pairs.size() - 2).member + ">" + "<" + tmp.pairs.get(tmp.pairs.size() - 1).member + ">");
                rules2.pairs.add(new Pair(tmp.pairs.get(tmp.pairs.size() - 2).member, Rules.VARIABLE));
                rules2.pairs.add(new Pair(tmp.pairs.get(tmp.pairs.size() - 1).member, Rules.VARIABLE));
                hashtable.get(tmp1[tmp1.length - 1]).add(rules2);
            }
        }
    }

    private Rules MakeNewTrans(String firstPair, Rules tmp) {

        Rules res = new Rules(tmp.name.replace("<" + firstPair + ">", ""));
        res.pairs.addAll(1, tmp.pairs);
        return res;
    }

    private void Step1(ContextFreeGrammar grammar) {

        Hashtable<String, List<Rules>> hashtable = new Hashtable<>();
        grammar.transitions.forEach((key, rules) -> {

            for (int i = 0; i < rules.size(); i++) {

                int firstTerminal = multiple(rules.get(i).pairs);
                //has terminal
                if (firstTerminal != -1) {
                    if (rules.get(i).pairs.size() > 1) {
                        addVarToTerminal(firstTerminal, hashtable, rules.get(i));
                    }
                }
                //don't have terminal
                else {
                    //do nothing
                }
            }

        });
        grammar.transitions.putAll(hashtable);
    }

    private void addVarToTerminal(int firstTerminal, Hashtable<String, List<Rules>> grammar, Rules rules) {
        for (int i = firstTerminal; i < rules.pairs.size(); i++) {
            if (rules.pairs.get(i).type == Rules.TERMINAL) {

                String lowerCase = rules.pairs.get(i).member;
                String upperCase = lowerCase.toUpperCase() + "0";

                rules.name = rules.name.replace(rules.pairs.get(i).member, "<" + upperCase + ">");
                rules.pairs.get(i).type = Rules.VARIABLE;
                rules.pairs.get(i).member = upperCase;
                if (!grammar.containsKey(upperCase))
                    grammar.put(upperCase, new ArrayList<Rules>());

                Rules rules1 = new Rules(lowerCase);
                rules1.pairs.add(new Pair(lowerCase, Rules.TERMINAL));
                grammar.get(upperCase).add(rules1);
            }
        }
    }

    private void checkStart(ContextFreeGrammar grammar, List<Rules> start) {
        for (int i = 0; i < start.size(); i++) {
            if (start.get(i).name.contains("START")) {
                grammar.transitions.put("S0", new ArrayList<>(start));
                break;
            }
        }
    }

    public int multiple(List<Pair> pairs) {
        int firstTerminal = -1;
        for (int i = 0; i < pairs.size(); i++) {
            if (pairs.get(i).type == Rules.TERMINAL) {
                firstTerminal = i;
                break;
            }
        }
        return firstTerminal;
    }
}
