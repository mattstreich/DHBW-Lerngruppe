package de.state;

public class StateGreen extends AbstractStateOn{
    //Aufrufen des Konstruktors der Oberklasse (AbstractStateOn)
	public StateGreen(TrafficLight trafficLight) {
		super(trafficLight);
		
	}
    //Ausgabe der akutellen Ampelfarbe/-zustand
	@Override
	public void getActualColor() {
		System.out.println("Die Ampel ist Grün.");
	}
    //Wechseln auf den nächsten Ampelzustand (Rot)
	@Override
	public void nextColor() {
		getTrafficLight().current = getTrafficLight().stateRed;
	}
}
