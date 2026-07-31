## Python - From Novice to Master in 100 Days

> **Author**: Luo Hao
>
> **Note**: From the launch of the project to the acquisition of 8w+ stars, we have received feedback that the basic part (the content of the first 15 days) is difficult for novices, and it is recommended to have supporting videos to explain it. Recently, the basic part of the content was remade into a project called ["Python-Core-50-Courses"](<https://github.com/jackfrued/Python-Core-50-Courses>), ** use This part of the content has been rewritten in a simpler and more popular way and comes with video explanation**. Beginners can pay attention to this new project. If you need **Python Basics Video**, you can search for ["Get Started Quickly with Zero Basics of Python"] (https://www.bilibili.com/video/BV1FT4y1R7sz) on "Bilibili". This set of videos is from when I was giving lectures The video recorded during the class has acceptable picture quality and average sound quality, but it should be of some help to beginners. Everyone is welcome to leave messages, comments, and comments. Friends who feel that they have gained something after learning can support the UP master (Qianfeng Python) with "one click and three consecutive connections". If domestic users are slow to access GitHub, they can follow my **Zhihu account [Python-Jack](https://www.zhihu.com/people/jackfrued)**, the above ["Learn Python from scratch" ”](<https://zhuanlan.zhihu.com/c_1216656665569013760>) column is more suitable for beginners. Other columns are also being continuously created and updated. Everyone is welcome to follow, like and comment.
>
> Creation is not easy, thank you all for your support. The money will not be used for personal consumption (for example: buying coffee), but will be donated to those in need through platforms such as Tencent Charity, Meituan Charity, Shuidichou ([click] (./changelog.md) for donations). If you need to join the QQ learning group, you can scan the QR code below. Just add one of the three groups. Do not join the group repeatedly. The study group will provide you with **learning resources** and **question answers**. If there are **Python experience classes** and **industry open classes**, you will be notified in the group in advance. Everyone is welcome to join.
>

<img src="https://github.com/jackfrued/mypic/raw/master/20220616120218.JPG" style="zoom: 75%;">

### Python application fields and career development analysis

Simply put, Python is an "elegant", "clear" and "simple" programming language.

 -Low learning curve, even non-professionals can get started
 - Open source system with a strong ecosystem
 - Interpreted language, perfect platform portability
 - Dynamically typed language, supporting object-oriented and functional programming
 - The code is highly standardized and readable

Python is useful in the following fields.

 - Backend Development - Python/Java/Go/PHP
 - DevOps - Python/Shell/Ruby
 - Data Acquisition - Python/C++/Java
 - Quantitative Trading- Python/C++/R
 - Data Science - Python/R/Julia/Matlab
 - Machine Learning - Python/R/C++/Julia
 - Automated testing - Python/Shell

As a Python developer, there are many employment fields to choose from based on personal preferences and career plans.

- Python back-end development engineer (server, cloud platform, data interface)
- Python operation and maintenance engineer (automated operation and maintenance, SRE, DevOps)
- Python data analyst (data analysis, business intelligence, digital operations)
- Python data mining engineer (machine learning, deep learning, algorithm expert)
- Python crawler engineer
- Python test engineer (automated testing, test development)

> **Note**: Currently, **data analysis and data mining are very popular directions**, because both the Internet industry and traditional industries have accumulated a large amount of data, and all walks of life need data analysts from the past. More business value is found in some data, thereby providing data support for corporate decision-making. This is the so-called data-driven decision-making.

A few suggestions for beginners:

- Make English as your working language.
- Practice makes perfect.
- All experience comes from mistakes.
- Don't be one of the leeches.
- Either outstanding or out. (either outstanding or out)

### Day01~15 - [Python Language Basics](./Day01-15)

#### Day01 - [First introduction to Python](./Day01-15/01. First introduction to Python.md)

- Introduction to Python - History of Python/Advantages and Disadvantages of Python/Application Fields of Python
- Build a programming environment - Windows environment/Linux environment/MacOS environment
- Run Python program from terminal - Hello, world / `print` function / Run program
- Using IDLE - Interactive environment (REPL) / Write multiple lines of code / Run program / Exit IDLE
- Comments - The role of comments/single-line comments/multi-line comments

#### Day02 - [Language Element](./Day01-15/02.Language Element.md)

- Programs and Base - Instructions and Programs/Von Neumann Machine/Binary and Decimal/Octal and Hexadecimal
- Variables and types - naming of variables/use of variables/`input` function/checking variable types/type conversion
- Numbers and strings - Integers/Floating point numbers/Complex numbers/Strings/Basic string operations/Character encoding
- Operators - mathematical operators/assignment operators/comparison operators/logical operators/identity operators/operator precedence
- Application case - Convert Fahrenheit temperature to Celsius temperature / Enter the radius of the circle to calculate the circumference and area / Enter the year to determine whether it is a leap year

#### Day03 - [Branch Structure](./Day01-15/03.Branch Structure.md)

-Application scenarios of branch structure-conditions/indentation/code blocks/flow charts
- if statement - simple `if` / `if`-`else` structure / `if`-`elif`-`else` structure / nested `if`
- Application cases - User authentication/Interchange of imperial units and metric units/Rolling dice to decide what to do/Converting percentile scores to grades/Evaluating piecewise functions/Inputting the lengths of three sides will calculate the perimeter and area if a triangle can be formed.

#### Day04 - [Loop Structure](./Day01-15/04.Loop Structure.md)

- Application scenarios of loop structures - conditions/indentation/code blocks/flow charts
- while loop- basic structure/`break` statement/`continue` statement
- for loop- basic structure/`range` type/branch structure in the loop/nested loops/end the program early
- Application cases - Summing 1~100 / Determining prime numbers / Guessing number games / Printing ninety-nine tables / Printing triangle patterns / Monkey eating peaches / Hundreds of coins and hundreds of chickens

#### Day05 - [Construct program logic](./Day01-15/05. Construct program logic.md)

- Classic cases: Narcissus Number/Hundred Money and Hundred Chickens/Craps Gambling Game
- Practice questions: Fibonacci Sequence/Perfect Numbers/Prime Numbers

#### Day06 - [Use of functions and modules](./Day01-15/06.Use of functions and modules.md)

- The role of functions - Bad smell of code/Use functions to encapsulate functional modules
- Define function - `def` keyword/function name/parameter list/`return` statement/call custom function
- Call functions - Python built-in functions/import modules and functions
- Function parameters - default parameters/variable parameters/keyword parameters/named keyword parameters
- The return value of the function - no return value/return a single value/return multiple values
- Scope issues - local scope/nested scope/global scope/built-in scope/scope-related keywords
- Using module management functions - The concept of modules/Using custom module management functions/What happens when there is a naming conflict (the same module and different modules)

#### Day07 - [Strings and Common Data Structures](./Day01-15/07.Strings and Common Data Structures.md)

- Use of strings - Calculation of length/subscript operation/slicing/common methods
- Basic usage of lists - define lists/use the following table to access elements/subscript out of bounds/add elements/delete elements/modify elements/slice/loop traverse
- Common operations on lists - connection/copy (copy elements and copy arrays)/length/sort/reverse/search
- Generate lists - use `range` to create lists of numbers/generate expressions/generators
- Use of tuples - Define tuples/Use values ​​in tuples/Modify tuple variables/Tuple and list conversions
- Basic usage of sets - The difference between sets and lists/Create a set/Add elements/Delete elements/Clear
- Common operations on sets - intersection/union/difference/symmetric difference/subset/superset
- Basic usage of dictionary - Features of dictionary/Create dictionary/Add element/Delete element/Get value/Clear
- Common dictionary operations - `keys` method/ `values` method/ `items` method/ `setdefault` method
- Basic exercises - Marquee effect/Finding the largest element in a list/The average score of statistical test scores/Fibonacci sequence/Yang Hui triangle
- Comprehensive case- Double Color Ball Number Selection/Tic-Tac-Toe

#### Day08 - [Basics of Object-Oriented Programming](./Day01-15/08.Basics of Object-Oriented Programming.md)

- Classes and Objects - What is a class/What is an object/Other related concepts of object-oriented
- Define class - basic structure/properties and methods/constructor/destructor/`__str__`method
- Use objects - create objects/send messages to objects
- The four pillars of object-oriented - abstraction/encapsulation/inheritance/polymorphism
-Basic exercises- Define student class/define clock class/define graphics class/define car class

#### Day09 - [Advanced Object-Oriented](./Day01-15/09.Advanced Object-Oriented.md)

- Attributes - class attributes/instance attributes/attribute accessors/attribute modifiers/attribute deleters/use `__slots__`
- Methods in classes - instance methods/class methods/static methods
- Operator overloading - `__add__` / `__sub__` / `__or__` / `__getitem__` / `__setitem__` / `__len__` / `__repr__` / `__gt__` / `__lt__` / `__le__` / `__ge__` / `__eq__ ` / `__ne__` / `__contains__`
- Relationship between classes (objects) - association/inheritance/dependence
- Inheritance and polymorphism - What is inheritance / inheritance syntax / calling parent class method / method overriding / type determination / multiple inheritance / diamond inheritance (diamond inheritance) and C3 algorithm
- Comprehensive cases - Salary settlement system/Automatic book discount system/Customized score categories

#### Day10 - [Graphical User Interface and Game Development](./Day01-15/10.Graphical User Interface and Game Development.md)

- Use `tkinter` to develop GUI programs
- Use `pygame` third-party library to develop game applications
- "Big ball eats small ball" game

#### Day11 - [Files and Exceptions](./Day01-15/11.Files and Exceptions.md)

- Read file - read the entire file / read line by line / file path
- Write file - overwrite/append/text file/binary file
-Exception handling-The importance of exception mechanism/`try`-`except` code block/`else` code block/`finally` code block/Built-in exception type/Exception stack/`raise` statement
- Data persistence - CSV file overview/Application of `csv` module/JSON data format/Application of `json` module

#### Day12 - [Strings and Regular Expressions](./Day01-15/12.Strings and Regular Expressions.md)

- Advanced operations on strings - Escape characters/original strings/multiline strings/`in` and `not in` operators/`is_xxx` methods/`join` and `split` methods/`strip` related methods/ `pyperclip` module/immutable strings and variable strings/use of `StringIO`
- Introduction to regular expressions - The role of regular expressions/metacharacters/escaping/quantifiers/grouping/zero-width assertions/greedy matching and lazy matching lazy/use the `re` module to implement regular expression operations (matching, searching, replacing, capture)
- Using regular expressions - `re` module / `compile` function / `group` and `groups` methods / `match` method / `search` method / `findall` and `finditer` methods / `sub` and `subn `method/ `split` method
- Application case - Use regular expressions to validate input strings

#### Day13 - [Processes and Threads](./Day01-15/13.Processes and Threads.md)

- Concepts of processes and threads - What is a process/What is a thread/Application scenarios of multi-threading
- Use process-`fork` function/`multiprocessing` module/process pool/inter-process communication
- Using threads - `threading` module / `Thread` class / `RLock` class / `Condition` class / thread pool

#### Day14 - [Introduction to Network Programming and Network Application Development](./Day01-15/14.Introduction to Network Programming and Network Application Development.md)

- Fundamentals of computer network - History of computer network development / "TCP-IP" model / IP address / port / protocol / other related concepts
- Network application mode - "Client-Server" mode/"Browser-Server" mode
- Access network resources based on HTTP protocol - Network API overview/Access URL/`requests` third-party library/Parse JSON format data
- Python network programming - The concept of sockets/`socket` module/`socket` function/ Create TCP server/ Create TCP client/ Create UDP server/ Create UDP client
- Email - SMTP/POP3/IMAP/`smtplib` module/`poplib` module/`imaplib` module
- SMS service - Call SMS service gateway

#### Day15 - [Image and Document Processing](./Day01-15/15.Image and Office Document Processing.md)

- Use Pillow to process pictures - picture reading and writing/picture synthesis/geometric transformation/color conversion/filter effects
- Reading and writing Word documents - Text content processing/paragraphs/headers and footers/style processing
- Read and write Excel files - `xlrd` / `xlwt` / `openpyxl`

### Day16~Day20 - [Python Language Advanced](./Day16-20/16-20.Python Language Advanced.md)

- Common data structures
- Advanced usage of functions - "First-class citizens" / Higher-order functions / Lambda functions / Scope and closure / Decorator
- Advanced object-oriented knowledge - "Three Pillars" / Relationship between classes / Garbage collection / Magic properties and methods / Mixing / Metaclass / Object-oriented design principles / GoF design pattern
- Iterators and Generators-Related Magic Methods/Two Ways to Create a Generator/
- Concurrent and asynchronous programming - multi-threading/multi-process/asynchronous IO/`async` and `awai`t

### Day21~30 - [Introduction to Web front-end](./Day21-30/21-30.Web front-end overview.md)

- Use HTML tags to carry page content
- Render the page with CSS
- Handle interactive behavior with JavaScript
- Getting started with jQuery and improving it
- Getting started with Vue.js
-Use of Element
-Usage of Bootstrap

### Day31~35 - [Fun with the Linux operating system](./Day31-35/31-35.Fun with the Linux operating system.md)

- History of operating system development and overview of Linux
- Linux basic commands
- Utilities in Linux
- Linux file system
- Application of Vim editor
- Environment variables and shell programming
- Software installation and service configuration
- Network access and management
- Other related content

### Day36~40 - [Database Basics and Advanced](./Day36-40)

- Overview of relational databases
- Installation and use of MySQL
- Use of SQL
- DDL - Data Definition Language - `create` / `drop` / `alter`
- DML - Data manipulation language - `insert` / `delete` / `update`
- DQL - Data Query Language - `select`
- DCL - Data Control Language - `grant` / `revoke`
- MySQL new features
- Application of window functions
- JSON data type
- related information
- Data integrity and consistency
- Views, functions, procedures, triggers
- Transactions and locks
- Execution plan and index
- Paradigm theory and anti-paradigm design
- Operate MySQL in Python

### Day41~55 - [Practical Django](./Day41-55)

#### Day41 - [Django Quick Start](./Day41-55/41.Django Quick Start.md)

- Web application working mechanism
- HTTP requests and responses
- Django framework overview
- Get started quickly in 5 minutes

#### Day42 - [In-depth model](./Day41-55/42.In-depth model.md)

- Relational database configuration
- Use ORM to complete CRUD operations on the model
- Use of management backend
- Django model best practices
- Model definition reference

#### Day43 - [Static Resources and Ajax Requests](./Day41-55/43.Static Resources and Ajax Requests.md)

- Load static resources
- Ajax Overview
- Use Ajax to implement voting function

#### Day44 - [Cookie and Session](./Day41-55/44.Cookie and Session.md)

- Implement user tracking
-The relationship between cookie and session
- Django framework’s support for sessions
- Cookie reading and writing operations in view functions

#### Day45 - [Reports and Logs](./Day41-55/45.Create Reports.md)

- Modify response headers through `HttpResponse`
- Use `StreamingHttpResponse` to handle large files
- Use `xlwt` to generate Excel reports
- Use `reportlab` to generate PDF reports
- Use ECharts to generate front-end charts

#### Day46 - [Log and Debug Toolbar](./Day41-55/46.Log and Debug Toolbar.md)

- Configuration log
- Configure Django-Debug-Toolbar
- Optimize ORM code

#### Day47 - [Application of middleware](./Day41-55/47.Application of middleware.md)

- What is middleware
-Middleware built into the Django framework
- Custom middleware and its application scenarios

#### Day48 - [Introduction to front-end and back-end separation development](./Day41-55/48. Introduction to front-end and front-end separation development.md)

- Return data in JSON format
- Render the page with Vue.js

#### Day49 - [Getting Started with RESTful Architecture and DRF](./Day41-55/49.Getting Started with RESTful Architecture and DRF.md)

#### Day50 - [RESTful Architecture and DRF Advanced](./Day41-55/50.RESTful Architecture and DRF Advanced.md)

#### Day51 - [Use cache](./Day41-55/51.Use cache.md)

- The first law of website optimization

- Use Redis to provide caching services in Django projects
- Read and write cache in view functions
- Use decorators to implement page caching
- Provide caching services for data interfaces

#### Day52 - [Access to the third-party platform](./Day41-55/52.Access to the third-party platform.md)

- File upload form control and image file preview
- How the server handles uploaded files

#### Day53 - [Asynchronous tasks and scheduled tasks](./Day41-55/53.Asynchronous tasks and scheduled tasks.md)

- The second law of website optimization
- Configure message queue service
- Use Celery to implement task asynchronousization in the project
- Use Celery to implement scheduled tasks in the project

#### Day54 - [Unit Test](./Day41-55/54.Unit Test.md)

#### Day55 - [Project online](./Day41-55/55.Project online.md)

- Unit testing in Python
- Django framework support for unit testing
- Use version control system
- Configure and use uWSGI
- Static and dynamic separation and Nginx configuration
- Configure HTTPS
- Configure domain name resolution

### Day56~60 - [Develop data interface using FastAPI](./Day56-60/56-60.Develop data interface using FastAPI.md)

- Get started with FastAPI in five minutes
- Requests and responses
- Access to relational database
- Dependency injection
- middleware
- Asynchronous
- Virtualization deployment (Docker)
- Project practice: vehicle violation inquiry project

### Day61~65 - [Reptile Development](./Day61-65)

#### Day61 - [Overview of Network Data Collection](./Day61-65/61.Overview of Network Data Collection.md)

- The concept of web crawler and its application fields
- Discussion on the legality of web crawlers
- Related tools for developing web crawlers
- The composition of a crawler program

#### Day62 - Data capture and parsing

- [Use `requests` third-party library to implement data capture](./Day61-65/62. Obtain network resources with Python-1.md)
- [Three ways of page parsing](./Day61-65/62. Parsing HTML pages with Python-2.md)
    - Regular expression parsing
    - XPath parsing
    - CSS selector parsing


#### Day63 - Concurrent Programming in Python

- [Multi-threading](./Day61-65/63.Concurrent Programming in Python-1.md)
- [Multiple processes](./Day61-65/63.Concurrent programming in Python-2.md)
- [Asynchronous I/O](./Day61-65/63.Concurrent Programming in Python-3.md)

#### Day64 - [Use Selenium to crawl dynamic content of web pages](./Day61-65/64.Use Selenium to crawl dynamic content of web pages.md)

#### Day65 - [Introduction to crawler framework Scrapy](./Day61-65/65.Introduction to crawler framework Scrapy.md)

### Day66~80 - [Data Analysis](./Day66-80)

#### Day66 - [Data Analysis Overview](./Day66-80/66.Data Analysis Overview.md)

#### Day67 - [Environment Preparation](./Day66-80/67.Environment Preparation.md)

#### Day68 - [Application of NumPy-1](./Day66-80/68.Application of NumPy-1.md)

#### Day69 - [Application of NumPy-2](./Day66-80/69.Application of NumPy-2.md)

#### Day70 - [Application of NumPy-3](./Day66-80/70.Application of NumPy-3.md)

#### Day71 - [Application of NumPy-4](./Day66-80/71.Application of NumPy-4.md)

#### Day72 - [In-depth explanation of pandas-1](./Day66-80/72. In-depth explanation of pandas-1.md)

#### Day73 - [Introduction to pandas-2](./Day66-80/73.In-depth explanation of pandas-2.md)

#### Day74 - [In-depth explanation of pandas-3](./Day66-80/74. In-depth explanation of pandas-3.md)

#### Day75 - [Introduction to pandas-4](./Day66-80/75.In-depth explanation of pandas-4.md)

#### Day76 - [In-depth explanation of pandas-5](./Day66-80/76. In-depth explanation of pandas-5.md)

#### Day77 - [In-depth explanation of pandas-6](./Day66-80/77. In-depth explanation of pandas-6.md)

#### Day78 - [Data Visualization-1](./Day66-80/78.Data Visualization-1.md)

#### Day79 - [Data Visualization-2](./Day66-80/79.Data Visualization-2.md)

#### Day80 - [Data Visualization-3](./Day66-80/80.Data Visualization-3.md)

### Day81~90 - [Machine Learning and Deep Learning](./Day81-90)

#### Day81 - [Basics of Machine Learning](./Day81-90/81.Basics of Machine Learning.md)

#### Day82 - [k nearest neighbor classification](./Day81-90/82.k nearest neighbor classification.md)

#### Day83 - [Decision Tree](./Day81-90/83.Decision Tree.md)

#### Day84 - [Bayesian Classification](./Day81-90/84.Bayesian Classification.md)

#### Day85 - [Support Vector Machine](./Day81-90/85.Support Vector Machine.md)

#### Day86 - [K-means clustering](./Day81-90/86.K-means clustering.md)

#### Day87 - [Regression Analysis](./Day81-90/87.Regression Analysis.md)

#### Day88 - [Introduction to Deep Learning](./Day81-90/88.Introduction to Deep Learning.md)

#### Day89 - [PyTorch Overview](./Day81-90/89.PyTorch Overview.md)

#### Day90 - [PyTorch in action](./Day81-90/90.PyTorch in action.md)

### Day91~100 - [Team Project Development](./Day91-100)

#### Day 91: [Problems and Solutions for Team Project Development](./Day91-100/91.Problems and Solutions for Team Project Development.md)

1. Software process model
   - Classic process model (waterfall model)
     - Feasibility analysis (whether to do the research or not), and output the "Feasibility Analysis Report".
     - Requirements analysis (research on what to do), output "Requirements Specification" and product interface prototype diagram.
     - Outline design and detailed design, output conceptual model diagrams (ER diagrams), physical model diagrams, class diagrams, sequence diagrams, etc.
     - Coding/testing.
     - Go live/maintenance.

     The biggest disadvantage of the waterfall model is that it cannot embrace changes in demand. The product cannot be seen until the entire process is completed, which leads to low team morale.
   - Agile Development (Scrum) - Product Owner, Scrum Master, R&D Staff - Sprint
     - Product Backlog (user stories, product prototypes).
     - Planning meetings (evaluation and budgeting).
     - Daily development (stand-up meetings, Pomodoro Technique, pair programming, test first, code refactoring...).
     - Fix bugs (problem description, reproduction steps, testers, assignees).
     - release version.
     - Review meeting (Showcase, users need to participate).
     - Retrospective meeting (make a summary of the current iteration cycle).

     > Supplement: Manifesto for Agile Software Development
     >
     > - **Individuals and interactions** over processes and tools
     > - **Working software** above thorough documentation
     > - **Customer cooperation** comes before contract negotiation
     > - **Responding to Change** is higher than following a plan

     ![](./res/agile-scrum-sprint-cycle.png)

     > Role: Product owner (the person who decides what to do and can make decisions on requirements), team leader (solves various problems, focuses on how to work better, and shields external influence on the development team), development team (project executive) , specifically developers and testers).

     > Preparation: business case and funding, contracts, vision, initial product requirements, initial release plan, taking ownership, building a team.

     > Agile teams usually have 8-10 people.

     > Workload estimation: Quantify development tasks, including prototypes, Logo design, UI design, front-end development, etc., and try to decompose each work into the minimum task amount. The minimum task amount standard is that the working time cannot exceed two days, and then estimate the overall project time. Post each task on the Kanban board, which is divided into three parts: to do (to be completed), in progress (in progress) and done (completed).

