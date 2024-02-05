




#自定义命令

1. 在shell脚本目录下新建一个叫myecho.sh的文件

2. 编辑myecho文件

```bash



#!/bin/zsh


echo "$1" "$2"  #$1和$2是两个输入参数，可以从终端中获取两个输入，并原样输出。必须用英文双引号扩起来，中间有空格，全部是在英文输入法下输入




```


3. 添加可执行权限

4. 给myecho取一个别名

将 alias ee="～/shell脚本/myecho.sh" 写入～/.zshrc

5. 重载.zshrc文件



或者把myecho.sh移动到/usr/local/bin/下面
mv ~/shell脚本/myecho.sh /usr/local/bin/myecho  (去掉.sh后缀即可)
之后可以在任何地方调用myecho命令














