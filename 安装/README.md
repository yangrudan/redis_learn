# Redis安装

# 目录

+ **[POSIX](#POSIX)**
+ **[macOS](#macOS)**
+ **[启动和停止](#启动和停止)**
    + [resis可执行软件](#resis可执行软件)


## POSIX

* 1. wget http://download.redis.io/redis-stable.tar.gz

* 2. tar xzf redis-stable.tar.gz

* 3. cd redis-stable

* 4. make


ps: 也可以用apt-get install 安装


## macOS

* 1. 安装Homebrew

* 2. 通过$ brew install redis

* 3. brew services start redis

## 安装启动和停止



### resis可执行软件

|文件名	|说明	|
|---------------|---------------|
|redis-server| resis服务器|
|redis-cli| resis命令行客户端|
|redis-benchmark| resis性能测试工具|
|redis-check-aof| AOF文件修复工具|
|redis-check-rdb| RDB文件检查工具|
|redis-sentinel| Sentinel服务器|


