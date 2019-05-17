#include <iostream>
#include <string>

using namespace std;

int main(){
    int n = 500, upper = 1000, lower = 0;
    string input = "";
    while (input != "correct"){
        cout << n << endl;
        cout.flush()
        cin >> input;
        if (input == "lower"){
            upper = n-1;
            n = (lower+1+upper)/2;
        }
        else if (input == "higher"){
            lower = n+1;
            n = (upper + lower)/2;
        }
    }
}
