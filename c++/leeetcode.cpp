//LEETCODE
//
///////////////////////////LEETCODE 1 TWO SUM //////////////////////////////////////////////////////////////
//
//
//
//class Solution {
//public:
//    vector<int> twoSum(vector<int>& nums, int target) {
//           std::unordered_map<int, int> numMap; // Create a hash map to store the number and its index
//
//        for (int i = 0; i < nums.size(); ++i) {
//            int complement = target - nums[i]; // Calculate the complement
//
//            if (numMap.find(complement) != numMap.end()) {
//                // If the complement is found in the map, return the indices
//                return {numMap[complement], i};
//            }
//
//            numMap[nums[i]] = i; // Store the current number and its index in the map
//        }
//
//        // If no solution is found, return an empty vector
//        return {};
//    }
//};
//
//
//
//
////////////////////leetcode  876/////////////APPROACH 1///////////////////////////////
//
///**
// * Definition for singly-linked list.
// * struct ListNode {
// *     int val;
// *     ListNode *next;
// *     ListNode() : val(0), next(nullptr) {}
// *     ListNode(int x) : val(x), next(nullptr) {}
// *     ListNode(int x, ListNode *next) : val(x), next(next) {}
// * };
// */
//class Solution {
//public:
//    ListNode* middleNode(ListNode* head) {
//    ListNode* temp;
//    ListNode* temp1;
//    int mid;
//    int c=0;
//    if(head==NULL)
//       return 0;
//    while(temp!=NULL)
//    {c++;
//    temp=temp->next;
//    }
//    cout<<c;
//        mid=(c/2);
//    if(c%2==0){
//        mid=mid+1;
//    }
//    for(int i=1; i=mid;i++)
//    {
//        if(i==mid)
//        cout<<temp->val;
//
//    }
//    return temp;
//    }
//};
//
//
//
//
//
//
//
//
////////////////////leetcode  876/////////////APPROACH 2///////////////////////////////
//
///**
// * Definition for singly-linked list.
// * struct ListNode {
// *     int val;
// *     ListNode *next;
// *     ListNode() : val(0), next(nullptr) {}
// *     ListNode(int x) : val(x), next(nullptr) {}
// *     ListNode(int x, ListNode *next) : val(x), next(next) {}
// * };
// */
//class Solution {
//public:
//    ListNode* middleNode(ListNode* head) {
//    ListNode* slow=head;
//    ListNode* fast=head;
//    while(fast!=NULL && fast-> next!=NULL)
//    {
//        slow=slow->next;
//        fast=fast->next->next;
//    }
//
//    
//    return slow;
//    }
//};
///////////////////////////////////////LEETCODE 217/////////////CONTAINS DUPLICATE//////////////////////////
