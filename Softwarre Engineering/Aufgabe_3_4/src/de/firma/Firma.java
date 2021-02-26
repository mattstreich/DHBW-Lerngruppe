package de.firma;

import java.util.ArrayList;
import java.util.List;

import de.mitarbeiter.AbstractMitarbeiter;
import de.mitarbeiter.events.MitarbeiterAnzahlHatSichVeraendertListener;
import de.mitarbeiter.vistors.MitarbeiterVisitor;

public class Firma {
	
	private List<AbstractMitarbeiter> mitarbeiters = new ArrayList<>();
	//Erstellt eine Liste, in der die Listener gespeichert werden
	private List<MitarbeiterAnzahlHatSichVeraendertListener> listeners = new ArrayList<>();
	
	//Methode zum Hinzufügen eines Listeners zur Liste
	public boolean addAnzahlVerändertListerner(MitarbeiterAnzahlHatSichVeraendertListener anzahlVerändertListerner) {
		return listeners.add(anzahlVerändertListerner);
	}
	//Methode zum Löschen eines Listeners zur Liste
	public boolean removeAnzahlVerändertListerner(MitarbeiterAnzahlHatSichVeraendertListener anzahlVerändertListerner) {
		return listeners.remove(anzahlVerändertListerner);
	}
	//Methode zum Feuern jedes Listeners der Liste
	private void fireAnzahlVerändertListerner() {
		for (MitarbeiterAnzahlHatSichVeraendertListener listener : listeners) {
			listener.AnzahlVeraendert(this);
		}
	}

	//Feuert bei einer Veränderung der Mitarbeiteranzahl (Hinzufügen oder Löschen) den Listener
	public boolean add(AbstractMitarbeiter mitarbeiter) {
		boolean finished = mitarbeiters.add(mitarbeiter);
		fireAnzahlVerändertListerner();
		return finished;
	}

	public boolean remove(AbstractMitarbeiter mitarbeiter) {
		boolean finished = mitarbeiters.remove(mitarbeiter);
		fireAnzahlVerändertListerner();
		return finished;
	}
	
//	public void print() {
//		for (AbstractMitarbeiter mitarbeiter : mitarbeiters) {
//			System.out.println(mitarbeiter);
//		}
//	}
	
	public void iterate(MitarbeiterVisitor visitor) {
		for (AbstractMitarbeiter mitarbeiter : mitarbeiters) {
			mitarbeiter.accept(visitor);
		}
		//ruft am Ende der Interate Methode die atEnd Methode der Visitor auf (z.B.: Mitarbeiteranzahl ausgeben)
		visitor.atEnd();
	}

}
