# 定义函数
def greet(name, gender, age, height):
    print(f'我叫{name},性别{gender},年龄是{age},身高是{height}cm')


# 调用函数(使用关键字参数)
# 注意：使用关键字参数时，位置参数必须在关键字参数之前
greet(name='张三', gender='男', age=172, height=18)
greet(height=172, age=18, gender='男', name='张三')
greet('张三', '男', height=172, age=18)
