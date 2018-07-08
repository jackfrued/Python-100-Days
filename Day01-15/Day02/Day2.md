## Day02 - Language Elements

#### Instructions and Programs

A computer's hardware system typically consists of five major components, including: an operator, a controller, a memory, an input device, and an output device. Among them, the operator and controller are put together as what we usually call the central processor, its function is to execute various arithmetic and control instructions and process the data in the computer software. What we usually call a program is actually a collection of instructions. Our program organizes a series of instructions in a way that is used to control the computer to do what we want it to do. The computer we use today, although the device is more and more sophisticated, the processing power is more and more powerful, but in essence it still belongs to ["von Neumann structure"] (https://en.wikipedia.org/wiki /%E5%86%AF%C2%B7%E8%AF%BA%E4%BC%8A%E6%9B%BC%E7%BB%93%E6%9E%84) Computer. The "von Neumann structure" has two key points. One is to separate the storage device from the central processor, and the second is to encode the data in binary mode. Binary is a kind of counting method that “every two times into one”. There is no substantial difference between the counting method of “ten and ten in one” used by humans. Humans use decimal because they have ten fingers (because when counting After ten fingers are used up, they can only carry in. Of course, there are exceptions. The Maya may have counted their toes because of their bare feet for a long time, so they used the twenty-digit counting method. Under the guidance of the counting method, the Maya calendar is not consistent with ours. According to the Maya calendar, 2012 is the last year of the so-called “Sun Ji”, and in 2013 it is the new “Sun”. The beginning of Ji, and later this matter was misrepresented in the way of rumors that 2012 is the absurd saying of the end of the world predicted by the Maya. Today we can boldly speculate that the reason why the development of Maya civilization is slow is also estimated to be used. Decimal), for the computer, binary is the easiest to implement on physical devices (high voltage means 1, low voltage means 0), so in the "von Neumann knot Computers use binary. Although we don't need every programmer to work in binary way, we understand the binary and its conversion relationship with the decimals in our lives, and the binary and octal and hexadecimal conversions. necessary. If you are unfamiliar with this, you can use [Wikipedia] (https://zh.wikipedia.org/wiki/%E4%BA%8C%E8%BF%9B%E5%88%B6) or [degrees Niang] (https://www.baidu.com) popular science.
### Variables and types

In programming, a variable is a vector that stores data. The variables in the computer are the actual data or a memory space in which the data is stored in the memory. The values ​​of the variables can be read and modified, which is the basis of all calculations and controls. There are many types of data that a computer can process. In addition to numerical values, it can process text, graphics, audio, video, and other data. Different data needs to define different storage types. There are many types of data in Python, and it also allows us to customize new data types (as we'll see later). Let's start with a few common data types.

- Integer: Python can handle integers of any size (Python 2.x has both int and long integers, but this distinction does not make much sense to Python, so in Python 3.x integers only int This one), and supports binary (such as `0b100`, converted to decimal is 4), octal (such as `0o100`, converted to decimal is 64), decimal (`100`) and hexadecimal (`0x100 `, converted to decimal is 256) representation.
- Floating point type: Floating point number is also a decimal number. It is called floating point number because the decimal point position of a floating point number is variable according to scientific notation. The floating point number is not only mathematically written (such as `123.456`). In addition to scientific notation (such as `1.23456e2`).
- String: Strings are any text enclosed in single or double quotes, such as `'hello'` and `"hello"`, as well as strings, raw string notation, byte string notation, Unicode string notation, and can be written in multiple lines (starting with three single quotes or three double quotes, three single quotes or three double quotes).
- Boolean: Boolean values ​​are only `True`, `False`, either `True` or `False`. In Python, you can use `True`, `False` to represent Boolean values ​​(please note) The case can also be calculated by Boolean operations (for example, `3 < 5` will produce a Boolean value of `True`, and `2 == 1` will produce a Boolean value `False`).
- Plural type: The shape is like `3+5j`, which is the same as the mathematical plural representation. The only difference is that the i of the imaginary part is replaced by j.

#### Variable naming

For each variable we need to give it a name, just as each of us has its own loud name. In Python, variable naming needs to follow the following non-hard rules that must be followed by hard rules and strongly recommended.

- Hard rules:
  - Variable names consist of letters (generalized Unicode characters, excluding special characters), numbers, and underscores, and numbers cannot begin.
  - Case sensitive (the uppercase `a` and lowercase `A` are two different variables).
  - Don't conflict with keywords (words with special meanings, as discussed later) and system reserved words (such as names of functions, modules, etc.).
- PEP 8 requirements:
  - Spell in lowercase letters and connect multiple words with underscores.
  - Protected instance properties begin with a single underscore (described later).
  - Private instance properties start with two underscores (described later).

Of course, as a professional programmer, it is also important to name variables (in fact, all identifiers) to be known.

#### Use of variables

The following is a few examples to illustrate the type of variables and the use of variables.

```Python
"""

Use variables to save data and perform arithmetic operations

Version: 0.1
Author: 骆昊
Date: 2018-02-27

"""

a = 321
b = 123
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

```

```Python
"""

Use the input function to enter
Type conversion using int()
Format the output string with a placeholder

Version: 0.1
Author: 骆昊
Date: 2018-02-27

"""

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

```

```Python
"""

Check the type of the variable using type()
Version: 0.1
Author: 骆昊
Date: 2018-02-27

"""

a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

```

在对变量类型进行转换时可以使用Python的内置函数（准确的说下面列出的并不是真正意义上的函数，而是后面我们要讲到的创建对象的构造方法）。

- int(): Converts a numeric value or string to an integer, which can be specified in hexadecimal.
- float(): Converts a string to a floating point number.
- str(): Converts the specified object to a string and specifies the encoding.
- chr(): Converts an integer to the string (one character) corresponding to the encoding.
- ord(): Converts a string (a character) to the corresponding encoding (integer).

### Operator

Python supports a variety of operators. The following table lists all the operators in order of priority from high to low, and we will use them one after another.

| Operator                                                     | Description                    |
| ------------------------------------------------------------ | ------------------------------ |
| `[]` `[:]`                                                   | Subscript, Slice               |
| `**`                                                         | power                          |
| `~`                                                          | Bitwise Negation, Addition, Subtraction|
| `*` `/` `%` `//`                                             | Multiplication,Division,                                                                                             Modulus,Floor Division|
| `+` `-`                                                      | Addition, Subtraction          |
| `>>` `<<`                                                    | Binary Left Shift, Right Shift |
| `&`                                                          | Binary And                     |
| `^` `|`                                                      | Bitwise XOR, Bitwise OR        |
| `<=` `<` `>` `>=`                                            | Less/Equal to, Less than, Greaterthan,                                                                            Greater than or equal to |
| `==` `!=`                                                    | is Equal to, Not Equal to      |
| `is`  `is not`                                               | Checks if it is same object    |
| `in` `not in`                                                | Checks occurence in iterable   |
| `not` `or` `and`                                             | Logical operators              |
| `=` `+=` `-=` `*=` `/=` `%=` `//=` `**=` `&=` `|=` `^=` `>>=` `<<=` | Composite Assignment operators
** Description: ** In actual development, if you don't know the priority, you can use parentheses to ensure the order of execution of the operation.
The following example demonstrates the use of operators.
```Python
"""

Use of operators

Version: 0.1
Author: 骆昊
Date: 2018-02-27

"""

a = 5
b = 10
c = 3
d = 4
e = 5
a += b
a -= c
a *= d
a /= e
print("a = ", a)

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is not False)

```

### Exercise

#### Exercise 1: Fahrenheit temperature to Celsius.

```Python
"""

Convert Fahrenheit to Celsius
F = 1.8C + 32

Version: 0.1
Author: 骆昊
Date: 2018-02-27

"""

f = float(input('Please enter Fahrenheit: '))
c = (f - 32) / 1.8
Print('%.1fFahrenheit = %.1f degrees Celsius' % (f, c))

```

#### Exercise 2: Enter the radius of the circle to calculate the perimeter and area.

```Python
"""

Enter the radius to calculate the perimeter and area of the circle

Version: 0.1
Author: 骆昊
Date: 2018-02-27

"""
import math

radius = float(input('Enter the radius of circle: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('Perimeter: %.2f' % perimeter)
print('Area: %.2f' % area)

```

#### Exercise 3: Enter the year to determine whether it is a leap year.

```Python
"""

Enter the year If it is a leap year output True, otherwise output False

Version: 0.1
Author: 骆昊
Date: 2018-02-27

"""

year = int(input('Enter a year: '))
# If the code is too long to write in a line, it is not easy to read. You can use \ or () to fold
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)
```

