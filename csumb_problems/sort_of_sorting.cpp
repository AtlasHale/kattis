#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

bool compare_letters(string s1, string s2){
    if (s1[0] < s2[0])
        return true;
    if (s2[0] < s1[0])
        return false;
    return (s1[1] < s2[1]);
}


int main(){
    int n;
    cin >> n;
    while (n){
        vector<string> words;
        words.clear();
        for (int i = 0; i < n; i++){
            string temp = "";
            cin >> temp;
            words.push_back(temp);
        }
        stable_sort(words.begin(), words.end(), compare_letters);
        for (auto x : words)
            cout << x << endl;
        cout << endl;
        cin >> n;
    }
    return 0;
}

