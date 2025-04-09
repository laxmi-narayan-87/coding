// ////////////////////////////////////////////////////////////////////////////////////////////////
// #include <iostream>
// #include<string>
// #include <map>
// using namespace std;

// void frequency(int arr[], int n) {
//    unordered_map<int, int> map;

//    for(int i = 0; i < n; i++) {
//        map[arr[i]]++;
//    }

//    cout << "Element : Frequency" << endl;
//    for(auto i : map) {
//        cout << i.first << " : " << i.second << endl;
//    }
// }

// int main() {
//    int arr[] = {10, 20, 20, 10, 10, 20, 5, 20};
//    int n = sizeof(arr)/sizeof(arr[0]);
//    frequency(arr, n);
//    return 0;
// }
// /////////////////////////////////////////////////////////////////////////////////////////

// #include <iostream>
// #include<string>
// int main() {
// forward_list<string>myflist{"i","am","at","psit"};
// myflist.sort();
// for(auto it= myflist.begin();it!=myflist.end();++it)
// cout<< '' <<*it;
//    return 0;
// }


// ///////////////////////////////////////////////////////////////////////////////////////////////////


// #include<iostream>
// using namespace std;
// // CREATING THE LIST
// int main()
// {
	
// 	//CREATE THE LIST
// 	list<int>numbers{1,2,3,4};//1-><-2
// 	//DISPLAY THE ELEMENTS OF LIST
// 	cout<< "List Elements:";
// 	for(int x:numbers){
// 		cout<<x<<;
// 		}
		
// 		return 0;
		
// 	}
	
// ///////////////////////////////////////////////////////////////////////////////////////////////////

// #include<iostream>

// int main(){
	
// 	// CREATE A LIST
// 	list<int>numbers={1,2,3};
// 	//ADD ELEMENT AT THE BEGINING
// 	numbers.push_front(0);
// 	//ADD ELEMENT AT THE BACK
// 	numbers.push_back(4);
	
// 		cout<<endl<<<"Final  List:";
// 	for (int number:numbers)
// 	{
// 		cout<<number<<",";
		
// 	}	
// 	//REMOVE ELEMENT FROM THE BEGINING
// 	numbers.pop_front();
// 	for(auto itr =numbers.begin();itr!=numbers.endl();itr++)
// 	cout<<*itr<<"";
// 	//REMOVE ELEMENT FROM THE BACK
// 	numbers.pop_back();
// 	for(auto itr =numbers.begin();itr!=numbers.endl();itr++)
// 	cout<<*itr<<"";
	
// 	return 0;
// }
// ////////////////////////////////////////////////////////////////////////////////////////


// #include<iostream>
// using namespace std

// int main(){
	
// 	 //CREATE A LIST
// 	list<int>numbers={1,2,3,4,5};
// 	list<int>numbrese={1,1,1,1,2,2,3,4,4,4,5,5,5,5,2,2,1,1,3,3,4};
// 		cout<<numbers.size()<<;//RETURNS NUMBERS OF ELEMENTS IN THE LIST
// 		cout<<numbers.sort()<<;// SORT THE LIST
// 		cout<<numbers.unique<<();//REMOVES CONSECUTIVE DUPLICATE ELEMENTS
// 		cout<<numberse.empty<<();//CHECK LIST IS EMPTY
// 		cout<<numbers.reverse<<();// REVERSE THE ORDER 
// 	list<int>numbers1={12,23,35,47,52};
// 	cout<<numbers.merge(numbers1)<<;// MERGE THE LIST
// 	for (auto it=numbers.begin();it!=numbers.end();++it)
// 	cout<<*it<<"";
// 	numberse.clear();
// 	for (auto it=numbers.begin();it!=numbers.end();++it)
// 	cout<<*it<<"";
// 	cout<<numberse.size();
// 	return 0;
// }
// /////////////////////////////////////////////////////////////////////////////////////////////////////////////
// //
// //
// //splice()
// //
// list1_name.splice(iterator position, list 2, iterator first, iterator last)
// transfer all the elements of list x into another list at some position .
// transfer only the element pointed by 1 from from list x into the list at some position
// transfer the range (first,last) from list x into the list at some position


