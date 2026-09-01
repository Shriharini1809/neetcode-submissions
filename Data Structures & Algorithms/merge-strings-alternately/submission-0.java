class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder sb = new StringBuilder();
        int w1=word1.length();
        int w2=word2.length();
        int a=0;
        int b=0;
        for(int i=0;i<w1+w2;i++){
            if(a < w1){
                sb.append(word1.charAt(a));
                a++;
            }
            if(b < w2){
                sb.append(word2.charAt(b++));
            }
        }
        return sb.toString();

    }
}