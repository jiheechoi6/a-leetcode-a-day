class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(candidates);
        backtrack(candidates, target, 0, res, new ArrayList<>());
        return res;
    }

    private void backtrack(int[] candidates, int target, int start, List<List<Integer>> res, List<Integer> comb){
        if(target == 0){
            res.add(new ArrayList<Integer>(comb));
            return;
        }
        if(target<0) return;

        for(int i = start; i<candidates.length; i++){
            if(i != start && candidates[i] == candidates[i-1]){
                continue;
            }
            comb.add(candidates[i]);
            backtrack(candidates, target-candidates[i], i+1, res, comb);
            comb.remove(comb.size()-1);
        }
    }
}
