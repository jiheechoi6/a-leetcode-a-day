class Solution {
    public String longestCommonPrefix(String[] strs) {
        HashMap<Character, Integer> mp = new HashMap<> ();
       for (int j = 0; j<text.length (); j++) {
           char ch = text.charAt(j);
              if(mp.containsKey(ch)){
                    int cnt = mp.get(ch);
                 mp.put(ch, ++cnt);
             }else{
                mp.put(ch, 1);
              }
        }
        Set<Character> charct = map.keySet();

        for (Character ch: charct){
             int c= mp.get(ch);
             if(c>1){
                System.out.println(ch+ " - " + c);
             }
        }
    }
}
