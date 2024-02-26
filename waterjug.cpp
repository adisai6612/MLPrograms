#include <iostream>
#include <unordered_map>

using namespace std;

unordered_map<int, bool> memo;

bool canMeasureWater(int x, int y, int z) {
    if (z == 0) return true;
    if (x + y < z) return false;
    if (x == z || y == z || x + y == z) return true;
    
    int key = x * 1000 + y; // Using a unique key for memoization
    
    if (memo.find(key) != memo.end()) return memo[key];
    
    bool result = canMeasureWater(0, y, z) ||  // Pour from x to y
                  canMeasureWater(x, 0, z) ||  // Pour from y to x
                  canMeasureWater(x - min(x, y), y - min(x, y), z);  // Transfer water between jugs
    
    memo[key] = result;
    
    return result;
}

int main() {
    int x, y, z;
    
    cout << "Enter the capacities of the two jugs (x and y): ";
    cin >> x >> y;
    
    cout << "Enter the target amount of water (z): ";
    cin >> z;
    
    bool result = canMeasureWater(x, y, z);
    
    if (result) {
        cout << "Yes, it's possible to measure " << z << " units of water with jugs of capacities " << x << " and " << y << "." << endl;
    } else {
        cout << "No, it's not possible to measure " << z << " units of water with jugs of capacities " << x << " and " << y << "." << endl;
    }
    
    return 0;
}
