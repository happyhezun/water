## 什么是ELK

1. 作用：
LogStash 负责文本数据的收集、处理
Elasticsearch 负责数据的存储和索引
Kibana 负责数据的可视化和统计分析

1. ELK的特点：
   处理方式灵活
   配置简易
   检索性能高效
   集群线性扩展
   前端操作绚丽
1. ELK结构：

   Nginx、MySQL、... -> LogStash（主动收集，数据规范化）-> Elasticsearch(存储数据并索引)->Kibana（查询分析和统计）

## Elasticsearch安装步骤：

1. 下载对应的二进制包

1. 修改配置文件配置：

   path.data
   path.logs
   对应存储目录
   network.host: 0.0.0.0

   http.cors.enabled: true
   http.cors.allow-origin: "*"
   允许跨域

1. 使用root用户修改打开最大文件数和虚拟内存大小和打开文件最大数

   ```shell
   /etc/security/limits.conf
   
   * soft nofile 65
   * hard nofile 13
   * soft nproc 20
   * herd nproc 4096
   
   /etc/security/limits.d/20-nproc.conf
   * soft nproc 4096
   root soft nproc unlimited
   
   /etc/sysctl.conf
   vm.max_map_count=655360
   fs.file-max=655360
   ```
1. 使配置生效

   ```shell
   sysctl -p 
   ```
1.  后台启动elasticsearch服务

   ```shell
   ./bin/elasticsearch -d
   ```

1. 访问并验证：
   访问：http://xxx.xxx.xxx.xxx:9200

- 注意：

  默认需要4GB内存
  
  以普通用户运行:
  
  ```shell
  cd /usr/local/elk/elasticsearch
  ES_JAVA_OPTS="-Xms512m -Xmx512m" ./bin/elasticsearch -d
  cd /usr/local/elk/Kibana
  nohup ./bin/Kibana -H 0.0.0.0 & > run.log &
  ```



## Elasticsearch Head插件安装

1. 对Elasticearch管理和查看, 进行简单的查询、状态的浏览。

2. 下载npm二进制安装包
3. 下载elasticsearch 插件,存放在/usr/local/node/
   ```shell
   wget https://github.com/mobz/elasticsearch-head/archive/master.zip
   npm install -g cnpm --registry=https://registry.npm.taobao.org
   cd /usr/local/elk/elasticsearch-head
   cnpm install 
   cnpm run start 
   ```
4. 访问方式：http://xxx.xxx.xxx.xxx:9100
   配置 elasticsearch 的地址
5. 后台运行： nohup cnpm run start & > run.log &

## logstash部署安装

```shell
1、编辑logstash配置文件
cd logstash
config/test.conf
input {
    file {
        path => ["/tmp/test_data"]
        codec => json {
            charset => "UTF-8"
        }
    }
}

output {
    elasticsearch {
        hosts => "127.0.0.1"
        index => "logstash-%{+YYYY.MM.dd}"
        document_type => "test"
    }
}
```

index :相当于MYSQL库
document_type: 相当于MYSQL表

3、启动logstash服务

```shell
./bin/logstash -f config/test.conf
nohub ./bin/logstash -f config/test.conf &> run.log &
```



## Kibana安装部署：

1、启动方式:

```shell
./bin/kibana -H 0.0.0.0
```

2、访问方式：
在浏览器打开网址：http://127.0.0.1:5601

在web界面配置index(等于配置数据库)
删除已经有的index：
curl -XDELETE  http://127.0.0.1:9200/logstash-2018.05.23

3、准备测试数据：

```shell
cat /tmp/test_data
{"name": "test", "kind": "iphone"}
{"name": "test", "kind": "iphone"}
{"name": "test", "kind": "iphone"}
{"name": "test", "kind": "iphone"}
```

使用elk做统计分析：
数据输入流程： 数据 -> Logstash Input -> Logstash Filter -> 
Logstash Output
数据获取的流程：
Elasticsearch -> Kibana

配置Logstash

配置Logstash Input为TCP
配置Logstash Output为Elasticsearch

修改logstash配置:

```shell
cat config/test.conf
input {
    tcp {
        port => 123456
        codec => json {
            charset => "UTF-8"
        }
    }
}
```

1. 生成数据要求：

   数据格式为JSON
   数据包含整数和字符串

2. 使用socket连接到Logstash

   ```shell
   cat test_data.py
   ```

   ```python
   #coding=utf-8
   import socket
   import json
   import datetime
   import random
   
   s = socket.socket()
   s.connect(('192.168.1.45',12345))
   
   user = ['tom', 'hary', 'wada', 'dilong', 'eric', 'simon', 'sam']
   pages = ['index', 'course', 'pay', 'login']
   device = ['android', 'iphone', 'ipad']
   
   line = 100
   
   while line > 0：
       line = line -1
       temp_time = (datetime.datetime.utcnow() + datetime.timedelta(seconds=random.randint(0,10))).isoformat()
       data = {
           'name': random.choice(user),
           'visit_time': temp_time,
           'device': random.choice(device),
           'page': random.choice(page),
           'num': random.randint(0, 10)
       }
   s.send(json.dumps(data)+'\r\n')
   ```
1. 界面配置Kibana

   打开Kibana
   添加Index
   打开Dicover页面
