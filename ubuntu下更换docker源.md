国内的docker源：

Docker 官方中国区
https://registry.docker-cn.com

网易
http://hub-mirror.c.163.com

ustc
https://docker.mirrors.ustc.edu.cn

更换方法：

sudo echo "DOCKER_OPTS=\"$DOCKER_OPTS --registry-mirror=http://hub-mirror.c.163.com\"" >> /etc/default/docker service docker restart