// int main(){
// 	//intialising lists
// 	list<int>l1={1,2,3};
// 	list<int>l2={4,5};
// 	list<int>l3={6,7,8};
// 	//transfer all the elements of l2
// 	l1.splice(l1.begin(),l2); // 4,5,1,2,3
// 	//print and check
// 	for (auto it=l3.begin();it!=l3.end();++it)
// 		cout<<*it<<"";	
	
// 	// tarnsfer all the lements of l1
// 	l3.splice(l3.end(),l1);// 6,7,8,4,5,1,2,3
// 		for (auto it=l3.begin();it!=l3.end();++it)
// 		cout<<*it<<"";
// 	return 0;
// }

// /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// #include<iostream>
// #include<queue>
// #include<array>

// using namespace std;
// int kth_smallest(int arr[], int n, int k) {
//     priority_queue<int> pq;
//     for ( int i = 0; i < n; i++) {
//         pq.push(arr[i]);
//         if (pq.size() > k) 
//             pq.pop();   
//     }
//     return (pq.top());
// }

// int main ()
// {
//     int arr[]={1,4,3,6,7,9,4,7,90,4,3,2,4,6};

//      return ( kth_smallest(arr,14,3));
  
// }
// /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


// //////////////////////////////////////////////////////////////////////////////////////////
// // empty()  It is used to check whether the array is empty or not 
// int main()
// {
// 	array<int,3>; arr=(1,2,3);
// 	array<int,3>; arr=(4,5,6);
// 	bool x= arr.empty();
// 	cout<<(x);
// 	return 0;
	
// }

// /////////////////////////////////////////////////////////////////////////////////////////////
// at() function 
// it is used to access the element stored at a specific location
// if we try to access the element which is out of bounds then it show an exception 

// int main(){
// 	array<int,4>; arr=(1,2,3,4);
// 	array<int,5>; arr=(2,3,4,5,6);
// 	cout<< arr.at(2)<<"" arr1.at(2);
// 	return 0;
// }
// //
// ///////////////////////////////////////////////////////////////////////////////////////////
// size() or max_size() and sizeof() function 
// both size() or max_size () are used to get the maximum number of indexes in the array
// while  sizeof ()









// ///////////////////////////////////////////////////////////////////////////////
// data() : this function return s the pointer to the 
// //
// //
// //
// //
// //
// //
// //
// //
// //
// //
// //
// //
// //
// //
// //
// //
// //
// //
// //
// //
// //
// //
// ////////////////////////////////////////////////////////////////////////////////////////////////////////
// array::begin()
// array::end()
// int main()
// {
// 	/// declaration of array container
// 	array<int,5> myarray(1,2,3,4,5);
	
// 	// to print the reverse string 
// 	for (auto it= myarray.rbegin(); it!= myarray.rend(); ++it)
// 	{
// 		cout<<''*it;
// 	}
// 	return 0;
// }
// //////////////////////////////////////////////////////////////////////////////////////
////////////////////_________SET_____________/////////////////////////////////////////////////////////
// #include<iostream>
// #include<set>
// using namespace std;

// int main()
// {
//     set<char> a;            //INIATIALISING SET & INSERT THE CHARACTER ELEMENTS
//     a.insert('G');
//     a.insert('F');
//     a.insert('G');
//     for(auto &x:a){
//         cout<<x<<" ";
//     }
//     cout<< '\n';
//     return 0;
// }
// ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////

// #include<iostream>
// #include<set>
// #include<vector>
// using namespace std;

// int main()
// {
//    vector<int>v={4,3,6,1,8};                //INITAILISING SET  USING VECTOR
// set<int>s1(v.begin(),v.end());
//     for(auto &x:v){
//         cout<<x<<" ";
//     }
//     return 0;
// }
// ////////////////////////////////////////////////////////////////////////////////////

