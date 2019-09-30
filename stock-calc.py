import sys

def stockSwap(tfbStocks, fromStockId, toStockId):
	amount = tfbStocks[fromStockId] * 0.1
	tfbStocks[fromStockId] -= amount
	tfbStocks[toStockId] += amount

def calculateReturns(tfbStocks, allStocks):
	returns = []
	for stocks in tfbStocks:
		test = 1 #Ignore this line, it's a placeholder
		

stockFileName = sys.argv[1]
stockFile = open(stockFileName, 'r')
stocks = []
index = -1

COMPANY = 0
PRICE = 1
CHANGE = 2

#Creates a 2d list of all stocks and assigns it to the stocks variable. Here's how the list is formatted:
#	stock['initial'] accesses the data for a specific company (replace 'initial' with the company's initial). From there,
#	stock['initial'][price] accesses the company's stock price.
#	stock['initial'][change] accesses the company's percent change over 30 days.
for row in stockFile:
	#Skip over the header
	if (index == -1):
		index += 1
		continue
		
	separatedData = row.split(',')
	separatedData[PRICE] = float(separatedData[1])
	separatedData[CHANGE] = float(separatedData[2].rstrip('\n'))
	data = []
	data.insert("price", separatedData[PRICE])
	data.insert("change", separatedData[CHANGE])
	stocks.insert(separatedData[COMPANY], data)
	index += 1

print(stocks)
