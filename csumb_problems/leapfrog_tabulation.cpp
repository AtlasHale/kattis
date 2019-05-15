#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int jump_t(vector<int> jumps){
    vector<int> mins(jumps.size(), 999);
    mins[0] = 0;
    for (int i = 0; i < jumps.size(); i++){
        int limit = jumps[i];
        bool valid = false;

        for (int j = i+1; j <= i + limit; j++){
            if (j < jumps.size()){
                if (jumps[j] != 0){
                    if (mins[j] > mins[i]+1)
                        mins[j] = mins[i]+1;
                }
            }
        }
        
    }
    if (mins[jumps.size()-1] == 999)
        return -1;
    return mins[jumps.size()-1];
}

int main() {
    int num_pads;
    cin >> num_pads;
    vector<int> jumps;
    for (int i = 0; i < num_pads; i++){
        int temp;
        cin >> temp;
        jumps.push_back(temp);
    }
    cout << jump_t(jumps);
        
    return 0;
}

