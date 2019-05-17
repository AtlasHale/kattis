#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <climits>

using namespace std;


bool sort_backwards(string s1, string s2){
    int l1 = s1.length()-1, l2 = s2.length()-1;
    char c1, c2;
    while (l1 >= 0 && l2 >= 0){
        c1 = s1[l1]; 
        c2 = s2[l2];
        if (c1 < c2) return true;
        if (c2 < c1) return false;
        if (l1 == 0 && l2) return true;
        if (l2 == 0 && l1) return false;
        if (!l1 && !l2) return true;
        l1--;
        l2--;
    }
    return false;
}

bool read_words(string first){
    string s = first;
    bool last = false;
    vector<string> words;
    int max_len = s.length();
    words.push_back(s);
    while(!s.empty()){
        getline(cin, s);
        if(s.empty())
            break;
        if (cin.eof())
            last = true;
        int curr = s.length();
        if (curr > max_len){
            max_len = s.length();
        }
        words.push_back(s);
    }
    sort(words.begin(), words.end(), sort_backwards);
    for (auto x : words){
        for (int i = 0; i < max_len - x.length(); i++)
            cout << " ";
        cout << x << endl;
    }
    return last;
}

int main(){
    int i = 0;
    string s = "";
    while (getline(cin, s)){
        if (i != 0)
            cout << endl;
        read_words(s);
        i++;
    }
}

