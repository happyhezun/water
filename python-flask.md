听不懂不要捉急，可以多看几遍。耐心的听、耐心的练习。
实战增加编程能力。

主流的python3
玩转Flask
搭建高可用的Flask MVC框架
Flask 生产环境部署

额外的企业知识
HTTP请求流程的讲解
提供对外可访问网站需要的准备
构建更符合企业实战需求的高可用MVC
符合企业环境的生产环境部署方案

分页、定时任务、爬虫、

环境准备：
Python3.7
PyCharm

pip 和 virtualenv
mysql
Python3 和 Python2

if __name__ == "__main__":
    a, b, c, d = 50, 5.5, True, 5+3j
    print(type(a), type(b), type(c), type(d))


str = "imooc"
print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])

vscode列选择：Shift+Alit+鼠标左键拖动
字符串的操作主要是赋值、拼接、截取。
列表可以完成大多数集合类的数据结构实现、可变的数组

list = ['abcd', 786, 2.23, 'imooc', 70.2]
tinylist = [123, 'imooc']

print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist*2)
print(list + tinylist)

tinylist.append("569")
print(tinylilst)

tuple 只读的列表

student = {"Tom", "Jim", "Jack", "Mary", "Rose"}
print( student )
if "Rose" in student:
    print( "Rose在集合中" )
else:
    print("Rose不在集合中")

a = set("abrasdfsdfs")
b = set("sdafwerdfd")

print( a )
print( b )

print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

字典是无序的