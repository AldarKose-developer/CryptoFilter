# CryptoFilter
 CryptoFilter outputs top N crytocurencies by market capitalization
## Installation
### Install pycoingecko library 
```
pip install pycoingecko
```
### Or from source
```
git clone https://github.com/man-c/pycoingecko.git
cd pycoingecko
python3 setup.py install
```
### Change path in test.py file
You should change this part of test.py file (3 line). Replace path with path where your folder with project located.
```
sys.path.append('MYPATH')
```

## Usage
Run test.py file from folder 'test'
```
cd test 
test.py
```
## Examples
You should input number of cryptocurrencies that you want to see e.g 5
### For example
```
Enter how many cryptocurrencies you want to see: 
5
['Bitcoin', 'Ethereum', 'Cardano', 'Tether', 'Binance Coin']
```
## License

[MIT](https://choosealicense.com/licenses/mit/)
