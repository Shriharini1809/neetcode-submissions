class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        for(int i=0;i<prices.length-1;i++){
            int price = 0;
            int cur = 0;
            for(int j=i+1;j<prices.length;j++){
                price = prices[j] - prices[i];
                if(price > cur){
                    cur = price;
                }
            }
            if(cur > max){
                max = cur;
            }
            
        }
        return max;
    }
}
