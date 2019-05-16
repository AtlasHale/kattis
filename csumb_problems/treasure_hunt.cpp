#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

int hashed(int x, int y, int grid_size){
    return y*grid_size + x;
}

bool is_invalid(int x, int y, int rows, int columns){
    if (x < 0 || y < 0 || y == columns || x == rows)
        return true;
    return false;
}

bool is_lost(int x, int y, int rows, int columns, unordered_set<int> &visited){
    if (visited.count(hashed(x, y, rows*columns))!= 0)
        return true;
    visited.insert(hashed(x, y, rows*columns));
    return false;
}

int main() {
    vector<vector<char> > grid;
    unordered_set<int> visited;
    int rows, columns;
    cin >> rows >> columns;
    for (int i = 0; i < rows; i++){
        auto t = vector<char>(columns);
        for (int j = 0; j < columns; j++){
            cin >> t[j];
        }
        grid.push_back(t);
    }
    int x(0), y(0), moves(0);
    bool invalid = false, lost = false;
    char curr = grid[x][y];
    while (true){
        switch(curr){
            case 'N':
                x--;
                break;
            case 'S':
                x++;
                break;
            case 'W':
                y--;
                break;
            case 'E':
                y++;
                break;
            case 'T':
                cout << moves;
                exit(0);
        }
        moves++;
        invalid = is_invalid(x, y, rows, columns);
        lost = is_lost(x, y, rows, columns, visited);
        if (invalid){
            cout << "Out";
            break;
        }
        if (lost){
            cout << "Lost";
            break;
        }
        curr = grid[x][y];
    }
}
