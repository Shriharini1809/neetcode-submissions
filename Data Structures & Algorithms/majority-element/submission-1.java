class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(map.containsKey(nums[i])){
                map.put(nums[i],map.get(nums[i])+1);
            }
            else{
                map.put(nums[i],1);
            }
        }
        int a=0;
        int max=0;
        int val=-1;
        for(int i=0;i<map.size();i++){
            if(map.get(nums[a]) > max){
                max=map.get(nums[a]);
                val=nums[i];
            }
            a++;
        }
        return val;

    }
}