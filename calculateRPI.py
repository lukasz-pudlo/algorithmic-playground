def calculateRPI():
    print("")
    previousRPI = float(
        input("What was the RPI at the point in time of comparison?     "))
    valuesKnownBool = input("Do you know your price ratios and weights? y/n ")
    if valuesKnownBool == 'y':
        numberOfCategories = int(input("How many categories? "))
        items = []
        for i in range(numberOfCategories):
            r = float(input("Enter price ratio for item %d out of %d:   " %
                            (i + 1, numberOfCategories)))
            w = float(input("Enter weight for item %d out %d:   " %
                            (i + 1, numberOfCategories)))
            rw = r * w
            items.append({'w': w, 'rw': rw})

        calculateAllItemsPriceRatio(previousRPI, items)

    else:
        numberOfProducts, totalExpenditure = productsAndExpenditure()

        items = []

        # calculates the RPI for a given month for each item
        for i in range(numberOfProducts):
            inputForEachItem(totalExpenditure, items)

        calculateAllItemsPriceRatio(JanuaryRPI, items)


def productsAndExpenditure():
    numberOfProducts = int(input("How many items will we be calculating? "))
    totalExpenditure = int(input("What is the total expenditure? "))
    return numberOfProducts, totalExpenditure


def inputForEachItem(totalExpenditure, items):
    currentPrice = int(input("What is the price of the item this month? "))
    priceLastJanuary = int(input(
        "What was the price of the item last January? "))

    # price ratio is calculated by dividing the price of an item in a given month by the price of the same item the previous January
    rw = currentPrice / priceLastJanuary

    # weight of an item or cateogry of items is calculated by dividing the expenditure for an item or category of items by the total expenditure and multiplying the result by a chosen total weight, for example 1000

    itemExpenditure = int(
        input("What is the item or category expenditure? "))

    w = (itemExpenditure / totalExpenditure) * 1000

    items.append({'rw': rw, 'w': w})

    return items


def calculateAllItemsPriceRatio(previousRPI, items):
    sumOfProducts = 0
    sumOfWeights = 0
    for item in items:
        sumOfProducts += item['rw']
        sumOfWeights += item['w']

    allItemsPriceRatio = sumOfProducts / sumOfWeights
    currentRPI = previousRPI * allItemsPriceRatio
    print("The current RPI is %.1f" % currentRPI)


calculateRPI()
