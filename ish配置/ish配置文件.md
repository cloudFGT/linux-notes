



### 换源

https://mirrors.ustc.edu.cn/alpine/  （清华源）

```Bash
/etc/apk/repositories该文件里面还是官方的源
但是用下面的指令更新源后能够搜到很多包
sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories

sed 命令无法起作用，仓库文件没有变化
只能手动把源添加进去，apk更新后能起作用
重启后源会恢复，要把ish目录删掉
这样ash就不会默认覆写rep文件

step 1、手动配置清华园
vim /etc/apk/repositories  

step 2、删掉ish目录
rm -r /ish


step 3、更新源
apk update
```

### 安装软件包

```Bash
安装实用工具包
apk add openssh vim g++ python3 git unzip unrar
```

### 从ash切换到zsh

```Bash
step 1、apk update
step 2、apk add shadow  安装shadow包，不然chsh用不了
step 3、passwd   为root设置密码，忘了密码就重新设置一下
step 4、chsh -s /bin/zsh
step 5、重启ish软件
大功告成
------------------------------------------------


RUN printf "MyPassword\nMyPassword" | passwd
RUN echo "MyPassword" | chsh -s $(which zsh)
这两行不用管
-------------------------------------------------
```

### 查看IP地址

```Python
#使用python脚本，名字叫get-my-ip.py
#在zshrc中添加getip别名


import socket

#creating a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#sending a dummy packet to a public DNS server
s.connect(("8.8.8.8", 80))

#getting the local IP address
ip = s.getsockname()[0]

#printing the IP address
print("Your IP address is:", ip)

#closing the socket connection
s.close()
```

### 开启sshd

```Bash
https://github.com/januszoles/ish




step 1 apk add openssh    # install ssh and ssh server.
step 2 ssh-keygen -A      # create host keys (no questions asks!)
step 3 passwd             # set a password for root to protect your iOS device

step 4 echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config  # modified config for root login. 
第4步不是必要的步骤

step 5 /usr/sbin/sshd     # start ssh daemon，可以在zshrc中添加别名，因为开启sshd必须用绝对路径

注意：ps -ef 但是看不到sshd进程，只有在生成host keys之后才能开启sshd进程
--------------------------------------------------------------------------------



查看ssh端口
netstat -anp | grep ssh  行不通

去sshd配置文件修改默认端口
```




### 苹果手机与Windows互传文件

在Windows上新建一个共享文件夹，在苹果手机上输入用户名，IP地址，连接

**注意：所有设备都处于同一局域网下**

### 把Python脚本封装成Linux一样的命令

要将Python脚本封装成类似于Linux命令的形式，需要执行以下步骤：

1. 在Python脚本的开头添加Shebang（即`#!/usr/bin/env python`），以指定解释器。
2. 在脚本中使用`argparse`模块解析命令行参数，这样可以让脚本接收命令行参数。
3. 将脚本保存为可执行文件。可以使用`chmod +x`命令给脚本添加可执行权限。
4. 将脚本所在的目录添加到系统的`PATH`环境变量中，这样就可以直接在命令行中执行脚本。

下面是一个示例脚本，演示了如何将Python脚本封装成命令：

```python
#!/usr/bin/env python

import argparse

def main():


parser = argparse.ArgumentParser(description='A simple command.')

parser.add_argument('input', help='Input argument')

args = parser.parse_args()

print('Input argument:', args.input)

if __name__ == '__main__':

main()
```





保存脚本为`mycommand`，然后给脚本添加可执行权限：

$ chmod +x mycommand

将脚本所在的目录添加到`PATH`环境变量中，可以通过修改`.bashrc`文件来实现：

$ echo "export PATH=$PATH:/path/to/script/dir" >> ~/.bashrc

重新加载`.bashrc`文件，使环境变量生效：

$ source ~/.bashrc

现在就可以在命令行中直接执行`mycommand`命令，并传递参数了：

$ mycommand argument

这样就能够将Python脚本封装成类似于Linux命令的形式。





python脚本封装成像Linux一样的命令

```Python
#!/usr/bin/python3


import sys

def main():
    if len(sys.argv) != 3:
       print('Usage: mypyadd <num1> <num2>')
       return

    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        result = num1 + num2
        print('Result:', result)
    except ValueError:
        print('Invalid input. Please enter integer numbers.')

if __name__ == '__main__':

    main()  #代码运行成功
    
    #在zshrc中给python脚本添加命令别名
```

**注意：在zshrc中给python脚本添加命令别名**

