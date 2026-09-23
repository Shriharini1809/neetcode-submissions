class Solution {
    public int numUniqueEmails(String[] emails) {
        HashSet<String> s = new HashSet<>();
        int n = emails.length;

        for(int i=0;i<n;i++){
            StringBuilder sb = new StringBuilder();
            int j=0;
            int index =0;
            while(emails[i].charAt(j) != '@'){
                if(emails[i].charAt(j)=='.'){
                    j++;
                    index++;
                    continue;
                }
                else if(emails[i].charAt(j)=='+'){
                    while(emails[i].charAt(j) != '@'){
                        j++;
                        index++;
                    }
                    break;
                }
                else{
                    sb.append(emails[i].charAt(j));
                    j++;
                }
                index ++;
            }
            for(int a=index;a<emails[i].length();a++){
                sb.append(emails[i].charAt(a));
            }
            s.add(sb.toString());

        }
        return s.size();
        
    }
}