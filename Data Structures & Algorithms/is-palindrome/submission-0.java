class Solution {
    public boolean isPalindrome(String s) {
        String str=s.toLowerCase();
        StringBuilder sb1=new StringBuilder();
        StringBuilder sb=new StringBuilder();
        for(int i=0;i<str.length();i++){
            if(str.charAt(i) >='0' && str.charAt(i) <='9'){
                sb1.append(str.charAt(i));
            }
            else if(str.charAt(i) >= 'a' && str.charAt(i) <= 'z'){
                sb1.append(str.charAt(i));
            }
            else{
                continue;
            }

        }
        for(int i=str.length()-1;i>=0;i--){
            if(str.charAt(i) >='0' && str.charAt(i) <='9'){
                sb.append(str.charAt(i));
            }
            else if(str.charAt(i) >= 'a' && str.charAt(i) <= 'z'){
                sb.append(str.charAt(i));
            }
            else{
                continue;
            }

        }
        if(sb1.toString().equals(sb.toString())){
            return true;
        }
        return false;
    }
}
