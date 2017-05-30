#!/usr/bin/env
import commands
get_line_cmd = "cat -n docker-compose.yml |awk '/testing/,/links/{print}'|grep 'dockerrun'|awk '{print $1}'"
status, output = commands.getstatusoutput(get_line_cmd)
print output
edit_cmd = "sed -i '%ss/100/86400/' docker-compose.yml" % output
status, output = commands.getstatusoutput(edit_cmd)
