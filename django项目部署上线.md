# nginx+uwsgi+django

## 一、虚拟环境

```
# 1.安装virtualenv和virtualenvwrapper
pip install virtualenv
pip install virtualenvwrapper

# 创建虚拟环境 mkvirtualenv [env_name]
mkvirtualenv -p python3 django_env_py3
workon       // 进入虚拟环境
deactivate   // 退出虚拟环境
rmvirtualenv django_env_py3  //删除虚拟环境

# 或者直接在启动文件添加,这样每次启动自动进入虚拟环境 
vi .bash_profile
export PATH
source /Env/python/bin/activate
```
## 二、uWSGI服务器部署：
已经安装好uwsgi后（pip install uwsgi），只需要增加配置, 告诉uWSGI-server的框架入口函数在哪,就能让django和uWSGI服务器对接上。
1. 在django项目的setting.py文件的同级目录下，增加一个配置文件 uwsgi.ini
2. 对配置文件进行配置

```
[uwsgi]
# 配置服务器的监听ip和端口，让uWSGI作为nginx的支持服务器的话，设置socke就行；如果要让uWSGI作为单独的web-server，用http
# http = 127.0.0.1:3309
socket = 127.0.0.1:8808
# 配置项目目录（此处设置为项目的根目录）
chdir = /home/www/ThinkStore 
# 配置入口模块 (django的入口函数的模块，即setting同级目录下的wsgi.py)
wsgi-file = ThinkStore/wsgi.py
# 开启master, 将会多开一个管理进程, 管理其他服务进程
master = True
# 服务器开启的进程数量
processes = 4
# 以守护进程方式提供服, 输出信息将会打印到log中
daemonize = /home/www/ThinkStore/log/wsgi.log
# 服务器进程开启的线程数量
threads = 4
# 退出的时候清空环境变量
vacuum = true
# 进程pid
pidfile = uwsgi.pid
# 配uWSGI搜索静态文件目录（及django项目下我们存放static文件的目录，用uWSGI作为单独服务器时才需要设置，此时我们是用nginx处理静态文件）
check-static = /home/www/ThinkStore
```

3. 启动uWSGI服务器:在配置文件uwsgi.ini所在目录下,用我们刚才配置好的配置文件启动uWSGI：
```
uwsgi --ini uwsgi.ini
```

## 二、Nginx
配置nginx：
- vi /etc/nginx/nginx.conf  --改三处
```
server {
    listen       80 default_server;
    listen       [::]:80 default_server;
    server_name  _;
    root         /usr/share/nginx/html;

    # Load configuration files for the default server block.
    include /etc/nginx/default.d/*.conf;

    location / {
    	include uwsgi_params;　　# 设置将所有请求转发给uwsgi服务器处理
    	uwsgi_pass: 127.0.0.1:8808;　　# 指定uwsgi服务器url
    }
    location /static {
		alias /home/www/ThinkStore/static/;　　# 设置将/static的静态请求交给nginx，并指定静态文件的目录
	}

    error_page 404 /404.html;
        location = /40x.html {
    }

    error_page 500 502 503 504 /50x.html;
        location = /50x.html {
    }
}
```



```
systemctl status nginx.service  //查看nginx的状态
system start/stop/enable/disable nginx  //启动/关闭/设置开机启动/禁止开机启动
service nginx status/stop/restart/start //查看状态/停止/重启/开启 ngnix
./nginx -s reload  重新加载配置文件进行重启
ps -ef | grep nginx
kill -9 
```

## 修改django中的配置文件
设置DEBUG=FALSE, ALLOWED_HOST = ['']

## 其它参考
```
# python依赖包同步：
python3 -m pip install pypg_name == 版本 
pip freeze > env_requirement.txt     //导出依赖包 
pip install -r renv_requirement.txt  //导入依赖包

#查看进程：如果80端口被占用了，下面可以更换到其他端口，也可以直接kill -9 掉占用端口的程序
netstat -lntp

# 手动启动django
python3 manage.py runserver 0.0.0.0:8000

```













参考：
- [django项目部署上线](https://www.jianshu.com/p/c060448b3e78)
- [nginx+uwsgi+django部署流程](https://www.cnblogs.com/leexl/p/7810843.html)





