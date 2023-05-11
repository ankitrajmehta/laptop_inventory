def buy(data, id, quantity):
    data[id - 1][4] = int(data[id - 1][4])
    data[id - 1][4] -= quantity
    data[id - 1][4] = str(data[id - 1][4])
    return data

def order(data, id , quantity):
    data[id - 1][4] = int(data[id - 1][4])
    data[id - 1][4] += quantity
    data[id - 1][4] = str(data[id - 1][4])