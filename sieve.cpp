// This is a script to generate a file with all of the primes less than a given maximum

#include <iostream>
#include <cmath>
#include <fstream>
#include <string>
#include <cstdio>
#include <ctime>

using namespace std;

int main(){
  int max;
  cout << "What is the maximum? ";
  cin >> max;
  if (max < 2){
    cout << "Invalid choice of maximum." << endl;
    return 0;
  }
  // timer setup
  clock_t start;
  double duration;
  start = clock();
  
  int nums[max-1];
  // first we initialize our candidtes of primes
  for (int i = 0; i <= max-2; i++){
    nums[i] = i+2;
  }
  int num = 2;
  int mul;
  while (num <= ceil(sqrt(max))){
    mul = 2*num; // initial multiple
    while (mul <= max){
      nums[mul - 2] = 0;
      mul += num;      
    }
    num+=1;
    while (num <= max && nums[num - 2] == 0){
      num += 1;
    }
  } 
  // now, nums should have a 0 value if the number isn't prime and prime otherwise
  string filename = "primes_up_to_" + to_string(max) + ".txt";
  ofstream myout;
  myout.open(filename);
  for (int i = 0; i <= max-2; i++){
    if (nums[i] != 0){
      myout << nums[i] << endl;
    }
  }
  myout.close();

  duration = ( clock() - start ) / (double) CLOCKS_PER_SEC;
  cout << "printf: " << duration << '\n';
  return 0;
}
