#include <iostream>
using namespace std;

int main() {
    int n, d;
    cout << "Enter the size of the array and the number of rotations to perform: ";
    cin >> n >> d;
    int a[n] = {};
    int ele;
    
    for (int j = 0; j < n; j++) {
        cout << "Enter an element";
        cin >> a[j];
    }
    
    int rotatedArray[n] = {};
    
    for (int i = 0; i < n; i++) {
        int newIndex = (i + n - d) % n;
        rotatedArray[newIndex] = a[i];
    }
    
    cout << "Rotated array is: " << endl;
    
    for (int i = 0; i < n; i++) {
        cout << rotatedArray[i] << endl;
    }

    return 0;
}