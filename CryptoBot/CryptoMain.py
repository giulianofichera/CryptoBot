import json
import requests
from tabulate import tabulate

usdc_ars_url = 'https://api.exchange.ripio.com/api/v1/rate/USDC_ARS/'

data = requests.get(usdc_ars_url)
data = data.json()

# Convert possible items to float
for k,v in data.items():
    try:
        data[k] = float(v)
    except (ValueError, TypeError):
        pass


print(data, end = '\n\n')

usdc_ars_title = ' ' + str(data['base_name']) + ' - ' + str(data['quote_name'] + ' ')
usdc_ars = str(data['base']) + ' - ' + str(data['quote'])
usdc_ars_last_price = data['last_price']
usdc_ars_avg = data['avg']
usdc_ars_high24 = data['high']
usdc_ars_low24 = data['low']
usdc_ars_variation24 = data['variation']

info = [('Pair', usdc_ars),
        ('Last Value: ', usdc_ars_last_price),
        ('Avg: ', usdc_ars_avg),
        ('Low 24hs: ', usdc_ars_low24),
        ('High 24hs: ', usdc_ars_high24),
        ('Variation: ', usdc_ars_variation24),
        ]


print(usdc_ars_title)
print(tabulate(info))
