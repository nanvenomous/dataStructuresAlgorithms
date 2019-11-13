package two_sum;

import org.junit.Test;
import static org.junit.Assert.*;
import java.util.Arrays;

public class TwoSumTest {
	@Test public void should_return_set_one() { 
		int[] nums = {2, 7, 11, 15};
		int target = 9;
		int[] sln = {0, 1};
		TwoSum twosum = new TwoSum();
		int[] ans = twosum.run(nums, target);
		assertEquals(Arrays.toString(ans), Arrays.toString(sln));
	} 
	@Test public void should_return_set_two() { 
		int[] nums = {0, 4, 3, 0};
		int target = 0;
		int[] sln = {0, 3};
		TwoSum twosum = new TwoSum();
		int[] ans = twosum.run(nums, target);
		assertEquals(Arrays.toString(ans), Arrays.toString(sln));
	} 

	// @Test public void should_fail() { 
		// int[] nums = {1, 4, 3, 0};
		// int target = 0;
		// TwoSum twosum = new TwoSum();
		// int[] ans = twosum.run(nums, target);
		// throw new IllegalArgumentException("no two values in the array sum to the target");
	// } 
}
