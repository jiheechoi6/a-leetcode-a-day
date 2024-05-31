class Solution {
    public int rob(int[] nums) {
        if(nums.length == 1){
            return nums[0];
        }

        int i1 = nums[0], i2 = Math.max(nums[0], nums[1]), res = 0;

        for(int i = 2; i < nums.length; i++){
            int temp = i2;
            i2 = Math.max(nums[i] + i1, i2);
            i1 = temp;
        }

        return i2;
    }
}
