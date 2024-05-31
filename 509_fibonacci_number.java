class Solution {
    public int fib(int n) {
        if(n == 0) return 0;

        int n1 = 0, n2 = 1, i = 2;

        while(i <= n){
            int temp = n2;
            n2 = n1 + n2;
            n1 = temp;
            i++;
        }

        return n2;
    }
}
