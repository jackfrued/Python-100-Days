## Python容器类型使用小技巧

Python中提供了非常丰富的容器型数据类型，大家最为熟悉的有`list`、`tuple`、`set`、`dict`等。下面为大家分享一些使用这些类型的小技巧，希望帮助大家写出更加Pythonic的代码。

### 从字典中取最大

假设字典对象对应的变量名为`my_dict`。

- 取出最大值

    ```Python
    max(my_dict.values())
    ```

- 取值最大值的键

    ```Python
    max(my_dict, key=my_dict.get)
    ```

- 取出最大值的键和值

    ```python
     max(my_dict.items(), key=lambda x: x[1])
    ```

    或

    ```Python
    import operator
    
    max(my_dict.items(), key=operator.itemgetter(1))
    ```
    
    > **说明**：上面用到了`operator`模块的`itemgetter`函数，这个函数的的作用如下所示。在上面的代码中，`itemgetter`帮我们获取到了二元组中的第2个元素。
    >
    > ```Python
    > def itemgetter(*items):
    >     if len(items) == 1:
    >         item = items[0]
    >         def g(obj):
    >             return obj[item]
    >     else:
    >         def g(obj):
    >             return tuple(obj[item] for item in items)
    >     return g
    > ```

### 统计列表元素出现次数

假设列表对象对应的变量名为`my_list`。

```Python
{x: my_list.count(x) for x in set(my_list)}
```

或

```Python
from itertools import groupby

{key: len(list(group)) for key, group in groupby(sorted(my_list))}
```

> **说明**：`groupby`函数会将相邻相同元素分到一个组中，所以先用`sorted`函数排序就是为了将相同的元素放到一起。

或

```Python
from collections import Counter

dict(Counter(my_list))
```

### 截断列表元素

假设列表对象对应的变量名为`my_list`，通常大家会想到用下面的方式来截断列表。
```Python
my_list = my_list[:i]
my_list = my_list[j:]
```

然而，更好的方式使用下面的操作，大家可以认真想想为什么。

```Python
del my_list[i:]
del my_list[:j]
```

### 按最长列表实现zip操作

Python的内置函数`zip`可以产生一个生成器对象，该生成器对象将两个或多个可迭代对象的元素组装到一起，如下所示。

```Python
list(zip('abc', [1, 2, 3, 4]))
```

执行上面的代码会得到一个如下所示的列表，相信大家也注意到了，列表中元素的个数是由`zip`函数中长度最小的可迭代对象决定的，所以下面的列表中只有3个元素。

```Python
[('a', 1), ('b', 2), ('c', 3)]
```

如果希望由`zip`函数中长度最大的可迭代对象来决定最终迭代出的元素个数，可以试一试`itertools`模块的`zip_longest`函数，其用法如下所示。

```Python
from itertools import zip_longest

list(zip_longest('abc', [1, 2, 3, 4]))
```

上面的代码创建出的列表对象如下所示。

```Python
[('a', 1), ('b', 2), ('c', 3), (None, 4)]
```

### 快速拷贝一个列表

如果希望快速拷贝一个列表对象，可以通过切片操作来实现，但是切片操作仅实现了浅拷贝，简单的说就是切片创建了新的列表对象，但是新列表中的元素是和之前的列表共享的。如果希望实现深拷贝，可以使用`copy`模块的`deepcopy`函数。

- 浅拷贝

    ```Python
    thy_list = my_list[:]
    ```

    或

    ```Python
    import copy
    
    thy_list = copy.copy(my_list)
    ```

- 深拷贝

    ```Python
    import copy
    
    thy_list = copy.deepcopy(my_list)
    ```

### 对两个或多个列表对应元素进行操作

Python内置函数中的`map`函数可以对一个可迭代对象中的元素进行“映射”操作，这个函数在批量处理数据时非常有用。但是很多人都不知道，这个函数还可以作用于多个可迭代对象，通过传入的函数对多个可迭代对象中的对应元素进行处理，如下所示。

```Python
my_list = [11, 13, 15, 17]
thy_list = [2, 4, 6, 8, 10]
list(map(lambda x, y: x + y, my_list, thy_list))
```

上面的操作会得到如下所示的列表。

```Python
[13, 17, 21, 25]
```

当然，同样的操作也可以用`zip`函数配合列表生成式来完成。

```Python
my_list = [11, 13, 15, 17]
thy_list = [2, 4, 6, 8, 10]
[x + y for x, y in zip(my_list, thy_list)]
```

### 处理列表中的空值和零值

假设列表对象对应的变量名为`my_list`，如果列表中有空值（`None`）和零值，我们可以用下面的方式去掉空值和零值。

```Python
list(filter(bool, my_list))
```

对应的列表生成式语法如下所示。

```Python
[x for x in my_list if x]
```

### 从嵌套列表中抽取指定列

假设`my_list`是一个如下所示的嵌套列表，该嵌套列表可以用来表示数学上的矩阵，如果要取出矩阵第一列的元素构成一个列表，我们可以这样写。

```Python
my_list = [
    [1, 1, 2, 2],
    [5, 6, 7, 8],
    [3, 3, 4, 4],
]
col1, *_ = zip(*my_list)
list(col1)
```

这里我们会得到一个如下所示的列表，刚好是矩阵的第一列。

```Python
[1, 5, 3]
```

以此类推，如果想取出矩阵第二列的元素构成一个列表，可以用如下所示的方法。

```Python
_, col2, *_ = zip(*my_list)
list(col2)
```

至此，如果要实现矩阵的转置操作，我们也可以按照上面的思路写出下面的代码。

```Python
[list(x) for x in zip(*my_list)]
```

经过上面的操作，我们会得到如下所示的列表。

```Python
[[1, 5, 3], 
 [1, 6, 3], 
 [2, 7, 4], 
 [2, 8, 4]]
```

### 小结

不知道上面的内容有没有触及到大家的知识盲区，如果有的话欢迎在评论区留言讨论。

  