package de.state;

public class StateOff extends AbstractState{
    //Aufrufen des Konstruktors der Oberklasse (AbstractState)
    public StateOff(TrafficLight trafficLight) {
		super(trafficLight);
		
	}
    
    @Override
	public void switchOn() {
        //Aus Sicherheitsgründe starten wir die Ampel im Roten Zustand
		getTrafficLight().current = getTrafficLight().stateRed;
	}
}
