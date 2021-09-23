from pycoingecko import CoinGeckoAPI


def filter_by_market_cap(num):
    cg = CoinGeckoAPI()
    filtered_currencies = []
    list = cg.get_coins_markets(vs_currency='usd')
    for i in range(num):
        filtered_currencies.append(list[i].get('name'))
    return filtered_currencies
