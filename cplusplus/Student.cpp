#include "Student.h"
#include <iostream>

using namespace std;

Student::Student(const std::string& name, int age) : name(name), age(age) {}

void Student::setName(const string& name){
    this->name = name;
}

void Student::setAge(int age){
    this->age = age;
}

string Student::getName() const {
    return name;
}

int Student::getAge() const {
    return age;
}

void Student::displayInfo() const {
    cout << "name = " << name << " ,age " << age << endl;
}

Student::~Student(){
    cout << "student has been destroyed" << endl;
}

