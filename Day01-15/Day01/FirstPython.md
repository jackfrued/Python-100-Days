## Day01 - First Python

### Introduction to Python

#### History of Python

1. Christmas 1989: Guido von Rossum began writing compilers for the Python language.
2. February 1991: The first Python compiler (also an interpreter) was born, which was implemented in C (there were Java and C# implementations of Jython and IronPython, and PyPy, Brython, Pyston, etc.). Other implementations), you can call library functions in C language. In the earliest versions, Python already provided support for building blocks such as "classes", "functions", "exception handling", and provided core data types such as "list" and "dictionary", while supporting module-based. Expansion system.
3. January 1994: Python 1.0 is officially released.
4. October 16, 2000: Python 2.0 released, adding a complete [garbage collection] (https://en.wikipedia.org/wiki/%E5%9E%83%E5%9C%BE%E5% 9B%9E%E6%94%B6_(%E8%A8%88%E7%AE%97%E6%A9%9F%E7%A7%91%E5%AD%B8)), and supports [Unicode](https ://zh.wikipedia.org/wiki/Unicode). At the same time, the entire development process of Python is more transparent, the community's influence on the development progress is gradually expanding, and the ecosystem is slowly forming.
5. December 3, 2008: Python 3.0 released, this version is not fully compatible with the previous Python code, but many new features were later ported to the old Python 2.6/2.7 version, because there are still companies in the project and operation and maintenance Use the Python 2.x version of the code.

The version of Python 3.6.x we are currently using was released on December 23, 2016. The version number of Python is divided into three sections, which are shaped like A.B.C. Where A indicates the large version number, generally when the overall rewrite, or the change is not backward compatible, increase A; B indicates the function update, increase B when new features appear; C indicates small changes (such as fixing a bug) ), increase C as long as there is a change. If you're interested in the history of Python, check out a blog post titled "A Brief History of Python" (http://www.cnblogs.com/vamei/archive/2013/02/06/2892628.html).

#### Advantages and disadvantages of Python

The advantages of Python are many, and the simple ones can be summarized as follows.

1. Simple and clear, there is only one way to do one thing.
2. The learning curve is low, and it is easier to get started with many other languages.
3. Open source, with a strong community and ecosystem.
4. Interpreted language, perfect platform portability.
5. Support two mainstream programming paradigms, using object-oriented and functional programming.
6. Extensibility and embeddability, can call C / C + + code can also be called in C / C + +.
7. The code is highly standardized and readable, suitable for people with code cleanliness and obsessive-compulsive disorder.

The shortcomings of Python are mainly focused on the following points.

1. Execution is inefficient, so computationally intensive tasks can be written in C/C++.
2. The code can't be encrypted, but many companies don't sell software but sell services. This problem will gradually fade.
3. There are too many frameworks to choose from during development, and there are errors in the choices.

#### Python applications

Currently, Python has a wide range of applications in cloud infrastructure, DevOps, web crawler development, data analysis mining, machine learning, etc., so it also serves in server development, data interface development, automated operation and maintenance, scientific computing and data visualization, and chat bots. Most used in image recognition and image processing


#### Windows Setup

### Building a programming environment

#### Windows Environment

You can download the Python Windows installer (exe file) from [Python's official website] (https://www.python.org). Note that if you install in Windows 7, you need to install the Service Pack 1 patch. (It can be installed by some tool software to automatically install the system patch function). It is recommended to check "Add Python 3.6 to PATH" (add Python 3.6 to PATH environment variable) and select custom installation. Set "Optional Features" It is best to check all the items "pip", "tcl/tk", "Python test suite", etc. It is highly recommended to use a custom installation path and ensure that there is no Chinese in the path. After the installation is complete, you will see the prompt "Setup was successful", but when you start the Python environment, the Python interpreter may not run due to missing some dynamic link library files. The common problem is mainly api-ms-win-crt\* The .dll is missing and some DirectX library files are missing after updating DirectX. The former can be processed according to the method described in [api-ms-win-crt\*.dll Missing Cause Analysis and Solution] () or directly Download the Visual C++ Redistributable for Visual Studio 2015 file for repair at [Microsoft's official website] (https://www.microsoft.com/en-us/download/details.aspx?id=48145), which can download a DirectX repair tool Repair it.

#### Linux Environment

The Linux environment comes with Python 2.x, but if you want to update to the 3.x version, you can download the Python source code and pass the source code on [Python's official website] (https://www.python.org). Install the installation method, the specific steps are as follows.

Install dependent libraries (because these dependent libraries may fail when the source code artifacts are installed because of missing the underlying dependencies).

```Shell
Yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
```

Download the Python source code and extract it to the specified directory.

```Shell
Wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tar.xz
Xz -d Python-3.6.1.tar.xz
Tar -xvf Python-3.6.1.tar
```

Switch to the Python source directory and execute the following commands to configure and install.

```Shell
Cd Python-3.6.1
./configure --prefix=/usr/local/python3.6 --enable-optimizations
Make && make install
```

Create a soft link so you can launch the Python interpreter directly from python3.

```Shell
Ln -s /usr/local/python3.6/bin/python3 /usr/bin/python3
```


#### MacOS Environment

MacOS comes with the Python 2.x version. The 3.x version can be installed via the installation file (pkg file) provided by [Python's official website] (https://www.python.org). After the default installation is complete, you can start the 2.x version of the Python interpreter by executing the python command on the terminal. You can start the 3.x version of the Python interpreter by executing the python3 command. Of course, you can also modify the startup by resetting the soft link. The Python interpreter command.

### Running Python programs from the terminal

#### Confirm the version of Python

Type the following command at the terminal or command line prompt.

```Shell
Python --version
```
Of course, you can also enter python into the interactive environment, and then execute the following code to check the Python version.

```Python
Import sys

Print(sys.version_info)
Print(sys.version)
```

#### Writing Python source code

You can use the text editing tools (recommended to use Sublime, Atom, TextMate, VSCode and other advanced text editing tools) to write Python source code and save it as hello.py, the code content is as follows.

```Python
Print('hello, world!')
```

#### Running the program

Switch to the directory where the source code is located and execute the following command to see if "hello, world!" is output on the screen.

```Shell
Python hello.py
```

### Comments in the code

Annotations are an important part of the programming language. They are used to interpret the code in the source code to enhance the readability and maintainability of the program. Of course, you can also remove the code segments in the source code that do not need to be run. This is often used when debugging programs. Comments are removed when the source code enters the preprocessor or compiles, and are not retained in the target code and do not affect the execution results of the program.

1. Single line comment - part beginning with # and space
2. Multi-line comments - three quotes at the beginning, three quotes at the end

```Python
"""

The first Python program - hello, world!
Pay tribute to the great Mr. Dennis M. Ritchie

Version: 0.1
Author: Luo Wei
Date: 2018-02-26

"""

Print('hello, world!')
# print("Hello, the world!")
Print('hello', 'world')
Print('hello', 'world', sep=', ', end='!')
Print('goodbye, world', end='!\n')
```

### Other tools introduction

#### IDLE - Built-in integrated development tools

IDLE is an integrated development tool that comes with the Python environment, as shown in the following figure. But because IDLE's user experience is not so good, it is rarely used in actual development.

![](./res/python-idle.png)

#### IPython - Better interactive programming tools

IPython is a Python-based interactive interpreter. IPython provides more powerful editing and interactivity than the native Python Shell. IPython and Jupyter can be installed via Python's package management tool pip, as shown below.

```Shell
Pip install ipython jupyter
```

or

```Shell
Python -m pip install ipython jupyter
```

After the installation is successful, you can start IPython with the following ipython command, as shown in the following figure.

![](./res/python-ipython.png)

Of course, we can also use the Jupyter to run a project called notebook in the browser window interactive operation.

```Shell
Jupyter notebook
```

![](./res/python-jupyter-1.png)

![](./res/python-jupyter-2.png)

#### Sublime - Text Editing Artifact

![](./res/python-sublime.png)

- First you can install Sublime 3 or Sublime 2 by downloading the installer from [Official Website] (https://www.sublimetext.com/).

- Install package management tools. Open the console with the shortcut Ctrl+` or select Show Console from the View menu and enter the code below.

  - Sublime 3

  ```Python
  Import urllib.request,os;pf='Package Control.sublime-package';ipp=sublime.installed_packages_path();urllib.request.install_opener(urllib.request.build_opener(urllib.request.ProxyHandler()));open( Os.path.join(ipp,pf),'wb').write(urllib.request.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')) .read())
  ```

  - Sublime 2

  ```Python
  Import urllib2,os;pf='Package Control.sublime-package';ipp=sublime.installed_packages_path();os.makedirs(ipp)ifnotos.path.exists(ipp)elseNone;urllib2.install_opener(urllib2.build_opener(urllib2. ProxyHandler()));open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ', '%20')).read());print('Please restart Sublime Text to finish installation')
  ```

- Install the plugin. Open the command panel through the Package Control of the Preference menu or the shortcut key Ctrl+Shift+P. Enter the Install Package in the panel to find the tool to install the plugin, and then find the required plugin. We recommend that you install the following plugins.

  - SublimeCodeIntel - Code Completion Tool Plugin
  - Emmet - front-end development code template plugin
  - Git - Version Control Tool Plugin
  - Python PEP8 Autoformat - PEP8 specification autoformatting plugin
  - ConvertToUTF8 - Convert local encoding to UTF-8

#### PyCharm - Python Development Artifact

The installation, configuration and use of PyCharm will be introduced later.

![](./res/python-pycharm.png)

### Exercise

1. In the Python interactive environment, the following code looks at the results and translates the content into Chinese.

    ```Python
    Import this

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Though practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Though never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    ```

2. Learn to use the turtle to draw graphics on the screen.
    ```Python
    import turtle

    turtle.pensize(4)
    turtle.pencolor('red')
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.mainloop()
    ```
