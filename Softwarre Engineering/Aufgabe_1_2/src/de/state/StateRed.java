package de.state;

public class StateRed extends AbstractStateOn{
    //Aufrufen des Konstruktors der Oberklasse (AbstractStateOn)
	public StateRed(TrafficLight trafficLight) {
		super(trafficLight);	
	}
    //Ausgabe der akutellen Ampelfarbe/-zustand
	@Override
	public void getActualColor() {
		System.out.println("Die Ampel ist Rot.");
	}
    //Wechseln auf den nächsten Ampelzustand (Grün)
	@Override
	public void nextColor() {
		getTrafficLight().current = getTrafficLight().stateGreen;
	}
}
