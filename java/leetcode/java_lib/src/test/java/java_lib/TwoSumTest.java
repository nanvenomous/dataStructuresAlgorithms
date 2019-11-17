package java_lib;

import java.util.Arrays;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;
//import static org.junit.Assert.*;


public class TwoSumTest {
    @Test
    public void should_return_set_one() {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] sln = {0, 1};
        TwoSum twosum = new TwoSum();
        int[] ans = twosum.run(nums, target);
        assertEquals(Arrays.toString(ans), Arrays.toString(sln));
    }

    @Test
    public void should_sum_zeros_to_zero() {
        int[] nums = {0, 4, 3, 0};
        int target = 0;
        int[] sln = {0, 3};
        TwoSum twosum = new TwoSum();
        int[] ans = twosum.run(nums, target);
        assertEquals(Arrays.toString(ans), Arrays.toString(sln));
    }

    @Test
    public void should_sum_negatives_appropriately() {
        int[] nums = {-4, 4, 2, 0};
        int target = -2;
        int[] sln = {0, 2};
        TwoSum twosum = new TwoSum();
        int[] ans = twosum.run(nums, target);
        assertEquals(Arrays.toString(ans), Arrays.toString(sln));
    }

    @Test
    public void should_fail_if_no_solution() {
        System.out.println("Running test");
        int[] nums = {1, 4, 3, 0};
        int target = 0;
        TwoSum twosum = new TwoSum();
        assertThrows(IllegalArgumentException.class,
            () -> {
                int[] ans = twosum.run(nums, target);
            });
    }
}
