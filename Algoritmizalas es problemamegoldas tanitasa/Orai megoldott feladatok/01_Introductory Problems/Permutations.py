def bf_perm(n):
    if n == 1:
        print(1)
    elif n == 2 or n == 3:
        print("NO SOLUTION")
    else:
        parosok = [i for i in range(2, n+1, 2)]
        paratlanok = [i for i in range(1, n+1, 2)]
        print(*parosok, *paratlanok)


n = int(input())
bf_perm(n)
