#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    string s = "Access our most capable model with a 1 million token context window via the Gemini API. Integrate multimodal text, vision, and the new audio reasoning capabilities and take advantage of new API features including JSON mode, System Instructions and improved Function Calling.";
    cout << s << endl;
    s.erase(15, 90);
    cout << s << endl;
    sort(s.begin(), s.end());
    cout << s << endl;
    int N= s.length();
    traverse(&s,N);
    return 0;
}



void traverse(string &s,int N)
{for(auto &ch:str){
	cout<<s<<endl;
}
}
