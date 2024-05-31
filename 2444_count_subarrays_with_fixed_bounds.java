class Solution {
    public long countSubarrays(int[] nums, int minK, int maxK) {
        long badi = -1, mini = -1, maxi = -1, res = 0;

        for(int i = 0; i< nums.length; i++){
            if(nums[i] < minK || nums[i] > maxK) badi = i;
            if(nums[i] == minK) mini = i;
            if(nums[i] == maxK) maxi = i;
            res += Math.max(0, Math.min(mini, maxi) - badi);
        }

        return res;
    }
}
