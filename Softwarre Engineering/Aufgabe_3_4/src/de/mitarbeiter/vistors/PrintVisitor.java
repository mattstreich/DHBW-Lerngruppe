package de.mitarbeiter.vistors;

import de.mitarbeiter.GehaltsEmpfaenger;
import de.mitarbeiter.LohnEmpfaenger;


public class PrintVisitor extends AbstractMitarbeiterVisitor{
	
	@Override
	public void vistit(GehaltsEmpfaenger gehaltsEmpfaenger) {
		System.out.println(gehaltsEmpfaenger);
		
	}

	@Override
	public void vistit(LohnEmpfaenger lohnEmpfaenger) {
		System.out.println(lohnEmpfaenger);
		
	}
}
