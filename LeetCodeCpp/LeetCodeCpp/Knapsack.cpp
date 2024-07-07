//
//  Knapsack.cpp
//  LeetCodeCpp
//
//  Created by Xinhui on 4/23/23.
//

#include <stdio.h>
using namespace std;

#include <vector>
class Knapsack {
public:
    

    int max(int a, int b) { return (a > b) ? a : b; }
     
    
    int knapsackDP(int W, int weight[], int val[], int n) {
                
        // double pointer to declare the table dynamically
        int dp[n+1][W+1];

        // loop to initially filled the table with -1
        for (int i = 0; i <= n; i++)
            for (int j = 0; j < W + 1; j++)
                dp[i][j] = -1;
        
        
        for(int i=0; i <= n; i++)
        {
            for (int w = 0; w < W + 1; w++)
            {
                if(i==0 | w==0)
                    dp[i][w] = 0;
                else if (weight[i-1] <= W)
                    dp[i][w] = max(val[i-1]+dp[i-1][w-weight[i-1]], dp[i-1][w]);
                else
                    dp[i][w] = dp[i-1][w];
            }
        }
        return dp[n][W];
    };
    
    
    int knapsackRecursive(int W, int weight[], int val[], int n)
    {
     
        // Base Case
        if (n == 0 || W == 0)
            return 0;
     
        // If weight of the nth item is than Knapsack capacity W, then
        // this item cannot be included in the optimal solution
        if (weight[n - 1] > W)
            return knapsackRecursive(W, weight, val, n - 1);
     
        // Return the maximum of two cases:
        // (1) nth item included
        // (2) not included
        else
            return max(
                       val[n - 1] + knapsackRecursive(W - weight[n - 1], weight, val, n - 1),
                       knapsackRecursive(W, weight, val, n - 1));
    }
};
