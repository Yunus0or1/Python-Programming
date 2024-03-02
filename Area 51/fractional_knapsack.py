class ItemValue:
    """Item Value DataClass"""

    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt

    def __lt__(self, other):
        return self.cost < other.cost


def fractionalKnapSack(items,capacity):
    totalValue = 0


    for i in range(len(items)):
        currentWt = items[i].wt
        currentCost = items[i].cost
        currentVal = items[i].val

        if capacity - currentWt >= 0:
            totalValue = totalValue + currentVal
            capacity = capacity - currentWt
        else :
            remaining = currentWt - capacity
            added = remaining * currentCost
            totalValue = totalValue + added
            capacity = 0

    return totalValue

items = [ItemValue(10,60,0),ItemValue(40,40,1),ItemValue(20,100,2),ItemValue(30,120,3)]
items = sorted(items, reverse=True)
capacity = 50

# Function call
maxValue = fractionalKnapSack(items,capacity)
print("Maximum value in Knapsack =", maxValue)