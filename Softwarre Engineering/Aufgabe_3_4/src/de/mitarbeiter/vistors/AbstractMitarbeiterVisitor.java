package de.mitarbeiter.vistors;

import de.mitarbeiter.GehaltsEmpfaenger;
import de.mitarbeiter.LohnEmpfaenger;


public abstract class AbstractMitarbeiterVisitor implements MitarbeiterVisitor{

	//Der Abstrakte Visitor hat leere Methoden, damit nicht nichtbenutze Methoden bei anderen Listeners zu Fehler führen
	@Override
	public void vistit(GehaltsEmpfaenger gehaltsEmpfaenger) {
		// Ok

	}

	@Override
	public void vistit(LohnEmpfaenger lohnEmpfaenger) {
		// Ok

	}
	//Diese Methode soll am Ende des iterates ausgeführt werden (nach Durchlauf aller Mitarbeiter)
	@Override
	public void atEnd(){
		//Ok
	}

}
