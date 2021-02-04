#include <iostream>
#include <string>
#include <bitset>
using namespace std;

bool unique_chars(string s) {
    bitset<255> buckets;
    for (int i = 0; i < s.size(); i++) {
        if (buckets[int(s[i])])
            return false;
        else
            buckets[int(s[i])] = 1;
    }
    return true;
}

int main()
{
    cout << unique_chars("(A123abcdzZ!#)(");
    
    return 0;
}