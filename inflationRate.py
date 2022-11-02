# calculate annual inflation rate based on the RPI

def calculateInflationRate():
    indexType = getIndexType()
    month, year = getMonthYear()

    thisYearsIndex, lastYearsIndex = getRPIs(month, year, indexType)

    print("Calculating the annual inflation rate for %s %s with this year's %s equal to %.1f and the last year's %s equal to %.1f." % (
        month, year, indexType, thisYearsIndex, indexType, lastYearsIndex))

    annualInflationRate = getAnnualInflationRate(
        thisYearsIndex, lastYearsIndex)
    print("The annual inflation rate is %.1f%%." % annualInflationRate)
    return annualInflationRate


def getIndexType():
    indexChosen = ''
    indexType = ''
    while indexChosen != '1' or indexChosen != '2':
        indexChosen = input(
            "Do you want to calculate using RPI (enter 1) or CPI (enter 2)?   ")
        if indexChosen == '1':
            indexType = 'RPI'
            break
        elif indexChosen == '2':
            indexType = 'CPI'
            break
    return indexType


def getMonthYear():
    month = input("What month is it?    ")
    year = input("What year is it?    ")

    return month, year


def getRPIs(month, year, indexType):
    thisYearsIndex = float(
        input("What is the %s for %s %s?      " % (indexType, month, year)))
    lastYearsIndex = float(
        input("What was the %s this month last year?       " % indexType))
    return thisYearsIndex, lastYearsIndex


def getAnnualInflationRate(thisYearsRPI, lastYearsRPI):
    annualInflationRate = ((thisYearsRPI / lastYearsRPI) * 100) - 100
    return annualInflationRate


def calculateIndexLinkedPension():
    pension = float(input("What is the pension you want to index?   "))
    annualInflationRate = calculateInflationRate()

    indexLinkedPension = ((annualInflationRate / 100) * pension) + pension

    print("The index linked pension should be %.2f pounds." % indexLinkedPension)


def calculatePurchasingPower():
    annualInflationRate = calculateInflationRate()
    purchasingPower = 100 - annualInflationRate
    print("The purchasing power of the pound is %fp." % purchasingPower)


calculateIndexLinkedPension()
