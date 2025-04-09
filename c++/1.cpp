#include <iostream>
#include <vector>
int main()
{vector<int>v;

v.push_back(10);
v.push_back(20);
v.push_back(30);
v.push_back(40);

for(int x:v)
cout<<x<<"";

return 0;
}
