"""
变量的作用域以及Python搜索变量的顺序
LEGB: Local --> Embedded --> Global --> Built-in
global - 声明或定义全局变量（要么直接使用现有的全局作用域的变量，要么定义一个变量放到全局作用域）
nonlocal - 声明使用嵌套作用域的变量（如果嵌套作用域没有对应的变量直接报错）
"""
x = 100


def foo():
    global x
    x = 200

    def bar():
        x = 300
        print(x)

    bar()
    print(x)


foo()
print(x)
