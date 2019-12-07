package java_lib.RomanToInteger;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;

public class RomanToIntegerTest {
	private RomanToInteger subject;

	@BeforeEach
	public void setup() {
		subject = new RomanToInteger();
	}

	private void assert_converts_roman_numeral_to_integer(String roman, int expectedNumber) {
		int answer = subject.run(roman);
		assertEquals(expectedNumber, answer);
	}

	@Test
	public void should_get_correct_digits_to_reverse_odd() {
		String roman = "MCMXCIV";
		int number = 1994;
		assert_converts_roman_numeral_to_integer(roman, number);
	}
}
