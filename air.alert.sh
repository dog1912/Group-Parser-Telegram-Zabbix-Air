#!/bin/bash
grep повітряна /etc/zabbix/zabbix_agentd.d/data_file.json >>/dev/null
result=$?
#echo "exit code: ${result}"
if [ "${result}" -eq "0" ] ; then
echo 1
else
echo 0
fi
