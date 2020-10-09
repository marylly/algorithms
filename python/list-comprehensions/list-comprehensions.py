if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    permutation = []
    result = []
    i = 0
    j = 0
    k = 0
    while i <= x:
        j = 0
        while j <= y:
            k = 0
            while k <= z:
                permutation.append(i)
                permutation.append(j)
                permutation.append(k)
                k = k + 1

                if sum(permutation) != n:
                    result.append(permutation)
                permutation = []
            j = j + 1
        i = i + 1  

    print(result)
