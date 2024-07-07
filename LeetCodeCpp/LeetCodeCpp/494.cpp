//
//  494.cpp
//  LeetCodeCpp
//
//  Created by Xinhui on 4/23/23.
//

#include <stdio.h>
using namespace std;

#include <vector>
class Solution494 {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        S = abs(S);
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
        }

        if (S > sum | (S + sum) % 2 == 1) return 0;

        const int target = (S + sum) / 2;
        const  int N = nums.size();
        vector<vector<int>> dp_v(N + 1, vector<int>(target+1, 0));

        for (int i = 0; i <= N; i++)
        {
            for (int j = 0; j <= target; j++)
            {
                dp_v[i][j] = 0;
            }
        }

        dp_v[0][0] = 1;
        for (int i = 1; i <= N; i++)
        {
            for (int j = 0; j <= target; j++)
            {
                dp_v[i][j] += dp_v[i - 1][j];
                if(j-nums[i-1] >= 0) dp_v[i][j] +=  dp_v[i - 1][j - nums[i - 1]] ;
             }
        }

        return dp_v[N][target];
    }
};
