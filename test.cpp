#include <iostream>
using namespace std;
int main(void) {
int number[] = {23, 18, 22, 65, 97};
int x = number[0];
int i=1;
NEXT:
      if (number[i] < x) x = number[i];
      i++;
      if (i < 5) goto NEXT;
cout << x << endl;
}
