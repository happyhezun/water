Flask 轻量级
Django 比较大
Web2py
Bottle


python3.5.0
pip install flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World"

if __name__ == "__main__":
    app.run(host='0.0.0.0')


路由规划：

@app.route('/api')
def index():
    return 'Index Page'

@app.route('/api/hello')
def hello():
    return 'Hello World'


蓝图注入方式：

imooc.py

from flask import Blueprint

route_imooc = Blueprint("imooc_page", __name__)

@route_imooc.route("/")
def index():
    return "imooc index page"

@route_imooc.route("/hello")
def hello():
    return "imooc hello page"


main.py

from flask import Flask
from imooc imooc route_imooc

app = Flask(__name__)
app.register_blueprint(route_imooc, url_prefix='/imooc')

默认的路由没有规划：

链接管理器、版本管理器

链接管理器 url_for
根据视图的方法名找到对应的url路由

@app.route("/")
def hello_world():
    url = url_for("index")
    return "Hello World," + url

common/libs/UrlManager.py

class UrlManager(object):
    @staticmethod
    def buildUrl( path ):
        return path
    
    @staticmethod
    def buildStaticUrl( path )
    #版本管理
        path = path + "?ver=" + "201805021500"
        return UrlManager.buildStaticUrl(path)

from common.libs.UrlManger

@app.route("/")
def hello_world():
    url = url_for("index")
    url_1 = UrlManager.buildUrl("/api")
    url_2 = UrlManager.buildStaticUrl("/css/bootstrap.css")
    return "Hello World, url:%, url_1:%s, url_2:%s" % (url, url_1, url_2)

日志管理

@app.route("/")
def hello_world():
    url = url_for("index")
    url_1 = UrlManager.buildUrl("/api")
    url_2 = UrlManager.buildStaticUrl("/css/bootstrap.css")
    msg = "Hello World, url:%, url_1:%s, url_2:%s" % (url, url_1, url_2)
    app.logger.error( msg )
    app.logger.info( msg )
    app.logger.debug( msg )
    return msg

错误处理器
@app.errorhandler(404)
def page_not_found( error ):
    app.logger.error( error )
    return "This page does not exist", 404

'''
设置ubuntu分辨率
https://www.linuxidc.com/Linux/2017-11/148439.htm
https://www.heartnn.com/2019/11/21/ubuntu-display-resolution-on-vmware/
'''
数据库ORM
pip install flask_sqlalchemy
pip install mysqlclient



from flask import Flask, url_for
from imooc import route_immoc
from common.libs.UrlManager import UrlMangager
from Flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint( route_imooc, url_prefix="/imooc" )

app.config['SQLA']
db = SQLAchemy(app)

@app.route("/api/hello")
def hello():
    from sqlalchemy import text
    sql = text('select * from "user"')
    result = db.engine.execute(sql)
    return "Hello World"