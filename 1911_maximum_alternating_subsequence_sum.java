class Solution {
    public long maxAlternatingSum(int[] nums) {
        long even = 0, odd = 0; // max alternating subsequence sum that ends with even/odd idx

        for(int num: nums){
            long eventTmp = even;
            even = Math.max(even, odd + num);
            odd = Math.max(odd, eventTmp - num);
        }

        return even;
    }
}
