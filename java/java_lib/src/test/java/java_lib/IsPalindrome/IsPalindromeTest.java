package java_lib.IsPalindrome;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;

public class IsPalindromeTest {
	private IsPalindrome subject;

	@BeforeEach
	public void setup() {
		subject = new IsPalindrome();
	}

	private void assert_determines_digit_number_and_eveness(int num, int numDigits, boolean eveness) {
		subject.forward = num;
		subject.digits_to_reverse();
		if (eveness) { assertTrue(subject.isEven);
		} else { assertFalse(subject.isEven);}
		assertEquals(numDigits, subject.numDigits);
	}

	@Test
	public void should_get_correct_digits_to_reverse_odd() {
		int num = 1234321;
		int numDigits = 3;
		boolean eveness = false;
		assert_determines_digit_number_and_eveness(num, numDigits, eveness);
	}

	@Test
	public void should_get_correct_digits_to_reverse_even() {
		int num = 123321;
		int numDigits = 3;
		boolean eveness = true;
		assert_determines_digit_number_and_eveness(num, numDigits, eveness);
	}

	private void assert_determines_palindrome(int num, boolean isPal) {
		boolean ans = subject.run(num);
		assertEquals(isPal, ans);
	}

	@Test
	public void should_determine_is_not_palindrome() {
		int num = 123456;
		boolean isPal = false;
		assert_determines_palindrome(num, isPal);
	}

	@Test
	public void should_determine_odd_is_palindrome() {
		int num = 1234321;
		boolean isPal = true;
		assert_determines_palindrome(num, isPal);
	}

	@Test
	public void should_determine_even_is_palindrome() {
		int num = 123321;
		boolean isPal = true;
		assert_determines_palindrome(num, isPal);
	}

	@Test
	public void should_classify_negative_as_not_a_palindrome() {
		int num = -1234321;
		boolean isPal = false;
		assert_determines_palindrome(num, isPal);
	}

	@Test
	public void should_classify_zero_as_a_palindrome() {
		int num = 0;
		boolean isPal = true;
		assert_determines_palindrome(num, isPal);
	}

	private void assertReversesInteger(int reverse, int forward) {
		subject.forward = forward;
		subject.partial_reverse();
		assertEquals(reverse, subject.reversed);
	}

	@Test
	public void should_reverse_part_even() {
		int forward = 999321;
		int reverse = 123;
		assertReversesInteger(reverse, forward);
	}

	@Test
	public void should_reverse_with_zero() {
		int forward = 9991027;
		int reverse = 720;
		assertReversesInteger(reverse, forward);
	}

	@Test
	public void should_reverse_zero() {
		int forward = 0;
		int reverse = 0;
		assertReversesInteger(reverse, forward);
	}
}
