#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

int main(){
    int size;
    cin >> size;
    vector<int> v(size);
    int ppivots(0);
    for (int i = 0; i < size; i++){
        cin >> v[i];
    }
    unordered_map<int, int> max_up_to;
    unordered_map<int, int> min_up_to;

    int maximum = v[0];
    max_up_to[0] = maximum;
    for (int i = 1; i < size; i++){
        if (maximum < v[i])
            maximum = v[i];
        max_up_to[i] = maximum;
    }
    int minimum = v[size-1];
    min_up_to[size-1] = minimum;
    for (int i = size-2; i >= 0; i--){
        if (minimum > v[i])
            minimum = v[i];
        min_up_to[i] = minimum;
    }
    
    for (int i = 0; i < size; i++){
        bool possible = false;
        int curr = v[i];
        if (curr >= max_up_to[i-1] && curr <= min_up_to[i])
            possible = true;
        ppivots += possible;
    }
    cout << endl << ppivots;
}
