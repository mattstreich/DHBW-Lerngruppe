package de.mitarbeiter;

import de.mitarbeiter.vistors.MitarbeiterVisitor;

public class LohnEmpfaenger extends AbstractMitarbeiter {
	
	private double arbeitszeit = 36 * 4;
	private double stundenlohn = 12.5;

	public LohnEmpfaenger(String name) {
		super(name);
		// TODO Auto-generated constructor stub
	}

	public double getArbeitszeit() {
		return arbeitszeit;
	}

	public void setArbeitszeit(double arbeitszeit) {
		this.arbeitszeit = arbeitszeit;
	}

	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		builder.append("LohnEmpfae"
				+ "nger [arbeitszeit=");
		builder.append(arbeitszeit);
		builder.append(", stundenlohn=");
		builder.append(stundenlohn);
		builder.append(", Name=");
		builder.append(getName());
		builder.append("]");
		return builder.toString();
	}

	public double getStundenlohn() {
		return stundenlohn;
	}

	public void setStundenlohn(double stundenlohn) {
		this.stundenlohn = stundenlohn;
	}

	@Override
	public void accept(MitarbeiterVisitor visitor) {
		visitor.vistit(this);
		
	}
	
}
