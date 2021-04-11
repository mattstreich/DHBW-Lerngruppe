package de.tiere;

public class Schwein {
	
	private String name;
	private int gewicht;
	
	public Schwein() {
		this("nobody");
	}

	public Schwein(String name) {
		setGewicht(10);
		setName(name);
	}

	public String getName() {
		return name;
	}

	public final void setName(String name) {
		if(name == null || "elsa".equalsIgnoreCase(name)) throw new IllegalArgumentException("Ungültiger name");
		this.name = name;
	}

	public int getGewicht() {
		return gewicht;
	}

	private void setGewicht(int gewicht) {
		this.gewicht = gewicht;
	}
	
	public void fressen() {
		setGewicht(getGewicht() +1); 
	}

	@Override
	public String toString() {
		return "Schwein [name=" + name + ", gewicht=" + gewicht + "]";
	}
	

}
