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
    
    listName = []
    chosenStock = []
    listCount = 0

    for x in stocks:
        listName.append(x["name"])

    while listCount < 10:
        print("Names of Companies:", listName)
        print("Name", listCount+1, "of 10")
        tempStr = input('Enter the name of the company you wish to invest in: ')
        for x in stocks:
            if x["name"].lower() == tempStr.lower():
                print("Name found")
                chosenStock.append(x)
                stocks.remove(x)
                listName.remove(tempStr.upper())
                listCount += 1
                break


    print(chosenStock)





if __name__ == '__main__':
    main()