### ansible基础初试 ###

在centos6上安装ansible：  
yum install gcc glibc-devel zlib-devel  rpm-build openssl-devel –y  
rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm  
管理机上生成密钥：  
ssh-keygen -t rsa  
批量添加ssh免密认证:  
ansible db -m authorized_key -a "user=root key='{{ lookup('file', '/home/root/.ssh/id_rsa.pub') }}' path=/home/root/.ssh/authorized_keys manage_dir=no"  
command模块:   
ansible webservers -m command -a "df -h"  
shell模块：  
ansible webserver -m shell -a "/bin/echo 'hello'"
