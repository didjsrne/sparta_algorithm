input = 20

# fibo(N) = Fibo(N-1) + Fibo(N-2)
def fibo_recursion(n):
    if n == 1 or n == 2:  # 탈출조건
        return 1
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)


print(fibo_recursion(input))  # 6765