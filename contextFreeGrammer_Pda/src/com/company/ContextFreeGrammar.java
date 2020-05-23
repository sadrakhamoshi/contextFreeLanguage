package com.company;

public class ContextFreeGrammar {
    private boolean isChomskyForm;
    private boolean isDeleteTrash;
    private boolean isGreibachNormalForm;

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
}