// #include<iostream>
// #include<set>
// using namespace std;

// int main()
// {
//    set<int>v={4,3,6,1,8};                                     // INITAILSING SET 
//     for(int val:v){
//         cout<<val<<" ";
//     }
//     return 0;
// }
///////////////////////////////////////////////////////////////////////////////////////////////////////

// #include<iostream>
// #include<set>
// using namespace std;

// int main()
// {
//    set<int>v={4,3,6,1,8};                                     // INITAILSING SET &INSERT THE ELEMENTS IN SET
//    v.insert(10);
//     v.insert(2);
//     v.insert(7);
//     for(int val:v){
//         cout<<val<<" ";
//     }
//     return 0;
// }

/////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////SORT THE ELEMENTS IN DESCENDING ORDER IN SET
// #include<iostream>
// #include<set>
// using namespace std;

// int main()
// {
//    set<int,greater<int>> v={4,3,6,1,8};                                     // DESCENDING ORDER
//     for(int val:v){
//         cout<<val<<" ";
//     }
//     return 0;
// }

////////////////////////////////////////////////////////////////////////////////////////////////

// #include<iostream>
// #include<set>
// using namespace std;

// int main()
// {
//    set<int>v={4,3,6,1,8};                                     
//    int num=40;
//    if(v.count(num)==1)                           // CHECK THE ELEMENT EXISTS OR NOT
//         cout<<num<<"exists "<<endl;
//     else
//     cout<<num<<"not exists "<<endl;    
//     return 0;
// }
////////////////////////////////////////////////////////////////////////////////////////////////////////////


// #include<iostream>
// #include<set>
// using namespace std;

// int main()
// {
//    set<int>v={4,3,6,1,8};                                     // INSERT & REMOVE THE ELEMENTS IN SET
//    v.insert(10);
//     v.insert(2);
//     v.insert(7);
//     for(int val:v){
//         cout<<val<<" ";
//     }
//     v.erase(4);
//     v.erase(8);
//     for(int val:v){
//         cout<<val<<" ";
//     }
//     return 0;
// }
// //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// #include<iostream>
// #include<set>
// using namespace std;

// int main()
// {
//    set<int>v={4,3,6,1,8};                                     // PRINT ELEMENTS IN SET USING ITERATOR
//    v.insert(10);
//     v.insert(2);
//     v.insert(7);
//     for(auto it=v.begin();it!=v.end();++it){
//         cout<<*it<<" ";
//     }
//     return 0;
// }
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// #include<iostream>
// #include<set>
// using namespace std;

// int main()
// {
//    set<int>v={4,3,6,1,8};                                     // PRINT ELEMENTS IN REVERSE ORDER IN SET USING ITERATOR
//    v.insert(10);                                              //PRINT THE ELEMTS IN REVERSE ORDER OR DESCENDING ORDER
//     v.insert(2);
//     v.insert(7);
//     for(auto it=v.rbegin();it!=v.rend();++it){
//         cout<<*it<<" ";
//     }
//     return 0;
// }
// ///////////////////////////////////////////////////////_________UNORDERED SET ___________///////////////////////////////////////////////////////////////
// #include<iostream>
// #include<unordered_set>
// using namespace std;

// int main()
// {
//    unordered_set<int>v={4,3,6,1,8};                                     // INSERT THE ELEMENTS IN UNORDERED SET AND PRINT USING ITERATOR
//    v.insert(10);
//     v.insert(2);
//     v.insert(7);
//     for(auto it=v.cbegin();it!=v.cend();++it){
//         cout<<*it<<" ";
//     }
//     return 0;
// }

// //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// #include<iostream>
// #include<unordered_set>
// using namespace std;

// int main()
// {
//    unordered_set<int>v={4,3,6,1,8};                                     //  INSERT THE ELEMENTS IN UNORDERED SET
//    v.insert(10);
//     v.insert(2);
//     v.insert(7);
//     for(int val:v){
//         cout<<val<<" ";
//     }
//     return 0;
// }




