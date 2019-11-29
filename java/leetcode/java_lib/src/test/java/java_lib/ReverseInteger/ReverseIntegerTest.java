package java_lib.ReverseInteger;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import static org.junit.jupiter.api.Assertions.*;

public class ReverseIntegerTest {

    //    private TwoSum_HashTableTwoPass subject;
    private ReverseInteger subject;

    @BeforeEach
    public void setup() {
//        subject = new TwoSum_HashTableTwoPass();
        subject = new ReverseInteger();
    }

    private void assertReversesInteger(int forward, int reverse) {
        int ans = subject.run(forward);
        assertEquals(ans, reverse);
    }

    @Test
    public void should_reverse_with_negative() {
        int forward = -123;
        int reverse = -321;
        assertReversesInteger(forward, reverse);
    }

    @Test
    public void should_reverse_with_zero() {
        int forward = 120;
        int reverse = 21;
        assertReversesInteger(forward, reverse);
    }
}
