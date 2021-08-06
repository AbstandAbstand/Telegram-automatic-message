from telethon import TelegramClient, events, sync
import time

#generate api id and hash on https://my.telegram.org
api_id = '7775592'
api_hash = 'f5ab811b557248869d2705bb775952e9'
client = TelegramClient('session_name', api_id, api_hash)
client.start()
MYGROUP = client.get_entity('hq_drugs')
GROUP1 = client.get_entity('hq_weed')
count=0
while 1:
    client.send_message(MYGROUP, 't.me/hq_drugs')
    client.send_message(GROUP1, 't.me/hq_drugs')
    count=count+1
    print("Messages sent | count = {0}".format(count))
    time.sleep(33)
    
    
end
