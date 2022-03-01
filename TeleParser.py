# импорт библиотек
import configparser
import json
import os

# Считываем учетные данные
config = configparser.ConfigParser()
main_base = os.path.dirname(__file__)
config_file = os.path.join(main_base, "config.ini")
config.read(config_file)

# Присваиваем значения внутренним переменным
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
channels = config['Telegram']['chats']
token = os.path.join(main_base, "token.session")
json_file = os.path.join(main_base, "data_file.json")
from telethon import TelegramClient, events

client = TelegramClient(token, api_id, api_hash)
@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    #print(event.message)
    with open(json_file, 'w', encoding='utf8') as outfile:
                json.dump(event.message.to_dict()['message'], outfile, ensure_ascii=False)
client.start()
client.run_until_disconnected()


