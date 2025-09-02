// this will be a mini c++ calculator with some gui interface for practise
#include <iostream>
#include <limits>
#include <cmath>   // for isnan

using namespace std;

class Calculator {

public:
    double add(double a, double b)
    { return a + b; }

    double subtract(double a, double b)
    { return a - b; }

    double multiply(double a, double b) 
    { return a * b; }

    double divide(double a, double b) {
        if (b == 0) {
            cerr << "Error: Cannot divide by zero!" << endl;
            return numeric_limits<double>::quiet_NaN(); // Return NaN
        }
        return a / b;
    }
};

void displayMenu() {
    cout << "C++ Calculator" << endl;
    cout << "1. Add" << endl;
    cout << "2. Subtract" << endl;
    cout << "3. Multiply" << endl;
    cout << "4. Divide" << endl;
    cout << "5. Exit" << endl;
    cout << "Choose an option: ";
}

int main() {
    Calculator calc;
    int choice = 0;
    double num1, num2;

    while (true) {
        displayMenu();
        cin >> choice;
        if (choice == 5) {
            cout << "Exiting the calculator. Goodbye!" << endl;
        }

        
        cout << "Enter the first number: ";
        cin >> num1;
        cout << "Enter the second number: ";
        cin >> num2;


        double result = 0;
        switch (choice) {
            case 1:
                result = calc.add(num1, num2);
                cout << "Result: " << result << endl;
                
            case 2:
                result = calc.subtract(num1, num2);
                cout << "Result: " << result << endl;
                
            case 3:
                result = calc.multiply(num1, num2);
                cout << "Result: " << result << endl;
                
            case 4:
                result = calc.divide(num1, num2);
                if (!isnan(result)) {
                    cout << "Result: " << result << endl;
                }
                
            default:
                cerr << "Invalid choice. Please try again." << endl;
        }

        cout << endl;
    }

    return 0;
}
