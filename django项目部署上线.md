# nginx+uwsgi+django
https://uwsgi-docs-zh.readthedocs.io/zh_CN/latest/tutorials/Django_and_nginx.html


## 一、uWSGI服务器部署：
已经安装好uwsgi后（pip install uwsgi），只需要增加配置, 告诉uWSGI-server的框架入口函数在哪,就能让django和uWSGI服务器对接上。
1. 在django项目的setting.py文件的同级目录下，增加一个配置文件 ThinkStore_uwsgi.ini
2. 启动uWSGI服务器: uwsgi --ini /home/www/ThinkStore/ThinkStore/ThinkStore_uwsgi.ini
```
#ThinkStore_uwsgi.ini
[uwsgi]

# Django-related settings
# the base directory (full path)
chdir           = /home/www/ThinkStore
# Django's wsgi file
#module   = project.wsgi  
wsgi-file  =ThinkStore/wsgi.py

# the virtualenv (full path)
#home            = /path/to/virtualenv

# process-related settings
# master
master          = true
# maximum number of worker processes
processes       = 4
# the socket (use the full path to be safe
#socket          = /home/www/ThinkStore/ThinkStore.sock
socket = 127.0.0.1:8808
# 以守护进程方式提供服, 输出信息将会打印到log中
daemonize = /home/www/ThinkStore/log/wsgi.log
# ... with appropriate permissions - may be needed
#chmod-socket    = 664
# clear environment on exit
vacuum          = true
```


## 二、Nginx
配置nginx：
1. newfile: vi  /home/www/ThinkStore/uwsgi_params  add (https://github.com/nginx/nginx/blob/master/conf/uwsgi_params)
2. newfile: vi  /home/www/ThinkStore/ThinkStore_nginx.conf
3. 建立软连接：sudo ln -s  /home/www/ThinkStore/ThinkStore_nginx.conf /etc/nginx/conf.d/

```
# ThinkStore_nginx.conf

# the upstream component nginx needs to connect to
upstream django {
#   server unix:/home/www/ThinkStore/ThinkStore.sock; # for a file socket
   server 127.0.0.1:8808; # for a web port socket (we'll use this first)
}

# configuration of the server
server {
    # the port your site will be served on
    listen      80;
    # the domain name it will serve for
    server_name www.gufengshuyuan.com; # substitute your machine's IP address or FQDN
    charset     utf-8;

    # max upload size
    client_max_body_size 75M;   # adjust to taste

    # Django media
    # location /media  {
    #     alias /path/to/your/mysite/media;  # your Django project's media files - amend as required
    # }

    location /static {
        alias /home/www/ThinkStore/static; # your Django project's static files - amend as required
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        uwsgi_pass  django;
        include     uwsgi_params; # the uwsgi_params file you installed
    }
}
```




## 三：常用命令

```
systemctl status nginx.service  //查看nginx的状态
system start/stop/enable/disable nginx  //启动/关闭/设置开机启动/禁止开机启动
service nginx status/stop/restart/start //查看状态/停止/重启/开启 ngnix
./nginx -s reload  重新加载配置文件进行重启
ps -ef | grep nginx
kill -9 
```

## 四：其它参考
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

https://www.cnblogs.com/my_life/articles/7018681.html



