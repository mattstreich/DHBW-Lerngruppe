package de.tiere;

import static org.junit.Assert.assertTrue;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class SchweinTest {
	
	private Schwein objectUnderTest;
	
	@BeforeEach
	public void setup() {
		objectUnderTest = new Schwein();
	}

	@Test
	public void constructor_normal_returntrue() {
		assertEquals(10, objectUnderTest.getGewicht());
		assertEquals("nobody", objectUnderTest.getName());
	}
	
	@Test
	public void setName_overwriteParameterName_returntrue() {
		String name = "Matze";
		
		objectUnderTest.setName(name);
		
		assertEquals(name, objectUnderTest.getName());
	}
	
	@Test
	public void setName_overwriteParameterNameWithNull_throwExceptionByElsa() {
		String name = "elsa";
		String exceptionMessage = null;
		
		try{
			objectUnderTest.setName(name);
		}
		catch(IllegalArgumentException e){
			exceptionMessage = e.getMessage();
		}
		assertEquals(exceptionMessage, "Ungültiger name");
	}
	
	@Test
	public void setName_overwriteParameterNameWithElsa_throwExceptionByNull() {
		String name = null;
		String exceptionMessage = null;
		
		try{
			objectUnderTest.setName(name);
		}
		catch(IllegalArgumentException e){
			exceptionMessage = e.getMessage();
		}
		assertEquals(exceptionMessage, "Ungültiger name");
	}
	
	@Test
	public void fressen_overwriteParameter_trueByAdditionBy1() {
		int gewicht = objectUnderTest.getGewicht();
		
		objectUnderTest.fressen();
		
		assertTrue(objectUnderTest.getGewicht() == gewicht+1);
	}
	

}
