# 全局变量（在当前文件的任意位置都能使用）
a = 100
b = 200


def test():
    # 局部变量（只能在当前函数中使用）
    c = '抽烟'
    d = '烫头'
    # global a
    a = 300  # Python会创建一个局部变量a，值是300，这个a和全局的a是完全不同的两个变量，除非声明a是全局变量
    print('函数中的打印(a)', a)
    print('函数中的打印(b)', b)
    print('函数中的打印(c)', c)
    print('函数中的打印(d)', d)


test()
print('全局的打印(a)', a)
print('全局的打印(b)', b)
print(a)


# 局部作用域和局部变量，会在函数调用时创建，在函数执行结束后销毁
def test2():
    m = 100
    m += 1
    print(m)


test2()
test2()

# 全局作用域和全局变量，会在程序开始时创建，在函数程序结束后销毁
n = 100


def test3():
    global n
    n += 1
    print(f'我是test3函数中打印的n:{n}')


test3()
test3()
test3()
print(n)
