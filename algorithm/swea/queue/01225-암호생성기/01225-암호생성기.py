for tc in range(10):
    T = int(input())
    arr = list(map(int, input().split()))

    while True:
        result = False
        for i in range(5):
            arr[0] = arr[0] -i-1
            new_data = arr[1:]
            new_data.append(arr[0])
            arr = new_data[:]
            if arr[-1] <= 0:
                arr[-1] =0
                result = True
                break
        if result:
            break
    print('#{} {}'.format(T, ' '.join(map(str,arr))))