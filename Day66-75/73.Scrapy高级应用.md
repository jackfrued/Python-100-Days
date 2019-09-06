## Scrapy爬虫框架高级应用

### Spider的用法

在Scrapy框架中，我们自定义的蜘蛛都继承自scrapy.spiders.Spider，这个类有一系列的属性和方法，具体如下所示：

1. name：爬虫的名字。
2. allowed_domains：允许爬取的域名，不在此范围的链接不会被跟进爬取。
3. start_urls：起始URL列表，当我们没有重写start_requests()方法时，就会从这个列表开始爬取。
4. custom_settings：用来存放蜘蛛专属配置的字典，这里的设置会覆盖全局的设置。
5. crawler：由from_crawler()方法设置的和蜘蛛对应的Crawler对象，Crawler对象包含了很多项目组件，利用它我们可以获取项目的配置信息，如调用crawler.settings.get()方法。
6. settings：用来获取爬虫全局设置的变量。
7. start_requests()：此方法用于生成初始请求，它返回一个可迭代对象。该方法默认是使用GET请求访问起始URL，如果起始URL需要使用POST请求来访问就必须重写这个方法。
8. parse()：当Response没有指定回调函数时，该方法就会被调用，它负责处理Response对象并返回结果，从中提取出需要的数据和后续的请求，该方法需要返回类型为Request或Item的可迭代对象（生成器当前也包含在其中，因此根据实际需要可以用return或yield来产生返回值）。
9. closed()：当蜘蛛关闭时，该方法会被调用，通常用来做一些释放资源的善后操作。

### 中间件的应用

#### 下载中间件



#### 蜘蛛中间件



### Scrapy对接Selenium



### Scrapy部署到Docker

