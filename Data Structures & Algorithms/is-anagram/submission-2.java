class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }
        ArrayList<String> set1=new ArrayList<>();
        ArrayList<String> set2=new ArrayList<>();
        for(int i=0;i<s.length();i++){
            set1.add(Character.toString(s.charAt(i)));
        }
        for(int i=0;i<t.length();i++){
            set2.add(Character.toString(t.charAt(i)));
        }
        for(String str:set1){
            if(set2.contains(str)){
                set2.remove(str);
            }
        }
        if(set2.size()==0){
            return true;
        }
        return false;
    }
}
