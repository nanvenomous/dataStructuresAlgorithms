import java.util.Arrays;

// A Class that represents use-defined expception 
class TwoSum { 
  public int[] twoSum(int[] nums, int target) {
    for (int i = 0; i < nums.length; i++) {
      for (int j = i + 1; j < nums.length; j++) {
        if (nums[i] + nums[j] == target) {
          int ans[] = new int[]{i, j};
          return ans;
        }
      }
    }
    return new int[2];
  } 
  public static void main(String args[]) { 
    // int[] nums = {2, 7, 11, 15};
    int[] nums = {0, 4, 3, 0};
    int target = 0;
    TwoSum sln = new TwoSum();
    int[] ans = sln.twoSum(nums, target);
    System.out.println(Arrays.toString(ans));
  } 
}; 