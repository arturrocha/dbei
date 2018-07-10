# Get DBEI work permit processing date on Telegram

It fetches [dbei.gov.ie](https://dbei.gov.ie/en/What-We-Do/Workplace-and-Skills/Employment-Permits/Current-Application-Processing-Dates) and sends Standard processing date as a Bot to a list of telegram users.

How to create a bot.
> https://core.telegram.org/bots

How to use api to discover bot token and user chat id.
> https://core.telegram.org/bots/api


Change the folowing vars on app.py
```
token='YOUR BOT TOKEN'
telegram_chat_id = ['xxxxxxxxx', 'xxxxxxxxx']
```

Run at minute 0 past every 8th hour on linux.
```
root@raspberrypi:~# cat /etc/cron.d/dbei
0 */8 * * * root /usr/bin/python3 /root/dbei.py
```