//////////////////////////SORT THE ELEMENTS IN DESCENDING ORDER IN UNORDERED SET
// #include<iostream>
// #include<unordered_set>
// using namespace std;

// int main()
// {
//    unordered_set<int,greater<int>> v={4,3,6,1,8};                                     // DESCENDING ORDER
//     for(int val:v){
//         cout<<val<<" ";
//     }
//     return 0;
// }

////////////////////////////////////////////////////////////////////////////////////////////////

// #include<iostream>
// #include<unordered_set>
// using namespace std;

// int main()
// {
//    unordered_set<int>v={4,3,6,1,8};                                     
//    int num=40;
//    if(v.count(num)==1)                           // CHECK THE ELEMENT EXISTS OR NOT IN UNORDERED SET
//         cout<<num<<"exists "<<endl;
//     else
//     cout<<num<<"not exists "<<endl;    
//     return 0;
// }
////////////////////////////////////////////////////////////////////////////////////////////////////////////


// #include<iostream>
// #include<unordered_set>
// using namespace std;

// int main()
// {
//    unordered_set<int>v={4,3,6,1,8};                                     // INSERT & REMOVE THE ELEMENTS IN UNORDERED SET
//    v.insert(10);
//     v.insert(2);
//     v.insert(7);
//     for(int val:v){
//         cout<<val<<" ";
//     }
//     v.erase(4);
//     v.erase(8);
//     for(int val:v){
//         cout<<val<<" ";
//     }
//     return 0;
// }
// //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// #include<iostream>
// #include<unordered_set>
// using namespace std;

// int main()
// {
//    unordered_set<int>v={4,3,6,1,8};                                     // PRINT ELEMENTS IN UNORDERED SET USING ITERATOR
//    v.insert(10);
//     v.insert(2);
//     v.insert(7);
//     for(auto it=v.begin();it!=v.end();++it){
//         cout<<*it<<" ";
//     }
//     return 0;
// }
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// #include<iostream>
// #include<unordered_set>
// using namespace std;

// int main()
// {
//    unordered_set<int>v={4,3,6,1,8};                                     // PRINT ELEMENTS IN REVERSE ORDER IN UNORDERED SET USING ITERATOR
//    v.insert(10);                                              //PRINT THE ELEMTS IN REVERSE ORDER OR DESCENDING ORDER
//     v.insert(2);
//     v.insert(7);
//     for(auto it=v.rbegin();it!=v.rend();++it){
//         cout<<*it<<" ";
//     }
//     return 0;
// }
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////______MAP______///////////////////////////////////////////////////////////////////
// #include<iostream>
// #include<map>
// using namespace std;
// int main()
// {
//     map<int,string> m;                         // INITAILISING MAP
//     m['one']=1;
//     m['two']=2;
//     m['three']=3;
//     for(auto &x:m){
//         cout<<x.first<<" "<<x.second<<endl;                         // PRINT THE ELEMENTS IN MAP USING FOR LOOP
//     }
//     cout<< '\n';
//     return 0;
// }
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// #include<iostream>
// #include<map>
// using namespace std;

// int main()
// {
//     map<int,string> m;                         // INITAILISING MAP
//     m[1]="one";
//     m[2]="two";
//     m[3]="three";
    
//     auto it = m.begin();
    
//     while(it != m.end())
//     {
//         cout << it->first << " " << it->second << endl;                      // PRINT THE ELEMENTS IN MAP USING ITERATOR
//         ++it;
//     }
    
//     return 0;
// }
// ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// #include <iostream>
// #include <map>
// #include <string>
// using namespace std;

// int main() {
//     map<string, int> mp;                  // INITIALISATION MAP
//     mp["one"] = 1;
//     mp["two"] = 2;
//     mp["three"] = 3;

//        map<string, int>::iterator it = mp.begin();                              // Access values using keys
//     while (it != mp.end()) {
//         cout << "key: " << it->first << ", value: " << it->second << endl;
//         ++it;
//     }

