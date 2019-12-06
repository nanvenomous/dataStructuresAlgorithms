package java_lib.IsPalindrome;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class IsPalindromeTest {
    private IsPalindrome subject;

    @BeforeEach
    public void setup() {
        subject = new IsPalindrome();
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
    public void should_determine_is_palindrome() {
        int num = 1234321;
        boolean isPal = true;
        assert_determines_palindrome(num, isPal);
    }

    @Test
    public void should_classify_negative_as_not_a_palindrome() {
        int num = -1234321;
        boolean isPal = false;
        assert_determines_palindrome(num, isPal);
    }
}
