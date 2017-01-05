#!/bin/bash
APP_DIR='./app_package/'
#cd $APP_DIR && pwd
for i in $(ls $APP_DIR)
do
	sshpass -p'123456' scp -r ${APP_DIR}$i root@192.168.1.50:/opt/app_deploy1/
	sshpass -p'123456' scp -r ${APP_DIR}$i root@192.168.1.50:/opt/app_deploy2/
done
