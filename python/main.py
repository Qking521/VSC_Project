# main.py

# 1. Hello World Example
def hello_world():
    print("Hello, World!")

# 2. Basic Arithmetic Example
def basic_arithmetic():
    a = 10
    b = 5
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")

# 3. List Example
def list_example():
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(f"I like {fruit}")

# 4. Dictionary Example
def dictionary_example():
    person = {"name": "Alice", "age": 25, "city": "New York"}
    for key, value in person.items():
        print(f"{key}: {value}")

# 5. Function Example
def greet(name):
    return f"Hello, {name}!"

# 6. Class Example
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# 7. File Handling Example
def file_handling_example():
    with open("example.txt", "w") as file:
        file.write("This is a file handling example.")
    with open("example.txt", "r") as file:
        print(file.read())

# 8. Exception Handling Example
def exception_handling_example():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error: {e}")

# Main function to run all examples
if __name__ == "__main__":
    print("1. Hello World Example:")
    hello_world()
    print("\n2. Basic Arithmetic Example:")
    basic_arithmetic()
    print("\n3. List Example:")
    list_example()
    print("\n4. Dictionary Example:")
    dictionary_example()
    print("\n5. Function Example:")
    print(greet("Bob"))
    print("\n6. Class Example:")
    dog = Animal("Dog")
    print(dog.speak())
    print("\n7. File Handling Example:")
    file_handling_example()
    print("\n8. Exception Handling Example:")
    exception_handling_example()