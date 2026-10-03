class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefix = new int[nums.length];
        int[] post=new int[nums.length];
        int result = 1;
        prefix[0]= result;
        for(int i=1;i<nums.length;i++){
            prefix[i] = nums[i-1] * result;
            result = prefix[i];
        }
        int result1= 1;
        post[nums.length-1]=result1;
        for(int i=nums.length-2;i>=0;i--){
            post[i] = nums[i+1] * result1;
            result1 = post[i];
        }
        int[] res = new int[nums.length];
        for(int i=0;i<nums.length;i++){
            res[i] = prefix[i] * post[i];
        }
        return res;
    }
}  
