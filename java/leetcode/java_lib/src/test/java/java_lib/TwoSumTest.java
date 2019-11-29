package java_lib;

import java.util.Arrays;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import static org.junit.jupiter.api.Assertions.*;


public class TwoSumTest {

    private TwoSum_HashTable subject;

    @BeforeEach
    public void setup() {
        subject = new TwoSum_HashTable();
    }

    @Test
    public void should_sum_positive_integers() {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] sln = {0, 1};
        int[] ans = subject.run(nums, target);
        assertEquals(Arrays.toString(ans), Arrays.toString(sln));
    }

    @Test
    public void should_sum_zeros_to_zero() {
        int[] nums = {0, 4, 3, 0};
        int target = 0;
        int[] sln = {0, 3};
        int[] ans = subject.run(nums, target);
        assertEquals(Arrays.toString(ans), Arrays.toString(sln));
    }

    @Test
    public void should_sum_negatives_appropriately() {
        int[] nums = {-4, 4, 2, 0};
        int target = -2;
        int[] sln = {0, 2};
        int[] ans = subject.run(nums, target);
        assertEquals(Arrays.toString(ans), Arrays.toString(sln));
    }

    @Test
    public void should_fail_if_no_solution() {
        int[] nums = {1, 4, 3, 0};
        int target = 0;
        assertThrows(IllegalArgumentException.class,
            () -> {
                int[] ans = subject.run(nums, target);
            });
    }
}