//     return 0;
// }
// ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//INSERT () is a built in function in c++ stl which is used to insert  a particular elements in the map container.


// #include <iostream>
// #include <map>
// using namespace std;

// int main() {
//     map<int, int> mp;                  // INITIALISATION MAP
//     mp.insert({2,30});
//     mp.insert({1,40});
//     mp.insert({3,60});
//     mp.insert({2,20});
//     mp.insert({3,50});
//     for (auto it = mp.begin(); it != mp.end(); ++it) {
//         cout << it->first 
//         << '\t' << it->second << endl;
//     }
//     return 0;
// }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// #include <iostream>
// #include <map>
// using namespace std;

// int main() {
//     map<int, int> mp;                  // INITIALISATION MAP
//     mp.insert({2,30});                   // INSERT THE ELEMENTS IN MAP
//     mp.insert({1,40});
//     mp.insert({3,60});
//     mp.insert({2,20});
//     mp.insert({3,50});
// if(mp.count(1))                                 // CHECK THE ELEMENT EXISTS OR NOT
// cout<<"key1 is present\n";
// else
// cout<<"key1 is not present\n";
// if(mp.count(100))
// cout<<"key100 is present\n";
// else
// cout<<"key100 is not present\n";
// return 0;
// }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// map::erase()) function is used to remove the element from the map container It is used to remove the element from the map container with the help of the key value.
// map_name.erase(key);
// used to erase elements from the container -> O(log n)

// #include <iostream>
// #include <map>
// using namespace std;

// int main() {
//     map<int, int> mp;                  // INITIALISATION MAP
//     mp.insert({2,30});                   // INSERT THE ELEMENTS IN MAP
//     mp.insert({1,40});
//     mp.insert({3,60});
//     mp.insert({4,20});
//     mp.insert({7,50});
//     mp.erase(2);                            // ERASE THE ELEMENTS IN MAP
//     for (auto it = mp.begin(); it != mp.end(); ++it) {
//         cout << it->first 
//         << '\t' << it->second << endl;
//     }
//     return 0;
// }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// #include <iostream>
// #include <map>
// using namespace std;

// int main() {
// map<char, int>mymap;
// mymap.insert(make_pair('a',1));
// mymap.insert(make_pair('b',3));
// mymap.insert(make_pair('c',5);

// for (auto it =mymap.rbegin(); it!=mymap.end())




//////////////////////////////////////////////////////////////////////////////////////////////////////////////

// map::find() is a built in function in c++ stl that returns an iterator or a constant iterator that refers to the position where the key is present in the map. if the key is not present in the map container , it returns an iterator or a constant iterator which refers to map.end()
// iterator= map_name.find(key)
//           or
// constant iterator =map_name.find(key)

// #include <iostream>
// #include <map>
// using namespace std;

// int main() {
//     map<int, int> mp;                  // INITIALISATION MAP
//     mp.insert({2,30});                   // INSERT THE ELEMENTS IN MAP
//     mp.insert({1,40});
//     mp.insert({3,60});
//     mp.insert({4,20});
//     mp.insert({7,50});
//     int s=2;
//     if(mp.find(s)!=mp.end())
//     cout<<"key found\n";
//     else
//     cout<<"key not found\n";
//     return 0;
// }
// ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// /////////////////////              STACK                  /////////////////////////////////////////////////////////////////////////

// stack works on LIFO (lasr in first out)
// PUSH() : to add element in the stack 
// pop() : to remove the element from the stack
// stack_name.top() : it gives the last input element in the stack

