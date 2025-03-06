#include <iostream>
#include "Student.h"

using namespace std;

int main()
{
    
    cout <<  "hello world" << endl;

    Student student("wang", 30);
    student.displayInfo();

    Student* pStudent = new Student("qiang", 36);
    pStudent->displayInfo();
    delete pStudent;
  
}