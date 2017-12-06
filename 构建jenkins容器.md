在国内拿jenkins镜像：

docker pull index.tenxcloud.com/docker_library/jenkins

手动构建jenkins镜像步骤：

apt-get update

apt-get install software-properties-common -y

sudo add-apt-repository ppa:webupd8team/java -y

sudo apt-get update && sudo apt-get install oracle-java8-installer

wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -

sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'

sudo apt-get update

sudo apt-get install jenkins

apt-get install openssh-server

提交容器生成镜像：

docker commit 2413ae0e7a74 hezun/my-jenkins:v1

运行容器：

docker run -d -p 1234:8080 --name jenkins-ci hezun/my-jenkins:v1 /etc/init.d/ssh start -D
