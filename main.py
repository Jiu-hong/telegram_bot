import os
import requests
from dotenv import load_dotenv
import requests

f = open("chatids")
test_chat_ids = f.readlines()

load_dotenv()
api_token = os.getenv('api_token')

text = '''
This is test message!
🚨TESTNET UPGRADE to 1.5.2 ❗️

All Testnet validators should stage the upgrade to casper-node v1.5.2 immediately. The upgrade is now available, and will take effect at Era 9904, which will take place on Monday July 17, around 16:16 UTC. You should be prepared *well ahead of time*, since the exact era transition time is hard to predict.  Please start staging immediately.

Staging your upgrade is very easy - just run the command sudo -u casper /etc/casper/node_util.py stage_protocols casper-test.conf on your node, OR follow the very simple instructions here: https://docs.cspr.community/docs/testnet/upgrade-1_5_2.html
'''

for chat_id in test_chat_ids:   # for test
    # for chat_id in product_chat_ids:   # for production

    url = "https://api.telegram.org/bot{api_token}/sendMessage?chat_id={chat_id}&text={text}".format(
        api_token=api_token, text=text, chat_id=chat_id)

    x = requests.get(url)

    print(x.text)

# botname:https://t.me/CasperLabs_Notifs_bot
# -815692604 Burrito integration
# -551630615 LBank&Casper
# -528646781 CSPR & XT Listing Group
# -506264356 Torus ⇔ Casper ⇔ Arcadia ⇔ MAKE
# -1434723156 CasperLabs-KuCoin
# -1985487798 Casper - Binance - Ceffu
# -559544610 MCX/Casper
# -551916139 CasperLabs | AscendEX - Integration
# -559515751 CSPR / GSR / Figment
# -643182267 Kucoin Casper Tech Integraion group
# -607641751 CasperLabs <> Bitrue
# -411484184 ChangeNow-CasperLabs
# -761386263 Casper Labs <> Ankr
# -519669638  CSPR <> AML Safe integration
# -531083244  Casper - Bithumb Integration
# -732012795 Bitmart EVO token
# -397302091 Casper <> Gitcoin
# -590537194 Casper <> BitKeep Integration
# -1507787537 Casper <> Ferrum
# -662600927 CSPR (Casper) & BitForex Partnership
# -549412067 Casper <> POKT
# -1759290320 FIO <> CASPER
# -624746129 Casper&Bitget
# -1160563389 Casper-ZB Integration
# -614784342 CoinList Casper Node
# -1781106323 Casper Network <> deBridge
# -577503434 Casper <> Emirex
# -347384188 CasperLabs & Coinsuper
# -1399504403 Casper x Coin98
# -524908604 Casper <> Rainfall
# -734370537 Casper x Btok integration
# -538804100 Casper <> Brightpool
# -857003551 Casper <> Beast League
# -644678751 Openblock-Casper
# -756522203 Rainfall-India Tech
# -741907427 Casper <> Blockdaemon
# -531913958 Medha <> Au21 Capital (Casper help group)
# -1686013031 C14 <> Casper
# -550522805  Huobi x Casper integration (cspr)
# -657776678 Casper Labs <> TrustSwap
# -572773082 CasperLabs | NOWNodes
# -549957978 Allbridge <> Casper
# -792112187 Casper <> OKX
# -1180598269 Casperlabs Listing Latoken
# -1871386798 Casper Labs Support Official Release Announcements
# -790227584 DotOracle - Casper
