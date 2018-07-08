#!/usr/bin/python3
from bs4 import BeautifulSoup
import urllib.request, requests
import telegram

# TOKEN E.g. 675987757:BAzVnw-c5D2PeWtnTtxS-li90l3IJBV-Nbc
bot = telegram.Bot(token='YOUR TOKEN')

#<td class="left"><b class="tablesaw-cell-label">Date</b>12&nbsp;February 2018</td>

class AppURLopener(urllib.request.FancyURLopener):
    version = 'Mozilla/5.0'

url = "https://dbei.gov.ie/en/What-We-Do/Workplace-and-Skills/Employment-Permits/Current-Application-Processing-Dates"

opener = AppURLopener()
response = opener.open(url)
soup = BeautifulSoup(response, "html.parser")

result_search = str(soup.find("table", {"id": "table-196"}))
result_search = result_search.split("td")
result_search = result_search[-2].replace('class="left">', '').replace('</', '')

# telegram id of targets to receive
telegram_chat_id = ['xxxxxxxxx', 'xxxxxxxxx']
for user in telegram_chat_id:
	bot.send_message(chat_id=user, text="DBEI processing = {}".format(result_search))
