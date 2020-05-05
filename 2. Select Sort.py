def select_sort(data):
    for i in range(0, len(data) - 1):
        min = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min]:
                min = j
        data[i], data[min] = data[min], data[i]
        print("Pass", i+1, ": ", data)
    return data


data = [40, 10, 50, 90, 20, 80, 30, 60]
select_sort(data)
print("Result : ", data)