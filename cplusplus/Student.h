#ifndef STUDENT_H
#define STUDENT_H

#include "string"

class Student
{
private:
    std::string name;
    int age;
public:
    Student(const std::string& name, int age);
    ~Student();
    void setName(const std::string& name);
    void setAge(int age);

    std::string getName() const;
    int getAge() const;

    void displayInfo() const;
};
#endif //STUDENT_H