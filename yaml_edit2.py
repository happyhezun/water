# encoding: utf-8
#!/usr/bin/env python

import yaml
#
# stream = open(fname, 'r')
# data = yaml.load(stream)

def displayYaml():
    yamlDoc = open("docker-compose.yml",'r')
    data = {}
    for line in yaml.load_all(yamlDoc):
        print line

    # edit_data = data['kafka-broker-1']['labels']['aliyun.probe.timeout_seconds']=200
    yamlDoc.close()
    # with open('test1.yml', 'w') as yaml_file:
    #     prettyData = yaml.dump(data)
    #     yaml_file.write(prettyData)
    # return prettyData

doc = displayYaml()
print doc

# def editYaml():
#     edit_doc = doc['kafka-broker-1']['labels']['aliyun.probe.timeout_seconds']=200
#     return edit_doc
# print editYaml()

def loadYaml(self):
    getData = yaml.safe_load(f)
    prettyData = yaml.dump(getData, default_flow_style=False)