2. Project team formation

   - Team composition and roles

     > Description: Thank you Ms. Fu Xiangying** for helping me draw the beautiful company organizational chart below.

     ![company_architecture](./res/company_architecture.png)

   - Programming specifications and code review (`flake8`, `pylint`)

     ![](./res/pylint.png)

   - Some "conventions" in Python (please refer to ["Python Conventions-How to Write Pythonic Code"] (Python Conventions.md))

   - Reasons affecting code readability:

     - Too few or no code comments
     - Code breaks the best practices of the language
     - Anti-pattern programming (spaghetti code, copy-paste programming, ego programming,…)

3. Introduction to team development tools
   - Version control: Git, Mercury
   - Defect management: [Gitlab](https://about.gitlab.com/), [Redmine](http://www.redmine.org.cn/)
   - Agile closed-loop tools: [ZenTao](https://www.zentao.net/), [JIRA](https://www.atlassian.com/software/jira/features)
   - Continuous integration: [Jenkins](https://jenkins.io/), [Travis-CI](https://travis-ci.org/)

   Please refer to ["Problems and Solutions in Team Project Development"] (Day91-100/91. Problems and Solutions in Team Project Development.md).

##### Project topic selection and business understanding

1. Setting the scope of topic selection

   - CMS (client): news aggregation website, Q&A/sharing community, film review/book review website, etc.
   - MIS (user side + management side): KMS, KPI assessment system, HRS, CRM system, supply chain system, warehouse management system, etc.

   - App backend (management terminal + data interface): second-hand transactions, newspapers and magazines, niche e-commerce, news and information, travel, social networking, reading, etc.
   - Other types: own industry background and work experience, business is easy to understand and control.

2. Requirement understanding, module division and task allocation

   - Requirements understanding: brainstorming and competitive product analysis.
   - Module division: Draw a mind map (XMind). Each module is a branch node, and each specific function is a leaf node (expressed with verbs). It is necessary to ensure that each leaf node cannot regenerate new nodes, and determine each Importance, priority and workload of leaf nodes.
   - Task allocation: The project leader assigns tasks to each team member based on the above indicators.

   ![](./res/requirements_by_xmind.png)

3. Develop project schedule (updated daily)

   | Module | Function | People | Status | Completed | Hours | Planned Start | Actual Start | Planned End | Actual End | Notes |
   | ---- | -------- | ------ | -------- | ---- | ---- | -------- | -------- | -------- | -------- | ---------------- |
   | Comment | Add comment | Wang Dachui | Ongoing | 50% | 4 | 2018/8/7 | | 2018/8/7 | | |
   | | Delete comment | Wang Dachui | Wait | 0% | 2 | 2018/8/7 | | 2018/8/7 | | |
   | | View comments | Bai Yuanfang | Ongoing | 20% | 4 | 2018/8/7 | | 2018/8/7 | | Code review required |
   | | Comment voting | Bai Yuanfang | Waiting | 0% | 4 | 2018/8/8 | | 2018/8/8 | |

4. OOAD and database design

  - Class diagram of UML (Unified Modeling Language)

    ![uml](./res/uml-class-diagram.png)

  - Create tables through models (forward engineering). For example, in a Django project, you can create a two-dimensional table through the following command.

    ```Shell
    python manage.py makemigrations app
    python manage.py migrate
    ```

  - Use PowerDesigner to draw physical model diagrams.

    ![](./res/power-designer-pdm.png)

  - Create a model (reverse engineering) through a data table. For example, in a Django project, you can generate a model through the following command.

    ```Shell
    python manage.py inspectdb > app/models.py
    ```

#### Day 92: [Docker Container Detailed Explanation](./Day91-100/92.Docker Container Detailed Explanation.md)

1. Introduction to Docker
2. Install Docker
3. Use Docker to create containers (Nginx, MySQL, Redis, Gitlab, Jenkins)
4. Build Docker image (writing of Dockerfile and related instructions)
5. Container orchestration (Docker-compose)
6. Cluster management (Kubernetes)

#### Day 93: [MySQL Performance Optimization](./Day91-100/93.MySQL Performance Optimization.md)

#### Day 94: [Network API Interface Design](./Day91-100/94.Network API Interface Design.md)

#### Day 95: [Use Django to develop commercial projects](./Day91-100/95.Use Django to develop commercial projects.md)

##### Public issues in project development

1. Database configuration (multiple databases, master-slave replication, database routing)
2. Cache configuration (partition cache, key settings, timeout settings, master-slave replication, failure recovery (Sentinel))
3. Log configuration
4. Analysis and debugging (Django-Debug-ToolBar)
5. Useful Python modules (date calculation, image processing, data encryption, third-party API)

##### REST API design

1. RESTful architecture
   - [Understanding RESTful architecture](http://www.ruanyifeng.com/blog/2011/09/restful.html)
   - [RESTful API Design Guide](http://www.ruanyifeng.com/blog/2014/05/restful_api.html)
   - [RESTful API Best Practices](http://www.ruanyifeng.com/blog/2018/10/restful-api-best-practices.html)
2. Writing API interface documents
   - [RAP2](http://rap2.taobao.org/)
   - [YAPI](http://yapi.demo.qunar.com/)
3. Application of [django-REST-framework](https://www.django-rest-framework.org/)

##### Analysis of key and difficult points in the project

1. Use caching to relieve database pressure - Redis
2. Use message queues for decoupling and peak clipping - Celery + RabbitMQ

#### Day 96: [Software testing and automated testing] (Day91-100/96. Software testing and automated testing.md)

##### unit test

1. Types of tests
2. Write unit tests (`unittest`, `pytest`, `nose2`, `tox`, `ddt`,...)
3. Test coverage (`coverage`)

##### Django project deployment

1. Preparations before deployment
   - Key settings (SECRET_KEY / DEBUG / ALLOWED_HOSTS / cache / database)
   - HTTPS/CSRF_COOKIE_SECUR/SESSION_COOKIE_SECURE  
   - Log related configuration
2. Review of common Linux commands
3. Installation and configuration of common Linux services
4. Use of uWSGI/Gunicorn and Nginx
   - Comparison of Gunicorn and uWSGI
     - For simple applications that do not require a lot of customization, Gunicorn is a good choice. The learning curve of uWSGI is much steeper than Gunicorn, and Gunicorn's default parameters can already be adapted to most applications.
     - uWSGI supports heterogeneous deployment.
     - Since Nginx itself supports uWSGI, Nginx and uWSGI are generally deployed together online, and uWSGI is a fully functional and highly customized WSGI middleware.
     - In terms of performance, Gunicorn and uWSGI are actually equivalent.
5. Use virtualization technology (Docker) to deploy test environment and production environment

##### Performance Testing

1. Use of AB
2. Use of SQLslap
3. Use of sysbench

##### automated test

1. Automated testing using Shell and Python
2. Use Selenium to implement automated testing
   - Selenium IDE
   - Selenium WebDriver
   - Selenium Remote Control
3. Introduction to testing tool Robot Framework

#### Day 97: [Analysis of technical key points of e-commerce website](./Day91-100/97.Analysis of technical key points of e-commerce website.md)

#### Day 98: [Project deployment online and performance tuning] (./Day91-100/98. Project deployment online and performance tuning.md)

1. MySQL database tuning
2. Web server performance optimization
   - Nginx load balancing configuration
   - Keepalived achieves high availability
3. Code performance tuning
   - Multithreading
   - Asynchronous
4. Static resource access optimization
   - Cloud storage
   - CDN

#### Day 99: [Public Questions in Interviews](./Day91-100/99.Public Questions in Interviews.md)

#### Day 100: [Record of Python interview questions](./Day91-100/100.Record of Python interview questions.md)
