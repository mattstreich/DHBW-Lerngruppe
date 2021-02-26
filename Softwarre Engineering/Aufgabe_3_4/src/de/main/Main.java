package de.main;

import de.firma.Firma;
import de.mitarbeiter.GehaltsEmpfaenger;
import de.mitarbeiter.LohnEmpfaenger;
import de.mitarbeiter.vistors.PrintVisitor;
import de.mitarbeiter.vistors.StatistikVisitor;

public class Main {

	public static void main(String[] args) {	
		//Erstellen der Firma
		Firma firma = new Firma();
		//Firma werden 5 mitarbeiter hinzugefügt
		firma.add(new GehaltsEmpfaenger("Arnaudo"));
		firma.add(new GehaltsEmpfaenger("Engel"));
		firma.add(new GehaltsEmpfaenger("Streich"));
		firma.add(new LohnEmpfaenger("Reucher"));
		firma.add(new LohnEmpfaenger("Wiesemann"));
		//Daten der Mitarbeiter ausgegeben
		firma.iterate(new PrintVisitor());
		//Anzahl der Mitarbeiter Typen & Gesamt
		firma.iterate(new StatistikVisitor());

		/*Listener wird der Firma hinzugefügt, der immer bei der Änderung der Mitarbeiteranzahl feuert
		Die neuen Mitarbeiter Zahlen werden ausgegeben*/
		firma.addAnzahlVerändertListerner(e->firma.iterate(new StatistikVisitor()));

		firma.add(new GehaltsEmpfaenger("Geppert"));
		firma.add(new LohnEmpfaenger("Christen"));
	}

}
