package java_lib;

import java.util.Arrays;

// A Class that represents use-defined expception
class TwoSum_HashTable {
    public int[] run(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    int ans[] = new int[]{i, j};
                    return ans;
                }
            }
        }
        throw new IllegalArgumentException("no two values in the array sum to the target");
    }
};
