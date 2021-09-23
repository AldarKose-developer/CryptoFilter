import sys

sys.path.append('C:\\Users\\nurik\\Desktop\\CoinFilter\\CryptoFilter\\CryptoFilter')
from src import filter
print("Enter how many cryptocurrencies you want to see: ")
num = int(input())
print(filter.filter_by_market_cap(num))   