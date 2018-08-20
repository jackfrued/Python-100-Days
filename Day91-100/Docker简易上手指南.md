## Docker入门

### Docker简介

软件开发中最为麻烦的事情可能就是配置环境了。由于用户使用的操作系统具有多样性，即便使用跨平台的开发语言（如Java和Python）都不能保证代码能够在各种平台下都可以正常的运转，而且可能在不同的环境下我们的软件需要依赖的其他软件包也是不一样的。

那么问题来了，我们再安装软件的时候可不可以把软件运行的环境一并安装课？也就是说在安装软件的时候，我们是不是可以把原始环境一模一样地复制过来呢？

虚拟机（virtual machine）就是带环境安装的一种解决方案，它可以在一种操作系统里面运行另一种操作系统，比如在Windows系统里面运行Linux系统，在macOS上运行Windows，而应用程序对此毫无感知。使用过虚拟机的人都知道，虚拟机用起来跟真实系统一模一样，而对于虚拟机的宿主系统来说，虚拟机就是一个普通文件，不需要了就删掉，对宿主系统或者其他的程序并没有影响。但是虚拟机通常会占用较多的系统资源，启动和关闭也非常的缓慢，总之用户体验没有想象中的那么好。

Docker属于对Linux容器技术的一种封装，它提供了简单易用的容器使用接口，是目前最流行的 Linux 容器解决方案。Docker将应用程序与该程序的依赖打包在一个文件里面，运行这个文件，就会生成一个虚拟容器。程序在这个虚拟容器里运行，就好像在真实的物理机上运行一样。有了Docker就再也不用担心环境问题了。

![](./res/docker_vs_vm.png)

目前，Docker主要用于几下几个方面：

1. 提供一次性的环境。
2. 提供弹性的云服务（利用Docker很容易实现扩容和收缩）。
3. 实践微服务架构（隔离真实环境在容器中运行多个服务）。

### CentOS下的安装和使用

下面的讲解以CentOS为例，使用[Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)、[macOS](https://docs.docker.com/docker-for-mac/install/)或[Windows](https://docs.docker.com/docker-for-windows/install/)的用户可以通过点击链接了解这些平台下如何安装和使用Docker。

0. 确定操作系统内核版本（CentOS 7要求64位，内核版本3.10+；CentOS 6要求64位，内核版本2.6+）。

```Shell
uname -r
```

1. 在CentOS下使用yum安装Docker并启动。

```Shell
yum -y install docker-io
systemctl start docker
```

2. 检视Docker的信息和版本。

```Shell
docker version
docker info
```

3. 运行Hello-World项目来测试Docker。第一次运行时由于本地没有hello-world的镜像因此需要联网进行下载。

```Shell
docker run hello-world
```

	也可以先用下面的命令下载镜像，然后再来运行。

 ```Shell
docker pull <name>
 ```

4. 运行镜像文件。

```Shell
docker run <image-id>
docker run -p <port1>:<port2> <name>
```

6. 查看镜像文件。

```Shell
docker image ls
docker images
```

7. 删除镜像文件。

```Shell
docker rmi <name>
```

8. 查看正在运行容器。

```Shell
docker ps
```

9. 停止运行的容器。

```Shell
docker stop <container-id>
docker stop <name>
```

	对于那些不会自动终止的容器，就可以用下面的方式来停止。

```Shell
docker container kill <container-id>
```

在Ubuntu（内核版本3.10+）下面安装和启动Docker，可以按照如下的步骤进行。

```Shell
apt update
apt install docker-ce
service docker start
```

在有必要的情况下，可以更换Ubuntu软件下载源来提升下载速度，具体的做法请参照<https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/>。

安装Docker后，由于直接访问dockerhub下载镜像会非常缓慢，建议更换国内镜像，可以通过修改`/etc/docker/daemon.js`文件来做到。

```JavaScript
{
        "registry-mirrors": [
                "http://hub-mirror.c.163.com",
                "https://registry.docker-cn.com"
        ]
}
```

### Docker实战

#### 安装Nginx

Docker的使用肯定不止上面这点东西，但是有了这些知识之后，我们已经可以开始感受Docker的强大之处。下面我们就基于Docker来搭建HTTP服务器（Nginx）环境。

```Shell
docker container run -d -p 80:80 --rm --name mynginx nginx
```

> 说明：上面的参数`-d`表示容器在后台运行；`-p`是用来映射容器的端口到宿主机的端口；`--rm`表示容器停止后自动删除容器，例如通过`docker container stop mynginx`以后，容器就没有了；`--name`是自定义容器的名字。

如果需要将自己的页面部署到Nginx上，可以使用容器的拷贝命令将当前文件夹下所有的文件和文件夹拷贝到容器的指定目录中。当然也可以从容器中拷贝文件到我们指定的路径下。

```Shell
docker container cp ./index.html mynginx:/usr/local/nginx/html
```

如果不愿意拷贝文件也可以将文件夹映射到Nginx保存页面文件的目录。

```Shell
docker container run -d -p 80:80 --rm --name mynginx --volume "$PWD/html":/usr/share/nginx/html nginx
```

#### 安装MySQL

下载MySQL镜像。

```Shell
docker search mysql
docker pull mysql:5.7
docker images
```

启动容器运行MySQL。

```Shell
docker run --name mysql-docker -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7
```

在使用MySQL 8.x时可能会遇到“error 2059: Authentication plugin 'caching_sha2_password' cannot be loaded”的问题，这是因为MySQL 8.x默认使用了名为“caching_sha2_password”的机制对用户口令进行了更好的保护，但是如果客户端没有更新有可能无法基于这种方式进行身份验证，可以按照下面的方式加以解决。

```Shell
docker exec -it mysql8-docker /bin/bash
```

进入容器的交互式Shell之后，可以首先利用MySQL的客户端工具连接MySQL服务器。

```Shell
mysql -u root -p
Enter password:
Your MySQL connection id is 16
Server version: 8.0.12 MySQL Community Server - GPL
Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.
Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
mysql>
```

接下来通过SQL来修改用户口令就可以了。

```SQL
alter user 'root'@'%' identified with mysql_native_password by '123456' password expire never;
```

当然，如果愿意你也可以查看一下用户表检查是否修改成功。

```SQL
use mysql;
select user, host, plugin, authentication_string from user where user='root';
+------+-----------+-----------------------+-------------------------------------------+
| user | host      | plugin                | authentication_string                     |
+------+-----------+-----------------------+-------------------------------------------+
| root | %         | mysql_native_password | *6BB4837EB74329105EE4568DDA7DC67ED2CA2AD9 |
| root | localhost | mysql_native_password | *6BB4837EB74329105EE4568DDA7DC67ED2CA2AD9 |
+------+-----------+-----------------------+-------------------------------------------+
2 rows in set (0.00 sec)
```

