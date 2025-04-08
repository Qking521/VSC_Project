# main.py
# Python编程注意事项:
# 1. 使用明确的变量命名，遵循PEP 8规范。
# 2. 注意缩进，Python使用4个空格作为缩进标准。
# 3. 使用虚拟环境管理依赖，避免全局安装包冲突。
# 4. 捕获异常时尽量具体，避免使用裸的except。
# 5. 定期运行静态代码检查工具（如flake8或pylint）。
# 6. 写单元测试，确保代码的可靠性和可维护性。
# 7. 避免在循环中修改正在迭代的对象。
# 8. 使用with语句管理资源（如文件或网络连接）。

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