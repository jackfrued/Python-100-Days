## Scrapy爬虫框架分布式实现

### 分布式爬虫原理



### Scrapy分布式实现

1. 安装Scrapy-Redis。
2. 配置Redis服务器。
3. 修改配置文件。
   - SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
   - DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
   - REDIS_HOST = '1.2.3.4'
   - REDIS_PORT = 6379
   - REDIS_PASSWORD = '1qaz2wsx'
   - SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
   - SCHEDULER_PERSIST = True（通过持久化支持接续爬取）
   - SCHEDULER_FLUSH_ON_START = True（每次启动时重新爬取）

### Scrapyd分布式部署

1. 安装Scrapyd
2. 修改配置文件
   - mkdir /etc/scrapyd
   - vim /etc/scrapyd/scrapyd.conf
3. 安装Scrapyd-Client
   - 将项目打包成Egg文件。
   - 将打包的Egg文件通过addversion.json接口部署到Scrapyd上。

