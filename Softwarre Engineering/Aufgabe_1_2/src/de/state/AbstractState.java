package de.state;

public class AbstractState implements State {

    private final TrafficLight trafficLight;
    //Konstruktur, übergebenes TrafficLight Objekt wird in Variable gespeichert
	public AbstractState(TrafficLight trafficLight) {
		this.trafficLight = trafficLight;
	}
    //Gibt das trafficLight Objekt zurück
	public TrafficLight getTrafficLight() {
		return trafficLight;
	}
    //Exception Implementierung für jede Methode, damit spätere State Klasse nur die Methoden überschreiben müssen, welche sie brauchen
    @Override
	public void getActualColor() {
		throw new UnsupportedOperationException("Diese Funtion macht in diesem Status keinen Sinn!");
		
	}

	@Override
	public void nextColor() {
		throw new UnsupportedOperationException("Diese Funtion macht in diesem Status keinen Sinn!");
		
	}
    @Override
	public void switchOff() {
		throw new UnsupportedOperationException("Diese Funtion macht in diesem Status keinen Sinn!");
		
	}
    @Override
	public void switchOn() {
		throw new UnsupportedOperationException("Diese Funtion macht in diesem Status keinen Sinn!");
		
	}
}
