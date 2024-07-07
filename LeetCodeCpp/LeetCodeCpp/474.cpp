//
//  474.cpp
//  LeetCodeCpp
//
//  Created by Xinhui on 4/26/23.
//
#include <string>
#include <stdio.h>
using namespace std;
class Solution474 {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        
        int dp[m+1][n+1];
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                dp[i][j] = 0;
            }
        }
        
        for(string str:strs)
        {
            int numOne=0, numZero=0;
            for (char c : str)
            {
                if (c == '0') numZero +=1;
                else numOne +=1;
            }
            
            for (int i = m; i>= numZero; i--){
                for (int j = n; j>= numOne; j--){
                    dp[i][j] = max(dp[i-1][j-1], dp[i-numZero][j-numOne] + 1);
                }
            }
        }
        
        return  dp[m][n];
    }
};
