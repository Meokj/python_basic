# 定义函数（使用/和*限制传参方式）
def greet(name, /, gender, *, age, height):
    print(f'我叫{name},性别{gender},年龄是{age},身高是{height}cm')


# 调用函数(/前面只能用位置参数，*后面只能用关键字参数，/必须在*前面，否则报错)
greet('张三', '男', age=18, height=172)
greet('张三', gender='男', age=18, height=172)
