import argparse

def stockSwap(tfbStocks, fromStockId, toStockId):
    amount = tfbStocks[fromStockId]['price'] * 0.1
    tfbStocks[fromStockId]['price'] -= amount
    tfbStocks[toStockId]['price'] += amount

def stockLookup(search, allStocks):
    for stock in allStocks:
        if (search['name'] == stock['name']):
            return stock
    
    return None

def calculateReturns(tfbStocks, allStocks):
    stockReturns = []
    for stock in tfbStocks:
        lookup = stockLookup(stock, allStocks)
        change = stock['price'] * lookup['change']
        newPrice = stock['price'] + change
        stockReturn = {
            "name": stock['name'],
            "price": newPrice
        }
        
        stockReturns.append(stockReturn)
    
    return stockReturns



def main():
    parser = argparse.ArgumentParser(description='TFB Calculator', prog='PROG') # create an instance of a parser object.
    parser.add_argument('-f', '--file', help='File name of stocks', type=str, required=True)
    args = parser.parse_args()
    list = []


    stockFileName = args.file
    if stockFileName.find('.') == -1:
        parser.error('File does not have extention')
    COMPANY = 0
    PRICE = 1
    CHANGE = 2

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

if __name__ == '__main__':
    main()