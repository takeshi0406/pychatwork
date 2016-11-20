# pychatwork                                                              

A Python wrapper for ChatWork's API

http://developer.chatwork.com/

チャットワークのAPIを簡単に使えるPythonのライブラリです。

## Instollation
Install from PyPI.

```
pip install pychatwork
```

Install from github.

```
pip install git+https://github.com/takeshi0406/pychatwork
```

## Usage

``` python
import pychatwork as ch

client = ch.ChatworkClient('your access token')

# get message from room 1234
res = client.get_messages(room_id='1234', force=True)

# post message to room 1234
client.post_messages(room_id='1234', message='hello chatwork!')
```

## TODO

Now, only post message and get message methods were implemented.
