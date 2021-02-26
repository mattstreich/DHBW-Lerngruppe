package de.mitarbeiter.vistors;

import de.mitarbeiter.GehaltsEmpfaenger;
import de.mitarbeiter.LohnEmpfaenger;


public class StatistikVisitor implements MitarbeiterVisitor{

    //Erstellen der Counter für die Mitarbeiter anzahl

    private int anzahlGehaltsEmpfaenger = 0;
    private int anzahlLohnEmpfaenger = 0;

    //zählt jeweiligen Counter um 1 hoch
	@Override
	public void vistit(GehaltsEmpfaenger gehaltsEmpfaenger) {
		anzahlGehaltsEmpfaenger++;
		
	}

	@Override
	public void vistit(LohnEmpfaenger lohnEmpfaenger) {
		anzahlLohnEmpfaenger++;
	}

    //Überschreibt die ToString Methode, um gewüschte Informationen auszugeben
    @Override
    public String toString() {
        return "{" +
            " Anzahl Gehaltsempfaenger='" + anzahlGehaltsEmpfaenger + "'" +
            ", Anzahl Lohnempfaenger='" + anzahlLohnEmpfaenger + "'" +
            ", Anzahl Gesamt='" + (anzahlLohnEmpfaenger + anzahlGehaltsEmpfaenger) + "'" +
            "}";
    }

    //Am Ende des iterate werden die Counter ausgegeben
    @Override
    public void atEnd(){
        System.out.println(this);
    }
}