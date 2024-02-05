

#!/bin/zsh


cd ~/LaTex-notes/

echo 获取远程仓库最新的修改

git fetch origin

echo 将远程更改合并到本地仓库

git merge origin/main

echo 同步完成，本地仓库已更新，用户可执行其他相关的操作


