import os
import requests
from dotenv import load_dotenv
import requests

f = open("chatids")
# f = open("chatids_test")
test_chat_ids = f.readlines()

# print(test_chat_ids)

load_dotenv()
api_token = os.getenv('api_token')

text = '''
🚨 Casper Mainnet Peregrine(1.5.6) Protocol Release - Urgent Staging Announcement 🚨

We are pleased to announce the imminent release of the Casper Mainnet Peregrine(1.5.6) protocol upgrade. In preparation for this significant milestone, we kindly request that all Mainnet validators promptly initiate the staging process for the upgrade to casper-node v1.5.6.

The activation point for this crucial upgrade is set to occur at Era 12509. Please be advised that this activation is scheduled to take place on the following date and times:

2024-02-08 14:44 UTC
2024-02-08 6:44 US/Pacific
2024-02-08 9:44 US/Eastern
2024-02-08 15:44 Europe/Zurich
2024-02-08 22:44 Asia/Hong_Kong

To ensure a seamless transition and to stay aligned with the Casper Network's evolving protocol, please follow the comprehensive instructions provided in the following link: 

Casper 1.5.6 Upgrade Instructions.
https://github.com/casper-network/casper-node/wiki/Stage-upgrade-to-Casper-node-v1.5.6
'''

for chat_id in test_chat_ids:   # for test
    # for chat_id in product_chat_ids:   # for production

    url = "https://api.telegram.org/bot{api_token}/sendMessage?chat_id={chat_id}&text={text}".format(
        api_token=api_token, text=text, chat_id=chat_id)
    print(url)

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
