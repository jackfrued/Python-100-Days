## Python - From Novice to Master in 100 Days

> **author**: Luo Hao
>
> **illustrate**: From the launch of the project to the acquisition of 8w+ stars, I have always received feedback that the basic part (the content of the first 15 days) is difficult for beginners, and it is recommended to have a supporting video to explain. Recently, the content of the basic part has been remade into a file called[“Python-Core-50-Courses”](https://github.com/jackfrued/Python-Core-50-Courses)s project,**Rewrote this part in a simpler and more popular way with video explanations**, beginners can pay attention to this new project. If needed**Python Basics Video**, you can search at "B station"["Python Zero Basic Quick Start"](https://www.bilibili.com/video/BV1FT4y1R7sz), this video is a video I recorded during my lectures. The picture quality and sound quality are acceptable, but it should be helpful for beginners. You are welcome to leave messages, comments, and barrage. After learning, friends who feel that they have gained something can "one-click three connections" to support the UP master (Qianfeng Python). If domestic users are slow to access GitHub, they can follow me**Zhihu account[Python-Jack](https://www.zhihu.com/people/jackfrued)**, the above["Learn Python from scratch"](https://zhuanlan.zhihu.com/c_1216656665569013760)The column is more suitable for beginners, and other columns are also being continuously created and updated. You are welcome to pay attention and like and comment.
>
> It is not easy to create. Thank you for your support. These funds will not be used for personal consumption (for example: buying coffee), but will be donated to those in need through platforms such as Tencent Charity, Meituan Charity, and Shuidichou ([click](./更新日志.md)Learn about donations). If you need to join the QQ learning group, you can scan the QR code below, add one to the three groups, and do not enter the group repeatedly. The study group will provide you with**Learning Resources**and**Questions and Answers**,If there is**Python experience class**and**Industry Open Course**We will notify everyone in advance in the group, and everyone is welcome to join.
>
> The "Day80~90" part of the project is still under creation, because the author usually can't squeeze too much time to write the document, so the update speed is relatively slow, thank you for your understanding.

<img src="https://gitee.com/jackfrued/mypic/raw/master/20211120192545.png">

### Analysis of Python application areas and career development

Simply put, Python is an "elegant", "clear" and "simple" programming language.

-   Low learning curve, even non-professionals can get started
-   Open source system with a strong ecosystem
-   Interpreted language, perfect platform portability
-   Dynamically typed language that supports object-oriented and functional programming
-   The code is standardized and highly readable

Python is useful in the following areas.

-   Backend Development - Python/Java/Go/PHP
-   DevOps - Python / Shell / Ruby
-   Data Acquisition - Python / C++ / Java
-   Quantitative Trading - Python / C++ / R
-   Data Science - Python/R/Julia/Matlab
-   Machine Learning - Python/R/C++/Julia
-   Automated Testing - Python/Shell

As a Python developer, depending on your personal preferences and career planning, you can choose from a lot of employment fields.

-   Python back-end development engineer (server, cloud platform, data interface)
-   Python operation and maintenance engineer (automated operation and maintenance, SRE, DevOps)
-   Python data analyst (data analysis, business intelligence, digital operations)
-   Python data mining engineer (machine learning, deep learning, algorithm expert)
-   Python crawler engineer
-   Python test engineer (automated testing, test development)

> **illustrate**:Currently,**Data analysis and data mining are very popular directions**, because both the Internet industry and traditional industries have accumulated a large amount of data, all walks of life need data analysts to find more business value from the existing data, so as to provide data support for the decision-making of enterprises, which is So-called data-driven decision-making.

A few suggestions for beginners:

-   Make English as your working language.
-   Practice makes perfect.
-   All experience comes from mistakes.
-   Don't be one of the leeches.
-   Either outstanding or out.

### Day01~15 -[Python language basics](./Day01-15)

#### Day01 -[Getting to know Python](./Day01-15/01.初识Python.md)

-   Introduction to Python - History of Python / Advantages and Disadvantages of Python / Areas of Application of Python
-   Build a programming environment - Windows environment / Linux environment / MacOS environment
-   Run a Python program from the terminal - Hello, world /`print`function / runner
-   Using IDLE - Interactive Environment (REPL) / Writing Multiple Lines of Code / Running Programs / Exiting IDLE
-   Comments - The role of comments / single-line comments / multi-line comments

#### Day02 -[language element](./Day01-15/02.语言元素.md)

-   Programs and Bases - Instructions and Programs / Von Neumann Machines / Binary and Decimal / Octal and Hexadecimal
-   Variables and Types - Naming of Variables / Use of Variables /`input`function / check variable type / type conversion
-   Numbers and Strings - Integer / Float / Complex / String / Basic String Operations / Character Encoding
-   Operators - Math Operators / Assignment Operators / Comparison Operators / Logical Operators / Identity Operators / Precedence of Operators
-   Application Case - Convert Fahrenheit to Celsius / Enter the radius of a circle to calculate the perimeter and area / Enter the year to determine whether it is a leap year

#### Day03 -[branch structure](./Day01-15/03.分支结构.md)

-   Application scenarios of branch structure - conditional / indentation / code block / flowchart
-   if statement - simple`if`/`if`-`else`structure /`if`-`elif`-`else`structure / nested`if`
-   Use Cases - User Authentication / Swap Imperial and Metric Units / Rolling Dice to Decide What to Do / Converting Percentages to Grades / Evaluating Piecewise Functions / Entering the Lengths of Three Sides and Calculating Perimeter and Area if They Can Form a Triangle

#### Day04 -[loop structure](./Day01-15/04.循环结构.md)

-   Application scenarios of loop structure - conditional / indentation / code block / flowchart
-   while loop - basic structure /`break`statement /`continue`statement
-   for loop - basic structure /`range`Types / Branching in Loops / Nested Loops / Ending a Program Early
-   Application Case - 1~100 Summation / Judging Prime Numbers / Number Guessing Game / Printing Nine-Nine Tables / Printing Triangle Patterns / Monkeys Eat Peach / Hundred Money Hundred Chickens

#### Day05 -[Constructor logic](./Day01-15/05.构造程序逻辑.md)

-   Classic Case: Daffodil Number / Hundred Money Hundred Chickens / Craps Gambling Game
-   Exercise questions: Fibonacci sequence / perfect numbers / prime numbers

#### Day06 -[Use of functions and modules](./Day01-15/06.函数和模块的使用.md)

-   What Functions Do - Bad Code Smell / Encapsulating Functional Modules with Functions
-   Define function -`def`keyword / function name / parameter list /`return`statement / call custom function
-   Calling functions - Python built-in functions / importing modules and functions
-   Function parameters - default parameters / variadic parameters / keyword parameters / named keyword parameters
-   Return value of function - no return value / return single value / return multiple values
-   Scope Issues - Local Scope / Nested Scope / Global Scope / Built-in Scope / Scope Related Keywords
-   Managing Functions with Modules - Concept of Modules / Managing Functions with Custom Modules / What Happens When There Are Name Conflicts (Same Module and Different Modules)

#### Day07 -[Strings and Common Data Structures](./Day01-15/07.字符串和常用数据结构.md)

-   Use of Strings - Length Calculation / Subscripting / Slicing / Common Methods
-   Basic usage of lists - define lists / access elements with the following table / subscript out of bounds / add elements / delete elements / modify elements / slice / loop through
-   List common operations - join / copy (copy elements and copy arrays) / length / sort / reverse / find
-   Generate a list - use`range`Create a list of numbers / generate expressions / generators
-   Use of tuples - define tuples / use values ​​in tuples / modify tuple variables / tuple and list conversions
-   Basic usage of sets - the difference between sets and lists / create a set / add elements / delete elements / empty
-   Common Set Operations - Intersection / Union / Difference / Symmetric Difference / Subset / Superset
-   Basic usage of dictionary - features of dictionary / create dictionary / add element / delete element / get value / clear
-   Common dictionary operations -`keys`method /`values`method /`items`method /`setdefault`method
-   Basic Exercises - Marquee Effect / Find the Largest Element in a List / Average Score of Statistical Test Scores / Fibonacci Sequence / Yang Hui's Triangle
-   Comprehensive case - two-color ball selection / tic-tac-toe

#### Day08 -[Object Oriented Programming Fundamentals](./Day01-15/08.面向对象编程基础.md)

-   Classes and Objects - What is a Class / What is an Object / Object Oriented Other Related Concepts
-   Defining Classes - Basic Structure / Properties and Methods / Constructors / Destructors /`__str__`method
-   Working with Objects - Creating Objects / Sending Messages to Objects
-   The Four Pillars of Object Orientation - Abstraction / Encapsulation / Inheritance / Polymorphism
-   Basic Exercises - Define Student Class / Define Clock Class / Define Graphics Class / Define Car Class

#### Day09 -[object-oriented advanced](./Day01-15/09.面向对象进阶.md)

-   Attributes - Class Attributes / Instance Attributes / Attribute Accessors / Attribute Modifiers / Attribute Deleters / Use`__slots__`
-   Methods in a class - instance method / class method / static method
-   Operator overloading -`__add__`/`__sub__`/`__or__`/`__getitem__`/`__setitem__`/`__len__`/`__repr__`/`__gt__`/`__lt__`/`__le__`/`__ge__`/`__eq__`/`__ne__`/`__contains__`
-   Relationship between classes (objects) - Association / Inheritance / Dependency
-   Inheritance and Polymorphism - What is Inheritance / Inheritance Syntax / Calling Parent Class Methods / Method Overriding / Type Determination / Multiple Inheritance / Diamond Inheritance (Diamond Inheritance) and C3 Algorithm
-   Comprehensive Case - Salary Settlement System / Book Automatic Discount System / Custom Score Class

#### Day10 -[Graphical User Interface and Game Development](./Day01-15/10.图形用户界面和游戏开发.md)

-   use`tkinter`Develop GUI programs
-   use`pygame`Third-party library to develop game applications
-   "Big Ball Eats Small Ball" Game

#### Day 11 -[files and exceptions](./Day01-15/11.文件和异常.md)

-   read file - read entire file / read line by line / file path
-   Write File - Overwrite Write / Append Write / Text File / Binary File
-   Exception Handling - The Importance of Exception Mechanisms /`try`-`except`code block /`else`code block /`finally`Code Blocks / Built-in Exception Types / Exception Stack /`raise`statement
-   Data Persistence - CSV File Overview /`csv`Module Application / JSON Data Format /`json`module application

#### Day12 -[Strings and Regular Expressions](./Day01-15/12.字符串和正则表达式.md)

-   String Advanced Operations - Escape Characters / Raw Strings / Multi-Line Strings /`in`and`not in`operator /`is_xxx`method /`join`and`split`method /`strip`related methods /`pyperclip`Modules / Immutable Strings and Mutable Strings /`StringIO`usage of
-   Getting Started with Regular Expressions - The Role of Regular Expressions / Metacharacters / Escaping / Quantifiers / Grouping / Zero Width Assertions / Greedy Matching vs Lazy Matching / Using Lazy`re`Modules implement regular expression operations (match, search, replace, capture)
-   Using regular expressions -`re`module /`compile`function /`group`and`groups`method /`match`method /`search`method /`findall`and`finditer`method /`sub`and`subn`method /`split`method
-   Use Case - Validating Input Strings Using Regular Expressions

#### Day13 -[processes and threads](./Day01-15/13.进程和线程.md)

-   The concept of process and thread - what is a process / what is a thread / application scenarios of multithreading
-   use process -`fork`function /`multiprocessing`Module / Process Pool / Interprocess Communication
-   use thread -`threading`module /`Thread`kind /`RLock`kind /`Condition`class / thread pool

#### Day14 -[Introduction to web programming and web application development](./Day01-15/14.网络编程入门和网络应用开发.md)

-   Computer Networking Fundamentals - History of Computer Networking / "TCP-IP" Model / IP Addresses / Ports / Protocols / Other Related Concepts
-   Web Application Mode - "Client-Server" Mode / "Browser-Server" Mode
-   Accessing Network Resources Based on HTTP Protocol - Network API Overview / Access URL /`requests`Third-party library / Parse JSON format data
-   Python network programming - the concept of sockets /`socket`module /`socket`Functions / Create TCP Server / Create TCP Client / Create UDP Server / Create UDP Client
-   Email - SMTP Protocol / POP3 Protocol / IMAP Protocol /`smtplib`module /`poplib`module /`imaplib`module
-   SMS Service - Invoke SMS Gateway

#### Day15 -[Image and document processing](./Day01-15/15.图像和办公文档处理.md)

-   Process pictures with Pillow - picture reading and writing / picture composition / geometric transformation / color transformation / filter effect
-   Read and write Word documents - processing of text content / paragraph / header and footer / style processing
-   Read and write Excel files -`xlrd`/`xlwt`/`openpyxl`

### Day16~Day20 -[Advanced Python language](./Day16-20/16-20.Python语言进阶.md)

-   Common data structures
-   Advanced Use of Functions - "First Class Citizens" / Higher Order Functions / Lambda Functions / Scope and Closures / Decorators
-   Advanced Object-Oriented Knowledge - "Three Pillars" / Relationship Between Classes / Garbage Collection / Magic Properties and Methods / Mixins / Metaclasses / Object-Oriented Design Principles / GoF Design Patterns
-   Iterators and Generators - Related Magic Methods / Two Ways to Create Generators /
-   Concurrency and Asynchronous Programming - Multithreading / Multiprocessing / Asynchronous IO /`async`and`awai`t

### Diaze 1~30 -[Getting Started with the Web Front End](./Day21-30/21-30.Web前端概述.md)

-   Host page content with HTML tags
-   Render the page with CSS
-   Handling interactive behavior with JavaScript
-   Getting Started and Improving with jQuery
-   Getting Started with Vue.js
-   Use of Elements
-   Use of Bootstrap

### Day31~35 -[Play with the Linux operating system](./Day31-35/31-35.玩转Linux操作系统.md)

-   Operating System History and Linux Overview
-   Linux basic commands
-   Utilities in Linux
-   Linux file system
-   Application of Vim editor
-   Environment Variables and Shell Programming
-   Software installation and service configuration
-   Network access and management
-   Other related content

### Day36~40 -[Database Basics and Advanced](./Day36-40)

-   An overview of relational databases
-   MySQL installation and use
-   Use of SQL
-   DDL - Data Definition Language -`create`/`drop`/`alter`
-   DML - Data Manipulation Language -`insert`/`delete`/`update`
-   DQL - Data Query Language -`select`
-   DCL - Data Control Language -`grant`/`revoke`
-   MySQL New Features
-   Application of window functions
-   JSON data type
-   related information
-   Data Integrity and Consistency
-   Views, functions, procedures, triggers
-   Transactions and Locks
-   Execution plan and index
-   Paradigm theory and anti-paradigm design
-   Manipulating MySQL in Python

### Day41~55 -[Actual Django](./Day41-55)

#### Day41 -[Getting started with Django](./Day41-55/41.Django快速上手.md)

-   Web application working mechanism
-   HTTP requests and responses
-   Django framework overview
-   Get started in 5 minutes

#### Day42 -[deep model](./Day41-55/42.深入模型.md)

-   Relational database configuration
-   Use ORM to complete CRUD operations on models
-   Use of management background
-   Django Model Best Practices
-   Model Definition Reference

#### Day43 -[Static resources and Ajax requests](./Day41-55/43.静态资源和Ajax请求.md)

-   load static resources
-   Ajax overview
-   Implement voting function with Ajax

#### Day44 -[Cookies and Sessions](./Day41-55/44.Cookie和Session.md)

-   Implement user tracking
-   The relationship between cookies and sessions
-   Django framework's support for sessions
-   Cookie read and write operations in view functions

#### Day45 -[Reports and Logs](./Day41-55/45.制作报表.md)

-   pass`HttpResponse`Modify response headers
-   use`StreamingHttpResponse`Handling large files
-   use`xlwt`Generate Excel reports
-   use`reportlab`Generate PDF report
-   Use ECharts to generate front-end charts

#### Day46 -[Log and debug toolbar](./Day41-55/46.日志和调试工具栏.md)

-   configuration log
-   Configure Django-Debug-Toolbar
-   Optimize ORM code

#### Day47 -[Application of middleware](./Day41-55/47.中间件的应用.md)

-   what is middleware
-   Middleware built into the Django framework
-   Custom middleware and its application scenarios

#### Day48 -[Getting started with front-end and back-end separation development](./Day41-55/48.前后端分离开发入门.md)

-   Returns data in JSON format
-   Rendering pages with Vue.js

#### Day49 -[Getting Started with RESTful Architecture and DRF](./Day41-55/49.RESTful架构和DRF入门.md)

#### Day50 -[RESTful Architecture and DRF Advancement](./Day41-55/50.RESTful架构和DRF进阶.md)

#### Day51 -[use cache](./Day41-55/51.使用缓存.md)

-   The first law of website optimization

-   Use Redis to provide caching services in Django projects

-   Read and write cache in view function

-   Page caching using decorators

-   Provide caching services for data interfaces

#### Dizzy -[Access to the third-party platform](./Day41-55/52.接入三方平台.md)

-   File upload form controls and image file preview
-   How to handle uploaded files on the server side

#### submissive -[Asynchronous tasks and scheduled tasks](./Day41-55/53.异步任务和定时任务.md)

-   The second law of website optimization
-   Configuring the Message Queuing Service
-   Use Celery to achieve task asynchrony in the project
-   Implementing scheduled tasks using Celery in the project

#### Day54 -[unit test](./Day41-55/54.单元测试.md)

#### dick -[The project is online](./Day41-55/55.项目上线.md)

-   Unit Testing in Python
-   Django framework support for unit testing
-   Use a version control system
-   Configure and use uWSGI
-   Dynamic and static separation and Nginx configuration
-   Configure HTTPS
-   Configure domain name resolution

### Daykht~60 -[Develop data interface with FastAPI](./Day56-60/56-60.用FastAPI开发数据接口.md)

-   Get started with FastAPI in five minutes
-   request and response
-   Access relational database
-   dependency injection
-   middleware
-   Asynchronous
-   Virtualized Deployment (Docker)
-   Project combat: vehicle violation inquiry project

### Day61~65 -[crawler development](./Day61-65)

#### Day61 -[Overview of Network Data Collection](./Day61-65/61.网络数据采集概述.md)

-   The concept of web crawler and its application fields
-   Discussion on the legality of web crawler
-   Tools for developing web crawlers
-   The composition of a crawler

#### Day62 - Data scraping and parsing

-   [use`requests`Three-party library realizes data capture](./Day61-65/62.用Python获取网络资源-1.md)
-   [Three ways of page parsing](./Day61-65/62.用Python解析HTML页面-2.md)
    -   Regular Expression Parsing
    -   XPath parsing
    -   CSS selector parsing

#### Day63 - Concurrent Programming in Python

-   [Multithreading](./Day61-65/63.Python中的并发编程-1.md)
-   [multi-Progress](./Day61-65/63.Python中的并发编程-2.md)
-   [Extra step I/O](./Day61-65/63.Python中的并发编程-3.md)

#### Day64 -[Use Selenium to scrape dynamic content of web pages](./Day61-65/64.使用Selenium抓取网页动态内容.md)

#### Day65 -[Introduction to the crawler framework Scrapy](./Day61-65/65.爬虫框架Scrapy简介.md)

### Day66~80 -[data analysis](./Day66-80)

#### Day66 -[Data Analysis Overview](./Day66-80/66.数据分析概述.md)

#### deth -[Environmental preparation](./Day66-80/67.环境准备.md)

#### Day68 -[NumPy application-1](./Day66-80/68.NumPy的应用-1.md)

#### Day69 -[NumPy Applications-2](./Day66-80/69.NumPy的应用-2.md)

#### Day70 -[Application of Pandas-1](./Day66-80/70.Pandas的应用-1.md)

#### Day71 -[Application of Pandas-2](./Day66-80/71.Pandas的应用-2.md)

#### sloppy -[Application of Pandas-3](./Day66-80/72.Pandas的应用-3.md)

#### awful -[Application of Pandas-4](./Day66-80/73.Pandas的应用-4.md)

#### Yes74[Application of Pandas-5](./Day66-80/74.Pandas的应用-5.md)

#### dekh -[Data Visualization-1](./Day66-80/75.数据可视化-1.md)

#### dethroned -[Data Visualization-2](./Day66-80/76.数据可视化-2.md)

#### Dih -[Basics of Probability and Statistics](./Day66-80/77.概率统计基础.md)

#### refute -[ANOVA and Parameter Estimation](./Day66-80/78.方差分析和参数估计.md)

#### deiss -[Correlation and regression](./Day66-80/79.相关和回归.md)

#### day80 -[Data Analysis Methodology](./Day66-80/80.数据分析方法论.md)

### Day81~90 -[Machine Learning and Deep Learning](./Day81-90)

#### Day81 -[Machine Learning Fundamentals](./Day81-90/81.机器学习基础.md)

#### Day82 -[k-nearest neighbor classification](./Day81-90/82.k最近邻分类.md)

#### narrow -[decision tree](./Day81-90/83.决策树.md)

#### Day84 -[Bayesian classification](./Day81-90/84.贝叶斯分类.md)

#### Day85 -[Support Vector Machines](./Day81-90/85.支持向量机.md)

#### tight -[K-means clustering](./Day81-90/86.K-均值聚类.md)

#### narrow -[regression analysis](./Day81-90/87.回归分析.md)

#### Day88 -[Getting Started with Deep Learning](./Day81-90/88.深度学习入门.md)

#### narrow -[Overview of PyTorch](./Day81-90/89.PyTorch概述.md)

#### Day90 -[PyTorch in action](./Day81-90/90.PyTorch实战.md)

### Day91~100 -[Team project development](./Day91-100)

#### Day 91:[Team project development problems and solutions](./Day91-100/91.团队项目开发的问题和解决方案.md)

1.  software process model

    -   Classical Process Model (Waterfall Model)

        -   Feasibility analysis (research to do or not to do), output "feasibility analysis report".
        -   Requirement analysis (research what to do), output "Requirements Specification" and product interface prototype diagram.
        -   Outline design and detailed design, output conceptual model diagram (ER diagram), physical model diagram, class diagram, sequence diagram, etc.
        -   Coding/Testing.
        -   Go live/maintain.

        The biggest disadvantage of the waterfall model is that it cannot embrace changes in requirements. The product can only be seen after the entire process is completed, and team morale is low.
    -   Agile Development (Scrum) - Product Owner, Scrum Master, Developers - Sprint

        -   Backlog of the product (user stories, product prototypes).
        -   Planning meeting (assessment and budget).
        -   Daily development (standup meetings, Pomodoro Technique, pair programming, test first, code refactoring...).
        -   Bug fixes (problem description, steps to reproduce, testers, assignees).
        -   release version.
        -   Review meeting (Showcase, users need to participate).
        -   Retrospective meeting (a summary of the current iteration cycle).

        > Supplement: Manifesto for Agile Software Development
        >
        > -   **individuals and interactions**Above Process and Tools
        > -   **working software**Above Detailed Documentation
        > -   **Customer cooperation**above contract negotiation
        > -   **respond to changes**higher than following plan

        ![](./res/agile-scrum-sprint-cycle.png)

        > Roles: product owner (who decides what to do, who can decide on requirements), team leader (solving various problems, focusing on how to work better, shielding external influences on the development team), development team (project executives, Specifically developers and testers).

        > Preparations: Business case and funding, contracts, vision, initial product requirements, initial release plans, stakes, team building.

        > Agile teams typically have 8-10 people.

        > Workload estimation: Quantify development tasks, including prototype, logo design, UI design, front-end development, etc., try to decompose each work into the minimum task volume, the minimum task volume standard is that the working time cannot exceed two days, and then estimate the overall project time . Post each task on the board, which is divided into three parts: to do (to be completed), in progress (in progress) and done (completed).

2.  Project team formation

    -   Team composition and roles

        > Description: thank you**Fu Xiangying**The lady helped me draw this beautiful company org chart below.

        ![company_architecture](./res/company_architecture.png)

    -   Programming specifications and code reviews (`flake8`、`pylint`）

        ![](./res/pylint.png)

    -   Some "conventions" in Python (see["Python Conventions - How to Write Pythonic Code"](Python惯例.md)）

    -   Reasons that affect code readability:

        -   Too few or no code comments
        -   Code breaks language best practices
        -   Anti-pattern programming (spaghetti code, copy-paste programming, conceited programming, …)

3.  Introduction to Team Development Tools

    -   Version Control: Git, Mercury
    -   Defect management:[Gitlab](https://about.gitlab.com/)、[Redmine](http://www.redmine.org.cn/)
    -   Agile closed-loop tools:[Zen Way](https://www.zentao.net/)、[JIRA](https://www.atlassian.com/software/jira/features)
    -   Continuous Integration:[Jenkins](https://jenkins.io/)、[Travis-CI](https://travis-ci.org/)

    Please refer to["Problems and Solutions for Team Project Development"](Day91-100/91.团队项目开发的问题和解决方案.md)。

##### Project topic selection and business understanding

1.  Topic range setting

    -   CMS (Client): News aggregation website, Q&A/sharing community, movie review/book review website, etc.

    -   MIS (user terminal + management terminal): KMS, KPI assessment system, HRS, CRM system, supply chain system, warehouse management system, etc.

    -   App background (management terminal + data interface): second-hand transactions, newspapers and magazines, niche e-commerce, news, travel, social networking, reading, etc.

    -   Other types: their own industry background and work experience, and the business is easy to understand and control.

2.  Requirements understanding, module division and task assignment

    -   Needs Understanding: Brainstorming and Competitive Analysis.
    -   Module division: draw a mind map (XMind), each module is a branch node, and each specific function is a leaf node (expressed by a verb), it is necessary to ensure that each leaf node cannot regenerate new nodes, and determine each leaf The importance, priority, and workload of the node.
    -   Task Assignment: Assign tasks to each team member based on the metrics above by the project leader.

    ![](./res/requirements_by_xmind.png)

3.  Develop project schedule (updated daily)

    | module  | Function       | personnel         | state       | Finish | working hours | plan to start | actual start | program ends | actual end | Remark               |
    | ------- | -------------- | ----------------- | ----------- | ------ | ------------- | ------------- | ------------ | ------------ | ---------- | -------------------- |
    | Comment | add comment    | king sledgehammer | in progress | 50%    | 4             | 2018/8/7      |              | 2018/8/7     |            |                      |
    |         | delete comment | king sledgehammer | wait        | 0%     | 2             | 2018/8/7      |              | 2018/8/7     |            |                      |
    |         | View comments  | Bai Yuanfang      | in progress | 20%    | 4             | 2018/8/7      |              | 2018/8/7     |            | Code review required |
    |         | Comment vote   | Bai Yuanfang      | wait        | 0%     | 4             | 2018/8/8      |              | 2018/8/8     |            |                      |

4.  OOAD and database design

-   Class diagram for UML (Unified Modeling Language)

    ![uml](./res/uml-class-diagram.png)

-   Create a table through a model (forward engineering), for example, in a Django project, you can create a two-dimensional table with the following command.

    ```Shell
    python manage.py makemigrations app
    python manage.py migrate
    ```

-   Use PowerDesigner to draw physical model diagrams.

    ![](./res/power-designer-pdm.png)

-   Create a model from a data table (reverse engineering), for example, in a Django project, you can generate a model with the following command.

    ```Shell
    python manage.py inspectdb > app/models.py
    ```

#### Day 92:[Docker container details](./Day91-100/92.Docker容器详解.md)

1.  Introduction to Docker
2.  Install Docker
3.  Create containers with Docker (Nginx, MySQL, Redis, Gitlab, Jenkins)
4.  Build Docker image (Dockerfile writing and related instructions)
5.  Container orchestration (Docker-compose)
6.  Cluster Management (Kubernetes)

#### Day 93:[MySQL performance optimization](./Day91-100/93.MySQL性能优化.md)

#### Day 94:[Network API interface design](./Day91-100/94.网络API接口设计.md)

#### Day 95:[Develop commercial projects with Django]\(./Day91-100/95.Developing commercial projects with Django.md)

##### Common issues in project development

1.  Database configuration (multiple databases, master-slave replication, database routing)
2.  Cache configuration (partition cache, key settings, timeout settings, master-slave replication, failover (sentry))
3.  log configuration
4.  Profiling and debugging (Django-Debug-ToolBar)
5.  Easy-to-use Python modules (date calculation, image processing, data encryption, third-party API)

##### REST API Design

1.  RESTful architecture
    -   [Understand RESTful Architecture](http://www.ruanyifeng.com/blog/2011/09/restful.html)
    -   [RESTful API Design Guidelines](http://www.ruanyifeng.com/blog/2014/05/restful_api.html)
    -   [RESTful API Best Practices](http://www.ruanyifeng.com/blog/2018/10/restful-api-best-practices.html)
2.  Writing API interface documentation
    -   [usury](http://rap2.taobao.org/)
    -   [STRUCTURE](http://yapi.demo.qunar.com/)
3.  [django-REST-framework](https://www.django-rest-framework.org/)Applications

##### Analysis of key and difficult points in the project

1.  Relieving Database Pressure Using Caches - Redis
2.  Decoupling and peak clipping using message queues - Celery + RabbitMQ

#### Day 96:[Software Testing and Automation Testing](Day91-100/96.软件测试和自动化测试.md)

##### unit test

1.  Kind of test
2.  Write unit tests (`unittest`、`pytest`、`nose2`、`tox`、`ddt`、……）
3.  test coverage (`coverage`）

##### Django project deployment

1.  Preparation before deployment
    -   Key Settings (SECRET_KEY / DEBUG / ALLOWED_HOSTS / Cache / Database)
    -   HTTPS / CSRF_COOKIE_SECUR  / SESSION_COOKIE_SECURE
    -   Log related configuration
2.  Review of common Linux commands
3.  Installation and configuration of common services in Linux
4.  Use of uWSGI/Gunicorn and Nginx
    -   Comparison of Gunicorn and uWSGI
        -   For simple applications that don't require a lot of customization, Gunicorn is a good choice, uWSGI has a much steeper learning curve than Gunicorn, and Gunicorn's default parameters are already suitable for most applications.
        -   uWSGI supports heterogeneous deployments.
        -   Since Nginx itself supports uWSGI, Nginx and uWSGI are generally deployed online together, and uWSGI is a fully functional and highly customized WSGI middleware.
        -   In terms of performance, Gunicorn and uWSGI are actually equivalent.
5.  Deploy test and production environments using virtualization technology (Docker)

##### Performance Testing

1.  Use of AB
2.  Use of SQLslap
3.  Use of sysbench

##### automated test

1.  Automated Testing with Shell and Python
2.  Automated Testing with Selenium
    -   Selenium IDE
    -   Selenium WebDriver
    -   Selenium Remote Control
3.  Introduction to the testing tool Robot Framework

#### Day 97:[Analysis of technical points of e-commerce website](./Day91-100/97.电商网站技术要点剖析.md)

#### Day 98:[Project deployment online and performance tuning](./Day91-100/98.项目部署上线和性能调优.md)

1.  MySQL database tuning
2.  Web server performance optimization
    -   Nginx load balancing configuration
    -   Keepalived achieves high availability
3.  Code performance tuning
    -   Multithreading
    -   Asynchronous
4.  Static resource access optimization
    -   cloud storage
    -   CDN

#### Day 99:[Common questions in interviews](./Day91-100/99.面试中的公共问题.md)

#### Day 100:[Python Interview Questions Record](./Day91-100/100.Python面试题实录.md)
