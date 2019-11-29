package java_lib.TwoSum;

import java.util.Hashtable;

class TwoSum_HashTable {
    public int[] run(int[] nums, int target) {
        Hashtable<Integer, Integer> ht = new Hashtable<>();
        int check_value;
        int possible_solution;
        for (int i = 0; i < nums.length; i++) {
            check_value = nums[i];
            possible_solution = target - check_value;
            try {
                int solution_index = ht.get(possible_solution);
                if (i != solution_index) {
                    return new int[]{i, solution_index};
                }
            } catch (NullPointerException ex){}
            ht.put(check_value, i);
        }
        throw new IllegalArgumentException("no two values in the array sum to the target");
    }
};
