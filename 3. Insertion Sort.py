def insertion_sort(data):
    for i in range(1, len(data)):
        CurrentElement = data[i]
        j = i - 1
        while(j >= 0 and data[j] > CurrentElement):
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = CurrentElement
        print("Pass", i, ": ", data)
    return data


data = [40, 10, 50, 90, 20, 80, 30, 60]
insertion_sort(data)
print("Result : ", data)