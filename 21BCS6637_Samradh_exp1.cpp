#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the size of an array";
    cin >> n;
    int a[n] = {};
    int ele;
    
    for (int j = 0; j < n; j++) {
        cout << "Enter an element";
        cin >> ele;
        a[j] = ele;
    }
    
    cout << "Reverse of the array is: " << endl;
    
    for (int i = 4; i--; i >= 0) {
        cout << a[i] << endl;
    }

    return 0;
}