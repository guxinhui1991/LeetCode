//
//  main.cpp
//  LeetCodeCpp
//
//  Created by Xinhui on 4/23/23.
//

#include <iostream>
#include "494.cpp"
#include "474.cpp"
#include "Knapsack.cpp"
int main(int argc, const char * argv[]) {
    
    using namespace std;
    
    /*
    int profit[] = { 5, 3, 5, 3, 2};
    int weight[] = { 1, 2, 4, 2, 5};
    int W = 10;
    int n = sizeof(profit) / sizeof(profit[0]);
    
    cout<< Knapsack().knapsackRecursive(W, weight, profit, n)<<endl;
    cout<< Knapsack().knapsackDP(W, weight, profit, n)<<endl;
     
     */
    
    
    // 494 - completed
    /*
     */
    vector<int> nums = {1,1,1,1,1};
    int target = 3;
    cout<<Solution494().findTargetSumWays(nums, target)<<endl;

    
    // 474 - completed
    /*
    vector<string> strs = {"10","0001","111001","1","0"};
    int m = 5;
    int n = 3;
    cout<<Solution474().findMaxForm(strs,m,n)<<endl;

    
    strs = {"10","0", "1"};
    m, n = 1, 1;
    cout<<Solution474().findMaxForm(strs,m,n)<<endl;
     */


    return 0;
}
