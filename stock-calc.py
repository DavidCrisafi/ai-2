import argparse
import random

#0. Randomly distributes a total amount among the 10 selected companies
#1. Checks every possible move.
#2. Picks the move with the best improvement. If there are multiple moves with equal improvement, randomly selects one.
#3. Repeatedly picks moves until it reaches a state where no moves improves its situation.
#4. Restarts with a new randomly generated state.
#5. Continues restarting for the number of times specified.
def hillClimbing(money, restarts, tfbStocks):
    finalProfit = None
    finalSelectedMove = None
    
    for z in range(0, restarts):
        #Randomizes the order of stocks before sequentially putting money in them.
        stockOrder = []
        for i in range(0, len(tfbStocks)):
            stockOrder.append(i)
        random.shuffle(stockOrder)
        
        #Sequentially puts a random amount of the available money in each stock
        remainingMoney = money
        selectedMove = copyStockList(tfbStocks)
        for i in stockOrder:
            if stockOrder.index(i) == 9:
                selectedMove[i]['price'] = remainingMoney
            else:
                amount = random.randint(0, remainingMoney)
                selectedMove[i]['price'] = amount
                remainingMoney -= amount
        
        profit = calculateProfit(money, selectedMove)
        profitToCompare = None
        while(True):
            moves = []
            for i in range(0, len(selectedMove)):
                for j in range(0, len(selectedMove)):
                    if j != i:
                        newStock = copyStockList(selectedMove)
                        stockSwap(newStock, i, j)
                        moves.append(newStock)
            
            possibleProfits = []
            for i in range(0, len(moves)):
                possibleProfits.append(calculateProfit(money, moves[i]))
            
            compareIndex = None
            for i in range(0, len(possibleProfits)):
                if not profitToCompare or possibleProfits[i] > profitToCompare:
                    profitToCompare = possibleProfits[i]
                    compareIndex = i
                elif possibleProfits[i] == profitToCompare and random.randint(0, 1) == 1:
                    compareIndex = i
            
            if (profitToCompare > profit):
                profit = profitToCompare
                selectedMove = moves[compareIndex]
            else:
                break
        
        if (not finalProfit or profit > finalProfit):
            finalProfit = profit
            finalSelectedMove = selectedMove
        
    return finalProfit, finalSelectedMove, calculateReturns(finalSelectedMove)
            
#Returns a list containing a copy of every dictionary in stocks
def copyStockList(stocks):
    copiedList = []
    for stock in stocks:
        copiedList.append(stock.copy())
    
    return copiedList

#Takes %10 from one stock at the specified stockId, then moves it to the other specified stockId
def stockSwap(tfbStocks, fromStockId, toStockId):
    amount = tfbStocks[fromStockId]['price'] * 0.1
    tfbStocks[fromStockId]['price'] -= amount
    tfbStocks[toStockId]['price'] += amount

#Returns a list of stock dictionaries, with their prices increased or decreased by their monthly percent change
def calculateReturns(tfbStocks):
    stockReturns = []
    for stock in tfbStocks:
        change = stock['price'] * stock['change'] * 0.01
        newPrice = stock['price'] + change
        
        if (newPrice < 0):
            newPrice = 0
        
        stockReturn = {
            "name": stock['name'],
            "price": newPrice
        }
        
        stockReturns.append(stockReturn)
    
    return stockReturns

#Given the initial money spent on stocks and the stock returns 30 days lateer, calculate the total profit.
def calculateProfit(startMoney, tfbStocks):
    stockReturns = calculateReturns(tfbStocks)
    endMoney = totalStockPrice(stockReturns)
    return endMoney - startMoney

#Given a list of stocks, calculates the total stock price.
def totalStockPrice(stocks):
    endMoney = 0
    for stock in stocks:
        endMoney += stock['price']
    return endMoney

#Prints out a stock list in an easy to read format.
def printStocks(stocks):
    for stock in stocks:
        print("Name:", stock['name'], "  Price:", '${:,.2f}'.format(stock['price']))

#Returns true if the total price of stocks equals the total amount. Otherwise, returns false.
def checkValidity(totalAmount, stocks):
    if totalStockPrice(stocks) != totalAmount:
        return False
    return True

def main():
    parser = argparse.ArgumentParser(description='TFB Calculator', prog='PROG') # create an instance of a parser object.
    parser.add_argument('-f', '--file', help='File name of stocks', type=str, required=True)
    parser.add_argument('-t', '--test', help='Automatically selects stocks for quick testing', action='store_true', required=False)
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
    
    stockFile.close()
    listName = []
    chosenStock = []
    listCount = 0

    if (not args.test):
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
    else:
        chosenStock = stocks[0:10]


    #print(chosenStock)
    amount = 10000
    profit, finalStockState, finalReturns = hillClimbing(amount, 1, chosenStock)
    
    if (checkValidity):
        print("RECCOMENDED STOCK PURCHASES WITH", '${:,.2f}'.format(amount))
        printStocks(finalStockState)
        print("\nFINAL RETURNS")
        printStocks(finalReturns)
        print("\nTOTAL STOCK PRICE")
        print('${:,.2f}'.format(totalStockPrice(finalReturns)))
        print("\nPROFIT")
        print('${:,.2f}'.format(profit))
    else:
        print("Error: algorithm failed to properly distribute money")

if __name__ == '__main__':
    main()
