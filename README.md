# Group-Parser-Telegram-Zabbix-Air
Parser of a group of telegrams about the presence of a missile attack in Kiev and notification on zabbix
## Installation
```sh
pip3 install telethon
mv air.alert.conf /etc/zabbix/zabbix_agentd.d/
systemctl restart zabbix-agent.service
mv TeleParser.py  /etc/zabbix/zabbix_agentd.d/
mv config.ini /etc/zabbix/zabbix_agentd.d/
mv air.alert.service /etc/systemd/system/
systemctl daemon-reload
systemctl status air.alert.service
```
## Edit config
```sh
vi /etc/zabbix/zabbix_agentd.d/config.ini
```
## Authentication
```sh
/usr/bin/python3.7 /etc/zabbix/zabbix_agentd.d/TeleParser.py
```
Enter the phone number and authorization code
```sh
systemctl restart air.alert.service
```
## Create zabbix items and triggers
![Image alt](https://i.imgur.com/gKBhzA1.png)
![Image alt](https://i.imgur.com/2IutW1d.png)
