class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> res = new ArrayList<>();
        if(k>n) return res;
        backtrack(k, n, res, new ArrayList<Integer>());
        return res;
    }

    private void backtrack(int k, int n, List<List<Integer>> res, List<Integer> comb) {
        if(k == 0){
            if(n == 0) res.add(new ArrayList<Integer>(comb));
            return;
        }
        
        int nextNum = comb.size() == 0? 1: comb.get(comb.size()-1)+1;
        while(nextNum<=(n-k+1) && nextNum<=9){
            comb.add(nextNum);
            backtrack(k-1, n-nextNum, res, comb);
            comb.remove(comb.size()-1);
            nextNum++;
        }
    }
}
