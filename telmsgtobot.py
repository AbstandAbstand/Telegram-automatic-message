from telethon import TelegramClient, events, sync
import time

#generate api id and hash on https://my.telegram.org
api_id = #enter api id
api_hash = #enter api hash
client = TelegramClient('session_name', api_id, api_hash)
client.start()
BCbot = client.get_entity('hq_drugs')
count=0
while 1:
    client.send_message(BCbot, 't.me/hq_drugs')
    count=count+1
    print("Message sent | count = {0}".format(count))
    time.sleep(33)
end
