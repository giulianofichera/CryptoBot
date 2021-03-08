import json
import requests
from tabulate import tabulate

### ------------ USDC - ARS ------------
def info_btc_usdc():
    
    btc_usdc_url = 'https://api.exchange.ripio.com/api/v1/rate/BTC_USDC/'

    data = requests.get(btc_usdc_url)
    data = data.json()

    # Convert possible items to float
    for k,v in data.items():
        try:
            data[k] = float(v)
        except (ValueError, TypeError):
            pass


    #print(data, end = '\n\n')

    btc_usdc_title = ' ' + str(data['base_name']) + ' - ' + str(data['quote_name'] + ' ')
    btc_usdc = str(data['base']) + ' - ' + str(data['quote'])
    btc_usdc_last_price = data['last_price']
    btc_usdc_avg = data['avg']
    btc_usdc_high24 = data['high']
    btc_usdc_low24 = data['low']
    btc_usdc_variation24 = data['variation']

    info = [('Pair', btc_usdc),
            ('Last Value: ', btc_usdc_last_price),
            ('Avg: ', btc_usdc_avg),
            ('Low 24hs: ', btc_usdc_low24),
            ('High 24hs: ', btc_usdc_high24),
            ('Variation: ', btc_usdc_variation24),
            ]


    #print(btc_usdc_title)
    #print(tabulate(info))
    return tabulate(info)


# ------------------------------------