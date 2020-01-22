def CCS(A):
    n = len(A)
    Count = []
    S = []

    for i in range(0, n):
        Count[i] = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if A[i] < A[j]:
                Count[j] = Count[j] + 1
            else:
                Count[i] = Count[i] + 1
    print(Count)
    for i in range(0, n):
        S[Count[i]] = A[i]
    return S


def main():
    CCS([42, 17, 18, 23, 37, 9])


if __name__ == '__main__':
    main()