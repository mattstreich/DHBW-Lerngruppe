package de.state;

public class AbstractStateOn extends AbstractState{
	//Aufrufen des Konstruktors der Oberklasse (AbstractState)
    public AbstractStateOn(TrafficLight trafficLight) {
		super(trafficLight);
		
	}
	/*Überschreiben der switchOff Methode, State Wechsel nach StateOff
	Implimentierung einer StateOn Klasse, von der spätere Klassen erben
	Damit die switchOff-Methode nicht redundant geschrieben werden muss*/
    @Override
	public void switchOff() {
		getTrafficLight().current = getTrafficLight().stateOff;
	}
    
}
