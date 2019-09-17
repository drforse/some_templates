from telethon import TelegramClient, events, connection
from config import api_id, api_hash, proxy_type
from proxy_config import proxy
from telethon import errors as tel_errs

print(proxy)
if proxy is None:
    client = TelegramClient('anon', api_id, api_hash)
elif proxy_type == 'MTProto':
    client = TelegramClient(
        'anon',
        api_id,
        api_hash,
        connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
        proxy=proxy
    )
else:
    client = TelegramClient('anon', api_id, api_hash, proxy=proxy)

with client:
    client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))