#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int main() {
    int n, total(0);
    char d;
    cin >> n >> d;
    unordered_map<char, int> dominant;
    unordered_map<char, int> no;
    dominant['A'] = 11;
    dominant['K'] = 4;
    dominant['Q'] = 3;
    dominant['J'] = 20;
    dominant['T'] = 10;
    dominant['9'] = 14;
    dominant['8'] = 0;
    dominant['7'] = 0;
    no['A'] = 11;
    no['K'] = 4;
    no['Q'] = 3;
    no['J'] = 2;
    no['T'] = 10;
    no['9'] = 0;
    no['8'] = 0;
    no['7'] = 0;
    string curr;
    while(getline(cin, curr)){
        if (curr[1] == d){
            total += dominant[curr[0]];
        }
        else
            total += no[curr[0]];
    }
    cout << total;
}
