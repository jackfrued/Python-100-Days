## 常见反爬策略及应对方案

1. 构造合理的HTTP请求头。
   - Accept

   - User-Agent

   - Referer
   
   - Accept-Encoding
   
   - Accept-Language
2. 检查网站生成的Cookie。
   - 有用的插件：[EditThisCookie](http://www.editthiscookie.com/)
   - 如何处理脚本动态生成的Cookie
3. 抓取动态内容。
   - Selenium + WebDriver
   - Chrome / Firefox - Driver
4. 限制爬取的速度。
5. 处理表单中的隐藏域。
   - 在读取到隐藏域之前不要提交表单
   - 用RoboBrowser这样的工具辅助提交表单
6. 处理表单中的验证码。
   - OCR（Tesseract） - 商业项目一般不考虑 

   - 专业识别平台 - 超级鹰 / 云打码

     ```Python
     from hashlib import md5
     
     class ChaoClient(object):
     
         def __init__(self, username, password, soft_id):
             self.username = username
             password =  password.encode('utf-8')
             self.password = md5(password).hexdigest()
             self.soft_id = soft_id
             self.base_params = {
                 'user': self.username,
                 'pass2': self.password,
                 'softid': self.soft_id,
             }
             self.headers = {
                 'Connection': 'Keep-Alive',
                 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
             }
     
         def post_pic(self, im, codetype):
             params = {
                 'codetype': codetype,
             }
             params.update(self.base_params)
             files = {'userfile': ('captcha.jpg', im)}
             r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
             return r.json()
     
     
     if __name__ == '__main__':
         client = ChaoClient('用户名', '密码', '软件ID')
         with open('captcha.jpg', 'rb') as file:                                                
             print(client.post_pic(file, 1902))                                          
     ```

7. 绕开“陷阱”。
   - 网页上有诱使爬虫爬取的爬取的隐藏链接（陷阱或蜜罐）
   - 通过Selenium+WebDriver+Chrome判断链接是否可见或在可视区域
8. 隐藏身份。
   - 代理服务 -  快代理 / 讯代理 / 芝麻代理 / 蘑菇代理 / 云代理

     [《爬虫代理哪家强？十大付费代理详细对比评测出炉！》](https://cuiqingcai.com/5094.html)

   - 洋葱路由 - 国内需要翻墙才能使用

     ```Shell
     yum -y install tor
     useradd admin -d /home/admin
     passwd admin
     chown -R admin:admin /home/admin
     chown -R admin:admin /var/run/tor
     tor
     ```
