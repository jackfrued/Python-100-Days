def merge(items1, items2):
    items3 = []
    index1, index2 = 0, 0
    while index1 < len(items) and index2 < len(items2):
        if items[index1] < items2[index2]:
            items3.append(items1[index1])
            index1 += 1
        else:
            items3.append(items2[index2])
            index2 += 1
