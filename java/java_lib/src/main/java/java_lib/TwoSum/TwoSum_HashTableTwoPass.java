package java_lib;

import java.util.Hashtable;

class TwoSum_HashTableTwoPass {
    public int[] run(int[] nums, int target) {
        Hashtable<Integer, Integer> ht = new Hashtable<>();
        for (int i = 0; i < nums.length; i++) {
            ht.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
            int check_value = nums[i];
            int possible_solution = target - check_value;
            try {
                int solution_index = ht.get(possible_solution);
                if (i != solution_index) {
                    return new int[]{i, solution_index};

                }
            } catch (NullPointerException ex){}
        }
        throw new IllegalArgumentException("no two values in the array sum to the target");
    }
};
