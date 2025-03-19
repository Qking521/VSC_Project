#!"C:\Program Files\Git\bin\bash"
# 设置编码为UTF-8
export LANG=en_US.UTF-8

# 打印当前日期和时间
echo "当前日期和时间: $(date)"

# 打印当前工作目录
echo "当前工作目录: $(pwd)"

# 列出当前目录下的所有文件和目录
echo "当前目录下的所有文件和目录:"
ls -la

# 打印系统信息
echo "系统信息:"
uname -a

# 打印磁盘使用情况
echo "磁盘使用情况:"
df -h

# 打印内存使用情况
echo "内存使用情况:"
free -h

# 打印环境变量
echo "环境变量:"
printenv

# 检查特定文件是否存在
FILE="/d/VSC_Project/somefile.txt"
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else
    echo "$FILE does not exist."
fi

# 读取用户输入
#read -p "请输入你的名字: " name
#echo "你好, $name!"

# 循环示例
echo "循环示例:"
for i in {1..5}; do
    echo "循环次数: $i"
done

# 函数示例
greet() {
    echo "Hello, $1!"
}

greet "World"