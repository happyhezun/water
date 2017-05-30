#!/bin/bash

#aliyun.probe.dockerrun: 86400
#get line for edit
LINE=$(cat -n docker-compose.yml |awk '/testing/,/links/{print}'|grep 'dockerrun'|awk '{print $1}')

#echo ${LINE}
sed -i "${LINE}s/''/100/" docker-compose.yml 



