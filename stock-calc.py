import sys

stockFileName = sys.argv[1]
stockFile = open(stockFileName, 'r')
stocks = []
index = -1

for row in stockFile:
	#Skip over the header
	if (index == -1):
		index += 1
		continue
		
	separatedData = row.split(',')
	separatedData[1] = float(separatedData[1])
	separatedData[2] = float(separatedData[2].rstrip('\n'))
	stocks.insert(index, separatedData)
	index += 1

print(stocks)
