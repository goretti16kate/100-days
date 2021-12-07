#include<iostream>
#include <cmath>
using namespace std;
int main(){
    int Name;
    int Deposit;
    int Shares;
    int Interest;
    int Savings;
    cout << "Enter your Name : " <<endl;
    getline(cin,Name);
    cout << "Enter your Deposit : " <<endl;
    cin >> Deposit;
    cout << "Enter the amount of Shares : "<<endl;
    cin >> Shares;
    cout << "Hello: " << Name <<endl;
    cout << "Your Deposit is : " << Deposit <<endl;
    cout << "Your Shares are : " << Shares <<endl;
    //interest
    if(Shares>100000)
        {
            Interest = 0.05 * Shares;
            cout << "Your Interest amounts to : " << Interest <<endl;
        }
        else
        {
            Interest = 0.03 * Shares;
            cout <<"Your Interest amounts to : " << Interest <<endl;
        }
    return 0;
    //Savings
    Savings = Deposit + Shares + Interest;
    cout << "Your Total Savings Amount To : " << Savings <<endl;
}