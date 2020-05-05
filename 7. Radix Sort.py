def radix_sort(data, base):
    size = len(data)
    Max = max(data)

    k = 1  # 자리수

    while k <= Max:
        output = [0] * size  # [0, 0, 0, 0, 0]
        count = [0] * base  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # count 발생 횟수를 count[] 에 저장
        for i in range(size):
            count[(data[i] // k) % base] += 1

        # count[i]가 output에서 숫자의 실제 위치를 포함하도록(안정성이 지켜지도록) count[i] 변경
        for i in range(1, base):
            count[i] += count[i-1]

        # output 생성
        for i in range(size-1, -1, -1):
            j = (data[i] // k) % base
            output[count[j]-1] = data[i]
            count[j] -= 1

        for i in range(size):
            data[i] = output[i]

        print(k, "의 자리 정렬 결과 : ", data)
        k *= base
    return data


data = [89, 70, 35, 131, 910]
base = 10  # 진수
radix_sort(data, base)
print("\nResult : ", data)


