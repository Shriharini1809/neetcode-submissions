class Solution {
    public boolean hasDuplicate(int[] nums) {
        int n=nums.length;
        HashSet<Integer> map = new HashSet<>();
        for(int i=0;i<n;i++){
            map.add(nums[i]);
        }
        if(n==map.size()){
            return false;
        }
        return true;

    }
}