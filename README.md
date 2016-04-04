# pychatwork                                                              

chatwork api library for Python 3

チャットワークのAPIを簡単に使えるPython3のライブラリです。

## Description

``` python
import pychatwork as ch

client = ch.chatworkClient('your access token')

# get message from room 1234
res = client.get_messages(room_id='1234', force=True)

# post message to room 1234
client.post_messages(room_id='1234', message='hello chatwork!')
```
