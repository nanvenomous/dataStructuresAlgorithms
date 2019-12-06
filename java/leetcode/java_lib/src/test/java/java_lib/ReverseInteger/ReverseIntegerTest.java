package java_lib.ReverseInteger;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class ReverseIntegerTest {
    private ReverseInteger subject;

    @BeforeEach
    public void setup() {
        subject = new ReverseInteger();
    }

    private void assertReversesInteger(int reverse, int forward) {
        int ans = subject.run(forward);
        assertEquals(ans, reverse);
    }

    @Test
    public void should_reverse() {
        int forward = 123;
        int reverse = 321;
        assertReversesInteger(reverse, forward);
    }

    @Test
    public void should_reverse_with_negative() {
        int forward = -123;
        int reverse = -321;
        assertReversesInteger(reverse, forward);
    }

    @Test
    public void should_reverse_with_zero() {
        int forward = 120;
        int reverse = 21;
        assertReversesInteger(reverse, forward);
    }

    @Test
    public void should_reverse_zero() {
        int forward = 0;
        int reverse = 0;
        assertReversesInteger(reverse, forward);
    }
}
