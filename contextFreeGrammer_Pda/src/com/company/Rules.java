package com.company;

import java.util.ArrayList;
import java.util.List;

public class Rules {

    public static final int TERMINAL = 0;
    public static final int VARIABLE = 1;
    public static final int SPACE = 2;

    public String name;
    public List<Pair> pairs;

    public void setPairs(Pair pair) {
        pairs.add(pair);
    }

    public Rules(String n) {
        pairs = new ArrayList<>();
        name = n;
    }
}

class Pair {
    public Integer type;
    public String member;

    public Pair(String str, Integer typee) {
        type = typee;
        member = str;
    }
}
