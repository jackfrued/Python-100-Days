## Web前端概述

### HTML简史

1. 1991年10月：一个非正式CERN（[欧洲核子研究中心](https://zh.wikipedia.org/wiki/%E6%AD%90%E6%B4%B2%E6%A0%B8%E5%AD%90%E7%A0%94%E7%A9%B6%E7%B5%84%E7%B9%94)）文件首次公开18个HTML标签，这个文件的作者是物理学家[蒂姆·伯纳斯-李](https://zh.wikipedia.org/wiki/%E8%92%82%E5%A7%86%C2%B7%E4%BC%AF%E7%BA%B3%E6%96%AF-%E6%9D%8E)，因此他是[万维网](https://zh.wikipedia.org/wiki/%E4%B8%87%E7%BB%B4%E7%BD%91)的发明者，也是[万维网联盟](https://zh.wikipedia.org/wiki/%E4%B8%87%E7%BB%B4%E7%BD%91%E8%81%94%E7%9B%9F)的主席。
2. 1995年11月：HTML 2.0标准发布（RFC 1866）。
3. 1997年1月：HTML 3.2作为[W3C](https://zh.wikipedia.org/wiki/W3C)推荐标准发布。
4. 1997年12月：HTML 4.0作为W3C推荐标准发布。
5.  1999年12月：HTML4.01作为W3C推荐标准发布。
6. 2008年1月：HTML5由W3C作为工作草案发布。
7. 2011年5月：W3C将HTML5推进至“最终征求”（Last Call）阶段。
8. 2012年12月：W3C指定HTML5作为“候选推荐”阶段。
9. 2014年10月：HTML5作为稳定W3C推荐标准发布，这意味着HTML5的标准化已经完成。

#### HTML5新特性

1. 引入原生多媒体支持（audio和video标签）
2. 引入可编程内容（canvas标签）
3. 引入语义Web（article、aside、details、figure、footer、header、nav、section、summary等标签）
4. 引入新的表单控件（日历、邮箱、搜索等）
5. 引入对离线存储更好的支持
6. 引入对定位、拖放、WebSocket、后台任务等的支持

### 使用标签承载内容

####  结构

- head
  - title
  - meta
- body

#### 文本

- 标题和段落
- 粗体和斜体
- 上标和下标
- 空白（白色空间折叠）
- 折行和水平标尺
- 语义化标记
  - 加粗和强调
  - 引用
  - 缩写词和首字母缩写词
  - 引文
  - 所有者联系信息
  - 内容的修改

#### 列表（list）

 - 有序列表（ordered list）
 - 无序列表（unordered list）
 - 定义列表（definition list）

#### 链接（anchor）

- 页面链接
- 锚链接
- 功能链接

#### 图像（image）

- 图像存储位置
- 图像及其宽高
- 选择正确的图像格式
  - JPEG
  - GIF
  - PNG
- 矢量图
- figure标签

#### 表格（table）

- 基本的表格结构
- 表格的标题
- 跨行和跨列
- 长表格

#### 表单（form）

- 如何收集信息
- 表单控件（input）
  - 文本框 / 密码框 / 文本域
  - 单选按钮 / 复选按钮 / 下拉列表
  - 提交按钮 / 图像按钮 / 文件上传
- 组合表单元素
  - fieldset / legend
- HTML5的表单控件
  - 日期
  - 电子邮件 / URL
  - 搜索

#### 音视频（audio / video）

- 视频格式和播放器
- 视频托管服务
- 添加视频的准备工作
- video标签和属性
- audio标签和属性

#### 其他

- 文档类型
- 注释
- 属性
  - id
  - class
- 块级元素 / 行级元素
- 内联框架（internal frame）
- 页面信息（meta）
- 转义字符（实体替换符）

### 使用CSS渲染页面

#### 简介

- CSS的作用
- CSS的工作原理
- 规则、属性和值

#### 颜色（color）

- 如何指定颜色
- 颜色术语和颜色对比
- 背景色

#### 文本（text / font）

- 文本的大小和字型(font-size / font-family)
- 斜体、粗体、大写和下划线(font-weight / font-style / text-decoration)
- 行间距(line-height)、字母间距(letter-spacing)和单词间距(word-spacing)
- 对齐(text-align)方式和缩进(text-ident)
- 链接样式（:link / :visited / :active / :hover）
- CSS3新属性
  - 投影
  - 首字母和首行文本(p:first-letter / p:first-line)
  - 响应用户

#### 盒子（box model）

- 盒子大小的控制（width / height）
- 盒子的边框、外边距和内边距（border /  margin / padding）
- 盒子的显示和隐藏（display / visibility）
- CSS3新属性
  - 边框图像（border-image）
  - 投影（border-shadow）
  - 圆角（border-radius）

#### 列表、表格和表单

- 列表的项目符号（list-style）
- 表格的边框和背景（border-collapse）
- 表单控件的外观
- 表单控件的对齐
- 浏览器的开发者工具

#### 图像

- 控制图像的大小（display: inline-block）
- 对齐图像
- 背景图像（background / background-image / background-repeat / background-position）

#### 布局

- 控制元素的位置（position / z-index）
  - 普通流
  - 相对定位
  - 绝对定位
  - 固定定位
  - 浮动元素（float / clear）
- 网站布局
  - HTML5布局
- 适配屏幕尺寸
  - 固定宽度布局
  - 流体布局
  - 布局网格

### 使用JavaScript控制行为

#### JavaScript基本语法

- 语句和注释
- 变量和数据类型
  - 声明和赋值
  - 简单数据类型和复杂数据类型
  - 变量的命名规则
- 表达式和运算符
  - 赋值运算符
  - 算术运算符
  - 比较运算符
  - 逻辑运算符
- 分支结构
  - if…else...
  - switch…case…default...
- 循环结构
  - for循环
  - while循环
  - do…while循环
- 数组
  - 创建数组
  - 操作数组中的元素
- 函数
  - 声明函数
  - 调用函数
  - 参数和返回值
  - 匿名函数
  - 立即调用函数

#### 面向对象

 - 对象的概念
 - 创建对象的字面量语法
 - 访问成员运算符
 - 创建对象的构造函数语法
    - this关键字
 - 添加和删除属性
    - delete关键字
 - 全局对象
    - Number / String / Boolean
    - Date / Math / RegEx / Array

#### BOM

 - window对象的属性和方法
 - history对象
    - forward() / back() / go()
 - location对象
 - navigator对象
 - screen对象

#### DOM

 - DOM树
 - 访问元素
    - getElementById() / querySelector()
    - getElementsByClassName() / getElementsByTagName() / querySelectorAll()
    - parentNode / previousSibling / nextSibling / firstChild / lastChild
- 操作元素
  - nodeValue
  - innerHTML / textContent / createElement() / createTextNode() / appendChild() / removeChild()
  - className / id / hasAttribute() / getAttribute() / setAttribute() / removeAttribute()
- 事件处理
  - 事件类型
    - UI事件：load / unload / error / resize / scroll
    - 键盘事件：keydown / keyup / keypress
    - 鼠标事件：click / dbclick / mousedown / mouseup / mousemove / mouseover / mouseout
    - 焦点事件：focus / blur
    - 表单事件：input / change / submit / reset / cut / copy / paste / select
  - 事件绑定
    - HTML事件处理程序（不推荐使用，因为要做到标签与代码分离）
    - 传统的DOM事件处理程序（只能附加一个回调函数）
    - 事件监听器（旧的浏览器中不被支持）
  - 事件流：事件捕获 / 事件冒泡
  - 事件对象（低版本IE中的window.event）
    - target（低版本IE中的srcElement）
    - type
    - cancelable
    - preventDefault()
    - stopPropagation()（低版本IE中的cancelBubble）
  - 鼠标事件 - 事件发生的位置
    - 屏幕位置：screenX和screenY
    - 页面位置：pageX和pageY
    - 客户端位置：clientX和clientY
  - 键盘事件 - 哪个键被按下了
    - keyCode属性
    - String.fromCharCode(event.keyCode)
  - HTML5事件
    - DOMContentLoaded
    - hashchange
    - beforeunload

#### JavaScript API

- HTML5中的API：geolocation / localStorage / sessionStorage / history

### 使用jQuery

#### jQuery概述

1. Write Less Do More（用更少的代码来完成更多的工作）
2. 使用CSS选择器来查找元素（更简单更方便）
3. 使用jQuery方法来操作元素（解决浏览器兼容性问题、应用于所有元素并施加多个方法）

#### 引入jQuery

- 下载jQuery的开发版和压缩版
- 从CDN加载jQuery

```HTML

<script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>
<script>
    window.jQuery || 
        document.write('<script src="js/jquery-3.3.1.min.js"></script>')
</script>
```

#### 查找元素

- 选择器
  - \* / element / #id / .class / selector1, selector2
  - ancestor descendant / parent>child / previous+next / previous~siblings 
- 筛选器
  - 基本筛选器：:not(selector) / :first / :last / :even / :odd / :eq(index) / :gt(index) / :lt(index) / :animated / :focus
  - 内容筛选器：:contains('…') / :empty / :parent / :has(selector)
  - 可见性筛选器：:hidden / :visible
  - 子节点筛选器：:nth-child(expr) / :first-child / :last-child / :only-child
  - 属性筛选器：[attribute] / [attribute='value'] / [attribute!='value'] / [attribute^='value'] / [attribute$='value'] / [attribute|='value'] / [attribute~='value']
- 表单：:input / :text / :password / :radio / :checkbox / :submit / :image / :reset / :button / :file / :selected / :enabled / :disabled / :checked

#### 执行操作

- 内容操作
  - 获取/修改内容：html() / text() / replaceWith() / remove()
  - 获取/设置元素：before() / after() / prepend() / append() / remove() / clone() / unwrap() / detach() / empty() / add()
  - 获取/修改属性：attr() / removeAttr() / addClass() / removeClass() / css()
  - 获取/设置表单值：val()
- 查找操作
  - 查找方法：find() /  parent() / children() / siblings() / next() / nextAll() / prev() / prevAll()
  - 筛选器：filter() / not() / has() / is() / contains()
  - 索引编号：eq()
- 尺寸和位置
  - 尺寸相关：height() / width() / innerHeight() / innerWidth() / outerWidth() / outerHeight()
  - 位置相关：offset() / position() / scrollLeft() / scrollTop()
- 特效和动画
  - 基本动画：show() / hide() / toggle()
  - 消失出现：fadeIn() / fadeOut() / fadeTo() / fadeToggle()
  - 滑动效果：slideDown() / slideUp() / slideToggle()
  - 自定义：delay() / stop() / animate()
- 事件
  - 文档加载：ready() / load()
  - 用户交互：on() / off()

#### 链式操作

#### 检测页面是否可用

```HTML

<script>
    $(document).ready(function() {
        
    });
</script>
```

```HTML

<script>
    $(function() {
        
    });
</script>
```

#### jQuery插件

- jQuery Validation
- jQuery Treeview
- jQuery Autocomplete
- jQuery UI

#### 避免和其他库的冲突

先引入其他库再引入jQuery的情况。

```HTML

<script src="other.js"></script>
<script src="jquery.js"></script>
<script>
	jQuery.noConflict();
    jQuery(function() {
        jQuery('div').hide();
    });
</script>
```

先引入jQuery再引入其他库的情况。

```HTML

<script src="jquery.js"></script>
<script src="other.js"></script>
<script>
    jQuery(function() {
        jQuery('div').hide();
    });
</script>
```

#### 使用Ajax

- 原生的Ajax
- 基于jQuery的Ajax
  - 加载内容
  - 提交表单

### 使用Bootstrap

#### 特点

1. 支持主流的浏览器和移动设备
2. 容易上手
3. 响应式设计

#### 内容

1. 网格系统
2. 封装的CSS
3. 现成的组件
4. JavaScript插件
