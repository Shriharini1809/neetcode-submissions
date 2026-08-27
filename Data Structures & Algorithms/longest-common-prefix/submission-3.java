class Solution {
    public String longestCommonPrefix(String[] strs) {
        int len=999;
        if(strs.length==1){
            return strs[0];
        }
        for(int i=0;i<strs.length;i++){
            int length=strs[i].length();
            if(length < len){
                len=length;
            }
        }
        String prefix=strs[0];
        String pre="";
        for(int i=0;i<len;i++){
            if(prefix.charAt(i)==strs[1].charAt(i)){
                pre+=prefix.charAt(i);
            }
            else{
                break;
            }
        }
        int found=0;
        for(int i=2;i<strs.length;i++){
            StringBuilder sb=new StringBuilder();
            for(int j=0;j<pre.length();j++){
                if(pre.charAt(j) == strs[i].charAt(j)){
                    sb.append(pre.charAt(j));
                }
                else{
                    break;
                }
            }
            pre=sb.toString();
        }
        
        return pre;
        
    }
}