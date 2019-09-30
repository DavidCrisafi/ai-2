import sys

def stockSwap(tfbStocks, fromStockId, toStockId):
    amount = tfbStocks[fromStockId] * 0.1
    tfbStocks[fromStockId] -= amount
    tfbStocks[toStockId] += amount

def stockLookup(search, allStocks):
    return allStocks[search]

def calculateReturns(tfbStocks, allStocks):
    returns = []
    for stockPrice in tfbStocks:
        stockName = tfbStocks.index(stockPrice)
        stockData = stockLookup(stockName, allStocks)
        change = stockPrice * stockData[change]
        newPrice = stockPrice + change
        returns[stockName] = newPrice

COMPANY = 0
PRICE = 1
CHANGE = 2

stockFileName = sys.argv[1]
stockFile = open(stockFileName, 'r')
stocks = []
firstRow = True

#Creates a list of dictionaries that contain stock information.
for row in stockFile:
    #Skip past header
    if (firstRow):
        firstRow = False
        continue
        
    separatedData = row.split(',')
    separatedData[PRICE] = float(separatedData[1])
    separatedData[CHANGE] = float(separatedData[2].rstrip('\n'))
    data = {
        "name": separatedData[COMPANY],
        "price": separatedData[PRICE],
        "change": separatedData[CHANGE]
    }
    stocks.append(data)

print(stocks)
