// //////////////////////ADD TWO NUMBERS/////////////////////////////////////////////////////////
// //
// //
// //#include <iostream>
// //using namespace std;
// //int main() {
// //    int num1, num2;
// //    std::cout << "Enter first number: ";
// //    std::cin >> num1;
// //    std::cout << "Enter second number: ";
// //    std::cin >> num2;
// //
// //    int sum = num1 + num2;
// //    std::cout << "The sum is: " << sum << std::endl;
// //
// //    return 0;
// //}

// ///////////////////////////minimum loss//////////////////////////////////////////////{BRUTE FORCE APPROACH}
// int minimumloss(vector<long> price){                                                        // brute force approach
//     int n=price.size();
//     int minloss=INT_MAX;
//     for(int i=0;i<n;i++){
//         for(int j=i+1;j<n;j++){
//             if(price[i]>price[j]){
//                 int loss=price[i]-price[j];
//                 if(loss<minloss){
//                     minloss=loss;
//                 }           
//             }
//         }
//     }
// }
// //////////////////////////minimum loss////////////////////////////////////// {approach 2}
// int minimumLoss(vector<long>price){
//     int n=price.size();                 // approach using sorting
//     vector<pair<long,int>>v;
//     for(int i=0;i<n;i++){
//         v.push_back({price[i],i});
//     }
//     sort(v.begin(),v.end());
//     int minloss=INT_MAX;
//     for(int i=0;i<n-1;i++){
//         if(v[i].second>v[i+1].second){
//             int loss=v[i+1].first-v[i].first;
//             if(loss<minloss){
//                 minloss=loss;
//             }
//         }
//     }
//     return minloss;
// }



class Solution {
public:
    int minStartValue(vector<int>& nums) {
        int step_sum = 1;
        int result = 1;
        for (int i = 0; i < nums.size(); i++) {
            step_sum += nums[i];
            if (step_sum < 1) {
                result = result+ 1 - step_sum;
                step_sum = 1;
            }
        }
    }
};