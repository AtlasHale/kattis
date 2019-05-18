#include <iostream>
#include <vector>
#include <string>

using namespace std;


int main(){
    int n;
    cin >> n;
    while (n != 0){
        vector<int> places;
        vector<string> words;
        for (int i = 0; i < n; i++){
            int temp;
            cin >> temp;
            places.push_back(temp);
        }
        string full;
        cin.ignore();
        getline(cin, full);
        cout << "'";
        int move_up = 0;
        int i = 0;
        int counter = full.size();
        while(counter){
            if (i%n==0 && i)
                move_up += n;
            if (places[i%n]-1+move_up < full.size()){
                cout << full[places[i%n]-1+move_up];
                counter--;
            }
            else
                cout << " ";
            i++;
        }
        while (i%n){
            cout << " ";
            i++;
        }
        cout << "'"<< endl;
        cin >> n;
    }    
}
