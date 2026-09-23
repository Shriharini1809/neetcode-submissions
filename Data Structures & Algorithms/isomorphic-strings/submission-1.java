
class Solution {
    public boolean isIsomorphic(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        java.util.HashMap<Character,Character> map = new java.util.HashMap<>();
        java.util.HashMap<Character,Character> map1 = new java.util.HashMap<>();
        for(int i=0;i<s.length();i++){
            if(map.containsKey(s.charAt(i))){
                if(map.get(s.charAt(i)) != t.charAt(i)){
                    return false;
                }
            }
            if(map1.containsKey(t.charAt(i))){
                if(map1.get(t.charAt(i)) != s.charAt(i)){
                    return false;
                }
            }
            map.put(s.charAt(i),t.charAt(i));
            map1.put(t.charAt(i),s.charAt(i));
        }
        return true;
    }
}