#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2020/02/09 21:32
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   02 终端和远程管理.py
# @Desc     :   


# 远程管理

# 1.关机/重启
# shutdown 选项 时间
# - 不指定时间，系统将会在 1 分钟以后自动关闭电脑
# - shutdown 20:30
# - -c -- 取消关机/重启
# - -r -- 重启
# -- shutdown -r now
# -- 通常远程控制不关机，只重启，所以必须加 -r

# 2.网卡和IP地址
# 2.1 ifconfig - configure a network interface -- 查看/配置计算机当前的网卡配置信息

# 2.2 提示：
# - 在一台主机中，可能有一个物理网卡和多个虚拟网卡
# - 在 Linux 中，物理网卡的名字通常以 ensXX 表示
# 2.2.1 查看网卡配置信息
# - ifconfig

# 2.2.2 查看ip地址
# - ifconfig | grep inet

# 2.2.3 本地回环/还回地址
# - 127.0.0.1
# - 一般用来测试本机网卡是否正常

# 2.2 ping ip地址 - ping -- 检测到目标 ip地址 的链接是否正常

# 2.2.1 检测到目标主机是否连接正常
# - ping IP地址
#  (Mac电脑)control + c 暂停查看接受/传递的信息

# 2.2.2 检测本地网卡工作正常
# - ping 127.0.0.1

# 3.远程登录和复制文件

# 3.1 SSH基础(重点)
# - 在 Linux 中，SSH是 非常常用 的工具
# - 通过 SSH客户端 可以连接到运行了 SSH服务器 的远程机器上
# - 数据传输是 加密 的，可以 防止信息泄露
# - 数据传输是 压缩 的，可以 提高传输速度

# 3.2 域名
# - 由 一串用点分隔 的名字组成，例如：www.baidu.com
# - 是 IP地址 的别名，方便用户记忆

# 3.3 端口号
# - IP地址：听过 IP地址 找到网络上的计算机
# - 端口号：通过 端口号 可以找到 计算机上运行的应用程序
# -- SSH服务器 的默认端口号是 22
# -- 如果是默认端口号，在连接的时候，可以省略
# -- 常见端口号：
#       序号 - 服务 -- 端口号
#       01 - SSH服务器 -- 22
#       02 - Web服务器 -- 80
#       03 - HTTPS -- 443
#       04 - FTP服务器 -- 21

# 3.4 SSH客户端

# 终端需要输入的代码：ssh [-p port] user@remote
# -p (小写)

# user：是远程机器上的用户名，如果不指定的话，就会默认当前用户
# remote：是远程机器的地址，可以是 IP/域名，或者是 别名
# port：是SSH Server监听的端口，如果不指定，就为默认值 22
# exit：退出当前用户的登陆
# 注意：
#   - SSH这个终端命令只能在Linux或者Unix系统下使用
#   - 如果在win中，可以安装PuTTY或者XShell客户端软件即可

# 3.5 SSH 高级
# - 有关 SSH 配置信息都保存在用户家目录下的 .ssh目录 下

# 3.5.1 免密码登陆
# - 配置公钥：执行 ssh-keygen 即可生成 SSH 钥匙，一路回车即可
# - 执行 ssh-copy-id -p user@remote，可以让远程服务器记住我们的公钥

# 3.5.2 配置别名
# - 每次都输入 ssh -p port user@remote 很麻烦
# - 配置别名 可以简化步骤，譬如：ssh mac 来代替之前的输入
# - mac 就是别名，可以是任何名字，中间不能有空格
# - 就在 ~/.ssh.config 里面追加一下内容：
# Host mac:
#   HostName ip地址
#   User 用户名
#   Port 22
# 保存之后，即可用 ssh mac 实现远程登录，scp 同样可以使用

# 3.6 scp(掌握)

# 终端需要输入的代码：scp [-P port] user@remote:

# - 把本地文件复制到异地
# -- 例：scp -P port readme.txt user@remote:Desktop/readme.txt
# - 把异地文件复制到本地
# --  例：scp -P port user@remote:Desktop/readme.txt readme.txt

# - 把本地文件夹复制到异地
# -- 例：scp -r port demo user@remote:Desktop/demo
# - 把异地文件夹复制到本地
# --  例：scp -r port user@remote:Desktop/demo demo

# scp = secure copy，是一个在Linux下进行远程拷贝文件的名利
# 地址格式和 SSH 基本相同，需要注意的是：指定端口是用的是 -P (大写)
# 端口默认为 22
