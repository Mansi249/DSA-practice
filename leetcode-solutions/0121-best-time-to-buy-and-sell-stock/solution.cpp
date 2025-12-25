class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_price = INT_MAX;
        int max_profit = 0;
        for(int x:prices){
            if(x>min_price){
                max_profit = max(max_profit,x-min_price);
            }
            min_price = min(x,min_price);
        }
        return max_profit;
    }
};
