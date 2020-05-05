def shell_sort(data, gap):
    for h in range(len(gap)):
        for i in range(gap[h], len(data)):
            CurrentElement = data[i]
            j = i
            while(j >= gap[h] and data[j - gap[h]] > CurrentElement):
                data[j] = data[j - gap[h]]
                j = j - gap[h]
            data[j] = CurrentElement
        print("gap", gap[h], " : ", data)
    return data


data = [30, 60, 90, 10, 40, 80, 40, 20, 10, 60, 50, 30, 40, 90, 80]
gap = [5, 3, 1]
shell_sort(data, gap)
print("Result : ", data)