import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_token = os.getenv('api_token')


f = open("chatids")
test_chat_ids = f.readlines()
# for y in x:
#     print(y.strip())

# api_token = "6389110861:AAFe7nNGMArsbwi2mxGnUiGx22TiV2Far44"

text = '''
This is test message again!
'''


for chat_id in test_chat_ids:   # for test
    # for chat_id in product_chat_ids:   # for production

    url = "https://api.telegram.org/bot{api_token}/sendMessage?chat_id={chat_id}&text={text}".format(
        api_token=api_token, text=text, chat_id=chat_id)

    x = requests.get(url)

    print(x.text)
