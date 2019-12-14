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

	@Test
	public void should_correctly_set_the_conversion_map() {
		subject.convert_init();
		assertEquals(50, subject.convert['L' - 'A']);
	}

	private void assert_converts_roman_numeral_to_integer(String roman, int expectedNumber) {
		int answer = subject.run(roman);
		assertEquals(expectedNumber, answer);
	}

	@Test
	public void should_get_correct_digits_difficult() {
		String roman = "MCMXCIV";
		int number = 1994;
		assert_converts_roman_numeral_to_integer(roman, number);
	}

	@Test
	public void should_get_correct_digits_medium() {
		String roman = "LVIII";
		int number = 58;
		assert_converts_roman_numeral_to_integer(roman, number);
	}

	@Test
	public void should_get_correct_digits_simple() {
		String roman = "III";
		int number = 3;
		assert_converts_roman_numeral_to_integer(roman, number);
	}

	private void assert_collects_last_character(String roman, String shortened, char removed) {
		subject.roman = roman;
		subject.getAndRemoveLastChar();
		assertEquals(shortened, subject.roman);
		assertEquals(removed, subject.let);
	}

	@Test
	public void should_remove_and_collect_last_character() {
		String roman = "MCMXCIV";
		String shortened = "MCMXCI";
		char removed = 'V';
		assert_collects_last_character(roman, shortened, removed);
	}
}
