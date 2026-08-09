# %%
from regex import B
from sympy import N
import Code2

print("Lee called")

# %%
def foo():
    global a
    a = 200 #全局作用域
    b = 100 #嵌套作用域
    
    def bar():
        nonlocal b
        global c
        b = 200
        c = 200       
    bar()
    print(b)
        
if __name__ == '__main__':
    a = 100
    c = 100

    foo()
    print(a, c)
# %%
