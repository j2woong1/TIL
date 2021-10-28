T = int(input())
for t in range(1, T + 1):
    binary = input()
    A = int(binary, 2)
    trinary = input()
    money = []
    for i in range(len(binary)):
        money.append(A ^ (1 << i))


    def check():
        for i in range(len(trinary)):
            arr = ['0', '1', '2']
            for j in arr:
                if trinary[i] == j:
                    continue
                ans = int(trinary[:i] + j + trinary[i + 1:], 3)
                if ans in money:
                    return ans


    print("#{} {}".format(t, check()))
