
import fileinput
import re
pattern = "aliyun.probe.timeout_seconds: 60"

# def process(line):
#     return line.rstrip() + " line "
# # text = 'restart: always'
# # process(text)
conut = 1
for line in fileinput.input('docker-compose.yml', inplace=1):
    # print conut

    if re.search(pattern, line, ):
        # print conut
        if conut == 2:
            line=line.replace('aliyun.probe.timeout_seconds: 60','aliyun.probe.timeout_seconds: 300')
            # print line,
        conut = conut + 1
    # process(line)
    print line,

#


# 写入测试文件。
# f = open('1.txt', 'w')
# text_str='''
# first
# second
# '''
# f.write(text_str)
# f.close()

# 读取测试文件。
# f = open('1.txt', 'r')
# for line in f:
#     print line
#
# def process(line):
#     return line.rstrip() + 'line'
# count = 0
# for line in fileinput.input('docker-compose.yml'):
#     if line == "aliyun.probe.timeout_seconds: 60":
#         if count == 2:
#             line = line.replace('aliyun.probe.timeout_seconds: 60', 'aliyun.probe.timeout_seconds: 300')
#         count = count + 1
#     print line,



#
#     # if line == 'second':
#     #     print line ,'hello'
#     # # print type(line)
#     # # print line, 'line'

#
# for line in fileinput.input('1.txt', inplace=1):
#     line = line.replace('second', 'less')
#     print line,