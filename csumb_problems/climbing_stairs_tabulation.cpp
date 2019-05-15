#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int stairs_t(vector<int> steps, int size){
    vector<int> mins (size, -1);
    mins[0] = steps[0];
    mins[1] = steps[1];
    int index = size-1;
    for (int i = 2; i < size; i++){
        mins[i] = steps[i] + min(mins[i-1], mins[i-2]);
    }
    return mins[size-1];
}

int main() {
    int n;
    cin >> n;
    vector<int> steps(n);
    for (int i = 0; i < n; i++){
        cin >> steps[i];
    }
    cout << stairs_t(steps, n);
    return 0;
}

