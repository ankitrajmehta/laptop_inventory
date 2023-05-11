def readfile():
    data = []
    with open("laptop.txt") as file:
            for i, line in enumerate(file): #enumerate gives index as well as the element
                tmp = line.strip().split(', ')
                tmp.insert(0, str(i + 1))  # Add the ID number at the beginning of the row
                data.append(tmp)
    return data
