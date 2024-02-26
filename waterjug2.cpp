#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

struct State {
    int jug1, jug2;

    bool operator==(const State& other) const {
        return jug1 == other.jug1 && jug2 == other.jug2;
    }
};

struct StateHash {
    size_t operator()(const State& state) const {
        return hash<int>()(state.jug1) ^ hash<int>()(state.jug2);
    }
};

unordered_map<State, bool, StateHash> memo;

bool canMeasureWaterRecursive(int jug1, int jug2, int target) {
    if (jug1 == target || jug2 == target || jug1 + jug2 == target) {
        return true;
    }

    State currentState = {jug1, jug2};
    if (memo.find(currentState) != memo.end()) {
        return memo[currentState];
    }

    bool result = canMeasureWaterRecursive(0, jug2, target) ||
                  canMeasureWaterRecursive(jug1, 0, target) ||
                  canMeasureWaterRecursive(jug1, jug2, target) ||
                  canMeasureWaterRecursive(jug1, min(jug2 + jug1, jug2) - (jug2 + jug1 - jug1), target) ||
                  canMeasureWaterRecursive(min(jug1 + jug2, jug1) - (jug1 + jug2 - jug2), jug2, target);

    memo[currentState] = result;
    return result;
}

bool canMeasureWater(int jug1, int jug2, int target) {
    if (jug1 + jug2 < target) {
        return false;  // The total capacity of both jugs is less than the target.
    }

    if (jug1 == target || jug2 == target || jug1 + jug2 == target) {
        return true;  // We can measure the target amount.
    }

    if (jug1 == 0 && jug2 == 0) {
        return target == 0;  // Special case: both jugs are empty, target must be 0.
    }

    memo.clear();  // Clear the memoization map for each new problem.
    return canMeasureWaterRecursive(jug1, jug2, target);
}

int main() {
    int jug1, jug2, target;
    cout << "Enter the capacities of the two jugs (jug1 jug2): ";
    cin >> jug1 >> jug2;
    cout << "Enter the target amount to measure: ";
    cin >> target;

    if (canMeasureWater(jug1, jug2, target)) {
        cout << "It is possible to measure the target amount of water." << endl;
    } else {
        cout << "It is not possible to measure the target amount of water." << endl;
    }

    return 0;
}

