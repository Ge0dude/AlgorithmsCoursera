# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    addList = []
    result = 0
    
    for x in values:
        newVal = x / weights[values.index(x)]
        addList.append(newVal)
    
    
    while capacity > 0:
        maxVal = max(addList)
        if maxVal > 0: 
            maxValIndex = addList.index(max(addList))
            if weights[maxValIndex] <= capacity:  # >= 0:
                result = result + values[maxValIndex]
                addList[maxValIndex] = 0
                capacity = capacity - weights[maxValIndex]
            else:
                fraction = capacity / weights[maxValIndex]
                result = result + (values[maxValIndex] * fraction)
                addList[maxValIndex] = addList[maxValIndex] - (addList[maxValIndex] * fraction)
                capacity = capacity - (weights[maxValIndex] * fraction)
        elif maxVal == 0:
            break   

    return result


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
