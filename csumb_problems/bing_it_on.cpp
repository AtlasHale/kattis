#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int main() {
    unordered_map<string, int> words;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++){
        string temp;
        cin >> temp;
        cout << words[temp] << endl;
        for (int j = 0; j < temp.length(); j++){
            words[temp.substr(0, j+1)]++;
        }
    }
}
