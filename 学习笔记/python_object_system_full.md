# Python 对象体系全景图（完整版本）

## 📑 目录（TOC）

-   [1. Python 中的 object 是一切的根](#1-python-中的-object-是一切的根)
-   [2. object → collections.abc
    行为体系](#2-object--collectionsabc-行为体系)
    -   [2.1 Iterable（可迭代）](#21-iterable可迭代)
    -   [2.2 Sequence（序列）](#22-sequence序列)
    -   [2.3 Set（集合）](#23-set集合)
    -   [2.4 Mapping（映射）](#24-mapping映射)
    -   [2.5 Iterator（迭代器）](#25-iterator迭代器)
    -   [2.6 Generator（生成器）](#26-generator生成器)
    -   [2.7 Hashable（可哈希）](#27-hashable可哈希)
    -   [2.8 Callable（可调用）](#28-callable可调用)
-   [3. Python 数值体系（numbers 模块）](#3-python-数值体系numbers-模块)
-   [4. I/O 类型](#4-io-类型)
-   [5. 模块对象 module](#5-模块对象-module)
-   [6. 类与实例体系](#6-类与实例体系)
-   [7. 上下文管理器](#7-上下文管理器)
-   [8. 特殊类型](#8-特殊类型)
-   [9. 完整树形结构总结](#9-完整树形结构总结)
-   [10. 终极总结](#10-终极总结)

------------------------------------------------------------------------

# 1. Python 中的 object 是一切的根

Python 采用统一对象模型（Everything is an object）。

所有内容（int、list、dict、class、function...）都继承自 object。

------------------------------------------------------------------------

# 2. object → collections.abc 行为体系

collections.abc 定义了容器、序列、映射等行为规范。

------------------------------------------------------------------------

# 2.1 Iterable（可迭代）

    Iterable
    ├── Container
    ├── Sized
    └── Sequence

Iterable 典型类型：

-   list / tuple / dict / set\
-   str / bytes\
-   range\
-   file 对象\
-   generator

------------------------------------------------------------------------

# 2.2 Sequence（序列）

序列 = 有序 + 可索引。

    Sequence
    ├── list（可变）
    ├── tuple（不可变）
    ├── range（不可变）
    ├── str（不可变字符序列）
    └── bytes（不可变字节序列）

可变序列：

    MutableSequence
    └── list

------------------------------------------------------------------------

# 2.3 Set（集合）

    Set
    ├── set（可变）
    └── frozenset（不可变）

------------------------------------------------------------------------

# 2.4 Mapping（映射）

    Mapping
    ├── dict（可变）
    └── MappingProxyType（只读映射）

------------------------------------------------------------------------

# 2.5 Iterator（迭代器）

    Iterator
    ├── list_iterator
    ├── tuple_iterator
    ├── range_iterator
    └── dict_*iterator

只要实现了 **next** 和 **iter**，就是迭代器。

------------------------------------------------------------------------

# 2.6 Generator（生成器）

    Generator
    └── generator（yield）

------------------------------------------------------------------------

# 2.7 Hashable（可哈希）

可作为字典 key 或 set 元素。

    Hashable
    ├── int
    ├── float
    ├── str
    ├── bytes
    ├── tuple（内部全可哈希）
    └── frozenset

------------------------------------------------------------------------

# 2.8 Callable（可调用）

能执行 "()" 的就是 Callable。

    Callable
    ├── function
    ├── method
    ├── class（可实例化）
    └── 实现 __call__ 的对象

示例：

``` python
class A:
    def __call__(self):
        print("callable")
```

------------------------------------------------------------------------

# 3. Python 数值体系（numbers 模块）

    Number
    ├── Integral → int
    ├── Real → float
    ├── Complex → complex
    └── Rational → Fraction

------------------------------------------------------------------------

# 4. I/O 类型

    TextIOWrapper（文本文件）
    BufferedReader
    BufferedWriter
    BytesIO
    StringIO

------------------------------------------------------------------------

# 5. 模块对象 module

    module（如 math、os、sys）

模块也是对象。

------------------------------------------------------------------------

# 6. 类与实例体系

    type（类的类型）
    └── class A
          └── A 实例对象

------------------------------------------------------------------------

# 7. 上下文管理器

只要实现了：

    __enter__()
    __exit__()

即可用于 with 语句。

典型例子：文件、锁、数据库连接等。

------------------------------------------------------------------------

# 8. 特殊类型

    NoneType（None）
    bool
    ellipsis（...）
    NotImplementedType
    memoryview
    bytearray（可变字节序列）

------------------------------------------------------------------------

# 9. 完整树形结构总结

    object
     ├── Iterable
     │     ├── Sequence（list, tuple, range, str, bytes）
     │     ├── MutableSequence（list）
     │     ├── Set（set, frozenset）
     │     ├── Mapping（dict）
     │     ├── Iterator（所有迭代器）
     │     └── Generator
     │
     ├── Hashable（int, str, tuple, frozenset, bytes）
     │
     ├── Callable（函数、类、方法、__call__ 对象）
     │
     ├── Number（int, float, complex, Fraction）
     │
     ├── IO（文件对象、缓冲区）
     │
     ├── module（math, os...）
     │
     ├── type（所有类的类型）
     │
     ├── 自定义 class 与实例
     │
     └── 特殊类型（NoneType, bool, ellipsis 等）

------------------------------------------------------------------------

# 10. 终极总结

Python 的体系本质是：

> **行为驱动（Protocol / ABC）+ 鸭子类型（Duck Typing）**\
> 只要对象实现了对应方法（协议），就被视为该类。

例如：

-   有 `__iter__` → Iterable\
-   有 `__getitem__` → Sequence 行为\
-   有 `__next__` → Iterator\
-   有 `__call__` → Callable

Python 是通过行为判断，而不是类型名字判断。

------------------------------------------------------------------------

（全文结束）
