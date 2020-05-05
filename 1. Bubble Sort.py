def bubble_sort(data):
    for Pass in range(1, len(data)):
        for i in range(1, len(data) - Pass + 1):
            if data[i - 1] > data[i]:
                data[i - 1], data[i] = data[i], data[i - 1]
        print("Pass", Pass, ": ", data)
    return data


data = [40, 10, 50, 90, 20, 80, 30, 60]
bubble_sort(data)
print("Result : ", data)