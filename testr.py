from bs4 import BeautifulSoup
import requests

url = "https://beststocks.ru/crypto/rates/sol"

headers = {
    "Accept": "*/*",
    "User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

req = requests.get(url, headers=headers)

soup = BeautifulSoup(req.text, 'lxml')

Infowindow = soup.find('div', class_='cryptocurrency-view-info__wrap')
kyrs = Infowindow.find('h1', class_='h2')

nums = Infowindow.find('div', class_='cryptocurrency-view-info__content')
price = nums.find('div', class_='nobr h4')
pricechange = Infowindow.find('div', class_='cryptocurrency-view-info__price-change text-desc text-bold nobr text-green')

##print('Курс Solana(SOL): ', price.text, "\n"'Изм. за сегодня: ', pricechange.text)

urlbtc = 'https://beststocks.ru/crypto/rates/btc'

req1 = requests.get(urlbtc, headers=headers)
soup1 = BeautifulSoup(req1.text, 'lxml')

Windowbtc = soup1.find('div', class_='cryptocurrency-view-info__wrap')
kyrsbtc = Windowbtc.find('h1', class_='h2')

numsbtc = Windowbtc.find('div', class_='cryptocurrency-view-info__content')
pricebtc = numsbtc.find('div', class_='nobr h4')
pricecbtcchange = Windowbtc.find('div', class_='cryptocurrency-view-info__price-change text-desc text-bold nobr text-green')

pricechange_text = pricechange.text.strip()

SolShow = f'Курс SOL: {price.text} | Изм. за сегодня: {pricechange.text}'
print(SolShow.replace('\n', ''))




