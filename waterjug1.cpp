#include <bits/stdc++.h>
using namespace std;

int jug1 = 4;
int jug2 = 3;
int aim = 2;

int visited[10000][10000]={false};
bool waterJugSolver(int amt1, int amt2){

	if ((amt1 == aim && amt2 == 0) || (amt2 == aim && amt1 == 0)){
		cout<<amt1<<" "<<amt2<<endl;
		return true;
	}

	if (visited[amt1][amt2] == false){
		cout<<amt1<<" "<<amt2<<endl;
	
		visited[amt1][amt2] = true;
	
		return (waterJugSolver(0, amt2) ||
				waterJugSolver(amt1, 0) ||
				waterJugSolver(jug1, amt2) ||
				waterJugSolver(amt1, jug2) ||
				waterJugSolver(amt1 + min(amt2, (jug1-amt1)),
				amt2 - min(amt2, (jug1-amt1))) ||
				waterJugSolver(amt1 - min(amt1, (jug2-amt2)),
				amt2 + min(amt1, (jug2-amt2))));
	}
	else
		return false;
}

int main() {
cout<<("Steps: ")<<endl;

waterJugSolver(0, 0);

	return 0;
}
