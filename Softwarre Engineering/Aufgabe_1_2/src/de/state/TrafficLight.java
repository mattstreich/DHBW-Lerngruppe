package de.state;

public class TrafficLight {
	//Erstellen ein unveränderliches Objekt jedes nötigen Status
	protected final State stateGreen = new StateGreen(this);
	protected final State stateRed = new StateRed(this);
    protected final State stateOff = new StateOff(this);

    //Variable current State erstellen, startet Rot (protected = im package verfügbar)
	protected State current = stateRed;
	
	//Methoden rufen die entsprechenden Methoden der State Klassen auf
	public void getActualColor() {
		current.getActualColor();
	}
    public void nextColor(){
        current.nextColor();
    }
    public void switchOff(){
        current.switchOff();
    }
    public void switchOn(){
        current.switchOn();
    }
}