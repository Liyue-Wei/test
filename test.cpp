#include<iostream>
using namespace std;
int main()
{

    int i, n=10, t=20;
    bool T=false;
    if(!T){
        i=n;
    }

    else{
        i=t;
    }
    cout<<i<<endl;

    i = T ? n:t;
    cout<<i<<endl;
}
