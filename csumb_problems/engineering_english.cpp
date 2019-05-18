#include <iostream>
#include <unordered_set>
#include <string>
#include <sstream>

using namespace std;

int main(){
    string s;
    unordered_set<string> words;
    while(getline(cin, s)){
        string curr = "";
        string t = "";
        for (int i = 0; i < s.size(); i++){
            char c = s[i];
            if (c == ' ' || i == s.size()-1){
                if (i == s.size()-1){
                    curr += c;
                    t+= tolower(c);
                }
                if (words.find(t) != words.end())
                    cout << ".";
                else{
                    words.insert(t); 
                    cout << curr;        
                }
                cout << " ";
                curr = "";
                t = "";
            }
            else{
                curr += c;
                t+= tolower(c);
            }
        }
        cout << endl;
    }
}