// /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// #include <iostream>
// #include <stack>
// using namespace std;
// int main(){
//     stack<int> s;         //CREATE INTEGER STACK
//     s.push(10);           // ADD ELEMENT IN STACK
//     s.push(20);
//     s.push(30);
//     s.push(40);
//     cout<<"The stack is : ";
//     while(!s.empty()){                 /// PRINT STACK IF NOT EMPTY 
//         cout<<s.top()<<" ";
//         s.pop();
//     }
//     cout<<endl;
//         return 0;
//     }
// ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// #include<iostream>
// #include<stack>
// using namespace std;
// int main(){
//     stack<string> colors;        //CREATE STRING STACK
//     colors.push("Red");           // ADD ELEMENT IN STACK
//     colors.push("Green");
//     colors.push("Orange");

//     cout<< "stack : ";
//     while(!colors.empty()){                 /// PRINT STACK IF NOT EMPTY 
//         cout<<colors.top()<<" ";
//         colors.pop();
//     }
//         return 0;
// }

// // ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// string_name.size() : it returns the size of the stack


// #include <iostream>
// #include <stack>
// using namespace std;
// int main(){
// stack<string>nerw;
// nerw.push("python");
// nerw.push("java");
// nerw.push("c++");
// nerw.push("c");
// cout<< "language :";
// cout<<nerw.size();
// while(!nerw.empty()){
//     cout<<nerw.top()<<" ";
//     nerw.pop();
// }
// nerw.pop();
// cout<<nerw.size();
// return 0;

// }

// // ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 //////////////////////////       REVERSE STACK         ////////////////////////////////
// #include <iostream>
// #include <stack>
// using namespace std;


// class Solution{
// public:
//     void Reverse(stack<int> &St){
//         if(St.empty())
//         return;
//         int x=St.top();
//         St.pop();
//         Reverse(St);
//         InsertAtBottom(St,x);

//     }   
//     void InsertAtBottom(stack<int> &St,int x){
//         if(St.empty()){
//             St.push(x);
//             return;
//         }
//         int y=St.top();
//         St.pop();
//         InsertAtBottom(St,x);
//         St.push(y);
//     }
// };

// int main()
// {
//    stack<int> St;
//     St.push(41);
//     St.push(62);
//     St.push(23);
//     St.push(34);
//     cout<<"before reversing: ";
//     while(!St.empty()){
//         cout<<St.top()<<" ";
//         St.pop();
//     }
//     cout<<endl;
//     Solution().Reverse(St);
//     cout<<"after reversing: ";
//     while(!St.empty()){
//         cout<<St.top()<<" ";
//         St.pop();
//     }
//     cout<<endl;
//     return 0;
    
// }


//  stack<int> rollno.;
//     rollno.push(41); 
//     rollno.push(62);
//     rollno.push(23);
//     rollno.push(34);
//     rollno.push(53);
//     rollno.push(65);
//     rollno.push(17);
//     rollno.push(28);
//     cout<<" before reverse: "
//     while(!rollno.empty()){
//         cout<<rollno.top()<<" ";
//         rollno.pop();
//     }
//     cout<<endl;
//     rollno.Reverse(rollno);
//     cout<<" after reverse: "
//     while(!rollno.empty()){
//         cout<<rollno.top()<<" ";
//         rollno.pop();
//     }

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// #include<iostream>
// #include<stack>
// #include<queue>
// using namespace std;
// int main(){
//     stack<int> s;

//     queue<int> q1, q2;

//     void push(int x)
//         q1.push(x);

//     void pop() {
//         if (q1.empty()) {
//             cout << "Stack is empty" << endl;
//             return;
//         }

//         while (q1.size() > 1) {
//             q2.push(q1.front());
//             q1.pop();
//         }

//         q1.pop();

//         swap(q1, q2);
//     }

//     int top() {
//         if (q1.empty()) {
//             cout << "Stack is empty" << endl;
//             return -1;
//         }

//         while (q1.size() > 1) {
//             q2.push(q1.front());
//             q1.pop();
//         }

//         int topElement = q1.front();
//         q2.push(topElement);

//         swap(q1, q2);

//         return topElement;
//     }

//     bool empty() {
//         return q1.empty();
//     }
// }

// ////////////////////////////////////////////////////////////////////////////////////////////////
#include<iostream>
#include<priority_queue>


