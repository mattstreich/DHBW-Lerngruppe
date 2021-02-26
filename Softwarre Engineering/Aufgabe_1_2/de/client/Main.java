package de.client;

import de.state.TrafficLight;

public class Main {
    public static void main(String[] args) {
        
        //Ampel wird erstellt, Anfangs State=Rot
		TrafficLight ampel = new TrafficLight();
        //Ausgeben der Farbe (Rot)
        ampel.getActualColor();

        //Wechsel des Zustandes (Rot->Grün)
        ampel.nextColor();
        //Ausgeben der Farbe (Grün)
        ampel.getActualColor();

        //Wechsel des Zustandes (Grün->Rot) und dann (Rot->Grün)
        ampel.nextColor();
        ampel.nextColor();

        ampel.getActualColor();
        //Wechsel in Off Zustand

        ampel.switchOff();
        //Off Zustand hat keine Farbe ->Exception
        //ampel.getActualColor();

        //Wechsel in ON Zustand (immer Rot)
        ampel.switchOn();
        ampel.getActualColor();
	}
}
